bl_info = {
    "name": "New Object",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "OrtogOnBlender",
    "warning": "",
    "wiki_url": "",
    "category": "Ortog",
}

if "bpy" in locals():
    import imp
    imp.reload(ImportaArmature)
#    imp.reload(GeraModelosTomo)
    print("Reloaded multifiles")
else:
    from .SegmentaImagens import *
    from .CompareOnBlender import *
    from .RhinOnBlender import *
    from .ForensicOnBlender import *
    from .NomePaciente import *
    from .GeraModelosTomo import *
    from .AjustaTomo import *
    from .OrtogMeshes import *
    from .FerrSegmentacao import *
    from .FerrMedidas import *
    from .BooleanaOsteo import *
    from .AlinhaObjetos import *
    from .FotogrametriaOpenMVG import *
    from .FotogrametriaSMVS import *
    from .FotogrametriaMeshroom import *
#    from .AlinhaTresPontosNovo import *
    from .AlinhaRedimensiona import *
    from .DesenhaObjetos import *
    from .FerrFisica import *
    from .ConfOsteotomiaAuto import *
    from .DinamicaMole import *
    from .AtualizaScript import *
    from .PontosAnatomicos import *
    from .DesenhaGuia import *
    from .RelatorioAnimacao import *
    from .Poisson import *
    from .FerrImgTomo import *
    from .Cefalometria import *
    from .GeraRelatorio import *
    from .CriaSplint import *
    from .FerrMalhas import *


import bpy

from bpy_extras.object_utils import AddObjectHelper, object_data_add

from bpy.props import (StringProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )

VERSION = "20200218a"

# ATUALIZA SCRIPT
class ORTOG_PT_AtualizaAddonSec(bpy.types.Panel):
    bl_label = "Upgrade Script"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.label(text="VERSION: "+VERSION)

        row = layout.row()
        row.operator("object.atualiza_script", text="UPGRADE ORTOG!", icon="RECOVER_LAST")


class ORTOG_PT_NomePaciente(bpy.types.Panel):
    bl_label = "Patient's Name"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

#        scene = context.scene
#        rd = scene.render

#        row = layout.row()
#        row.label(text="CT-Scan Reconstruction:")

#        col = layout.column(align=True)
#        col.prop(scn.my_tool, "path", text="")

        row = layout.row()
#        row.operator("object.tomo_heli", text="CT-Scan")
#        row.operator("object.tomo_cone", text="CBCT")

        col = self.layout.column(align = True)
        col.prop(context.scene, "nome_paciente")

        col = self.layout.column(align = True)
        col.prop(context.scene, "sobrenome_paciente")

        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.5
        row.alignment = 'CENTER'
        row.operator("object.gera_dir_nome_paciente", text="SAVE!", icon="FILE_TICK")



# IMPORTA TOMO

class ORTOG_UI_Local(PropertyGroup):

    path = StringProperty(
        name="",
        description="Path to Directory",
        maxlen=1024,
        subtype='DIR_PATH')

    path_photo = StringProperty(
        name="",
        description="Path to Directory",
        maxlen=1024,
        subtype='DIR_PATH')

    filepathcsv = StringProperty(
        name="",
        description="Select File",
        maxlen=1024,
        subtype='FILE_PATH')

# IMPORTA TOMO MOLDES

class ENUM_VALUES_CTSCAN:
    MANUAL = 'Manual'
    VOXEL = 'Voxel'
    AUTO = 'Auto'
    CUSTOM = 'Custom'

class ORTOG_PT_CTScanSelect(bpy.types.Panel):
    bl_label = "CT-Scan Reconstruction"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.prop(scn, "my_enum_ct")

        my_enum_ct = scn.my_enum_ct

        if my_enum_ct == ENUM_VALUES_CTSCAN.MANUAL:
            row = layout.row()
            row.label(text="CT-Scan Preparing:")
            col = layout.column(align=True)
            col.prop(scn.my_tool, "path", text="")
    #        layout.prop(rd, "filepath", text="")

            if platform.system() == "Windows":
                row = layout.row()
                row.operator("wm.console_toggle", text="Open Terminal?", icon="CONSOLE")

            row = layout.row()
            row.operator("object.ajusta_tomo", text="Organize", icon="NODETREE")


            row = layout.row()
            row = layout.row()
    #        row.label(text="CT-Scan Fix:")
    #        col = layout.column(align=True)
    #        col.prop(scn.my_tool, "path", text="")
    #        row = layout.row()
    #        row.operator("object.corrige_dicom", text="Fix it!", icon="FILE_TICK")

            row = layout.row()
            row.label(text="Threshold Setup:")
            col = layout.column(align=True)
            col.prop(scn.my_tool, "path", text="")
            row = layout.row()
            row.operator("object.abre_slicer", text="Open Slicer!", icon="FILE_TICK")


            row = layout.row()
            row.label(text="CT-Scan 3D Reconstruction:")

            col = layout.column(align=True)
            col.prop(scn.my_tool, "path", text="")

            row = layout.row()
    #        row.operator("object.tomo_heli", text="CT-Scan")
    #        row.operator("object.tomo_cone", text="CBCT")


            col = self.layout.column(align = True)
            #col.scale_y=1.5
            col.alignment = 'CENTER'
            col.prop(context.scene, "interesse_ossos")

            col = self.layout.column(align = True)
            col.alignment = 'CENTER'
            col.prop(context.scene, "interesse_mole")

            col = self.layout.column(align = True)
            col.alignment = 'CENTER'
            col.prop(context.scene, "interesse_dentes")

            if platform.system() == "Windows":
                row = layout.row()
                row.operator("wm.console_toggle", text="Open Terminal?", icon="CONSOLE")

            row = layout.row()
    #        row.operator("object.gera_modelos_tomo", text="Convert DICOM to 3D", icon="SNAP_FACE")
            row.operator("object.gera_modelo_tomo_manual", text="Convert DICOM to 3D", icon="SNAP_FACE")

            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.5
            row.alignment = 'CENTER'
            row.operator("object.gera_dir_nome_paciente_tomo", text="SAVE!", icon="FILE_TICK")

        if my_enum_ct == ENUM_VALUES_CTSCAN.VOXEL:

            row = layout.row()
            row.label(text="CT-Scan Preparing:")
            col = layout.column(align=True)
            col.prop(scn.my_tool, "path", text="")
            row = layout.row()
            row.operator("object.ajusta_tomo", text="Organize", icon="NODETREE")


            row = layout.row()
            row.label(text="CT-Scan Voxel Importing:")
            col = layout.column(align=True)
            col.prop(scn.my_tool, "path", text="")
    #        layout.prop(rd, "filepath", text="")

            if platform.system() == "Windows":
                row = layout.row()
                row.operator("wm.console_toggle", text="Open Terminal?", icon="CONSOLE")

            row = layout.row()
            row.operator("object.importa_fatias_dcm", text="Import DICOM Slices", icon="ALEMBIC")

    #        row = layout.row()
    #        prefs = context.preferences
    #        system = prefs.system
    #        row.prop(system, "gl_clip_alpha", slider=True)

            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.5
            row.alignment = 'CENTER'
            row.operator("object.gera_dir_nome_paciente_voxel", text="SAVE!", icon="FILE_TICK")

        if my_enum_ct == ENUM_VALUES_CTSCAN.AUTO:

            row = layout.row()
            row.label(text="Automatic Reconstruction:")

            col = layout.column(align=True)
            col.prop(scn.my_tool, "path", text="")

            row = layout.row()
            row.operator("object.gera_modelos_tomo_auto", text="AUTOMATIC DICOM TO 3D", icon="SNAP_FACE")

            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.5
            row.alignment = 'CENTER'
            row.operator("object.gera_dir_nome_paciente_tomo_auto", text="SAVE!", icon="FILE_TICK")

        if my_enum_ct == ENUM_VALUES_CTSCAN.CUSTOM:
            row = layout.row()
            row.label(text="CT-Scan Preparing:")
            col = layout.column(align=True)
            col.prop(scn.my_tool, "path", text="")
    #        layout.prop(rd, "filepath", text="")

            if platform.system() == "Windows":
                row = layout.row()
                row.operator("wm.console_toggle", text="Open Terminal?", icon="CONSOLE")

            row = layout.row()
            row.operator("object.ajusta_tomo", text="Organize", icon="NODETREE")


            row = layout.row()
            row = layout.row()
    #        row.label(text="CT-Scan Fix:")
    #        col = layout.column(align=True)
    #        col.prop(scn.my_tool, "path", text="")
    #        row = layout.row()
    #        row.operator("object.corrige_dicom", text="Fix it!", icon="FILE_TICK")

            row = layout.row()
            row.label(text="Threshold Setup:")
            col = layout.column(align=True)
            col.prop(scn.my_tool, "path", text="")
            row = layout.row()
            row.operator("object.abre_slicer", text="Open Slicer!", icon="FILE_TICK")


            row = layout.row()
            row.label(text="CT-Scan 3D Reconstruction:")

            col = layout.column(align=True)
            col.prop(scn.my_tool, "path", text="")

            row = layout.row()
    #        row.operator("object.tomo_heli", text="CT-Scan")
    #        row.operator("object.tomo_cone", text="CBCT")

            col = self.layout.column(align = True)
            col.alignment = 'CENTER'
            col.prop(context.scene, "interesse_geral")

            col = self.layout.column(align = True)
            col.alignment = 'CENTER'
            col.prop(context.scene, "fator_simplificacao")

            col = self.layout.column(align = True)
            col.alignment = 'CENTER'
            col.prop(context.scene, "nome_objeto")

            if platform.system() == "Windows":
                row = layout.row()
                row.operator("wm.console_toggle", text="Open Terminal?", icon="CONSOLE")

            row = layout.row()
    #        row.operator("object.gera_modelos_tomo", text="Convert DICOM to 3D", icon="SNAP_FACE")
            row.operator("object.gera_modelo_tomo_custom", text="Convert DICOM to 3D", icon="SNAP_FACE")

            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.5
            row.alignment = 'CENTER'
            row.operator("object.gera_dir_nome_paciente_tomo", text="SAVE!", icon="FILE_TICK")


