import bpy
#import platform

from .CompareTools import *

class FORENSIC_PT_PontosFace17(bpy.types.Panel):
    bl_label = "Compare 17 Points"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Compare"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.label(text="Digital Points:")

        row = layout.row()
        linha=row.operator("object.pronasale_digi_pt", text="1 - Pronasale")

        row = layout.row()
        linha=row.operator("object.exocanthus_alar_base_right_digi_pt", text="2 - Exocanthus-Alar Base right")

        row = layout.row()
        linha=row.operator("object.cheek_right_digi_pt", text="3 - Cheek right")

        row = layout.row()
        linha=row.operator("object.alar_base_right_digi_pt", text="4 - Alar Base right")

        row = layout.row()
        linha=row.operator("object.subnasale_digi_pt", text="5 - Subnasale")

        row = layout.row()
        linha=row.operator("object.alar_base_left_digi_pt", text="6 - Alar Base left")

        row = layout.row()
        linha=row.operator("object.cheek_left_digi_pt", text="7 - Cheek left")

        row = layout.row()
        linha=row.operator("object.exocanthus_alar_base_left_digi_pt", text="8 - Exocanthus-Alar Base left")

        row = layout.row()
        linha=row.operator("object.cheilion_alar_base_right_digi_pt", text="9 - Cheilion-Alar Base right")

        row = layout.row()
        linha=row.operator("object.cupids_bow_right_digi_pt", text="10 - Cupid's Bow right")

        row = layout.row()
        linha=row.operator("object.cupids_bow_left_digi_pt", text="11 - Cupid's Bow left")

        row = layout.row()
        linha=row.operator("object.cheilion_alar_base_left_digi_pt", text="12 - Cheilion-Alar Base left")


        row = layout.row()
        linha=row.operator("object.cheilion_right_digi_pt", text="13 - Cheilion right")

        row = layout.row()
        linha=row.operator("object.cheilion_left_digi_pt", text="14 - Cheilion left")

        row = layout.row()
        linha=row.operator("object.lower_lip_digi_pt", text="15 - Lower Lip")

        row = layout.row()
        linha=row.operator("object.b_point_soft_digi_pt", text="16 - B point soft")

        row = layout.row()
        linha=row.operator("object.pogonion_soft_digi_pt", text="17 - Pogonion soft")


        row = layout.row()
        row = layout.row()
        row.label(text="Real Points:")

        row = layout.row()
        linha=row.operator("object.pronasale_real_pt", text="1 - Pronasale")

        row = layout.row()
        linha=row.operator("object.exocanthus_alar_base_right_real_pt", text="2 - Exocanthus-Alar Base right")

        row = layout.row()
        linha=row.operator("object.cheek_right_real_pt", text="3 - Cheek right")

        row = layout.row()
        linha=row.operator("object.alar_base_right_real_pt", text="4 - Alar Base right")

        row = layout.row()
        linha=row.operator("object.subnasale_real_pt", text="5 - Subnasale")

        row = layout.row()
        linha=row.operator("object.alar_base_left_real_pt", text="6 - Alar Base left")

        row = layout.row()
        linha=row.operator("object.cheek_left_real_pt", text="7 - Cheek left")

        row = layout.row()
        linha=row.operator("object.exocanthus_alar_base_left_real_pt", text="8 - Exocanthus-Alar Base left")

        row = layout.row()
        linha=row.operator("object.cheilion_alar_base_right_real_pt", text="9 - Cheilion-Alar Base right")

        row = layout.row()
        linha=row.operator("object.cupids_bow_right_real_pt", text="10 - Cupid's Bow right")

        row = layout.row()
        linha=row.operator("object.cupids_bow_left_real_pt", text="11 - Cupid's Bow left")

        row = layout.row()
        linha=row.operator("object.cheilion_alar_base_left_real_pt", text="12 - Cheilion-Alar Base left")

        row = layout.row()
        linha=row.operator("object.cheilion_right_real_pt", text="13 - Cheilion right")

        row = layout.row()
        linha=row.operator("object.cheilion_left_real_pt", text="14 - Cheilion left")

        row = layout.row()
        linha=row.operator("object.lower_lip_real_pt", text="15 - Lower Lip")

        row = layout.row()
        linha=row.operator("object.b_point_soft_real_pt", text="16 - B point soft")

        row = layout.row()
        linha=row.operator("object.pogonion_soft_real_pt", text="17 - Pogonion soft")

        row = layout.row()
        row = layout.row()
        row.label(text="Distances Report:")

        row = layout.row()
        linha=row.operator("object.calcula_distancias_compare", text="Calc All Distances!", icon="PREFERENCES")

bpy.utils.register_class(FORENSIC_PT_PontosFace17)
