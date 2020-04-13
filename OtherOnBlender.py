import bpy
import platform
from .__init__ import *
from .Version import *
from .FerrSegmentacao import *

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


class OTHER_PT_PontoAnatomicoCustom(bpy.types.Panel):
    bl_label = "Custom Anatomical Point"
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
        row.label(text="Select an object before!")

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
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        col = self.layout.column(align = True)
        col.alignment = 'CENTER'
        col.prop(context.scene, "nome_ponto_customizado")

        row = layout.row()
        row.operator("object.cria_ponto_medida", text="Create Custom Point!", icon="SHADING_RENDERED")

bpy.utils.register_class(OTHER_PT_PontoAnatomicoCustom)

bpy.types.Scene.nome_ponto_customizado = bpy.props.StringProperty \
  (
    name = "Object Name",
    description = "Object Name",
    default = "MeasurePoint"
  )
