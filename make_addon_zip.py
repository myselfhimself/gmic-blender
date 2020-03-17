import shutil
import urllib.request, json
import tempfile
import os
from distutils.dir_util import copy_tree
import zipfile
import re

import yolk.pypi

# CONSTANTS
RELEASE_NAME = "gmic_blender"
RELEASE_ADDONZIP_DIRECTORY_NAME = "downloads"
ADDON_PATH = f"downloads/{RELEASE_NAME}.zip"
PYPI_GMIC_PACKAGE_NAME = "gmic"
GMICPY_DIRECTORY_NAME = "gmic-py"
GMICPY_DOWNLOADS_CACHE_ENV_VARIABLE = "GMICPY_DOWNLOADS_CACHE"
ASSETS_DIRECTORY_NAME = "assets"
ASSETS_GMIC_FILTERS_JSON_PATH = os.path.join(ASSETS_DIRECTORY_NAME, "gmic_filters.json")
BLENDER_ADDON_MODULE_FILE = "__init__.py"
BLENDER_ADDON_README_FILE = "README.md"

def is_skippable_wheel(filename):
    """Skip cpython and non-manylinux linux releases"""
    return re.match(r".*cpython.*|.*-linux-.*|.*manylinux2010.*", filename) is not None

def is_targettable_python_version(filename):
    return re.match(r".*cp37.*", filename) is not None

def get_simplified_directory_name_from_wheel(whl_filename):
    """ Return a full target directory path where a wheel should be extracted, that the Blender addon can generate
    The target expression on the Blender addon side will be: platform.system().lower() + "-" + platform.architecture()[0]"""
    parent_directory_name = os.path.dirname(whl_filename)
    target_subdirectory_name = os.path.basename(whl_filename).replace(".whl", "")
    if re.match(r".*macosx.*x86_64.*", whl_filename):
        target_subdirectory_name = "darwin-64bit"
    elif re.match(r".*linux.*x86_64.*", whl_filename):
        target_subdirectory_name = "linux-64bit"
    elif re.match(r".*linux.*686.*", whl_filename):
        target_subdirectory_name = "linux-32bit"
    # Add support for macosx 32bit (or not..) and for Windows
    return os.path.join(parent_directory_name, target_subdirectory_name)

def _download_and_unzip_wheel_files(dirpath, latest_release_data):
    for release in latest_release_data:
        if is_targettable_python_version(release["filename"]):
            if is_skippable_wheel(release["filename"]):
                continue
            release_filename = os.path.basename(release["url"])

            if is_skippable_wheel(release_filename):
                continue

            if os.path.exists(os.path.join(dirpath, release_filename)):
                print(f"Found cached {release_filename}")
            else:
                print(f"Will download {release_filename} into {dirpath}")
                print(release["url"])
                datatowrite = urllib.request.urlopen(release["url"]).read()
                with open(os.path.join(dirpath, release_filename), "wb") as f:
                    f.write(datatowrite)
    copy_tree(dirpath, GMICPY_DIRECTORY_NAME)
    import glob
    whl_files = glob.glob(f"./{GMICPY_DIRECTORY_NAME}/*.whl")
    for whl_file in whl_files:
        extract_target_path = get_simplified_directory_name_from_wheel(whl_file)
        print(f"Extracting wheel {whl_file} into {extract_target_path}")
        with zipfile.ZipFile(whl_file, 'r') as zipObj:
            zipObj.extractall(extract_target_path)
        os.unlink(whl_file)

def download_gmicpy_wheel_files():
    releases = yolk.pypi.CheeseShop().package_releases(PYPI_GMIC_PACKAGE_NAME)
    releases.sort()
    latest_release_data = yolk.pypi.CheeseShop().release_urls(PYPI_GMIC_PACKAGE_NAME, releases[-1])

    tempdir = os.environ.get(GMICPY_DOWNLOADS_CACHE_ENV_VARIABLE, False)
    if tempdir:
        print(f"Detected cache path for Gmic Python wheel downloads: {tempdir}")
        tempdir = os.path.expanduser(tempdir)
        if not os.path.exists(tempdir):
            print(f"Creating non-existing configured cache path: {tempdir}")
            os.makedirs(tempdir)
        _download_and_unzip_wheel_files(tempdir, latest_release_data)
    else:
        with tempfile.TemporaryDirectory() as dirpath:
            _download_and_unzip_wheel_files(dirpath, latest_release_data)

def clean_old_directories():
    shutil.rmtree(RELEASE_ADDONZIP_DIRECTORY_NAME, ignore_errors=True)
    shutil.rmtree(GMICPY_DIRECTORY_NAME, ignore_errors=True)
    shutil.rmtree(RELEASE_NAME, ignore_errors=True)

def setup_addon_files():
    # Copy addon files into the RELEASE_NAME directory
    # The RELEASE_ADDONZIP_DIRECTORY_NAME directory is for final archives
    os.mkdir(RELEASE_ADDONZIP_DIRECTORY_NAME)
    os.mkdir(RELEASE_NAME)

    shutil.copy(BLENDER_ADDON_MODULE_FILE, RELEASE_NAME)
    shutil.copy(BLENDER_ADDON_README_FILE, RELEASE_NAME)
    copy_tree(GMICPY_DIRECTORY_NAME, RELEASE_NAME)

    # TODO This json file will be useless from gmic 2.9.0
    assets_dir = os.path.join(RELEASE_NAME, ASSETS_DIRECTORY_NAME)
    os.makedirs(assets_dir)
    shutil.copy(ASSETS_GMIC_FILTERS_JSON_PATH, assets_dir)

def zip_addon_files():
    # Per https://www.tutorialspoint.com/How-to-zip-a-folder-recursively-using-Python
    def zipdir(path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))
    zipf = zipfile.ZipFile(ADDON_PATH, 'w', zipfile.ZIP_DEFLATED)
    zipdir(RELEASE_NAME, zipf)
    zipf.close()

def make_addon_zip():
    clean_old_directories()
    # Grab gmic-py .whl(s) from Pypi.org and extract them
    download_gmicpy_wheel_files()
    setup_addon_files()
    zip_addon_files()
    shutil.rmtree(RELEASE_NAME)
    shutil.rmtree(GMICPY_DIRECTORY_NAME)
    print(f"here you are :) static add-on to test in Blender: {ADDON_PATH}")

if __name__ == "__main__":
    make_addon_zip()
