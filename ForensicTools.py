import bpy

def AdicionaMarcadorDef(nome, distancia):

    bpy.ops.object.empty_add(type='SINGLE_ARROW', view_align=False)
    bpy.context.object.empty_display_size = distancia

    bpy.context.object.name = nome


    context = bpy.context
    obj = context.object
    scn = context.scene

    Marcador_EMP = obj
#    Marcador_EMP.select_set(True)
#    bpy.context.view_layer.objects.active = Marcador_EMP

    Marcador_EMP.location = bpy.context.scene.cursor.location
    Marcador_EMP.rotation_euler = bpy.context.scene.cursor.rotation_euler

#    bpy.context.scene.tool_settings.snap_elements = {'FACE'}
#    bpy.context.scene.tool_settings.use_snap_align_rotation = True

#    bpy.ops.wm.tool_set_by_id(name="builtin.rotate")

#    bpy.context.scene.transform_orientation_slots[0].type = 'NORMAL'

#    bpy.ops.view3d.view_selected(use_all_regions=False)

#    bpy.ops.view3d.view_center_cursor()

class AdicionaMarcador(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.adiciona_marcador"
    bl_label = "Add Soft Tissue Marker"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        NomePonto = bpy.context.scene.nome_marcador
        DistPonto = float(bpy.context.scene.dimensao_marcador)
        AdicionaMarcadorDef(NomePonto, DistPonto)
        return {'FINISHED'}

bpy.utils.register_class(AdicionaMarcador)
