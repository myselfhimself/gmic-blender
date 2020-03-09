import sys
import os
import blender_addon_tester as BAT

if __name__ == "__main__":
    #config = {"blender_load_tests_script": "blender_load_pytest_without_zip_precompression.py"}
    #addon_path = os.path.realpath(os.path.dirname(__file__))
    addon_path = "downloads/gmic_blender.zip"
    #BAT.test_blender_addon(addon_path=addon_path, blender_revision="2.80", config=config)
    BAT.test_blender_addon(addon_path=addon_path, blender_revision="2.80")
