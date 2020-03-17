bl_info = {
    "name": "Blender G'MIC Add-on",
    "author": "Jonathan-David Schröder",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "category": "Object",
}

import os
import sys
import platform

# TODO ensure that globals are tolerated in Blender3d python scripting guidelines..
__GMIC_ADDON_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
__GMIC_FILTERS_JSON_PATH = os.path.join(__GMIC_ADDON_ROOT_PATH, "assets", "gmic_filters.json")
__GMIC_LOADED__ = False
__GMIC_PY_RELATIVE_LIBS_DIR = os.path.join("gmic-py", "-".join(platform.system().lower(), platform.architecture()[0]))

def register():
    print("Registering " + bl_info["name"])
    # TODO uncomment this when basic testing setup is ready
    # if not load_gmic_binary_library():
    #     print("Failed loading G'MIC binary library :-(")
    # else:
    #     print(dir(gmic))
    #     generate_nodes_from_gmic_filters(load_gmic_filters())


def unregister():
    print("Unregistring " + bl_info["name"])

def load_gmic_binary_library():
    global __GMIC_LOADED__

    if __GMIC_LOADED__:
        return

    import os
    import sys
    libdir = os.path.join(__GMIC_ADDON_ROOT_PATH, __GMIC_PY_RELATIVE_LIBS_DIR)
    if libdir not in sys.path:
        sys.path.append(libdir)
    try:
        import gmic
        __GMIC_LOADED__ = True
    except ImportError as err:
        raise LibraryLoadError("Cannot load gmic binary python module. Details:" + sys.exc_info()[0])

    return __GMIC_LOADED__

def load_gmic_filters():
    import json
    # TODO add cache? // mtime check?
    filters_json = None
    # TODO catch exception and make a nice error pop-in if open this file fails
    with open(__GMIC_FILTERS_JSON_PATH) as f:
        filters_json = f.read()
    return json.loads(filters_json)

def generate_nodes_from_gmic_filters(gmic_filters_dict):
    print(gmic_filters_dict)
    # TODO foreach loop on dict, create 1 node by filter
