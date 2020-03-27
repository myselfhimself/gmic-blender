pip install -r make_addon_requirements.txt
python make_addon_zip.py
pip install -r blender_addon_tester_requirements.txt
python test_gmic_blender_addon.py # Uses the BLENDER_VERSION environment variable