class ORTOG_OT_GeraModelosTomoArc(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_modelos_tomo_arc"
    bl_label = "Gera Tomografia Molde"

    def execute(self, context):
        GeraModelosTomoArcDef(self, context)
        return {'FINISHED'}


class ORTOG_PT_ImportaArc(bpy.types.Panel):
    bl_label = "Import Archs"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

#        scene = context.scene
#        rd = scene.render

        row = layout.row()
        row.label(text="Arch Teeth Import:")

        col = layout.column(align=True)
        col.prop(scn.my_tool, "path", text="")

        '''
        if platform.system() == "Windows":
            row = layout.row()
            row.operator("wm.console_toggle", text="Open Terminal?", icon="CONSOLE")
        '''

        row = layout.row()
        row.operator("object.abre_slicer", text="Open Slicer!", icon="FILE_TICK")

        col = self.layout.column(align = True)
        col.prop(context.scene, "interesse_arco")

        row = layout.row()
        row.operator("object.gera_modelos_tomo_arc", text="Arch Generator", icon="SNAP_FACE")

        row = layout.row()
        row = layout.row()
        row.label(text="Import File:")

        row = layout.row()
        row.operator("import_mesh.stl", text="Import STL", icon="IMPORT")

        row = layout.row()
        row.label(text="Mode:")

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        row = layout.row()
        row.label(text="Alignment:")

        row = layout.row()
        linha=row.operator("object.emp1a", text="Point 1a - Origin", icon="SORTBYEXT")

        row = layout.row()
        linha=row.operator("object.emp1b", text="Point 1b - Align", icon="SORTBYEXT")

        row = layout.row()
        row = layout.row()
        row = layout.row()
        linha=row.operator("object.emp2a", text="Point 2a - Origin", icon="SORTBYEXT")

        row = layout.row()
        linha=row.operator("object.emp2b", text="Point 2b - Align", icon="SORTBYEXT")

        row = layout.row()
        row = layout.row()
        row = layout.row()
        linha=row.operator("object.emp3a", text="Point 3a - Origin", icon="SORTBYEXT")

        row = layout.row()
        linha=row.operator("object.emp3b", text="Point 3b - Align", icon="SORTBYEXT")

        row = layout.row()
        row.label(text="Select align object!")
        row = layout.row()
        linha=row.operator("object.alinha_tres_pontos", text="ALIGN!", icon="MESH_DATA")


        row = layout.row()
        row.label(text="Select other object!")
#        row = layout.row()
#        linha=row.operator("object.align_icp", text="ICP Align", icon="TRACKING_REFINE_FORWARDS")
        row = layout.row()
        linha=row.operator("object.force_icp", text="Force ICP Align (Slow)", icon="TRACKING_REFINE_FORWARDS")


        row = layout.row()
        row = layout.row()
        row.label(text="Segmentation:")

        row = layout.row()
        row.operator("object.prepara_impressao_3d", text="Close Holes (Remesh)?", icon="META_CUBE")

        row = layout.row()
        row = layout.row()
        row = layout.row()
#        row.operator("gpencil.annotate", icon='LINE_DATA', text="Draw Line").mode = 'DRAW_POLY'
        row.operator("object.linha_corte_fora_a_fora", icon='LINE_DATA', text="Draw Line")


        row = layout.row()
        circle=row.operator("object.desenha_booleana_dentro", text="Subtract IN", icon="LIGHTPROBE_CUBEMAP")

        row = layout.row()
        circle=row.operator("object.desenha_booleana_fora", text="Subtract OUT", icon="MESH_CUBE")


        row = layout.row()
        row = layout.row()
        linha=row.operator("object.entra_editmode_limpo", text="Edit Mode Clean", icon="UV_VERTEXSEL")

        row = layout.row()
        linha=row.operator("mesh.select_more", text="Sel. More", icon="ADD")

        linha=row.operator("mesh.select_less", text="Sel. Less", icon="REMOVE")

        row = layout.row()
        linha=row.operator("object.separa_objeto", text="Separate Selected!", icon="MOD_BEVEL")

        row = layout.row()
        row = layout.row()
        circle=row.operator("object.booleana_osteo_union", text="Union", icon="MOD_CAST")

        row = layout.row()
        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        row.label(text="Pivot Rotation:")


        obj = context.active_object
        tool_settings = context.tool_settings

        object_mode = 'OBJECT' if obj is None else obj.mode

        if object_mode in {'OBJECT', 'EDIT', 'EDIT_GPENCIL', 'SCULPT_GPENCIL'} or has_pose_mode:
            layout.prop_with_popover(
                tool_settings,
                "transform_pivot_point",
                text="",
                icon_only=False,
                panel="VIEW3D_PT_pivot_point",
            )


        row = layout.row()
        row.label(text="Reconstruction:")

        row = layout.row()
        row.operator("object.fecha_buraco_todos", icon='MOD_TRIANGULATE', text="Close All Holes")

        row = layout.row()
        linha=row.operator("mesh.poisson", text="Poisson Reconstruction", icon="MESH_ICOSPHERE")

        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.5
        row.alignment = 'CENTER'
        row.operator("object.gera_dir_nome_paciente_arc", text="SAVE!", icon="FILE_TICK")

class ORTOG_PT_GraphicRefs(bpy.types.Panel):
    bl_label = "Graphic Rerefences"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.label(text="Mode:")

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        row.label(text="Frankfurt Alignment:")

        row = layout.row()
        linha=row.operator("object.oculta_mole", text="Hide Face (CT-Scan)", icon="HIDE_ON")

        row = layout.row()
        linha=row.operator("object.orbital_right_pt", text="Orbital right")
        linha=row.operator("object.orbital_left_pt", text="Orbital left")

        row = layout.row()
        linha=row.operator("object.n_pt", text="N point")
        linha=row.operator("object.po_left", text="Po left")

        row = layout.row()
        row = layout.row()
        row.operator("object.alinha_cranio_frankfurt", text="Align!", icon="ORIENTATION_LOCAL")


        row = layout.row()
        row.label(text="Reference Lines:")

        row = layout.row()
        linha=row.operator("mesh.add_linhabase", text="Vertical Center Line", icon="SORT_DESC")
        linha.location=(0,-200,0)

        row = layout.row()
        linha=row.operator("mesh.add_linhabase", text="Horizontal Center Line", icon="FORWARD")
        linha.location=(0,-200,0)
        linha.rotation=(0,1.5708,0)

        row = layout.row()
        linha=row.operator("mesh.add_linhabase", text="Horizontal Side Line", icon="FORWARD")
        linha.location=(200,30,0)
        linha.rotation=(1.5708,0,0)

        row = layout.row()
        row = layout.row()
        circle=row.operator("object.oculta_pontos_anatomicos", text="Hide Anatomical Points", icon="GHOST_DISABLED")

        row = layout.row()
        row = layout.row()
        row = layout.row()
        row.operator("object.desagrupa_tomo", text="UNGROUP!!!", icon="PARTICLE_DATA")

        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.5
        row.alignment = 'CENTER'
        row.operator("object.gera_dir_nome_paciente_ref", text="SAVE!", icon="FILE_TICK")

class ORTOG_PT_Segmentation(bpy.types.Panel):
    bl_label = "Segmentation"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.operator("object.segmenta_linked", icon='OUTLINER_DATA_CURVE', text="Separate Linked")

        row = layout.row()
        row = layout.row()
        row.operator("object.fecha_buraco_todos", icon='MOD_TRIANGULATE', text="Close All Holes")

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
        row.label(text="Teeth Segmentation Tube:")

        row = layout.row()
        circle=row.operator("wm.modal_cria_pontos_teeth", text="Create Points", icon="CURVE_DATA")

        row = layout.row()
        row.operator("mesh.add_curva_bezier_unido_teeth", icon='CURVE_BEZCIRCLE', text="Create Bezier Tube")

        row = layout.row()
        circle=row.operator("object.bezier_corta_dupla_teeth", text="Cut Line Teeth!", icon="MOD_THICKNESS")

        row = layout.row()
        row.label(text="Teeth Segmentation Line:")

        row = layout.row()
        circle=row.operator("object.prepara_malha_corte", text="Prepare Mesh to Cut", icon="ALEMBIC")

        row = layout.row()
        circle=row.operator("mesh.knife_tool", text="Knife Cut", icon="SCULPTMODE_HLT")

        row = layout.row()
        circle=row.operator("object.separa_edge_split", text="Edge Split Separation", icon="MATSPHERE")

        row = layout.row()
        row.label(text="Separated Teeth:")

        row = layout.row()
        row.operator("object.weight_1", text="Weight Paint 1", icon="COLORSET_01_VEC")

        row = layout.row()
        row.operator("object.weight_0", text="Weight Paint 0", icon="COLORSET_04_VEC")

        row = layout.row()
        linha=row.operator("object.mantem_pintado", text="Delete Blue", icon="GPBRUSH_ERASE_HARD")

        row = layout.row()
        linha=row.operator("object.apaga_pintado", text="Delete Red", icon="GPBRUSH_ERASE_HARD")

        row = layout.row()
        linha=row.operator("object.booleana_mandib", text="Separate Skull-Mandible", icon="FULLSCREEN_ENTER")

        row = layout.row()
        row.label(text="Teeth Touched:")

        row = layout.row()
        linha=row.operator("object.condylar_process_right_pt", text="Condylar Process right")

        row = layout.row()
        linha=row.operator("object.condylar_process_left_pt", text="Condylar Process left")

        row = layout.row()
        linha=row.operator("object.coronoid_process_right_pt", text="Coronoid Process right")

        row = layout.row()
        linha=row.operator("object.coronoid_process_left_pt", text="Coronoid Process left")

        row = layout.row()
        linha=row.operator("object.go_ramus_fracure_right_pt", text="Mid Go-Ramus Fracure right")

        row = layout.row()
        linha=row.operator("object.go_ramus_fracure_left_pt", text="Mid Go-Ramus Fracure left")

        row = layout.row()
        linha=row.operator("object.go_right_pt", text="Go right")

        row = layout.row()
        linha=row.operator("object.go_left_pt", text="Go left")

        row = layout.row()
        linha=row.operator("object.mid_mandibula_angle_right_pt", text="Mid Mandible Angle right")

        row = layout.row()
        linha=row.operator("object.mid_mandibula_angle_left_pt", text="Mid Mandible Angle left")

        row = layout.row()
        linha=row.operator("object.gn_pt", text="Gn point")

        row = layout.row()
        linha=row.operator("object.b_pt", text="B point")

        row = layout.row()
        linha=row.operator("object.mid_upper_incisors_pt", text="Mid Upper Incisors")

        row = layout.row()
        row = layout.row()
        linha=row.operator("object.separacao_mandibula", text="Mandible Segmentation", icon="PIVOT_ACTIVE")

        row = layout.row()
        row = layout.row()
        linha=row.operator("object.separacao_mandibula_cranio", text="Separate Skull from Mandible", icon="MONKEY")

        row = layout.row()
        row.label(text="Other Tools:")

        row = layout.row()
        linha=row.operator("mesh.poisson", text="Poisson Reconstruction", icon="MESH_ICOSPHERE")

        row = layout.row()
        row = layout.row()
#        row.operator("gpencil.annotate", icon='LINE_DATA', text="Draw Line").mode = 'DRAW_POLY'
        row.operator("object.linha_corte_fora_a_fora", icon='LINE_DATA', text="Draw Line")

        row = layout.row()
        linha=row.operator("object.segmenta_desenho", text="Cut Draw!", icon="FCURVE")

        row = layout.row()
        row = layout.row()
        linha=row.operator("object.entra_editmode_limpo", text="Edit Mode Clean", icon="UV_VERTEXSEL")

        row = layout.row()
        linha=row.operator("mesh.select_more", text="Sel. More", icon="ADD")

        linha=row.operator("mesh.select_less", text="Sel. Less", icon="REMOVE")

        row = layout.row()
        linha=row.operator("object.separa_objeto", text="Separate Selected!", icon="MOD_BEVEL")

        row = layout.row()
        row.label(text="Mode:")

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        row = layout.row()
        row.label(text="Pivot Rotation:")


        obj = context.active_object
        tool_settings = context.tool_settings

        object_mode = 'OBJECT' if obj is None else obj.mode

        if object_mode in {'OBJECT', 'EDIT', 'EDIT_GPENCIL', 'SCULPT_GPENCIL'} or has_pose_mode:
            layout.prop_with_popover(
                tool_settings,
                "transform_pivot_point",
                text="",
                icon_only=False,
                panel="VIEW3D_PT_pivot_point",
            )

        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.5
        row.alignment = 'CENTER'
        row.operator("object.gera_dir_nome_paciente_seg", text="SAVE!", icon="FILE_TICK")

class ORTOG_PT_SegmentacaoFace(bpy.types.Panel):
    bl_label = "Photo Face Segmentation"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        col = layout.column(align=True)
        col.prop(scn.my_tool, "path_photo", text="")

        row = layout.row()
        row.operator("object.segmenta_imagem_face", text="Start Segmentation!", icon="USER")

class ENUM_VALUES_PHOTOGRAMMETRY:
    OPENMVG = 'OpenMVG+OpenMVS'
    SMVS = 'SMVS+MeshLab'
    MESHROOM = 'Meshroom'


class ORTOG_PT_Fotogrametria(bpy.types.Panel):
    bl_label = "Photogrammetry Start"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.operator("object.prepara_cena_fotogram", text="Setup Scene!", icon="ERROR")

        row = layout.row()
        row = layout.row()
        row.label(text="Fotogrammetry Algorithm:")

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

class ORTOG_PT_AlinhaFace(bpy.types.Panel):
    bl_label = "Photogrammetry - Align & Scale"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.label(text="Mode:")

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
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

class ORTOG_PT_FotogramModif(bpy.types.Panel):
    bl_label = "Photogrammetry - Modifiers"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

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

class ORTOG_PT_AlinhaFaceCT(bpy.types.Panel):
    bl_label = "Align Face to CT-Scan"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene


        row = layout.row()
        row.label(text="Mode:")

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        row = layout.row()
        row.label(text="Align Points:")

        row = layout.row()
        linha=row.operator("object.emp1a", text="Point 1a - Origin", icon="SORTBYEXT")

        row = layout.row()
        linha=row.operator("object.emp1b", text="Point 1b - Align", icon="SORTBYEXT")

        row = layout.row()
        row = layout.row()
        row = layout.row()
        linha=row.operator("object.emp2a", text="Point 2a - Origin", icon="SORTBYEXT")

        row = layout.row()
        linha=row.operator("object.emp2b", text="Point 2b - Align", icon="SORTBYEXT")

        row = layout.row()
        row = layout.row()
        row = layout.row()
        linha=row.operator("object.emp3a", text="Point 3a - Origin", icon="SORTBYEXT")

        row = layout.row()
        linha=row.operator("object.emp3b", text="Point 3b - Align", icon="SORTBYEXT")

        row = layout.row()
        row = layout.row()
        row.label(text="Select the object to be aligned!")

        row = layout.row()
        linha=row.operator("object.alinha_tres_pontos", text="ALIGN!", icon="MESH_DATA")

        row = layout.row()
        row.label(text="Select other object!")
  #      row = layout.row()
  #      linha=row.operator("object.align_icp", text="ICP Align", icon="TRACKING_REFINE_FORWARDS")
        row = layout.row()
        linha=row.operator("object.force_icp", text="Force ICP Align (Slow)", icon="TRACKING_REFINE_FORWARDS")

        row = layout.row()
        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.5
        row.alignment = 'CENTER'
        row.operator("object.gera_dir_nome_paciente_alinha_foto_tomo", text="SAVE!", icon="FILE_TICK")

class ENUM_VALUES_ANATOMICAL:
    HEAD = 'Head'
    MAXILLA = 'Maxilla'
    MANDIBLE = 'Mandible'
    TEETH = 'Teeth'
    SOFTTISSUE = 'SoftTissue'


class ORTOG_PT_PontosAnatomicos(bpy.types.Panel):
    bl_label = "Anatomical Points"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.label(text="Mode:")

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        row.prop(scn, "my_enum_ana")

        my_enum_ana = scn.my_enum_ana

        if my_enum_ana == ENUM_VALUES_ANATOMICAL.HEAD:

            row = layout.row()
            linha=row.operator("object.orbital_right_pt", text="Orbital right")

            row = layout.row()
            linha=row.operator("object.orbital_left_pt", text="Orbital left")

            row = layout.row()
            linha=row.operator("object.n_pt", text="N point")

            row = layout.row()
            linha=row.operator("object.po_right", text="Po right")

            row = layout.row()
            linha=row.operator("object.po_left", text="Po left")

            row = layout.row()
            linha=row.operator("object.pt_right", text="Pt right")

            row = layout.row()
            linha=row.operator("object.pt_left", text="Pt left")

            row = layout.row()
            linha=row.operator("object.ba_pt", text="Ba point")

            row = layout.row()
            linha=row.operator("object.s_pt", text="S point")

            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.5
            row.alignment = 'CENTER'
            row.operator("object.gera_dir_nome_paciente_points_head", text="SAVE!", icon="FILE_TICK")


        if my_enum_ana == ENUM_VALUES_ANATOMICAL.MAXILLA:

            row = layout.row()
            linha=row.operator("object.u1_tip_pt", text="U1 Tip")

            row = layout.row()
            linha=row.operator("object.u1_labgenbor_pt", text="U1 Labial Gengival Border")

            row = layout.row()
            linha=row.operator("object.u1_lingenbor_pt", text="U1 Lingual Gengival Border")

            row = layout.row()
            linha=row.operator("object.u1_root_pt", text="U1 Root")

            row = layout.row()
            linha=row.operator("object.m_u6_pt", text="M U6")

            row = layout.row()
            linha=row.operator("object.d_u6_pt", text="D U6")

            row = layout.row()
            linha=row.operator("object.u6_occlusal_pt", text="U6 Occlusal")

            row = layout.row()
            linha=row.operator("object.pns_pt", text="PNS point")

            row = layout.row()
            linha=row.operator("object.a_pt", text="A point")

            row = layout.row()
            linha=row.operator("object.ans_pt", text="ANS point")

            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.5
            row.alignment = 'CENTER'
            row.operator("object.gera_dir_nome_paciente_points_maxilla", text="SAVE!", icon="FILE_TICK")


        if my_enum_ana == ENUM_VALUES_ANATOMICAL.MANDIBLE:

            row = layout.row()
            linha=row.operator("object.l1_tip_pt", text="L1 Tip")

            row = layout.row()
            linha=row.operator("object.l1_labgenbor_pt", text="L1 Labial Gengival Border")

            row = layout.row()
            linha=row.operator("object.l1_lingenbor_pt", text="L1 Lingual Gengival Border")

            row = layout.row()
            linha=row.operator("object.l1_root_pt", text="L1 Root")

            row = layout.row()
            linha=row.operator("object.b_pt", text="B point")

            row = layout.row()
            linha=row.operator("object.m_l6_pt", text="M L6")

            row = layout.row()
            linha=row.operator("object.l6_occlusal_pt", text="L6 Occlusal")

            row = layout.row()
            linha=row.operator("object.d_l6_pt", text="D L6")

            row = layout.row()
            linha=row.operator("object.mid_ramus_right_pt", text="Mid Ramus right")

            row = layout.row()
            linha=row.operator("object.mid_ramus_left_pt", text="Mid Ramus left")

            row = layout.row()
            linha=row.operator("object.r_right_pt", text="R right")

            row = layout.row()
            linha=row.operator("object.r_left_pt", text="R left")

            row = layout.row()
            linha=row.operator("object.go_right_pt", text="Go right")

            row = layout.row()
            linha=row.operator("object.go_left_pt", text="Go left")

            row = layout.row()
            linha=row.operator("object.ar_right_pt", text="Ar right")

            row = layout.row()
            linha=row.operator("object.ar_left_pt", text="Ar left")

            row = layout.row()
            linha=row.operator("object.sigmoid_right_pt", text="Sigmoid right")

            row = layout.row()
            linha=row.operator("object.sigmoid_left_pt", text="Sigmoid left")

            row = layout.row()
            linha=row.operator("object.co_right_pt", text="Co right")

            row = layout.row()
            linha=row.operator("object.co_left_pt", text="Co left")

            row = layout.row()
            linha=row.operator("object.pg_pt", text="Pg point")

            row = layout.row()
            linha=row.operator("object.gn_pt", text="Gn point")

            row = layout.row()
            linha=row.operator("object.me_pt", text="Me point")

            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.5
            row.alignment = 'CENTER'
            row.operator("object.gera_dir_nome_paciente_points_mandible", text="SAVE!", icon="FILE_TICK")


        if my_enum_ana == ENUM_VALUES_ANATOMICAL.TEETH:

            row = layout.row()
            row.label(text="Upper Teeth:")

            row = layout.row()
            linha=row.operator("object.tooth_8_pt", text="Tooth 8 (11)")

            row = layout.row()
            linha=row.operator("object.tooth_9_pt", text="Tooth 9 (21)")

            row = layout.row()
            linha=row.operator("object.tooth_6_pt", text="Tooth 6 (13)")

            row = layout.row()
            linha=row.operator("object.tooth_11_pt", text="Tooth 11 (23)")

            row = layout.row()
            linha=row.operator("object.tooth_3_pt", text="Tooth 3 (16)")

            row = layout.row()
            linha=row.operator("object.tooth_14_pt", text="Tooth 14 (26)")

            row = layout.row()
            row = layout.row()
            row.label(text="Lower Teeth:")

            row = layout.row()
            linha=row.operator("object.tooth_24_pt", text="Tooth 24 (31)")

            row = layout.row()
            linha=row.operator("object.tooth_25_pt", text="Tooth 25 (41)")

            row = layout.row()
            linha=row.operator("object.tooth_22_pt", text="Tooth 22 (33)")

            row = layout.row()
            linha=row.operator("object.tooth_27_pt", text="Tooth 27 (43)")

            row = layout.row()
            linha=row.operator("object.tooth_19_pt", text="Tooth 19 (36)")

            row = layout.row()
            linha=row.operator("object.tooth_30_pt", text="Tooth 30 (46)")

            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.5
            row.alignment = 'CENTER'
            row.operator("object.gera_dir_nome_paciente_points_teeth", text="SAVE!", icon="FILE_TICK")


        if my_enum_ana == ENUM_VALUES_ANATOMICAL.SOFTTISSUE:

            row = layout.row()
            linha=row.operator("object.st_glabella_pt", text="ST Glabella")

            row = layout.row()
            linha=row.operator("object.st_nasion_pt", text="ST Nasion")

            row = layout.row()
            linha=row.operator("object.bridge_nose_pt", text="Bridge of Nose")

            row = layout.row()
            linha=row.operator("object.tip_nose_pt", text="Tip of Nose")

            row = layout.row()
            linha=row.operator("object.columella_pt", text="Columella")

            row = layout.row()
            linha=row.operator("object.subnasale_pt", text="Subnasale")

            row = layout.row()
            linha=row.operator("object.st_a_point_pt", text="ST A point")

            row = layout.row()
            linha=row.operator("object.upper_lip_pt", text="Upper Lip")

            row = layout.row()
            linha=row.operator("object.stomion_superius_pt", text="Stomion Superius")

            row = layout.row()
            linha=row.operator("object.stomion_inferius_pt", text="Stomion Inferius")

            row = layout.row()
            linha=row.operator("object.lower_lip_pt", text="Lower Lip")

            row = layout.row()
            linha=row.operator("object.st_b_point_pt", text="ST B point")

            row = layout.row()
            linha=row.operator("object.st_pogonion_pt", text="ST Pogonion")

            row = layout.row()
            linha=row.operator("object.st_gnathion_pt", text="ST Gnathion")

            row = layout.row()
            linha=row.operator("object.st_menton_pt", text="ST Menton")

            row = layout.row()
            linha=row.operator("object.throat_point_pt", text="Throat point")

            row = layout.row()
            linha=row.operator("object.cb_right_pt", text="CB right")

            row = layout.row()
            linha=row.operator("object.cb_left_pt", text="CB left")

            row = layout.row()
            linha=row.operator("object.or_right_pt", text="OR' right")

            row = layout.row()
            linha=row.operator("object.or_left_pt", text="OR' left")

            row = layout.row()
            linha=row.operator("object.subpupil_right_pt", text="Subpupil right")

            row = layout.row()
            linha=row.operator("object.subpupil_left_pt", text="Subpupil left")

            row = layout.row()
            linha=row.operator("object.cheekbone_right_pt", text="Cheekbone right")

            row = layout.row()
            linha=row.operator("object.cheekbone_left_pt", text="Cheekbone left")

            row = layout.row()
            linha=row.operator("object.sp_right_pt", text="SP right")

            row = layout.row()
            linha=row.operator("object.sp_left_pt", text="SP left")

            row = layout.row()
            linha=row.operator("object.ab_right_pt", text="AB right")

            row = layout.row()
            linha=row.operator("object.ab_left_pt", text="AB left")

            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.5
            row.alignment = 'CENTER'
            row.operator("object.gera_dir_nome_paciente_points_soft", text="SAVE!", icon="FILE_TICK")

        row = layout.row()
        circle=row.operator("object.oculta_pontos_anatomicos", text="Hide Anatomical Points", icon="GHOST_DISABLED")

        row = layout.row()
        circle=row.operator("object.mostra_pontos_anatomicos", text="Show Anatomical Points", icon="GHOST_ENABLED")

class ENUM_VALUES_CEFALOMETRIA:
    USP = 'USP'
    ARNETT = 'ARNETT'

class ORTOG_PT_Cefalometria(bpy.types.Panel):
    bl_label = "Cephalometry"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        MaxOcPlane = "NONE"

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.label(text="Mode:")

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        row.prop(scn, "my_enum_cefalometria")

        my_enum_cefalometria = scn.my_enum_cefalometria

        if my_enum_cefalometria == ENUM_VALUES_CEFALOMETRIA.USP:

            # Plano oclusal maxila

            row = layout.row()
            circle=row.operator("object.mostra_pontos_anatomicos", text="Show Anatomical Points", icon="GHOST_ENABLED")

            row = layout.row()
            circle=row.operator("object.oculta_pontos_anatomicos", text="Hide Anatomical Points", icon="GHOST_DISABLED")

            row = layout.row()
            row.operator("object.calcula_tudo_usp", text="Calculate!!!", icon="PREFERENCES")


            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.operator("object.tooth_8_pt", text="Tooth 8 (11)")
            linha=row.operator("object.tooth_9_pt", text="Tooth 9 (21)")
            row = col.row()
            linha=row.operator("object.tooth_3_pt", text="Tooth 3 (16)")
            linha=row.operator("object.tooth_14_pt", text="Tooth 14 (26)")
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'CENTER'
            row.prop(context.scene, "plano_oclusal_maxila_classico")
            row = col.row()
            row.alignment = 'CENTER'
            row.label(text="4º-(8º)-12º")

            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            linha=row.operator("object.s_pt", text="S point")
            linha=row.operator("object.n_pt", text="N point")
            linha=row.operator("object.a_pt", text="A point")
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'CENTER'
            row.prop(context.scene, "angulo_sna")
            row = col.row()
            row.alignment = 'CENTER'
            row.label(text="> 82º Prognathic Maxilla (Class 2)")
            row = col.row()
            row.alignment = 'CENTER'
            row.label(text="< 82º Retrognathic Maxilla (Class 3)")


            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            linha=row.operator("object.s_pt", text="S point")
            linha=row.operator("object.n_pt", text="N point")
            linha=row.operator("object.b_pt", text="B point")
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'CENTER'
            row.prop(context.scene, "angulo_snb")
            row = col.row()
            row.alignment = 'CENTER'
            row.label(text="> 80º Prognathic Mandible")
            row = col.row()
            row.alignment = 'CENTER'
            row.label(text="< 80º Retrognathic Mandible")

            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            linha=row.operator("object.a_pt", text="A point")
            linha=row.operator("object.n_pt", text="N point")
            linha=row.operator("object.b_pt", text="B point")
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'CENTER'
            row.prop(context.scene, "angulo_anb")
            row = col.row()
            row.alignment = 'CENTER'
            row.label(text="0º-(2º)-4º")


            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            linha=row.operator("object.s_pt", text="S point")
            linha=row.operator("object.n_pt", text="N point")
            linha=row.operator("object.gn_pt", text="Gn point")
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'CENTER'
            row.prop(context.scene, "angulo_sngn")
            row = col.row()
            row.alignment = 'CENTER'
            row.label(text="65º-(67º)-69º")

            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            linha=row.operator("object.go_right_pt", text="Go right")
            linha=row.operator("object.go_left_pt", text="Go left")
            linha=row.operator("object.me_pt", text="Me point")
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'CENTER'
            row.prop(context.scene, "plano_mandibula_usp")
            row = col.row()
            row.alignment = 'CENTER'
            row.label(text="28º-(32º)-36º")


            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            linha=row.operator("object.s_pt", text="S point")
            linha=row.operator("object.n_pt", text="N point")
            row = col.row()
            linha=row.operator("object.go_right_pt", text="Go right")
            linha=row.operator("object.go_left_pt", text="Go left")
            linha=row.operator("object.gn_pt", text="Gn point")
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'CENTER'
            row.prop(context.scene, "angulo_sngogn")
            row = col.row()
            row.alignment = 'CENTER'
            row.label(text="28º-(32º)-36º")


        if my_enum_cefalometria == ENUM_VALUES_CEFALOMETRIA.ARNETT:

            row = layout.row()
            linha=row.operator("object.calcula_tudo_cefalo", text="Calculate All!!!", icon="PREFERENCES")

            row = layout.row()
            row = layout.row()


            row = layout.row()
            row.label(text="Angles:")

            # Plano oclusal maxila
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "plano_oclusal_maxila")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: 90º-120º Men: 85º-105º")

            # Ângulo nasolabial
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "angulo_nasolabial")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: 97.7º - 110.3º    Men: 98.7º - 114.1º") # Calculado

            # Ângulo Gn', Sn, Pog'
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "angulo_GbSnPog")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: 90º-120º Men: 85º-105º")

            row = layout.row()
            row.label(text="Distances:")

            # Glabella - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_glabella_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

            # Rima Orbital - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_rima_or_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

            # Mole malar - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_cheekbone_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

            # Subpupilar - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_subpupil_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

            # Proj. Nasal - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_proj_nasal_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

            # Base Nasal - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_base_nasal_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

            # A' - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_a_mole_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

            # Upper Lip - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_labio_superior_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

            # L1 - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_l1_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

            # U1 - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_u1_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

            # Lábio inferior - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_labio_inferior_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

            # B' - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_b_mole_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

            # Pog' - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_pog_mole_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

            # Pescoço-Garganta - LVV
            row = layout.row()
            row = layout.row()
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.scale_y=1.0
            row.alignment = 'RIGHT'
            row.prop(context.scene, "dist_pescoco_garganta_tvl")
            row = col.row()
            row.alignment = 'RIGHT'
            row.label(text="Women: -1 to 3 Men: -1 to 3")

