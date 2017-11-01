import bpy

def object(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene


    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "me"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["me"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 25
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 3
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'SHARP'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Mento"
    bpy.context.object.modifiers["Mento"].show_expanded = False

    
    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "cm"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["cm"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 35
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 12
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'SHARP'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Corpo Mandibula"
    bpy.context.object.modifiers["Corpo Mandibula"].show_expanded = False
    
    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "re"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["re"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 35
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 12
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'SHARP'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Ramo Esquerdo"
    bpy.context.object.modifiers["Ramo Esquerdo"].show_expanded = False
    
    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "rd"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["rd"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 35
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 12
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'SHARP'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Ramo Direito"
    bpy.context.object.modifiers["Ramo Direito"].show_expanded = False
    
    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "ma"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["ma"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 37
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 9.5
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'SHARP'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Maxila"
    bpy.context.object.modifiers["Maxila"].show_expanded = False
    
    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "ca"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["ca"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 90
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 0
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'SHARP'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Cabeça"
    bpy.context.object.modifiers["Cabeça"].show_expanded = False

class CriaAreasDeformacao(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_areas_deformacao"
    bl_label = "Cria Areas Deformação"
    
    def execute(self, context):
        object(self, context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(CriaAreasDeformacao)


def unregister():
    bpy.utils.unregister_class(CriaAreasDeformacao)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.object.cria_areas_deformacao()