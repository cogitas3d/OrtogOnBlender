import bpy
import platform
from .__init__ import *
from .RhinTools import *

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


class RHIN_PT_AlinhaFace(bpy.types.Panel):
    bl_label = "Photogrammetry - Align & Scale"
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
        row.label(text="Mode:")

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        row = layout.row()
        row.label(text="Align Points:")

        row = layout.row()
        linha=row.operator("object.emp1b", text="Cantal Lateral Right", icon="SORTBYEXT")

        row = layout.row()
        linha=row.operator("object.emp2b", text="Cantal Lateral Left", icon="SORTBYEXT")

        row = layout.row()
        linha=row.operator("object.emp3b", text="Down Point", icon="SORTBYEXT")

#        row = layout.row()
#        row.operator("object.cria_tres_pontos", text="3 Points Click", icon="OUTLINER_OB_MESH")

        col = self.layout.column(align = True)
        col.prop(context.scene, "medida_real2")

        row = layout.row()
        row.operator("object.alinha_forca", text="Align and Resize!", icon="ORIENTATION_LOCAL")

        row = layout.row()
        row = layout.row()
        row.label(text="Segmentation Cut Through:")

        row = layout.row()
        row.operator("gpencil.annotate", icon='LINE_DATA', text="Draw Line").mode = 'DRAW_POLY'

        row = layout.row()
        linha=row.operator("object.segmenta_desenho", text="Cut Draw!", icon="FCURVE")


        row = layout.row()
        row = layout.row()
        row.label(text="Surface Cut:")

        row = layout.row()
        row.operator("wm.modal_cria_pontos", icon='CURVE_DATA', text="Create Points")

        row = layout.row()
        row.operator("mesh.add_curva_bezier_unido", icon='CURVE_BEZCIRCLE', text="Create Bezier Line")

        row = layout.row()
        circle=row.operator("object.bezier_corta", text="Cut Line!", icon="SCULPTMODE_HLT")

        row = layout.row()
        circle=row.operator("object.bezier_corta_dupla", text="Cut Line Double!", icon="MOD_THICKNESS")

        row = layout.row()
        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.5
        row.alignment = 'CENTER'
        row.operator("object.gera_dir_nome_paciente_alinha_face", text="SAVE!", icon="FILE_TICK")

bpy.utils.register_class(RHIN_PT_AlinhaFace)


class RHIN_PT_FotogramModif(bpy.types.Panel):
    bl_label = "Photogrammetry - Modifiers"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Rhin"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        scn = context.scene

        row = layout.row()
        row.label(text="Modifiers:")

        ob = context.object

        layout.operator_menu_enum("object.modifier_add", "type")

        for md in ob.modifiers:
            box = layout.template_modifier(md)
            if box:
                # match enum type to our functions, avoids a lookup table.
                getattr(self, md.type)(box, ob, md)

        row = layout.row()
        row = layout.row()
        row = layout.row()
        linha=row.operator("object.convert", text="APPLY ALL!", icon="ERROR").target='MESH'

bpy.utils.register_class(RHIN_PT_FotogramModif)

class RHIN_PT_PontosAnatomicos(bpy.types.Panel):
    bl_label = "Anatomical Points"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Rhin"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        scn = context.scene

        row = layout.row()
        linha=row.operator("object.copia_face", text="COPY FACE!")

        row = layout.row()
        row.label(text="Mode:")

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        row.label(text="Anatomical Points:")

        row = layout.row()
        linha=row.operator("object.radix_pt", text="Radix")

        row = layout.row()
        linha=row.operator("object.tip_nose_pt", text="Tip of Nose")

        row = layout.row()
        linha=row.operator("object.subnasale_pt", text="Subnasale")

        row = layout.row()
        linha=row.operator("object.anterior_nostril_left_pt", text="Anterior Nostril left")

        row = layout.row()
        linha=row.operator("object.posterior_nostril_left_pt", text="Posterior Nostril left")

        row = layout.row()
        linha=row.operator("object.anterior_nostril_right_pt", text="Anterior Nostril right")

        row = layout.row()
        linha=row.operator("object.posterior_nostril_right_pt", text="Posterior Nostril right")

       	row = layout.row()
        row = layout.row()
        row.label(text="Parent Points:")

        row = layout.row()
        circle=row.operator("object.parenteia_emp", text="Parent Points", icon="LINKED")

        row = layout.row()
        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.5
        row.alignment = 'CENTER'
        row.operator("object.gera_dir_nome_paciente_points_soft", text="SAVE!", icon="FILE_TICK")

bpy.utils.register_class(RHIN_PT_PontosAnatomicos)

class RHIN_PT_DistAngles(bpy.types.Panel):
    bl_label = "Dists & Angles"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Rhin"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        scn = context.scene

        row = layout.row()
        linha=row.operator("object.dist_nariz", text="CALC ALL!", icon="PREFERENCES")

        row = layout.row()
        row.label(text="Results:")

        # Proporção do nariz
        row = layout.row()
        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.0
        row.alignment = 'RIGHT'
        row.prop(context.scene, "rhin_prop_nariz")
        row = col.row()
        row.alignment = 'RIGHT'
        row.label(text="Women: 0.67    Men: 0.67") # Calculado

        # Ângulo nasolabial esquerdo
        row = layout.row()
        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.0
        row.alignment = 'RIGHT'
        row.prop(context.scene, "rhin_angulo_nasolabial_esquerdo")
        row = col.row()
        row.alignment = 'RIGHT'
        row.label(text="Women: 97.7º - 110.3º    Men: 98.7º - 114.1º") # Calculado

        # Ângulo nasolabial direito
        row = layout.row()
        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.0
        row.alignment = 'RIGHT'
        row.prop(context.scene, "rhin_angulo_nasolabial_direito")
        row = col.row()
        row.alignment = 'RIGHT'
        row.label(text="Women: 97.7º - 110.3º    Men: 98.7º - 114.1º") # Calculado

bpy.utils.register_class(RHIN_PT_DistAngles)

bpy.types.Scene.rhin_prop_nariz = bpy.props.StringProperty \
    (
        name = "Nose Proportion",
        description = "Nose Proportion",
        default = "NONE"
    )

bpy.types.Scene.rhin_angulo_nasolabial_esquerdo = bpy.props.StringProperty \
    (
        name = "Nasolabial Angle left",
        description = "Nasolabial Angle left",
        default = "NONE"
    )

bpy.types.Scene.rhin_angulo_nasolabial_direito = bpy.props.StringProperty \
    (
        name = "Nasolabial Angle right",
        description = "Nasolabial Angle right",
        default = "NONE"
    )
