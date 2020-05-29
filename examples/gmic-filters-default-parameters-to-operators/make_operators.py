import json
from default_parameters_gmic_py import default_parameters 

print("""import gmic
import bpy
gmic.default_parameters = {DEFAULT_PARAMETERS}
""".format(DEFAULT_PARAMETERS=default_parameters))

operator_template = \
"""
def gmic_enum_items_cb{OperatorSuffix}(self, context):
    l = {MenuItems} #(('ONE','One','First'), ('TWO','Two','Second'), ('THREE', 'Three', 'Third'))
    gmic_enum_items_cb{OperatorSuffix}.lookup = {{id: name for id, name, desc in l}}
    return l

class GmicOperator{OperatorSuffix}(bpy.types.Operator):
    bl_idname = "object.gmic_operator{OperatorSuffix}"
    bl_label = "{Label}"

    myprop = bpy.props.EnumProperty(items=gmic_enum_items_cb{OperatorSuffix})

    def execute(self, context):
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render("somefile.tga")
        gmic.run("somefile.tga " + gmic.default_parameters[self.myprop] + " display")

        self.report({{'INFO'}}, gmic_enum_items_cb{OperatorSuffix}.lookup[self.myprop])
        return {{'FINISHED'}}
"""

opLines = []
opline_template = "op = layout.operator_menu_enum(GmicOperator{OperatorSuffix}.bl_idname, 'myprop', text=GmicOperator{OperatorSuffix}.bl_label)"
registerLines = []
register_template = "bpy.utils.register_class(GmicOperator{OperatorSuffix})"
unregisterLines = []
unregister_template = "bpy.utils.unregister_class(GmicOperator{OperatorSuffix})"
with open("/home/jd/Productions/GMIC/filters290.json", "r") as f:
    f_json = f.read()
    all_filters = json.loads(f_json)
if all_filters:
    for pos, category in enumerate(all_filters["categories"]):
        print(operator_template.format(Label=category['name'], OperatorSuffix=pos, MenuItems=tuple((filter['command'], filter['command'], filter['command']) for filter in category['filters'])))
        opLines.append(" "*8 + opline_template.format(OperatorSuffix=pos))
        registerLines.append(" "*4 + register_template.format(OperatorSuffix=pos))
        unregisterLines.append(" "*4 + unregister_template.format(OperatorSuffix=pos))

custom_menu_template = \
"""
class SimpleCustomMenu(bpy.types.Menu):
    bl_label = "G'MIC Quick Filters"
    bl_idname = "OBJECT_MT_simple_custom_menu"

    def draw(self, context):
        layout = self.layout
{operatorLines}
"""

print(custom_menu_template.format(operatorLines="\n".join(opLines)))

footer_template = \
"""
def register():
{registerLines}
    bpy.utils.register_class(SimpleCustomMenu)

def unregister():
{unregisterLines}
    bpy.utils.unregister_class(SimpleCustomMenu)

if __name__ == "__main__":
    register()

# The menu can also be called from scripts
bpy.ops.wm.call_menu(name=SimpleCustomMenu.bl_idname)
"""

print(footer_template.format(registerLines="\n".join(registerLines), unregisterLines="\n".join(unregisterLines)))
