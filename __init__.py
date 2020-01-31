bl_info = {
    "name": "Blender G'MIC Add-on",
    "blender": (2, 80, 0),
    "category": "Object",
}

# TODO ensure that globals are tolerated in Blender3d python scripting guidelines..
__GMIC_LOADED__ = False

def register():
    print("Registering " + bl_info["name"])
    if load_gmic_binary_library():
        print(dir(gmic))
    else:
        print("Failed loading G'MIC binary library :-(")

def unregister():
    print("Unregistring " + bl_info["name"])

def load_gmic_binary_library():
    global __GMIC_LOADED__

    if __GMIC_LOADED__:
        return

    import os
    import sys
    libdir = os.path.join(os.path.dirname(__file__), "gmic-py")
    if libdir not in sys.path:
        sys.path.append(libdir)
    try:
        import gmic
        __GMIC_LOADED__ = True
    except ImportError as err:
        raise LibraryLoadError("Cannot find fluid engine library: " + libname + "Details:" + sys.exc_info()[0])

    return __GMIC_LOADED__
