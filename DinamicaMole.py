import bpy
import bmesh
from mathutils import Matrix # Deformação do nariz

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


def GeraNarizDinamicaMole():

    foundTrichion = 'Trichion' in bpy.data.objects
    foundRadix = 'Radix' in bpy.data.objects
    foundTipofNose = 'Tip of Nose' in bpy.data.objects
    foundAlarGrooveright = 'Alar Groove right' in bpy.data.objects
    foundAlarGrooveleft = 'Alar Groove left' in bpy.data.objects
    foundSubmental = 'Submental' in bpy.data.objects

    if foundTrichion == True and foundRadix == True and foundTipofNose  == True and foundAlarGrooveright == True and foundAlarGrooveleft == True and foundSubmental == True:

        print("Pontos do nariz presentes!")

        def InverseMatrix():
            context = bpy.context

            ob = context.object
            constraints = [(pb, c) for pb in ob.pose.bones
                    for c in pb.constraints if c.type == 'CHILD_OF']

            cmd = 'SET' # or 'SET'
            for pb, c in constraints:

                if cmd == 'CLEAR':
                    c.inverse_matrix = Matrix.Identity(4)

                elif cmd == 'SET':
                    if c.target:
                        M = ob.convert_space(pose_bone=pb,
                                matrix=c.target.matrix_world,
                                from_space='WORLD',
                                to_space='POSE')
                        P = Matrix.Identity(4).lerp(M, c.influence)
                        c.inverse_matrix = P.inverted()
                # toggle a property
                target = c.target
                c.target = None
                c.target = target
                #pb.constraints.update()

        # Captura objetos

        ListaPontos = ['Radix', 'Tip of Nose', 'Alar Groove left', 'Alar Groove right', 'Trichion', 'Submental']

        print("LEITURA FEITA!")

        for i in ListaPontos:
        #            print("HÁ O NOME!", i.name)
            bpy.ops.object.select_all(action='DESELECT')

            ObjetoAtual = bpy.data.objects[i]
            ObjetoAtual.select_set(True)
            bpy.context.view_layer.objects.active = ObjetoAtual
            bpy.ops.object.duplicate()
            NovoNome = str(bpy.data.objects[i].name)+"_COPY_NOSE_DEFORM"
            bpy.context.object.name = NovoNome
            bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
            bpy.ops.object.select_all(action='DESELECT')


        EMPNasionSoft = bpy.data.objects["Radix_COPY_NOSE_DEFORM"]
        EMPPNPoint = bpy.data.objects["Tip of Nose_COPY_NOSE_DEFORM"]
        EMPAlaL = bpy.data.objects["Alar Groove left_COPY_NOSE_DEFORM"]
        EMPAlaR = bpy.data.objects["Alar Groove right_COPY_NOSE_DEFORM"]
        EMPTopHead = bpy.data.objects["Trichion_COPY_NOSE_DEFORM"]
        EMPBottomHead = bpy.data.objects["Submental_COPY_NOSE_DEFORM"]

        # Adiciona Empty Sphere
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.empty_add(type='SPHERE', radius=7, view_align=False, location=EMPPNPoint.location)
        bpy.context.object.name = "EMPNoseUpDown"

        EMPNoseUpDown = bpy.data.objects["EMPNoseUpDown"]

        bpy.ops.object.constraint_add(type='TRANSFORM')
        bpy.context.object.constraints["Transformation"].target = bpy.data.objects["ma"]
        bpy.context.object.constraints["Transformation"].use_motion_extrapolate = True
        bpy.context.object.constraints["Transformation"].from_max_y = 10
        bpy.context.object.constraints["Transformation"].map_to_x_from = 'Y'
        bpy.context.object.constraints["Transformation"].map_to_y_from = 'Y'
        bpy.context.object.constraints["Transformation"].map_to_z_from = 'Y'
        bpy.context.object.constraints["Transformation"].to_max_z = -5

        # O CURSOR TEM QUE ESTAR NA ORIGEM TOTAL
        #bpy.context.area.spaces[1].pivot_point='CURSOR' # ANTIGO 2.79
        bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
        #bpy.context.area.spaces[1].cursor_location = (0.0, 0.0, 0.0) # ANTIGO 2.79
        bpy.context.scene.cursor.location = 0,0,0


        # Adiciona Armature em modo de edição
        bpy.ops.object.armature_add(radius=1, view_align=False, enter_editmode=True)

        # Desseleciona tudo
        #bpy.ops.armature.select_all(action='TOGGLE')

        # Modifica posição dos bones
        #bpy.context.object.data.edit_bones["Bone"].head = Vector((1.0, 2.0, 3.0))

        bpy.context.object.data.edit_bones["Bone"].name = "Nose"

        bpy.context.object.data.edit_bones["Nose"].head = EMPPNPoint.location

        bpy.context.object.data.edit_bones["Nose"].tail = EMPNasionSoft.location

        # Adiciona Asa Esquerda
        bpy.ops.armature.bone_primitive_add()

        bpy.context.object.data.edit_bones["Bone"].name = "AlaL"

        bpy.context.object.data.edit_bones["AlaL"].head = EMPPNPoint.location

        bpy.context.object.data.edit_bones["AlaL"].tail = EMPAlaL.location

        # Adiciona Asa Direita
        bpy.ops.armature.bone_primitive_add()

        bpy.context.object.data.edit_bones["Bone"].name = "AlaR"

        bpy.context.object.data.edit_bones["AlaR"].head = EMPPNPoint.location

        bpy.context.object.data.edit_bones["AlaR"].tail = EMPAlaR.location

        # Adiciona Nariz
        bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
        bpy.context.scene.cursor.location = EMPPNPoint.location

        bpy.ops.armature.bone_primitive_add()

        bpy.context.object.data.edit_bones["Bone"].name = "IK_Nose"
        bpy.context.object.data.edit_bones["IK_Nose"].use_deform = False

        # Adicionar Top Bottom

        bpy.ops.armature.bone_primitive_add()

        bpy.context.object.data.edit_bones["Bone"].name = "TopBottomHead"

        bpy.context.object.data.edit_bones["TopBottomHead"].head = EMPTopHead.location

        bpy.context.object.data.edit_bones["TopBottomHead"].tail = EMPBottomHead.location


        # Parentamento
        bpy.context.object.data.edit_bones["Nose"].parent = bpy.context.object.data.edit_bones['IK_Nose']
        bpy.context.object.data.edit_bones["AlaL"].parent = bpy.context.object.data.edit_bones['IK_Nose']
        bpy.context.object.data.edit_bones["AlaR"].parent = bpy.context.object.data.edit_bones['IK_Nose']

        # bpy.context.object.data.draw_type = 'ENVELOPE' # ANTIGO 2.78
        bpy.context.object.data.display_type = 'ENVELOPE'


        # Aumenta tamanho envelope

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.context.object.data.edit_bones["Nose"].head_radius=8.5
        bpy.context.object.data.edit_bones["AlaL"].head_radius=8.5
        bpy.context.object.data.edit_bones["AlaR"].head_radius=8.5
        bpy.context.object.data.edit_bones["Nose"].tail_radius=3.5
        bpy.context.object.data.edit_bones["AlaL"].tail_radius=3.5
        bpy.context.object.data.edit_bones["AlaR"].tail_radius=3.5

        #bpy.context.object.data.edit_bones["Nose"].select_head=True
        #bpy.context.object.data.edit_bones["AlaL"].select_head=True
        #bpy.context.object.data.edit_bones["AlaR"].select_head=True
        #bpy.ops.transform.transform(mode='BONE_ENVELOPE', value=(85, 0, 0, 0))


        # Fazendo o constraint
        #obj = bpy.data.objects["Armature.002"]

        bpy.ops.object.mode_set(mode='OBJECT')
        context = bpy.context
        obj = context.active_object

        bpy.ops.object.mode_set(mode='POSE')
        pbase=obj.pose.bones['IK_Nose']
        pbase.bone.select=True
        bpy.context.object.data.bones.active = bpy.context.object.data.bones['IK_Nose']


        # Child Of
        selected_bone = pbase
        constraint = selected_bone.constraints
        ChildOf = constraint.new('CHILD_OF')
        ChildOf.target = EMPNoseUpDown
        InverseMatrix()
        bpy.context.object.pose.bones["IK_Nose"].constraints["Child Of"].influence = 0.5

        # Track to
        pbase=obj.pose.bones['Nose']
        pbase.bone.select=True
        bpy.context.object.data.bones.active = bpy.context.object.data.bones['Nose']
        selected_bone = pbase
        constraint = selected_bone.constraints
        StretchTo = constraint.new('STRETCH_TO')
        StretchTo.target = EMPNasionSoft

        pbase=obj.pose.bones['AlaL']
        pbase.bone.select=True
        bpy.context.object.data.bones.active = bpy.context.object.data.bones['AlaL']
        selected_bone = pbase
        constraint = selected_bone.constraints
        StretchTo = constraint.new('STRETCH_TO')
        StretchTo.target = EMPAlaL

        pbase=obj.pose.bones['AlaR']
        pbase.bone.select=True
        bpy.context.object.data.bones.active = bpy.context.object.data.bones['AlaR']
        selected_bone = pbase
        constraint = selected_bone.constraints
        StretchTo = constraint.new('STRETCH_TO')
        StretchTo.target = EMPAlaR

        bpy.ops.object.mode_set(mode='OBJECT')
        Armature = context.active_object


        bpy.ops.object.select_all(action='DESELECT')
        Armature.select_set(True)

        # Envelope configurações

        bpy.ops.object.mode_set(mode='EDIT')

        bpy.context.object.data.edit_bones["Nose"].envelope_distance = 14
        bpy.context.object.data.edit_bones["Nose"].head_radius = 5
        bpy.context.object.data.edit_bones["Nose"].tail_radius = 1

        bpy.context.object.data.edit_bones["AlaL"].envelope_distance = 9
        bpy.context.object.data.edit_bones["AlaL"].head_radius = 9
        bpy.context.object.data.edit_bones["AlaL"].tail_radius = 3.5

        bpy.context.object.data.edit_bones["AlaR"].envelope_distance = 9
        bpy.context.object.data.edit_bones["AlaR"].head_radius = 9
        bpy.context.object.data.edit_bones["AlaR"].tail_radius = 3.5

        bpy.context.object.data.edit_bones["TopBottomHead"].envelope_distance = 55
        bpy.context.object.data.edit_bones["TopBottomHead"].head_radius = 22
        bpy.context.object.data.edit_bones["TopBottomHead"].tail_radius = 22


        # Deformação
        bpy.ops.object.mode_set(mode='OBJECT')

        #bpy.context.object.data.draw_type = 'WIRE' # ANTIGO 2.78
        bpy.context.object.data.display_type = 'WIRE'

        bpy.ops.object.select_all(action='DESELECT')
        FaceMalha = bpy.data.objects['SoftTissueDynamic']
        Armature.select_set(True)
        FaceMalha.select_set(True)
        bpy.context.view_layer.objects.active = Armature

        bpy.ops.object.parent_set(type='ARMATURE_ENVELOPE')

        bpy.ops.object.select_all(action='DESELECT')
        FaceMalha.select_set(True)
        bpy.context.view_layer.objects.active = FaceMalha
        bpy.ops.object.modifier_move_up(modifier="Armature.001")

        # Oculta Objetos
        EMPNoseUpDown.hide_viewport=True
        Armature.hide_viewport=True
        EMPNasionSoft.hide_viewport=True
        EMPPNPoint.hide_viewport=True
        EMPAlaL.hide_viewport=True
        EMPAlaR.hide_viewport=True
        EMPTopHead.hide_viewport=True
        EMPBottomHead.hide_viewport=True

    else:
        print("Falta algum ponto anatômico no processo.")