bpy.types.Scene.angulo_sngogn = bpy.props.StringProperty \
    (
        name = "SNGoGn Angle",
        description = "SNGoGn Angle",
        default = "NONE"
    )
bpy.types.Scene.angulo_sna = bpy.props.StringProperty \
    (
        name = "SNA Angle",
        description = "SNA Angle",
        default = str("NONE"),
    )

bpy.types.Scene.angulo_snb = bpy.props.StringProperty \
    (
        name = "SNB Angle",
        description = "SNB Angle",
        default = str("NONE")
    )

bpy.types.Scene.angulo_anb = bpy.props.StringProperty \
    (
        name = "ANB Angle",
        description = "ANB Angle",
        default = "NONE"
    )
print("Falta algum ponto anatômico (ANB)!")

bpy.types.Scene.angulo_sngn = bpy.props.StringProperty \
    (
        name = "SNGn Angle",
        description = "SNGn Angle",
        default = "NONE"
    )

bpy.types.Scene.dist_pescoco_garganta_tvl = bpy.props.StringProperty \
    (
        name = "Throat point - TVL",
        description = "Throat point - TVL",
        default = "NONE"
    )

bpy.types.Scene.dist_pog_mole_tvl = bpy.props.StringProperty \
    (
        name = "ST Pogonion - TVL",
        description = "ST Pogonion - TVL",
        default = "NONE"
    )

