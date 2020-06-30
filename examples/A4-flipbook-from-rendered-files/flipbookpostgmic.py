import bpy
import os
import os.path
import gmic

rendering_dir = os.path.dirname(bpy.context.scene.render.filepath)

g = gmic.Gmic()

good_filenames = []
for filename in os.listdir(rendering_dir):
    if filename.startswith("engraved"):
        print(filename)
        good_filenames.append(os.path.join(rendering_dir, filename))

print(good_filenames)
g.run(" ".join(good_filenames) + " append_tiles , display")
