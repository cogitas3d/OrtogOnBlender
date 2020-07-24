import bpy
import platform
from .__init__ import *
from .Version import *
from .FerrSegmentacao import *
from .CortaOssoFibula import *
from .TomoReconsRapida import * # Apagar!
from .DesenhaObjetos import *

class OTHER_PT_AtualizaAddonSec(bpy.types.Panel):
    bl_label = "Upgrade Script"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Others"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.label(text="VERSION: "+VERSION)

        row = layout.row()
        row.operator("object.atualiza_script", text="UPGRADE OTHERTOOLS!", icon="RECOVER_LAST")



bpy.utils.register_class(OTHER_PT_AtualizaAddonSec)


class OTHER_PT_Converte_Video(bpy.types.Panel):
    bl_label = "Video to Images"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Others"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        col = layout.column(align=True)
        col.prop(scn.my_tool, "filepathvideo", text="")


        if platform.system() == "Linux":

            row = layout.row()
            row.operator("object.converte_video_imagem", text="Convert Video to Images!", icon="RENDER_STILL")


        if platform.system() == "Windows":

            row = layout.row()
            row.operator("object.converte_video_imagem_win", text="Convert Video to Images!", icon="RENDER_STILL")

bpy.utils.register_class(OTHER_PT_Converte_Video)


class OTHER_PT_Converte_Img_Tomo(bpy.types.Panel):
    bl_label = "Images to CT-Scan"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Others"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        col = layout.column(align=True)
        col.prop(scn.my_tool, "path_slices_img", text="")

        row = layout.row()
        row.label(text="Dimensions:")

        row = layout.row(align = True)
        row.prop(context.scene, "S1")

        row = layout.row(align = True)
        row.prop(context.scene, "S2")

        row = layout.row(align = True)
        row.prop(context.scene, "S3")

        row = layout.row()
        row.operator("object.converte_imagens_tomo", text="Convert Images to CT-Scan!", icon="RENDER_STILL")

        row = layout.row()
        row = layout.row()
        row.label(text="Calculations:")

        row = layout.row(align = True)
        row.label(text="Real Size:")
        row.prop(context.scene, "MedidaRealDCM")

        row = layout.row(align = True)
        row.label(text="Current Size:")
        row.prop(context.scene, "MedidaAtualDCM")

        row = layout.row()
        row.operator("object.calcula_dimensao_dcm", text="Calculate!", icon="RENDER_STILL")

        row = layout.row(align = True)
        row.label(text="Scale Factor:")
        row.prop(context.scene, "FatorEscalaDCM")

        row = layout.row()
        row.label(text="Convert MHA to DCM:")

        row = layout.row()
        col = layout.column(align=True)
        col.prop(scn.my_tool, "filepathmha", text="")

        row = layout.row()
        row.operator("object.abre_slicer_mha", text="Open Slicer", icon="RENDER_STILL")


bpy.utils.register_class(OTHER_PT_Converte_Img_Tomo)


bpy.types.Scene.S1 = bpy.props.StringProperty \
  (
    name = "s1",
    description = "s1",
    default = "1"
  )


bpy.types.Scene.S2 = bpy.props.StringProperty \
  (
    name = "s2",
    description = "s2",
    default = "1"
  )

bpy.types.Scene.S3 = bpy.props.StringProperty \
(
 name = "s3",
 description = "s3",
 default = "1"
)

bpy.types.Scene.FatorEscalaDCM = bpy.props.StringProperty \
(
 name = "",
 description = "Scale Factor",
 default = "NONE"
)

bpy.types.Scene.MedidaRealDCM = bpy.props.StringProperty \
(
 name = "",
 description = "Real Size",
 default = "NONE"
)

bpy.types.Scene.MedidaAtualDCM = bpy.props.StringProperty \
(
 name = "",
 description = "Current Measure",
 default = "NONE"
)


class OTHER_PT_Objeto_para_Dicom(bpy.types.Panel):
    bl_label = "3D Object to CT-Scan"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Others"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

#        row = layout.row()
#        row.label(text="Dimensions:")

