import urllib.request, json
import tempfile
import os
from distutils.dir_util import copy_tree
from zipfile import ZipFile
import re

r = urllib.request.urlopen("https://pypi.org/pypi/gmic/json")
data = json.loads(r.read())
releases = list(data["releases"].keys())
releases.sort()
latest_release = releases[-1]

def filename_to_skip(filename):
    """Skip cpython and non-manylinux linux releases"""
    return re.match(r".*cpython.*|.*-linux-.*", filename) is not None

def python_version_to_keep(filename):
    return re.match(r".*cp(35|36|37|38).*", filename) is not None

with tempfile.TemporaryDirectory() as dirpath:
    for release in data['releases'][latest_release]:
        if python_version_to_keep(release["filename"]):
            if filename_to_skip(release["filename"]):
                continue
            print(release["url"])
            datatowrite = urllib.request.urlopen(release["url"]).read()
            filename = release["url"].split("/")[-1]
            if filename_to_skip(filename):
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
                if filename_to_skip(anyfile):
                    os.unlink(anyfile)

