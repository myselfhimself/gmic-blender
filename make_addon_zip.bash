RELEASE_NAME=gmic-blender-addon-$(date +%F_%H_%M_%S)
mkdir $RELEASE_NAME
cp __init__.py gmic-py/ README.md $RELEASE_NAME -r
zip downloads/$RELEASE_NAME.zip -r $RELEASE_NAME
rm -rf $RELEASE_NAME
