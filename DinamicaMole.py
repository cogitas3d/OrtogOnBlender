import bpy
import bmesh

def AreasInfluenciaDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
    obj.name = "SoftTissueDynamic"


    #vg = obj.vertex_groups.new(name=slot.material.name)
    bpy.ops.object.mode_set(mode='EDIT')
#    bpy.ops.object.editmode_toggle()
    mesh=bmesh.from_edit_mesh(bpy.context.object.data)
    for v in mesh.verts:
        v.select = True


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


    # FRENTE

    vg = obj.vertex_groups.new(name="frente")

    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.vertex_group_assign()


    bpy.ops.object.mode_set(mode='OBJECT') # Depois de fazer tudo voltar ao modo de Objeto

class AreasInfluencia(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.areas_influencia"
    bl_label = "Áreas de Influência - Dinâmica de Tecidos Moles"

    def execute(self, context):
        AreasInfluenciaDef(self, context)
        return {'FINISHED'}


# CRIA ÁREA DE DEFORMAÇÃO

def CriaAreasDeformacaoDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene


    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "me"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["me"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist =30
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 12 #3
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'SHARP'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Mento"
    bpy.context.object.modifiers["Mento"].show_expanded = False


    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "cm"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["cm"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 20
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 11
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'LINEAR'
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

    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "frente"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["ma"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 40
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 20
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'LINEAR'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Frente"
    bpy.context.object.modifiers["Maxila"].show_expanded = False

class CriaAreasDeformacao(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_areas_deformacao"
    bl_label = "Cria Areas Deformação"

    def execute(self, context):
        CriaAreasDeformacaoDef(self, context)
        return {'FINISHED'}

# CONFIGURA DINÂMICA MOLE

def ConfiguraDinamicaMoleDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.areas_influencia()
    bpy.ops.object.cria_areas_deformacao()

    bpy.ops.object.convert(target='MESH')

    #    a = bpy.data.objects['FaceMalha.001']
    armatureHead = bpy.data.objects['Armature_Head']

    armatureHead.hide_viewport=False

    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = armatureHead
    obj.select_set(True)
    bpy.data.objects['Armature_Head'].select_set(True)
    bpy.ops.object.parent_set(type='ARMATURE_NAME')

    armatureHead.hide_viewport=True


    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
#    faceMalha = bpy.data.objects['FaceMalha.001']
    bpy.context.view_layer.objects.active = obj

    bpy.ops.object.modifier_add(type='SMOOTH')
    bpy.context.object.modifiers["Smooth"].factor = 2
    bpy.context.object.modifiers["Smooth"].iterations = 3
    bpy.context.object.modifiers["Smooth"].vertex_group = "frente"


def CursorParaSelecao():
    context = bpy.context

    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            ctx = bpy.context.copy()
            ctx['area'] = area
            ctx['region'] = area.regions[-1]
          #  bpy.ops.view3d.view_selected(ctx)
            bpy.ops.view3d.snap_cursor_to_selected(ctx)


def SelecaoParaCursor():
    context = bpy.context

    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            ctx = bpy.context.copy()
            ctx['area'] = area
            ctx['region'] = area.regions[-1]
          #  bpy.ops.view3d.view_selected(ctx)
            bpy.ops.view3d.snap_selected_to_cursor(ctx)


def SelectionaObjeto(Obj):
    context = bpy.context
    Objeto = bpy.data.objects[Obj]

    bpy.ops.object.select_all(action='DESELECT')
    Objeto.select_set(True)
    context.view_layer.objects.active = Objeto

def SelecionaOssos(Armature, Bone):
    context = bpy.context

    bpy.ops.object.select_all(action='DESELECT')

    ArmatureAtual = bpy.data.objects[Armature]
    ArmatureAtual.select_set(True)
    context.view_layer.objects.active = ArmatureAtual
    bpy.ops.object.mode_set(mode = 'EDIT')


    bpy.ops.armature.select_all(action='DESELECT')

    bpy.context.object.data.edit_bones[Bone].select_tail = True
    bpy.context.object.data.edit_bones[Bone].select_head = True

def CorrigeOssosArmature(Objeto, Armature, Osso):
    SelectionaObjeto(Objeto)
    CursorParaSelecao()
    SelecionaOssos(Armature, Osso)
    SelecaoParaCursor()
    bpy.ops.object.mode_set(mode = 'OBJECT')


class ConfiguraDinamicaMole(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_dinamica_mole"
    bl_label = "Configura Dinâmica do Mole"

    def execute(self, context):

        context = bpy.context
        ObjFace = context.active_object

        bpy.data.objects['Armature_Head'].hide_viewport=False
#        bpy.data.objects['Armature_Head'].hide_set(False)
        CorrigeOssosArmature('re', 'Armature_Head', 're')
        CorrigeOssosArmature('rd', 'Armature_Head', 'rd')
        CorrigeOssosArmature('ma', 'Armature_Head', 'ma')
        CorrigeOssosArmature('ma', 'Armature_Head', 'Maxila.GUIA')
        CorrigeOssosArmature('cm', 'Armature_Head', 'cm')
        CorrigeOssosArmature('cm', 'Armature_Head', 'Corpo_Mandibular.GUIA')
        CorrigeOssosArmature('me', 'Armature_Head', 'me')
        CorrigeOssosArmature('ca', 'Armature_Head', 'ca')
        CorrigeOssosArmature('ca', 'Armature_Head', 'Mandibula')
#        bpy.data.objects['Armature_Head'].hide_set(True)
        bpy.data.objects['Armature_Head'].hide_viewport=True

        SelectionaObjeto(str(ObjFace.name))

        ConfiguraDinamicaMoleDef(self, context)
        return {'FINISHED'}
