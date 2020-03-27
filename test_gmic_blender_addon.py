import sys
import os
import blender_addon_tester as BAT

addon_path = "downloads/gmic_blender.zip"

def usage():
    print("{}: [blender_version]".format(sys.argv[0]))
    print("Tests the {} addon archive on blender_version for your OS only (MacOS or Linux)".format(sys.argv[0]))
    print("A pytest coverage report is saved to coverage.xml in the current directory at the end of the test.")
    print("If the blender_version argument is not provided. The BLENDER_VERSION environment variable is checked. Else 2.80 is assumed.")
    print("This script requires the blender-addon-tester Python module installed first, see requirements.txt or install yourself with pip.")

if __name__ == "__main__":
    blender_revision = None
    if len(sys.argv) > 1:
        blender_revision = sys.argv[1]
    else:
        blender_revision = os.environ.get("BLENDER_VERSION", False)
    if not blender_revision:
        print("No blender_revision CLI argument or BLENDER_VERSION environment variable found, defaulting to Blender 2.80 for testing!")
    config = {"coverage": True}

    BAT.test_blender_addon(addon_path=addon_path, blender_revision=blender_revision, config=config)
