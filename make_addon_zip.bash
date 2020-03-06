# Clean old stuff first
rm -rf downloads/
rm -rf gmic-py/

# Grab gmic-py .whl from Pypi.org and extract them
python3 grab_whl_urls.py

# Zip all of this into the downloads/ directory
RELEASE_NAME=gmic-blender-addon #-$(date +%F_%H_%M_%S)
ADDON_PATH=downloads/$RELEASE_NAME.zip
mkdir -p downloads
mkdir $RELEASE_NAME
cp --parents __init__.py gmic-py/ assets/gmic_filters.json README.md $RELEASE_NAME -r
zip $ADDON_PATH -r $RELEASE_NAME
rm -rf $RELEASE_NAME
echo
echo "here you are :) static add-on to test in Blender: $ADDON_PATH"