bpy.types.Scene.dist_b_mole_tvl = bpy.props.StringProperty \
    (
        name = "ST B point - TVL",
        description = "ST B point - TVL",
        default = "NONE"
    )

bpy.types.Scene.dist_labio_inferior_tvl = bpy.props.StringProperty \
    (
        name = "Lower Lip - TVL",
        description = "Lower Lip - TVL",
        default = "NONE"
    )

bpy.types.Scene.dist_u1_tvl = bpy.props.StringProperty \
    (
        name = "U1 Tip - TVL",
        description = "U1 Tip - TVL",
        default = "NONE"
    )

bpy.types.Scene.dist_l1_tvl = bpy.props.StringProperty \
    (
        name = "L1 Tip - TVL",
        description = "L1 Tip - TVL",
        default = "NONE"
    )

bpy.types.Scene.dist_labio_superior_tvl = bpy.props.StringProperty \
    (
        name = "Upper Lip - TVL",
        description = "Upper Lip - TVL",
        default = "NONE"
    )

bpy.types.Scene.dist_a_mole_tvl = bpy.props.StringProperty \
    (
        name = "A' - TVL",
        description = "A' - TVL",
        default = "NONE"
    )

bpy.types.Scene.dist_base_nasal_tvl = bpy.props.StringProperty \
    (
        name = "AB - TVL",
        description = "AB - TVL",
        default = "NONE"
    )

bpy.types.Scene.dist_proj_nasal_tvl = bpy.props.StringProperty \
    (
        name = "Tip of Nose - TVL",
        description = "Tip of Nose - TVL",
        default = "NONE"
    )

bpy.types.Scene.dist_subpupil_tvl = bpy.props.StringProperty \
    (
        name = "Subpupil - TVL",
        description = "Subpupil - TVL",
        default = "NONE"
    )

bpy.types.Scene.dist_cheekbone_tvl = bpy.props.StringProperty \
    (
        name = "Cheekbone - TVL",
        description = "Cheekbone - TVL",
        default = "NONE"
    )

bpy.types.Scene.dist_rima_or_tvl = bpy.props.StringProperty \
    (
        name = "OR' - TVL",
        description = "OR' - TVL",
        default = "NONE"
    )

bpy.types.Scene.dist_glabella_tvl = bpy.props.StringProperty \
    (
        name = "Glabella - TVL",
        description = "Glabella - TVL",
        default = "NONE"
    )

bpy.types.Scene.plano_oclusal_maxila = bpy.props.StringProperty \
    (
        name = "Maxillary Occlusal Plane",
        description = "Maxillary Occlusal Plane",
        default = "NONE"
    )

bpy.types.Scene.angulo_nasolabial = bpy.props.StringProperty \
    (
        name = "Nasolabial Angle",
        description = "Nasolabial Angle",
        default = "NONE"
    )

bpy.types.Scene.angulo_GbSnPog = bpy.props.StringProperty \
	(
        name = "Gb', Sn, Pog' Angle",
        description = "Gb', Sn, Pog' Angle",
        default = str("NONE")
    )

class ENUM_VALUES_OSTEOTOMY:
    AUTO = 'Auto'
    MANUAL = 'Manual'
    BOOLEAN = 'Boolean'
    DRAW = 'Draw'

