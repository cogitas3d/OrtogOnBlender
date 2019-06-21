import bpy


def FechaMoldeSimplesDef(self, context):

    context = bpy.context
    obj = context.object
    scn = context.scene

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_non_manifold()

    bpy.ops.mesh.fill()
    bpy.ops.object.editmode_toggle()


class FechaMoldeSimples(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.fecha_molde_simples"
    bl_label = "Close hole simple"
    
    def execute(self, context):
        FechaMoldeSimplesDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(FechaMoldeSimples)
