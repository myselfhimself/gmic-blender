import shutil
import urllib.request, json
import tempfile
import os
from distutils.dir_util import copy_tree
from zipfile import ZipFile
import re

import yolk.pypi

# TODO add more constants here
RELEASE_NAME = "gmic_blender" #-$(date +%F_%H_%M_%S)
ADDON_PATH = f"downloads/{RELEASE_NAME}.zip"
PYPI_GMIC_PACKAGE_NAME = "gmic"

def is_skippable_wheel(filename):
    """Skip cpython and non-manylinux linux releases"""
    return re.match(r".*cpython.*|.*-linux-.*|.*manylinux2010.*", filename) is not None

def is_targettable_python_version(filename):
    return re.match(r".*cp37.*", filename) is not None

def download_gmicpy_wheel_files():
    releases = yolk.pypi.CheeseShop().package_releases(PYPI_GMIC_PACKAGE_NAME)
    releases.sort()
    latest_release_data = yolk.pypi.CheeseShop().release_urls(PYPI_GMIC_PACKAGE_NAME, releases[-1])

    # TODO set up download caching between jobs
    with tempfile.TemporaryDirectory() as dirpath:
        for release in latest_release_data:
            if is_targettable_python_version(release["filename"]):
                if is_skippable_wheel(release["filename"]):
                    continue
                print(release["url"])
                datatowrite = urllib.request.urlopen(release["url"]).read()
                filename = release["url"].split("/")[-1]
                if is_skippable_wheel(filename):
                    continue
                with open(os.path.join(dirpath, filename), "wb") as f:
                    f.write(datatowrite)
                copy_tree(dirpath, "gmic-py")
                import glob
                whl_files = glob.glob("./gmic-py/*.whl")
                for whl_file in whl_files:
                    # TODO get nicer per-os-platform directory naming, for easier in-blender import
                    extract_target_path = os.path.join(whl_file.replace(".whl", ""))
                    with ZipFile(whl_file, 'r') as zipObj:
                        zipObj.extractall(extract_target_path)
                    os.unlink(whl_file)

def clean_old_directories():
    shutil.rmtree("downloads/", ignore_errors=True)
    shutil.rmtree("gmic-py/", ignore_errors=True)
    shutil.rmtree(RELEASE_NAME, ignore_errors=True)

def setup_addon_files():
    # Copy addon files into the RELEASE_NAME directory
    # The downloads/ directory is for final archives
    os.mkdir("downloads")
    os.mkdir(RELEASE_NAME)

    shutil.copy('__init__.py', RELEASE_NAME)
    shutil.copy('README.md', RELEASE_NAME)
    copy_tree('gmic-py', RELEASE_NAME)

    # TODO This json file will be useless from gmic 2.9.0
    assets_dir = os.path.join(RELEASE_NAME, 'assets')
    os.makedirs(assets_dir)
    shutil.copy('assets/gmic_filters.json', assets_dir)

def zip_addon_files():
    # Per https://www.tutorialspoint.com/How-to-zip-a-folder-recursively-using-Python
    import os
    import zipfile
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
    shutil.rmtree('gmic-py')
    print(f"here you are :) static add-on to test in Blender: {ADDON_PATH}")

if __name__ == "__main__":
    make_addon_zip()
