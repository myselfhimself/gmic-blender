import sys
import os
import blender_addon_tester as BAT

if __name__ == "__main__":
    config = {"coverage": True}
    addon_path = "downloads/gmic_blender.zip"
    BAT.test_blender_addon(addon_path=addon_path, blender_revision="2.80", config=config)
