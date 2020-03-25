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
        row.operator("object.atualiza_script", text="UPGRADE FORENSIC!", icon="RECOVER_LAST")

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

        row = layout.row()
        row.operator("object.converte_video_imagem", text="Convert Video to Images!", icon="RENDER_STILL")

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
        row.operator("object.converte_imagens_tomo", text="Convert Images to CE-Scan!", icon="RENDER_STILL")

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
