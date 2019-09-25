import bpy
import platform
from .__init__ import *

class RHIN_PT_AtualizaAddonSec(bpy.types.Panel):
    bl_label = "Upgrade Script"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Rhin"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.label(text="VERSION: "+VERSION)

        row = layout.row()
        row.operator("object.atualiza_script", text="UPGRADE RHIN!", icon="RECOVER_LAST")

bpy.utils.register_class(RHIN_PT_AtualizaAddonSec)


class RHIN_PT_Fotogrametria(bpy.types.Panel):
    bl_label = "Photogrammetry Start"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Rhin"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.prop(scn, "my_enum")
        
        my_enum = scn.my_enum

        if my_enum == ENUM_VALUES_PHOTOGRAMMETRY.OPENMVG:
#            row = layout.row()
#            row.label(text="OpenMVG+OpenMVS:")

            row = layout.row()
            col = layout.column(align=True)
            col.prop(scn.my_tool, "path_photo", text="")

            col = self.layout.column(align = True)
            col.alignment = 'RIGHT'
            col.prop(context.scene, "d_factor")
            col.prop(context.scene, "smooth_factor")

            if platform.system() == "Windows":
                row = layout.row()
                row.operator("wm.console_toggle", text="Open Terminal?", icon="CONSOLE")

            row = layout.row()
            row.operator("object.gera_modelo_foto", text="Start Photogrammetry!", icon="IMAGE_DATA")

        if my_enum == ENUM_VALUES_PHOTOGRAMMETRY.SMVS:

#            row = layout.row()
#            row.label(text="SMVS+Meshlab:")

            row = layout.row()
            col = layout.column(align=True)
            col.prop(scn.my_tool, "path_photo", text="")

            row = layout.row()
            row.operator("object.gera_modelo_foto_smvs", text="Alternative Photogrammetry I", icon="IMAGE_DATA")


        if my_enum == ENUM_VALUES_PHOTOGRAMMETRY.MESHROOM:

#            row = layout.row()
#            row.label(text="Meshroom (AliceVision):")

            row = layout.row()
            col = layout.column(align=True)
            col.prop(scn.my_tool, "path_photo", text="")

            row = layout.row()
            row.operator("object.gera_modelo_foto_meshroom", text="Alternative Photogrammetry II", icon="IMAGE_DATA")

        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.5
        row.alignment = 'CENTER'
        row.operator("object.gera_dir_nome_paciente_fotogram", text="SAVE!", icon="FILE_TICK")

bpy.utils.register_class(RHIN_PT_Fotogrametria)