#       Add Volume Area

        row = layout.row()
        row.label(text="Setup Structure:")

        row = layout.row()
        row.operator("object.importa_voxelcube", text="Import VoxelCube", icon="MESH_CUBE")

        row = layout.row()
        row = layout.row()
        row.operator("object.cria_voxelcube_planos", text="Create VoxelCube Planes", icon="SNAP_VOLUME")


        row = layout.row()
        row = layout.row()
        circle=row.operator("object.booleana_osteo_geral", text="Difference", icon="MOD_BOOLEAN")

        row = layout.row()
        circle=row.operator("object.booleana_osteo_union", text="Union", icon="MOD_CAST")

        row = layout.row()
        circle=row.operator("object.booleana_osteo_inter", text="Intersect", icon="MOD_MASK")

        row = layout.row()
        circle=row.operator("object.booleana_union_multipla", text="MULTIPLE UNION", icon="STICKY_UVS_LOC")


        row = layout.row()
        row.label(text="Convert 3D to Voxel:")

        row = layout.row()
        row.label(text="1) Import VoxelCube.")

        row = layout.row()
        row.label(text="2) Select one or more objects.")

        row = layout.row()
        row.operator("object.converte_3d_voxel", text="Convert to DICOM!", icon="ALEMBIC")

        row = layout.row()
        row = layout.row()
        row.label(text="Convert MHA to DICOM:")

        row = layout.row()
        col = layout.column(align=True)
        col.prop(scn.my_tool, "filepathmha", text="")

        row = layout.row()
        row.operator("object.abre_slicer_mha", text="Open Slicer", icon="RENDER_STILL")

bpy.utils.register_class(OTHER_PT_Objeto_para_Dicom)


class OTHER_PT_Cut_Points(bpy.types.Panel):
    bl_label = "Cut Points"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Others"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

#        row = layout.row()
#        row.label(text="Dimensions:")

#       Add Volume Area

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        row.operator("object.cut_point_pt", text="Add Cut Point", icon="NODE_MATERIAL")

        row = layout.row()
        if context.window_manager.measureit_run_opengl is False:
            icon = 'PLAY'
            txt = 'Show'
        else:
            icon = "PAUSE"
            txt = 'Hide'
        row.operator("measureit.runopengl", text=txt, icon=icon)
        row.prop(scn, "measureit_gl_ghost", text="", icon='GHOST_ENABLED')

        row = layout.row()
        row.operator("object.cria_cotas_botao", text="Create Measures", icon="TRACKING_FORWARDS_SINGLE")


        row = layout.row()
        row.operator("object.cria_bones_fibula", text="Create Bones", icon="BONE_DATA")



bpy.utils.register_class(OTHER_PT_Cut_Points)

'''
class OTHER_PT_TomoReconRapida(bpy.types.Panel):
    bl_label = "CT-Scan Fast Reconstruction"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Others"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        col = layout.column(align=True)
        col.prop(scn.my_tool, "path", text="")

        row = layout.row()
        row.operator("object.gera_modelotomo_rec_rapida", text="CT-Scan Fast Recon", icon="NODE_MATERIAL")

bpy.utils.register_class(OTHER_PT_TomoReconRapida)
'''

class OTHER_PT_Vein(bpy.types.Panel):
    bl_label = "Vein and Nerves"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Others"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

#        row = layout.row()
#        row.label(text="Dimensions:")

#       Add Volume Area

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        row.operator("mesh.add_ponto_veia", text="Create Point", icon="NODE_MATERIAL")

        row = layout.row()
        row.operator("mesh.add_curva_bezier_veia", text="Create Vein or Nerve", icon="OUTLINER_OB_CURVE")


bpy.utils.register_class(OTHER_PT_Vein)