class ORTOG_PT_Osteotomia(bpy.types.Panel):
    bl_label = "Osteotomy"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.prop(scn, "my_enum_osteotomy")

        my_enum_ct = scn.my_enum_osteotomy

        if my_enum_ct == ENUM_VALUES_OSTEOTOMY.AUTO:

            row = layout.row()
            circle=row.operator("object.mostra_pontos_anatomicos", text="Show Anatomical Points", icon="GHOST_ENABLED")

            row = layout.row()
            circle=row.operator("object.oculta_pontos_anatomicos", text="Hide Anatomical Points", icon="GHOST_DISABLED")

            row = layout.row()
            linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
            linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

            row = layout.row()
            linha=row.operator("object.orbital_right_pt", text="Orbital right")
            linha=row.operator("object.orbital_left_pt", text="Orbital left")
            linha=row.operator("object.a_pt", text="A point")

            row = layout.row()
            linha=row.operator("object.tooth_30_pt", text="Tooth 30 (46)")
            linha=row.operator("object.go_right_pt", text="Go right")
            linha=row.operator("object.tooth_19_pt", text="Tooth 19 (36)")

            row = layout.row()
            linha=row.operator("object.go_left_pt", text="Go left")
            linha=row.operator("object.b_pt", text="B point")
            linha=row.operator("object.me_pt", text="Me point")

            row = layout.row()
            row = layout.row()
            circle=row.operator("object.adiciona_planos_corte_auto", text="Create Cut Planes!", icon="AXIS_TOP")


            row = layout.row()
            row.label(text="Pivot:")


            obj = context.active_object
            tool_settings = context.tool_settings

            object_mode = 'OBJECT' if obj is None else obj.mode

            if object_mode in {'OBJECT', 'EDIT', 'EDIT_GPENCIL', 'SCULPT_GPENCIL', 'WEIGHT_PAINT'} or has_pose_mode:
                layout.prop_with_popover(
                    tool_settings,
                    "transform_pivot_point",
                    text="",
                    icon_only=False,
                    panel="VIEW3D_PT_pivot_point",
                )

            row = layout.row()
            row = layout.row()
            row.label(text="Boolean:")

            row = layout.row()
            circle=row.operator("object.booleana_union_multipla", text="Join All (Union)", icon="GROUP")

            row = layout.row()
            circle=row.operator("object.booleana_osteo_geral", text="Cut Boolean", icon="MOD_BOOLEAN")


        if my_enum_ct == ENUM_VALUES_OSTEOTOMY.MANUAL:

            row = layout.row()
            circle=row.operator("mesh.add_mento", text="Chin Plane", icon="TRIA_DOWN")
            circle.location=(0,-35,-81)

            row = layout.row()
            circle=row.operator("mesh.add_ramo", text="Left Ramus Plane", icon="TRIA_RIGHT")
            circle.location=(36, -4, -45)

            row = layout.row()
            circle=row.operator("mesh.add_ramo", text="Right Ramus Plane", icon="TRIA_LEFT")
            circle.location=(-36, -4, -45)

            row = layout.row()
            circle=row.operator("mesh.add_maxila", text="Maxilla Plane", icon="TRIA_UP")
            circle.location=(0, -45, -31)

            row = layout.row()
            row = layout.row()
            row.label(text="Boolean:")

            row = layout.row()
            circle=row.operator("object.booleana_union_multipla", text="Join All (Union)", icon="GROUP")

            row = layout.row()
            circle=row.operator("object.booleana_osteo_geral", text="Cut Boolean", icon="MOD_BOOLEAN")

        if my_enum_ct == ENUM_VALUES_OSTEOTOMY.BOOLEAN:
            row = layout.row()
    #        row.operator("gpencil.annotate", icon='LINE_DATA', text="Draw Line").mode = 'DRAW_POLY'
            row.operator("object.linha_corte_fora_a_fora", icon='LINE_DATA', text="Draw Line")

            row = layout.row()
            row = layout.row()
            circle=row.operator("object.desenha_booleana_dentro", text="Subtract IN", icon="LIGHTPROBE_CUBEMAP")

            row = layout.row()
            circle=row.operator("object.desenha_booleana_fora", text="Subtract OUT", icon="MESH_CUBE")


        if my_enum_ct == ENUM_VALUES_OSTEOTOMY.DRAW:

            row = layout.row()
            row.operator("object.linha_corte", icon='LINE_DATA', text="Draw Surface Line")

            row = layout.row()
            circle=row.operator("object.desenha_linha_vertex", text="View Cut Line", icon="RESTRICT_VIEW_OFF")

            row = layout.row()
            circle=row.operator("object.desenha_linha_vertex_fin", text="Cut Visible Line", icon="SCULPTMODE_HLT")

        row = layout.row()
        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.5
        row.alignment = 'CENTER'
        row.operator("object.gera_dir_nome_paciente_osteotomy", text="SAVE!", icon="FILE_TICK")





class ENUM_VALUES_DYNAMIC:
    DEFAULT = 'Default'
    NOSE = 'Nose'
    EXPERIMENTAL = 'Experimental'

class ORTOG_PT_ArmatureDynamic(bpy.types.Panel):
    bl_label = "Dynamic"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.prop(scn, "my_enum_dynamic")

        my_enum_dynamic = scn.my_enum_dynamic

        if my_enum_dynamic == ENUM_VALUES_DYNAMIC.DEFAULT:

            row = layout.row()
            row.label(text="Configure Armature (Classic):")

            row = layout.row()
            row.operator("object.conf_osteo_auto", text="Setup Osteotomy Auto", icon="FILE_TICK")

            row = layout.row()
            row.label(text="Soft Tissue:")

            row = layout.row()
            circle=row.operator("object.configura_dinamica_mole", text="Setup Soft Tissue Dynamics", icon="STYLUS_PRESSURE")

            row = layout.row()
            circle=row.operator("view3d.clip_border", text="Clipping Border", icon="UV_FACESEL")

        if my_enum_dynamic == ENUM_VALUES_DYNAMIC.NOSE:

            row = layout.row()
            row.operator("object.conf_osteo_auto", text="Setup Osteotomy Auto", icon="FILE_TICK")

            row = layout.row()
            row.label(text="Mode:")

            row = layout.row()
            linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
            linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

            row = layout.row()
            row = layout.row()
            row.label(text="Anatomical Points:")

            row = layout.row()
            linha=row.operator("object.trichion_pt", text="Trichion")

            row = layout.row()
            linha=row.operator("object.radix_pt", text="Radix")

            row = layout.row()
            linha=row.operator("object.tip_nose_pt", text="Tip of Nose")

            row = layout.row()
            linha=row.operator("object.alar_groove_right_pt", text="Alar Groove right")

            row = layout.row()
            linha=row.operator("object.alar_groove_left_pt", text="Alar Groove left")

            row = layout.row()
            linha=row.operator("object.submental_pt", text="Submental")

            row = layout.row()
            row = layout.row()
            row.label(text="Soft Tissue:")

            row = layout.row()
            circle=row.operator("object.configura_dinamica_mole", text="Setup Soft Tissue Dynamics", icon="STYLUS_PRESSURE")

            row = layout.row()
            circle=row.operator("view3d.clip_border", text="Clipping Border", icon="UV_FACESEL")

        if my_enum_dynamic == ENUM_VALUES_DYNAMIC.EXPERIMENTAL:

            row = layout.row()
            row.label(text=" Auto Osteo+Soft Setup (Experimental):")

            row = layout.row()
            row.operator("object.nome_face_malha", text="Set Face and Hide", icon="USER")

            row = layout.row()
            row.operator("object.conf_osteo_mole_auto", text="Setup Auto!", icon="BONE_DATA")

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
        row.operator("object.gera_dir_nome_paciente_dynamic", text="SAVE!", icon="FILE_TICK")

class ORTOG_PT_CinematicaPanel(bpy.types.Panel):
    bl_label = "Kinematic"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Mode:")

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        row.label(text="Pivot Rotation:")


        obj = context.active_object
        tool_settings = context.tool_settings

        object_mode = 'OBJECT' if obj is None else obj.mode

        if object_mode in {'OBJECT', 'EDIT', 'EDIT_GPENCIL', 'SCULPT_GPENCIL', 'WEIGHT_PAINT'} or has_pose_mode:
            layout.prop_with_popover(
                tool_settings,
                "transform_pivot_point",
                text="",
                icon_only=False,
                panel="VIEW3D_PT_pivot_point",
            )

        row = layout.row()
        row.label(text="Reference Lines:")

        row = layout.row()
        linha=row.operator("mesh.add_linhabase", text="Vertical Center Line", icon="SORT_DESC")
        linha.location=(0,-200,0)

        row = layout.row()
        linha=row.operator("mesh.add_linhabase", text="Horizontal Center Line", icon="FORWARD")
        linha.location=(0,-200,0)
        linha.rotation=(0,1.5708,0)

        row = layout.row()
        linha=row.operator("mesh.add_linhabase", text="Horizontal Side Line", icon="FORWARD")
        linha.location=(200,30,0)
        linha.rotation=(1.5708,0,0)


        row = layout.row()
        row = layout.row()
        row.label(text="Upper Teeth:")

        row = layout.row()
        circle=row.operator("object.oculta_pontos_anatomicos", text="Hide Anatomical Points", icon="GHOST_DISABLED")

        row = layout.row()
        circle=row.operator("object.mostra_pontos_anatomicos", text="Show Anatomical Points", icon="GHOST_ENABLED")

        row = layout.row()
        row = layout.row()
        linha=row.operator("object.tooth_8_pt", text="Tooth 8 (11)")
        linha=row.operator("object.tooth_9_pt", text="Tooth 9 (21)")

        row = layout.row()
        linha=row.operator("object.tooth_6_pt", text="Tooth 6 (13)")
        linha=row.operator("object.tooth_11_pt", text="Tooth 11 (23)")

        row = layout.row()
        linha=row.operator("object.tooth_3_pt", text="Tooth 3 (16)")
        linha=row.operator("object.tooth_14_pt", text="Tooth 14 (26)")


        row = layout.row()
        row = layout.row()
        row.label(text="Vertical Measurements:")

        row = layout.row()
        row.operator("object.medverhor_dentes", text="Create Vertical Measurements", icon="DRIVER_DISTANCE")

        row = layout.row()
        row.operator("measureit.runopengl", text="Show/Hide Measurements", icon="GHOST_ENABLED")

        row = layout.row()
        row = layout.row()
        row.operator("object.apaga_pontos_objetos", text="Delete Measure", icon="CANCEL")

       	row = layout.row()
        row = layout.row()
        row.label(text="Parent Points:")

        row = layout.row()
        circle=row.operator("object.parenteia_emp", text="Parent Points", icon="LINKED")

#        row = layout.row()
#        row.operator("object.transforms_to_deltas", text="PUT Loc/Rot/Scale TO ZERO", icon="EMPTY_AXIS").mode='ALL'
#        bpy.ops.object.transforms_to_deltas(mode='ALL')

        try:
            cursor = context.active_object

            layout.column().prop(cursor, "location", text="Location")
            rotation_mode = cursor.rotation_mode
            if rotation_mode == 'QUATERNION':
                layout.column().prop(cursor, "rotation_quaternion", text="Rotation")
            elif rotation_mode == 'AXIS_ANGLE':
                layout.column().prop(cursor, "rotation_axis_angle", text="Rotation")
            else:
                layout.column().prop(cursor, "rotation_euler", text="Rotation")
            layout.prop(cursor, "rotation_mode", text="")
        except:
            print("Selectione objeto!")

#bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
#bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'


        row = layout.row()
        row.label(text="Controllers:")

        row = layout.row()
        row.operator("screen.frame_jump", text="Start", icon="TRIA_LEFT_BAR").end=False
        row.operator("screen.animation_play", text="", icon="PLAY_REVERSE").reverse=True
        row.operator("anim.ortog_loc_rot", text="", icon="VIEW_CAMERA")
        row.operator("screen.animation_play", text="", icon="PLAY")
        row.operator("screen.frame_jump", text="End", icon="TRIA_RIGHT_BAR").end=True

        row = layout.row()
        row.label(text="Align with Models:")

        row = layout.row()
        linha=row.operator("object.prepara_mandibula_cm", text="Prepare Mandible", icon="MESH_DATA")

        row = layout.row()
        row.operator("import_mesh.stl", text="Import STL", icon="IMPORT")

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        linha=row.operator("object.emp1a", text="Point 1a - Origin", icon="SORTBYEXT")

        row = layout.row()
        linha=row.operator("object.emp1b", text="Point 1b - Align", icon="SORTBYEXT")

        row = layout.row()
        row = layout.row()
        linha=row.operator("object.emp2a", text="Point 2a - Origin", icon="SORTBYEXT")

        row = layout.row()
        linha=row.operator("object.emp2b", text="Point 2b - Align", icon="SORTBYEXT")

        row = layout.row()
        row = layout.row()
        linha=row.operator("object.emp3a", text="Point 3a - Origin", icon="SORTBYEXT")

        row = layout.row()
        linha=row.operator("object.emp3b", text="Point 3b - Align", icon="SORTBYEXT")

        row = layout.row()
        linha=row.operator("object.alinha_tres_pontos", text="ALIGN!", icon="MESH_DATA")

        row = layout.row()
        linha=row.operator("object.force_icp", text="Force ICP Align (Slow)", icon="TRACKING_REFINE_FORWARDS")

        row = layout.row()
        row = layout.row()
        linha=row.operator("object.finaliza_mandibula_cm", text="Finish Mandible", icon="MESH_DATA")



        row = layout.row()
        row.label(text="Mandible Collision:")

        row = layout.row()
        row.operator("object.prepara_maxila_mandibula", text="Prepares Maxilla & Mandible", icon="SHADERFX")

        row = layout.row()
        row = layout.row()
        linha=row.operator("object.colisao_arcos_inverso", text="Solve Collision Inverted", icon="STYLUS_PRESSURE")

        row = layout.row()
        linha=row.operator("object.aplica_anima_cor", text="Contact Color", icon="COLORSET_01_VEC")

        row = layout.row()
        row = layout.row()
        linha=row.operator("object.finaliza_colisao_max_mand", text="Apply!!!", icon="FREEZE")



        row = layout.row()
        row.label(text="Piggyback:")

        row = layout.row()
        row.label(text="1) Select son(s)")
        row = layout.row()
        row.label(text="2) Select father")

        row = layout.row()
        row.operator("object.parenteia_objetos", text="MAKE PARENT", icon="RESTRICT_VIEW_OFF")

        row = layout.row()
        row = layout.row()
        row.operator("object.desparenteia_objetos", text="Clear Parent", icon="UNLINKED")

        row = layout.row()
        row.label(text="Capturing:")

        row = layout.row()
        row.operator("object.gera_deslocamento_todos", text="Generate Data Action", icon="FULLSCREEN_ENTER")

        row = layout.row()
        row.label(text="Spreadsheet:")

        row = layout.row()
        row.operator("object.gera_relatorio", text="GENERATE REPORT", icon="SHORTDISPLAY")

        row = layout.row()
        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.5
        row.alignment = 'CENTER'
        row.operator("object.gera_dir_nome_paciente_kinematic", text="SAVE!", icon="FILE_TICK")

class ORTOG_PT_FechaLabios(bpy.types.Panel):
    bl_label = "Close Lips"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

#        row = layout.row()
#        row.label(text="Close Lips:")

        row = layout.row()
        row.operator("object.cria_shape_keys", text="Create Shape Keys", icon="MOD_SIMPLEDEFORM")

        row = layout.row()
        ob = context.object
        key = ob.data.shape_keys
        kb = ob.active_shape_key

        enable_edit = ob.mode != 'EDIT'
        enable_edit_value = False

        if ob.show_only_shape_key is False:
            if enable_edit or (ob.type == 'MESH' and ob.use_shape_key_edit_mode):
                enable_edit_value = True

        if key.use_relative:
            if ob.active_shape_key_index != 0:
                layout.use_property_split = True

                row = layout.row()
                row.active = enable_edit_value
                row.prop(kb, "value")

                row = layout.row()
                linha=row.operator("object.escultura_grab", text="Grab", icon="BRUSH_GRAB")

                row = layout.row()
                linha=row.operator("object.escultura_smooth", text="Smooth", icon="BRUSH_SMOOTH")

                row = layout.row()
                linha=row.operator("object.escultura_mask", text="Mask", icon="BRUSH_MASK")

                row = layout.row()
                linha=row.operator("object.mode_set", text="OK! (Object Mode)", icon="META_CUBE").mode='OBJECT'

class ENUM_VALUES_ARCHSCOLLISION:
    DEFAULT = 'Default'
    INVERTED = 'Inverted'

class ORTOG_PT_GuideCreation(bpy.types.Panel):
    bl_label = "Guide and Splint Creation"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Ortog"

    def draw(self, context):

        context = bpy.context
        scn = context.scene

        layout = self.layout

        row = layout.row()
        row.label(text="Free Draw Solid:")

        row = layout.row()
        row.operator("object.linha_corte", icon='LINE_DATA', text="Draw Surface Line")

        row = layout.row()
        row.operator("object.desenha_guia", text="Create Solid by Line", icon="META_ELLIPSOID")

        row = layout.row()
        row.label(text="Draw Line Tube:")

        row = layout.row()
        row.operator("wm.modal_cria_pontos", icon='CURVE_DATA', text="Create Points")

#        row = layout.row()
#        row.operator("mesh.add_linha_pontos", icon='LINE_DATA', text="Create Object")

        row = layout.row()
        row.operator("mesh.add_curva_bezier", icon='MESH_CYLINDER', text="Create Bezier Volume")

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
        row.label(text="Sculpture:")

        row = layout.row()
        linha=row.operator("object.forensic_escultura_grab", text="Grab", icon="BRUSH_GRAB")

        row = layout.row()
        linha=row.operator("object.forensic_escultura_smooth", text="Smooth", icon="BRUSH_SMOOTH")

        row = layout.row()
        linha=row.operator("object.forensic_escultura_clay_strips", text="Clay Strips", icon="BRUSH_CLAY_STRIPS")

        row = layout.row()
        linha=row.operator("object.mode_set", text="OK! (Object Mode)", icon="META_CUBE").mode='OBJECT'

        row = layout.row()
        row.label(text="Teeth Points:")

        row = layout.row()
        circle=row.operator("object.oculta_pontos_anatomicos", text="Hide Anatomical Points", icon="GHOST_DISABLED")

        row = layout.row()
        circle=row.operator("object.mostra_pontos_anatomicos", text="Show Anatomical Points", icon="GHOST_ENABLED")

        row = layout.row()
        row = layout.row()
        linha=row.operator("object.pontos_oculta_nomes", text="Hide Names", icon="GHOST_DISABLED")

        row = layout.row()
        linha=row.operator("object.pontos_mostra_nomes", text="Show Names", icon="GHOST_ENABLED")

        row = layout.row()
        row.label(text="Mode:")

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"
        linha=row.operator("wm.tool_set_by_id", text="Select", icon="RESTRICT_SELECT_OFF").name="builtin.select_box"

        row = layout.row()
        linha=row.operator("object.tooth_8_pt", text="Tooth 8 (11)")
        linha=row.operator("object.tooth_9_pt", text="Tooth 9 (21)")
        row = layout.row()
        linha=row.operator("object.tooth_6_pt", text="Tooth 6 (13)")
        linha=row.operator("object.tooth_11_pt", text="Tooth 11 (23)")
        row = layout.row()
        linha=row.operator("object.tooth_3_pt", text="Tooth 3 (16)")
        linha=row.operator("object.tooth_14_pt", text="Tooth 14 (26)")

        row = layout.row()
        row = layout.row()
        row = layout.row()
        linha=row.operator("object.tooth_24_pt", text="Tooth 24 (31)")
        linha=row.operator("object.tooth_25_pt", text="Tooth 25 (41)")

        row = layout.row()
        linha=row.operator("object.tooth_22_pt", text="Tooth 22 (33)")
        linha=row.operator("object.tooth_27_pt", text="Tooth 27 (43)")

        row = layout.row()
        linha=row.operator("object.tooth_19_pt", text="Tooth 19 (36)")
        linha=row.operator("object.tooth_30_pt", text="Tooth 30 (46)")

        row = layout.row()
        linha=row.operator("object.head_of_condyle_pt", text="Condyle Rotation Point")

        row = layout.row()
        row = layout.row()
        row = layout.row()
        circle=row.operator("object.parenteia_emp", text="Parent Points", icon="LINKED")

        row = layout.row()
        row.label(text="Splint:")

        row = layout.row()
        row.operator("object.splint_maxila_origi_mand_final", text="Maxilla-Origin Mandible-Final", icon="GROUP_BONE")

        row = layout.row()
        row.operator("screen.frame_jump", text="Start", icon="TRIA_LEFT_BAR").end=False
        row.operator("screen.animation_play", text="", icon="PLAY_REVERSE").reverse=True
        row.operator("anim.ortog_loc_rot", text="", icon="VIEW_CAMERA")
        row.operator("screen.animation_play", text="", icon="PLAY")
        row.operator("screen.frame_jump", text="End", icon="TRIA_RIGHT_BAR").end=True

        row = layout.row()
        row.operator("object.cria_splint", text="Create Splint", icon="OUTLINER_OB_CURVE")

#        row = layout.row()
#        row.operator("object.duplica_max_mand", text="Prepares Maxilla & Mandible", icon="SHADERFX")

        row = layout.row()
        circle=row.operator("object.boolean_splint", text="Boolean Difference", icon="MOD_BOOLEAN")

        row = layout.row()
        row.operator("object.visualiza_max_mand", text="View Maxilla & Mandible", icon="VISIBLE_IPO_ON")

# ----------------------
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row.label(text="Collision Test:")

        row = layout.row()
        row.prop(scn, "my_enum_archscollision")

        my_enum_ct = scn.my_enum_archscollision

        if my_enum_ct == ENUM_VALUES_ARCHSCOLLISION.DEFAULT:

            row = layout.row()
            linha=row.operator("object.colisao_arcos", text="Solve Collision Default", icon="STYLUS_PRESSURE")

            row = layout.row()
            row = layout.row()
            linha=row.operator("object.aplica_anima_cor", text="Contact Color", icon="COLORSET_01_VEC")

            row = layout.row()
            row.label(text="Press ESC to enable Apply!")

            row = layout.row()
            linha=row.operator("object.trava_arco", text="Apply!", icon="FREEZE")


        if my_enum_ct == ENUM_VALUES_ARCHSCOLLISION.INVERTED:

            row = layout.row()
            linha=row.operator("object.colisao_arcos_inverso", text="Solve Collision Inverted", icon="STYLUS_PRESSURE")

            row = layout.row()
            row = layout.row()
            linha=row.operator("object.aplica_anima_cor", text="Contact Color", icon="COLORSET_01_VEC")

            row = layout.row()
            row.label(text="Press ESC to enable Apply!")

            row = layout.row()
            linha=row.operator("object.trava_arco", text="Apply!", icon="FREEZE")

