import bpy
D = bpy.data
C = bpy.context

bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
bpy.ops.object.shade_smooth()

bpy.ops.wm.save_as_mainfile(filepath="cube.blend")