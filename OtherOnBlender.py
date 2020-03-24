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