# ----------------------


        row = layout.row()
        row = layout.row()
        row.label(text="Finishing")

        row = layout.row()
        row.operator("object.prepara_impressao_3d", text="Prepares 3D Printing", icon="META_CUBE")

        row = layout.row()

        row.operator("export_mesh.stl", text="Export STL", icon="TRACKING_REFINE_FORWARDS").use_selection=True#.use_mesh_modifiers=True

        row = layout.row()
        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.5
        row.alignment = 'CENTER'
        row.operator("object.gera_dir_nome_paciente_guide", text="SAVE!", icon="FILE_TICK")


class ORTOG_PT_ImportTomoImg(bpy.types.Panel):
    bl_label = "Importing & Editing CT-Scan"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Ortog"
#    bl_category = "Image"

    def draw(self, context):
        layout = self.layout
#        layout.use_property_split = True

#        row = layout.row()
#        row.label(text="Free Draw Solid:")

        row = layout.row()
        row.operator("object.importa_img_tomo", text="Import CT-Scan IMG Slices", icon="IMAGE_DATA")

        row = layout.row(align = True)
        row.prop(context.scene, "IMGPathSeq")

        row = layout.row(align = True)
        row.prop(context.scene, "SliceThickness")

        row = layout.row(align = True)
        row.prop(context.scene, "PixelSpacingX")

        row = layout.row(align = True)
        row.prop(context.scene, "PixelSpacingY")

        row = layout.row(align = True)
        row.prop(context.scene, "IMGDimX")

        row = layout.row(align = True)
        row.prop(context.scene, "IMGDimY")

        row = layout.row()
        row = layout.row()
        row.operator("image.save_sequence", text="Save Sequence", icon="EXPORT")

        row = layout.row()
        row.operator("object.exporta_img_tomo", text="Export DICOM Slices", icon="EXPORT")



def register():
    bpy.utils.register_class(EMP1a)
    bpy.utils.register_class(EMP2a)
    bpy.utils.register_class(EMP3a)
    bpy.utils.register_class(EMP1b)
    bpy.utils.register_class(EMP2b)
    bpy.utils.register_class(EMP3b)
    bpy.utils.register_class(Orbital_right_pt)
    bpy.utils.register_class(Orbital_left_pt)
    bpy.utils.register_class(N_pt)
    bpy.utils.register_class(Po_right_pt)
    bpy.utils.register_class(Po_left_pt)
    bpy.utils.register_class(Pt_right_pt)
    bpy.utils.register_class(Pt_left_pt)
    bpy.utils.register_class(Ba_pt)
    bpy.utils.register_class(S_pt)
    bpy.utils.register_class(U1_Tip_pt)
    bpy.utils.register_class(U1_LabGenBor_pt)
    bpy.utils.register_class(U1_LinGenBor_pt)
    bpy.utils.register_class(M_U6_pt)
    bpy.utils.register_class(D_U6_pt)
    bpy.utils.register_class(U6_Occlusal_pt)
    bpy.utils.register_class(PNS_pt)
    bpy.utils.register_class(A_pt)
    bpy.utils.register_class(ANS_pt)
    bpy.utils.register_class(U1_Root_pt)
    bpy.utils.register_class(L1_Tip_pt)
    bpy.utils.register_class(L1_Root_pt)
    bpy.utils.register_class(L1_LabGenBor_pt)
    bpy.utils.register_class(L1_LinGenBor_pt)
    bpy.utils.register_class(B_pt)
    bpy.utils.register_class(M_L6_pt)
    bpy.utils.register_class(L6_Occlusal_pt)
    bpy.utils.register_class(ORTOG_UI_Local)
    bpy.utils.register_class(D_L6_pt)
    bpy.utils.register_class(MidRamusRight_pt)
    bpy.utils.register_class(MidRamusLeft_pt)
    bpy.utils.register_class(R_right_pt)
    bpy.utils.register_class(R_left_pt)
    bpy.utils.register_class(Go_right_pt)
    bpy.utils.register_class(Go_left_pt)
    bpy.utils.register_class(Ar_right_pt)
    bpy.utils.register_class(Ar_left_pt)
    bpy.utils.register_class(Sigmoid_right_pt)
    bpy.utils.register_class(Sigmoid_left_pt)
    bpy.utils.register_class(Co_right_pt)
    bpy.utils.register_class(Co_left_pt)
    bpy.utils.register_class(Pg_pt)
    bpy.utils.register_class(Gn_pt)
    bpy.utils.register_class(Me_pt)
    bpy.types.Scene.my_tool = PointerProperty(type=ORTOG_UI_Local)
    bpy.utils.register_class(ORTOG_PT_AtualizaAddonSec)
    bpy.utils.register_class(ORTOG_PT_NomePaciente)
    bpy.types.Scene.nome_paciente = bpy.props.StringProperty \
      (
        name = "Name",
        description = "Patient's name",
        default = ""
      )
    bpy.types.Scene.sobrenome_paciente = bpy.props.StringProperty \
      (
        name = "Surname",
        description = "Patient's surname",
        default = ""
      )
    bpy.utils.register_class(AtualizaScript)
    bpy.utils.register_class(AreasInfluencia)
    bpy.utils.register_class(CriaAreasDeformacao)
    bpy.utils.register_class(ConfiguraDinamicaMole)
    bpy.utils.register_class(ConfiguraMento)
    bpy.utils.register_class(ConfiguraCorpoMand)
    bpy.utils.register_class(ConfiguraRamoEsq)
    bpy.utils.register_class(ConfiguraRamoDir)
    bpy.utils.register_class(ConfiguraMaxila)
    bpy.utils.register_class(ConfiguraCabeca)
    bpy.utils.register_class(ImportaArmature)
    bpy.utils.register_class(ConfOsteotomiaAuto)
    bpy.utils.register_class(BooleanaOsteoGeral)
    bpy.utils.register_class(CriaMaxila)
    bpy.utils.register_class(CriaRamo)
    bpy.utils.register_class(CriaMento)
    bpy.utils.register_class(DesenhaLinhaVertex)
    bpy.utils.register_class(DesenhaLinhaVertexFin)
    bpy.utils.register_class(BooleanaOsteoClass)
    bpy.utils.register_class(DesenhaLinhaCorte)
    bpy.utils.register_class(LinhaCorte)
    bpy.utils.register_class(SegmentaDesenho)
    bpy.utils.register_class(BooleanaMand)
    bpy.utils.register_class(MantemPintado)
    bpy.utils.register_class(ApagaPintado)
    bpy.utils.register_class(Weight0)
    bpy.utils.register_class(Weight1)
    bpy.utils.register_class(SegmentaLinked)
    bpy.utils.register_class(LinhaBase)
    bpy.utils.register_class(ORTOG_PT_CTScanSelect)
#    bpy.utils.register_class(ORTOG_PT_CTScanOrgFIX)
    bpy.utils.register_class(CorrigeDicom)
    bpy.utils.register_class(AjustaTomo)
    bpy.types.Scene.my_enum_ct = bpy.props.EnumProperty(
        name="Select",
        description= "",
        items=[(ENUM_VALUES_CTSCAN.MANUAL, "MANUAL", "Manual CT-Scan Reconstruction"), (ENUM_VALUES_CTSCAN.VOXEL, "VOXEL", "Voxel Data CT-Scan Reconstruction"), (ENUM_VALUES_CTSCAN.AUTO, "AUTOMATIC", "Automatic CT-Scan Reconstruction"), (ENUM_VALUES_CTSCAN.CUSTOM, "CUSTOM", "Customized CT-Scan Reconstruction")],)
    bpy.utils.register_class(GeraModelosTomo)
#    bpy.utils.register_class(ORTOG_PT_CTScanFerrImg)
#    bpy.utils.register_class(ORTOG_PT_CTScanRec)


    bpy.types.Scene.interesse_geral = bpy.props.StringProperty \
      (
        name = "Reconst. Factor",
        description = "Reconstruction Factor",
        default = "NONE"
      )

    bpy.types.Scene.fator_simplificacao = bpy.props.StringProperty \
      (
        name = "Decimate Factor",
        description = "Decimate Factor",
        default = "0.90"
      )

    bpy.types.Scene.nome_objeto = bpy.props.StringProperty \
      (
        name = "Object Name",
        description = "Object Name",
        default = "CT-Scan Reconstructed"
      )

    bpy.types.Scene.interesse_ossos = bpy.props.StringProperty \
      (
        name = "Bone Factor",
        description = "Fatos interesse ossos",
        default = "200"
      )
    bpy.types.Scene.interesse_mole = bpy.props.StringProperty \
      (
        name = "Soft Factor",
        description = "Fatos interesse mole",
        default = "-300"
      )
    bpy.types.Scene.interesse_dentes = bpy.props.StringProperty \
      (
        name = "Teeth Factor",
        description = "Fatos interesse dentes",
        default = "1430"
      )
    bpy.utils.register_class(ORTOG_PT_GraphicRefs)

    bpy.types.Scene.interesse_arco = bpy.props.StringProperty \
      (
        name = "Factor",
        description = "Fatos interesse arco",
        default = "226"
      )

    bpy.types.Scene.my_enum_archscollision = bpy.props.EnumProperty(
        name="Select",
        description= "",
        items=[(ENUM_VALUES_ARCHSCOLLISION.DEFAULT, "DEFAULT", "Default gravity."), (ENUM_VALUES_ARCHSCOLLISION.INVERTED, "INVERTED", "Inverted gravity.")],)

    bpy.utils.register_class(ORTOG_PT_ImportaArc)
#    bpy.data.scenes['Scene'].render.filepath
    bpy.utils.register_class(AlinhaTresPontos)
    bpy.utils.register_class(ORTOG_OT_GeraModelosTomoArc)
    bpy.utils.register_class(ORTOG_PT_Segmentation)
    bpy.utils.register_class(ORTOG_PT_SegmentacaoFace)
    bpy.types.Scene.d_factor = bpy.props.StringProperty \
      (
        name = "D Factor",
        description = "D Factor",
        default = "6"
      )
    bpy.types.Scene.smooth_factor = bpy.props.StringProperty \
      (
        name = "Smooth Factor",
        description = "Smooth Factor",
        default = "16"
      )

    bpy.types.Scene.my_enum = bpy.props.EnumProperty(
        name="Select",
        description= "",
        items=[(ENUM_VALUES_PHOTOGRAMMETRY.OPENMVG, "OpenMVG+OpenMVS", "Standard Photogrammetry"), (ENUM_VALUES_PHOTOGRAMMETRY.SMVS, "SMVS+MeshLab", "Alternative Photogrammetry I"), (ENUM_VALUES_PHOTOGRAMMETRY.MESHROOM, "Meshroom (AliceVision)", "Alternative Photogrammetry II")],)

    bpy.utils.register_class(ORTOG_PT_Fotogrametria)
    bpy.utils.register_class(ORTOG_PT_AlinhaFace)
    bpy.utils.register_class(ORTOG_PT_FotogramModif)
    bpy.utils.register_class(ORTOG_PT_AlinhaFaceCT)
    bpy.utils.register_class(ORTOG_PT_PontosAnatomicos)
    bpy.types.Scene.plano_oclusal_maxila_classico = bpy.props.StringProperty \
        (
            name = "Maxillary Occlusal Angle",
            description = "Maxilla Occlusal",
            default = "NONE"
        )
    bpy.types.Scene.my_enum_ana = bpy.props.EnumProperty(
        name="Select",
        description= "",
        items=[(ENUM_VALUES_ANATOMICAL.HEAD, "HEAD", "Head Points"), (ENUM_VALUES_ANATOMICAL.MAXILLA, "MAXILLA", "Maxilla Points"), (ENUM_VALUES_ANATOMICAL.MANDIBLE, "MANDIBLE", "Mandible Points"), (ENUM_VALUES_ANATOMICAL.TEETH, "TEETH", "Teeth Points"), (ENUM_VALUES_ANATOMICAL.SOFTTISSUE, "SOFT TISSUE", "Soft Tissue Points")],)
