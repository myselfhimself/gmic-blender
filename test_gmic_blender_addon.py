import sys
import os
import blender_addon_tester as BAT

if __name__ == "__main__":
    blender_revision = os.environ.get("BLENDER_VERSION", False)
    if not blender_revision:
        print("Set the BLENDER_VERSION environment variable first!")
        sys.exit(1)
    config = {"coverage": True}
    addon_path = "downloads/gmic_blender.zip"
    BAT.test_blender_addon(addon_path=addon_path, blender_revision=blender_revision, config=config)
