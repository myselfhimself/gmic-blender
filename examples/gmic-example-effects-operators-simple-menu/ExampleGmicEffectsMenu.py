import bpy
import gmic

"""
This is a first example of using the gmic-blender 0.7+ addon for Blender 2.8x
It was showcased at the Libre Graphics Meeting 2020

Open or paste this script Blender 2.8x within the Text editor window
and run it with Alt+P to let a little menu pop-up under your mouse.
It will alter your last Render result (or may raise an error if no 
render has been done yet.
"""

class GmicEngraveOperator(bpy.types.Operator):
    bl_idname = "object.gmic_engrave_render"
    bl_label = "Gmic Engrave Render"

    def execute(self, context):
        #bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")

        gmic.run("somefile.tga fx_engrave 0.5,50,0,8,40,0,0,0,10,1,0,0,0,1,0 display")

        return {'FINISHED'}

class GmicDericheOperator(bpy.types.Operator):
    bl_idname = "object.gmic_deriche_render"
    bl_label = "Gmic Deriche Render"

    def execute(self, context):
        #bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")

        gmic.run("somefile.tga deriche 3,1,x display")

        return {'FINISHED'}

class GmicBlurOperator(bpy.types.Operator):
    bl_idname = "object.gmic_blur_render"
    bl_label = "Gmic Blur Render"

    def execute(self, context):
        #bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")

        gmic.run("somefile.tga blur 3 display")

        return {'FINISHED'}

class GmicDefaultRenderOperator(bpy.types.Operator):
    bl_idname = "object.gmic_default_render"
    bl_label = "Gmic Show Default Render"

    def execute(self, context):
        #bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")

        gmic.run("somefile.tga display")

        return {'FINISHED'}


class SimpleCustomMenu(bpy.types.Menu):
    bl_label = "G'MIC Quick Filters"
    bl_idname = "OBJECT_simple_custom_menu"

    def draw(self, context):
        layout = self.layout

        op = layout.operator(GmicDefaultRenderOperator.bl_idname, text = 'Default Render', icon='HAND' ) 
        op = layout.operator(GmicBlurOperator.bl_idname, text = 'Blur', icon='META_ELLIPSOID' ) 
        op = layout.operator(GmicDericheOperator.bl_idname, text = 'Deriche', icon='MESH_CUBE' ) 
        op = layout.operator(GmicEngraveOperator.bl_idname, text = 'Engrave', icon='LIGHT_POINT' ) 
        
def register():
    bpy.utils.register_class(GmicDefaultRenderOperator)
    bpy.utils.register_class(GmicBlurOperator)
    bpy.utils.register_class(GmicDericheOperator)
    bpy.utils.register_class(GmicEngraveOperator)
    bpy.utils.register_class(SimpleCustomMenu)

def unregister():
    bpy.utils.unregister_class(GmicDefaultRenderOperator)
    bpy.utils.unregister_class(GmicBlurOperator)
    bpy.utils.register_class(GmicDericheOperator)
    bpy.utils.register_class(GmicEngraveOperator)
    bpy.utils.unregister_class(SimpleCustomMenu)

if __name__ == "__main__":
    register()

# The menu can also be called from scripts
bpy.ops.wm.call_menu(name=SimpleCustomMenu.bl_idname)