#    bpy.utils.register_class(ORTOG_PT_PontosAnatomicosCabeca)
#    bpy.utils.register_class(ORTOG_PT_PontosAnatomicosMaxila)
#    bpy.utils.register_class(ORTOG_PT_PontosAnatomicosMandibula)
#    bpy.utils.register_class(ORTOG_PT_PontosAnatomicosDentes)
#    bpy.utils.register_class(ORTOG_PT_PontosAnatomicosMole)
    bpy.types.Scene.my_enum_cefalometria = bpy.props.EnumProperty(
        name="Select",
        description= "",
        items=[(ENUM_VALUES_CEFALOMETRIA.USP, "USP", "USP Cephalometry."), (ENUM_VALUES_CEFALOMETRIA.ARNETT, "ARNETT", "ARNETT Cephalometry.")],)
    bpy.types.Scene.plano_mandibula_usp = bpy.props.StringProperty \
        (
            name = "Mandibular Plane",
            description = "Mandibular Plane",
            default = "NONE"
        )
    bpy.utils.register_class(ORTOG_PT_Cefalometria)
    bpy.types.Scene.my_enum_osteotomy = bpy.props.EnumProperty(
        name="Select",
        description= "",
        items=[(ENUM_VALUES_OSTEOTOMY.AUTO, "AUTO", "Automatic Ostetotomy Cut Planes"), (ENUM_VALUES_OSTEOTOMY.MANUAL, "MANUAL", "Manual Ostetotomy Cut Planes"), (ENUM_VALUES_OSTEOTOMY.BOOLEAN, "BOOLEAN", "Boolean Ostetotomy Cut"), (ENUM_VALUES_OSTEOTOMY.DRAW, "DRAW", "Draw Ostetotomy")],)
    bpy.utils.register_class(ORTOG_PT_Osteotomia)
    bpy.types.Scene.medida_real2 = bpy.props.StringProperty \
      (
        name = "Real Size",
        description = "Real size distance between eyes",
        default = "None"
      )
    bpy.types.Scene.my_enum_dynamic = bpy.props.EnumProperty(
        name="Select",
        description= "",
        items=[(ENUM_VALUES_DYNAMIC.DEFAULT, "DEFAULT", "Default dynamic."), (ENUM_VALUES_DYNAMIC.NOSE, "NOSE EXP.", "Better deformation of nose."), (ENUM_VALUES_DYNAMIC.EXPERIMENTAL, "EXPERIMENTAL SLICES", "Dynamic with indetermined slices.")],)
    bpy.utils.register_class(ORTOG_PT_ArmatureDynamic)
    bpy.utils.register_class(ORTOG_PT_CinematicaPanel)
    bpy.utils.register_class(ORTOG_PT_FechaLabios)
    bpy.utils.register_class(ORTOG_PT_GuideCreation)
    bpy.utils.register_class(ORTOG_PT_ImportTomoImg)
    bpy.types.Scene.IMGPathSeq = bpy.props.StringProperty \
      (
        name = "IMGPathSeq",
        description = "IMGPathSeq",
        default = "NONE"
      )
    bpy.types.Scene.SliceThickness = bpy.props.StringProperty \
      (
        name = "SliceThickness",
        description = "Slice Thickness",
        default = "NONE"
      )

    bpy.types.Scene.PixelSpacingX = bpy.props.StringProperty \
      (
        name = "PixelSpacingX",
        description = "Pixel SpacingX",
        default = "NONE"
      )

    bpy.types.Scene.PixelSpacingY = bpy.props.StringProperty \
      (
        name = "PixelSpacingY",
        description = "Pixel SpacingY",
        default = "NONE"
      )

    bpy.types.Scene.IMGDimX = bpy.props.StringProperty \
      (
        name = "IMGDimX",
        description = "IMGDimX",
        default = "NONE"
      )

    bpy.types.Scene.IMGDimY = bpy.props.StringProperty \
      (
        name = "IMGDimY",
        description = "IMGDimY",
        default = "NONE"
      )



def unregister():
    bpy.utils.unregister_class(NomePaciente)
    bpy.utils.unregister_class(NomePacienteTomo)
    bpy.utils.unregister_class(NomePacienteArc)
    bpy.utils.unregister_class(NomePacienteRef)
    bpy.utils.unregister_class(NomePacienteSeg)
    bpy.utils.unregister_class(NomePacienteFotogram)
    bpy.utils.unregister_class(ORTOG_PT_NomePaciente)
    bpy.utils.unregister_class(Orbital_right_pt)
    bpy.utils.unregister_class(Orbital_left_pt)
    bpy.utils.unregister_class(N_pt)
    bpy.utils.unregister_class(Po_right_pt)
    bpy.utils.unregister_class(Po_left_pt)
    bpy.utils.unregister_class(Pt_right_pt)
    bpy.utils.unregister_class(Pt_left_pt)
    bpy.utils.unregister_class(Ba_pt)
    bpy.utils.unregister_class(S_pt)
    bpy.utils.unregister_class(U1_Tip_pt)
    bpy.utils.unregister_class(U1_LabGenBor_pt)
    bpy.utils.unregister_class(U1_LinGenBor_pt)
    bpy.utils.unregister_class(M_U6_pt)
    bpy.utils.unregister_class(D_U6_pt)
    bpy.utils.unregister_class(U6_Occlusal_pt)
    bpy.utils.unregister_class(PNS_pt)
    bpy.utils.unregister_class(A_pt)
    bpy.utils.unregister_class(ANS_pt)
    bpy.utils.unregister_class(L1_Tip_pt)
    bpy.utils.register_class(U1_Root_pt)
    bpy.utils.unregister_class(L1_LabGenBor_pt)
    bpy.utils.unregister_class(L1_LinGenBor_pt)
    bpy.utils.unregister_class(B_pt)
    bpy.utils.unregister_class(M_L6_pt)
    bpy.utils.unregister_class(L6_Occlusal_pt)
    bpy.utils.unregister_class(D_L6_pt)
    bpy.utils.unregister_class(MidRamusRight_pt)
    bpy.utils.unregister_class(MidRamusLeft_pt)
    bpy.utils.unregister_class(R_right_pt)
    bpy.utils.unregister_class(R_left_pt)
    bpy.utils.unregister_class(Go_right_pt)
    bpy.utils.unregister_class(Go_left_pt)
    bpy.utils.unregister_class(Ar_right_pt)
    bpy.utils.unregister_class(Ar_left_pt)
    bpy.utils.unregister_class(Sigmoid_right_pt)
    bpy.utils.unregister_class(Sigmoid_left_pt)
    bpy.utils.unregister_class(Co_right_pt)
    bpy.utils.unregister_class(Co_left_pt)
    bpy.utils.unregister_class(Pg_pt)
    bpy.utils.unregister_class(Gn_pt)
    bpy.utils.unregister_class(Me_pt)
    bpy.utils.unregister_class(ORTOG_PT_AtualizaAddonSec)
    bpy.utils.unregister_class(AtualizaScript)
    bpy.utils.unregister_class(AreasInfluencia)
    bpy.utils.unregister_class(CriaAreasDeformacao)
    bpy.utils.unregister_class(ConfiguraDinamicaMole)
    bpy.utils.unregister_class(ConfiguraMento)
    bpy.utils.unregister_class(ConfiguraCorpoMand)
    bpy.utils.unregister_class(ConfiguraRamoEsq)
    bpy.utils.unregister_class(ConfiguraRamoDir)
    bpy.utils.unregister_class(ConfiguraMaxila)
    bpy.utils.unregister_class(ConfiguraCabeca)
    bpy.utils.unregister_class(ImportaArmature)
    bpy.utils.unregister_class(ConfOsteotomiaAuto)
    bpy.utils.unregister_class(BooleanaOsteoGeral)
    bpy.utils.unregister_class(CriaMaxila)
    bpy.utils.unregister_class(CriaRamo)
    bpy.utils.unregister_class(CriaMento)
    bpy.utils.unregister_class(DesenhaLinhaVertex)
    bpy.utils.unregister_class(DesenhaLinhaVertexFin)
    bpy.utils.unregister_class(BooleanaOsteoClass)
    bpy.utils.unregister_class(DesenhaLinhaCorte)
    bpy.utils.unregister_class(LinhaCorte)
    bpy.utils.unregister_class(AlinhaTresPontos)
    bpy.utils.unregister_class(SegmentaDesenho)
    bpy.utils.unregister_class(BooleanaMand)
    bpy.utils.unregister_class(MantemPintado)
    bpy.utils.unregister_class(ApagaPintado)
    bpy.utils.unregister_class(Weight0)
    bpy.utils.unregister_class(Weight1)
    bpy.utils.unregister_class(SegmentaLinked)
    bpy.utils.unregister_class(LinhaBase)
#    bpy.utils.unregister_class(ORTOG_PT_CTScanOrgFIX)
    bpy.utils.unregister_class(CorrigeDicom)
    bpy.utils.unregister_class(AjustaTomo)
    bpy.utils.unregister_class(GeraModelosTomo)
#    bpy.utils.unregister_class(ORTOG_PT_CTScanFerrImg)
#    bpy.utils.unregister_class(CTScanRec)
    bpy.utils.unregister_class(ORTOG_PT_ImportaArc)
    bpy.utils.unregister_class(ORTOG_UI_CapturaLocal)
    bpy.utils.unregister_class(ORTOG_OT_GeraModelosTomoArc)
    bpy.utils.unregister_class(ORTOG_PT_GraphicRefs)
    bpy.utils.unregister_class(ORTOG_PT_Segmentation)
    bpy.utils.unregister_class(ORTOG_PT_Fotogrametria)
    bpy.utils.unregister_class(ORTOG_PT_AlinhaFace)
    bpy.utils.unregister_class(ORTOG_PT_FotogramModif)
    bpy.utils.unregister_class(ORTOG_PT_AlinhaFaceCT)
#    bpy.utils.unregister_class(ORTOG_PT_PontosAnatomicosCabeca)
#    bpy.utils.unregister_class(ORTOG_PT_PontosAnatomicosMaxila)
#    bpy.utils.unregister_class(ORTOG_PT_PontosAnatomicosMandibula)
#    bpy.utils.unregister_class(ORTOG_PT_PontosAnatomicosDentes)
#    bpy.utils.unregister_class(ORTOG_PT_PontosAnatomicosMole)
    bpy.utils.unregister_class(ORTOG_PT_Cefalometria)
    bpy.utils.unregister_class(ORTOG_PT_Osteotomia)
    del bpy.types.Scene.medida_real2
    bpy.utils.unregister_class(EMP1a)
    bpy.utils.unregister_class(EMP2a)
    bpy.utils.unregister_class(EMP3a)
    bpy.utils.unregister_class(EMP1b)
    bpy.utils.unregister_class(EMP2b)
    bpy.utils.unregister_class(EMP3b)
    bpy.utils.unregister_class(ORTOG_PT_ArmatureDynamic)
    bpy.utils.unregister_class(ORTOG_PT_CinematicaPanel)
    bpy.utils.unregister_class(ORTOG_PT_GuideCreation)
    bpy.utils.unregister_class(ORTOG_PT_ImportTomoImg)

if __name__ == "__main__":
    register()
