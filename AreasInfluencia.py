import bpy

def object(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    #vg = obj.vertex_groups.new(name=slot.material.name)

    # CORPO MANDÍBULA

    vg = obj.vertex_groups.new(name="cm")
        
    scn.tool_settings.vertex_group_weight=0

    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.vertex_group_assign()


    # MAXILA

    vg = obj.vertex_groups.new(name="ma")
        
    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.vertex_group_assign()


    # MENTO

    vg = obj.vertex_groups.new(name="me")
        
    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.vertex_group_assign()


    # CABEÇA

    vg = obj.vertex_groups.new(name="ca")
        
    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.vertex_group_assign()


    # RAMO DIREITO
        
    vg = obj.vertex_groups.new(name="rd")
        
    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.vertex_group_assign()


    # RAMO ESQUERDO

    vg = obj.vertex_groups.new(name="re")
        
    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.vertex_group_assign()
    

class AreasInfluencia(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.areas_influencia"
    bl_label = "Áreas de Influência - Dinâmica de Tecidos Moles"
    
    def execute(self, context):
        object(self, context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(AreasInfluencia)


def unregister():
    bpy.utils.unregister_class(AreasInfluencia)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.object.areas_influencia()