def CriaSplintDentesPintaDef():

    # Grava a arcada selecionada
    context = bpy.context
    objArcada = context.active_object

    bpy.ops.object.mode_set(mode = 'OBJECT')

    # Cria Metabal
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.metaball_add(type='BALL', radius=1, view_align=False, enter_editmode=False, location=(0,0,0))
    objMetaball = context.active_object

    # Seleciona a arcada
    bpy.ops.object.select_all(action='DESELECT')
    objArcada.select_set(True)
    bpy.context.view_layer.objects.active = objArcada


    # Adiciona partícula
    bpy.ops.object.particle_system_add()
    #bpy.data.particles.new("Espessura")
    bpy.data.particles["ParticleSettings"].type = 'HAIR'
    bpy.context.object.particle_systems["ParticleSettings"].vertex_group_density = "Group"
    bpy.data.particles["ParticleSettings"].render_type = 'OBJECT'
    bpy.data.particles["ParticleSettings"].instance_object = bpy.data.objects["Mball"]
    bpy.data.particles["ParticleSettings"].particle_size = 0.4
    bpy.data.particles["ParticleSettings"].name = "DELETE"

    # Seleciona MBall
    bpy.ops.object.select_all(action='DESELECT')
    objMetaball.select_set(True)
    bpy.context.view_layer.objects.active = objMetaball
    objMetaball.name = "Splint_Offset"
    objMetaball.name = "Splint_Offset"

    # Converte MBall em malha
    bpy.ops.object.convert(target='MESH')

    bpy.context.view_layer.objects.active = bpy.data.objects["Splint_Offset.001"]
    bpy.data.objects["Splint_Offset.001"].select_set(True)
    bpy.data.objects["Splint_Offset.001"].name = "Splint_Offset_final"


    # Modificador Smooth
    bpy.ops.object.modifier_add(type='SMOOTH')
    bpy.context.object.modifiers["Smooth"].factor = 2
    bpy.context.object.modifiers["Smooth"].iterations = 30

    # Modificador Remesh
    bpy.ops.object.modifier_add(type='REMESH')
    bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
    bpy.context.object.modifiers["Remesh"].octree_depth = 7

    # Converte malha
    bpy.ops.object.convert(target='MESH')


class CriaSplintDentesPinta(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_splint_dentes_pinta"
    bl_label = "Create Teeth Offset"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        CriaSplintDentesPintaDef()
        return {'FINISHED'}

bpy.utils.register_class(CriaSplintDentesPinta)


class OTHER_PintaOffset(bpy.types.Panel):
    bl_label = "Offset Splint"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Others"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.label(text="Create Offset:")

        row = layout.row()
        row.operator("object.weight_1", text="Weight Paint 1", icon="COLORSET_01_VEC")

        row = layout.row()
        row.operator("object.weight_0", text="Weight Paint 0", icon="COLORSET_04_VEC")

        row = layout.row()
        row.operator("object.cria_splint_dentes_pinta", text="Create Offset!", icon="MOD_SKIN")

        row = layout.row()
        row = layout.row()
        row.label(text="Boolean Segmentation:")

        row = layout.row()
#        row.operator("gpencil.annotate", icon='LINE_DATA', text="Draw Line").mode = 'DRAW_POLY'
        row.operator("object.linha_corte_fora_a_fora", icon='LINE_DATA', text="Draw Line")

        row = layout.row()
        row = layout.row()
        circle=row.operator("object.desenha_booleana_dentro", text="Subtract IN", icon="LIGHTPROBE_CUBEMAP")

        row = layout.row()
        circle=row.operator("object.desenha_booleana_fora", text="Subtract OUT", icon="MESH_CUBE")

        row = layout.row()
        row.label(text="Boolean:")

        row = layout.row()
        circle=row.operator("object.booleana_osteo_geral", text="Difference", icon="MOD_BOOLEAN")

        row = layout.row()
        circle=row.operator("object.booleana_osteo_union", text="Union", icon="MOD_CAST")

        row = layout.row()
        circle=row.operator("object.booleana_osteo_inter", text="Intersect", icon="MOD_MASK")

        row = layout.row()
        row = layout.row()
        circle=row.operator("object.booleana_union_multipla", text="MULTIPLE UNION", icon="STICKY_UVS_LOC")

bpy.utils.register_class(OTHER_PintaOffset)
