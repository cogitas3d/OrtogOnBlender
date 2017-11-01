import bpy

def object(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    bpy.ops.object.modifier_add(type='SOLIDIFY') 
    bpy.context.object.modifiers["Solidify"].thickness = 0.3
    bpy.context.object.modifiers["Solidify"].offset = 0

class CriaEspessura(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_espessura"
    bl_label = "Cria Espessura"
    
    def execute(self, context):
        object(self, context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(CriaEspessura)


def unregister():
    bpy.utils.unregister_class(CriaEspessura)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.object.cria_espessura()