def CorrigeDeformacaoOperacoesDef(self, context):

    # Maxila - correção
    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_MIX')
    bpy.context.object.modifiers["VertexWeightMix"].vertex_group_a = "ma"
    bpy.context.object.modifiers["VertexWeightMix"].vertex_group_b = "cm"
    bpy.context.object.modifiers["VertexWeightMix"].mix_mode = 'SUB'
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="VertexWeightMix")

    # Corpo da mandíbula - correções
    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_MIX')
    bpy.context.object.modifiers["VertexWeightMix"].vertex_group_a = "cm"
    bpy.context.object.modifiers["VertexWeightMix"].vertex_group_b = "ma"
    bpy.context.object.modifiers["VertexWeightMix"].mix_mode = 'SUB'
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="VertexWeightMix")

    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_MIX')
    bpy.context.object.modifiers["VertexWeightMix"].vertex_group_a = "cm"
    bpy.context.object.modifiers["VertexWeightMix"].vertex_group_b = "me"
    bpy.context.object.modifiers["VertexWeightMix"].mix_mode = 'SUB'
    bpy.context.object.modifiers["VertexWeightMix"].mask_constant = 0.30
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="VertexWeightMix")

    # Cabeça - correçoes
    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_MIX')
    bpy.context.object.modifiers["VertexWeightMix"].vertex_group_a = "ca"
    bpy.context.object.modifiers["VertexWeightMix"].vertex_group_b = "cm"
    bpy.context.object.modifiers["VertexWeightMix"].mix_mode = 'SUB'
    bpy.context.object.modifiers["VertexWeightMix"].mask_constant = 0.05
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="VertexWeightMix")

    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_MIX')
    bpy.context.object.modifiers["VertexWeightMix"].vertex_group_a = "ca"
    bpy.context.object.modifiers["VertexWeightMix"].vertex_group_b = "ma"
    bpy.context.object.modifiers["VertexWeightMix"].mix_mode = 'SUB'
    bpy.context.object.modifiers["VertexWeightMix"].mask_constant = 0.2
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="VertexWeightMix")


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
        # CorrigeDeformacaoOperacoesDef(self, context) # FAZER MAIS TESTES FUTUROS!
        GeraNarizDinamicaMole()

        return {'FINISHED'}
