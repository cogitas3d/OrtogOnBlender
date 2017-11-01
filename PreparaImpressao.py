import bpy

def object(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.modifier_add(type='REMESH') 
    bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
    bpy.context.object.modifiers["Remesh"].octree_depth = 7
    

class PreparaImpressao(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.prepara_impressao"
    bl_label = "Prepara Impressao"
    
    def execute(self, context):
        object(self, context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(PreparaImpressao)


def unregister():
    bpy.utils.unregister_class(PreparaImpressao)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.object.prepara_impressao()