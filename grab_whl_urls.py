import urllib.request, json
import tempfile
import os
from distutils.dir_util import copy_tree
from zipfile import ZipFile

r = urllib.request.urlopen("https://pypi.org/pypi/gmic/json")
data = json.loads(r.read())
releases = list(data["releases"].keys())
releases.sort()
latest_release = releases[-1]

with tempfile.TemporaryDirectory() as dirpath:
    for release in data['releases'][latest_release]:
        if "cp37" in release["filename"]:
            # Skip non manylinux linux releases
            if "-linux-" in release["filename"]:
                print("skipping " + release["filename"])
                continue
            print(release["url"])
            datatowrite = urllib.request.urlopen(release["url"]).read()
            filename = release["url"].split("/")[-1]
            with open(os.path.join(dirpath, filename), "wb") as f:
                f.write(datatowrite)
            copy_tree(dirpath, "gmic-py")
            import glob
            whl_files = glob.glob("./gmic-py/*.whl")
            for whl_file in whl_files:
                with ZipFile(whl_file, 'r') as zipObj:
                    zipObj.extractall('./gmic-py')

