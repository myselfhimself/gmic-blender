import sys
import os
import blender_addon_tester as BAT

if __name__ == "__main__":
    BAT.test_blender_addon(addon_path=".", blender_revision="2.80")
