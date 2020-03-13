/bin/bash: :qa : commande introuvable
import shutil
import urllib.request, json
import tempfile
import os
from distutils.dir_util import copy_tree
from zipfile import ZipFile
import re

# TODO put all constants definitions here

def is_skippable_wheel(filename):
    """Skip cpython and non-manylinux linux releases"""
    return re.match(r".*cpython.*|.*-linux-.*|.*manylinux2010.*", filename) is not None

def is_targettable_python_version(filename):
    return re.match(r".*cp37.*", filename) is not None

def download_gmicpy_wheel_files():
    # TODO reimplement this in yolk3k, see https://github.com/myselfhimself/gmic-blender/issues/4 and https://github.com/myselfhimself/gmic-blender/issues/6
    r = urllib.request.urlopen("https://pypi.org/pypi/gmic/json")
    data = json.loads(r.read())
    releases = list(data["releases"].keys())
    releases.sort()
    latest_release = releases[-1]

    with tempfile.TemporaryDirectory() as dirpath:
        for release in data['releases'][latest_release]:
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
                    with ZipFile(whl_file, 'r') as zipObj:
                        zipObj.extractall('./gmic-py')
                gmic_py_files = glob.glob("./gmic-py/*.*")
                for anyfile in gmic_py_files:
                    if is_skippable_wheel(anyfile):
                        os.unlink(anyfile)

def cp_parents(target_dir, files):
    """cp --parents Python implementation
    From https://stackoverflow.com/a/15340518/420684 with directory compatibility
    """
    import os, shutil
    dirs = []
    for file in files:
        dirs.append(os.path.dirname(file))
    dirs.sort(reverse=True)
    for i in range(len(dirs)):
        if not dirs[i] in dirs[i-1]:
            need_dir = os.path.normpath(target_dir + dirs[i])
            print("Creating", need_dir )
            os.makedirs(need_dir)
    for file in files:
        dest = os.path.normpath(target_dir + file)
        print("Copying %s to %s" % (file, dest))
        if os.path.isfile(file):
            shutil.copy(file, dest)
        else:
            shutil.copytree(file, dest)

# Clean old stuff first
shutil.rmtree("downloads/", ignore_errors=True)
shutil.rmtree("gmic-py/", ignore_errors=True)

# Grab gmic-py .whl(s) from Pypi.org and extract them
download_gmicpy_wheel_files()

# Zip all of this into the downloads/ directory
RELEASE_NAME = gmic_blender #-$(date +%F_%H_%M_%S)
ADDON_PATH = f"downloads/{RELEASE_NAME}.zip"
os.mkdir("downloads")
os.mkdir(RELEASE_NAME)
cp_parents(RELEASE_NAME, ['__init__.py', 'gmic-py/', 'assets/gmic_filters.json', 'README.md')
#zip $ADDON_PATH -r $RELEASE_NAME # Python make python
shutil.rmtree(RELEASE_NAME)
print()
print("here you are :) static add-on to test in Blender: $ADDON_PATH")
