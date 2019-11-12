import bpy
import platform

from .ForensicTools import *

class FORENSIC_PT_Fotogrametria(bpy.types.Panel):
    bl_label = "Photogrammetry Start"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Forensic"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.label(text="OpenMVG+OpenMVS:")

        row = layout.row()
        col = layout.column(align=True)
        col.prop(scn.my_tool, "path", text="")

        col = self.layout.column(align = True)
        col.alignment = 'RIGHT'
        col.prop(context.scene, "d_factorForensic")
        col.prop(context.scene, "smooth_factorForensic")

        if platform.system() == "Windows":
            row = layout.row()
            row.operator("wm.console_toggle", text="Open Terminal?", icon="CONSOLE")

        row = layout.row()
        row.operator("object.gera_modelo_foto", text="Start Photogrammetry!", icon="IMAGE_DATA")

        row = layout.row()
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.scale_y=1.5
        row.alignment = 'CENTER'
        row.operator("object.gera_dir_nome_paciente_fotogram", text="SAVE!", icon="FILE_TICK")

bpy.utils.register_class(FORENSIC_PT_Fotogrametria)

bpy.types.Scene.d_factorForensic = bpy.props.StringProperty \
  (
    name = "D FactorForensic",
    description = "D FactorForensic",
    default = "5"
  )
bpy.types.Scene.smooth_factorForensic = bpy.props.StringProperty \
  (
    name = "Smooth Factor",
    description = "Smooth Factor",
    default = "5"
  )

class FORENSIC_PT_AlinhaFace(bpy.types.Panel):
    bl_label = "Photogrammetry - Align & Scale"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Forensic"

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

bpy.utils.register_class(FORENSIC_PT_AlinhaFace)

class FORENSIC_PT_ColocaMarcadores(bpy.types.Panel):
    bl_label = "Soft Tissue Markers"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Forensic"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        linha=row.operator("wm.tool_set_by_id", text="Cursor", icon="PIVOT_CURSOR").name="builtin.cursor"

        row = layout.row()
        row = layout.row()
        row.label(text="Create Custom Marker:")

        col = self.layout.column(align = True)
        col.prop(context.scene, "nome_marcador")

        col = self.layout.column(align = True)
        col.prop(context.scene, "dimensao_marcador")

        row = layout.row()
        linha=row.operator("object.adiciona_marcador", text="Create Marker", icon="EMPTY_SINGLE_ARROW")

        row = layout.row()
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row.label(text="Import CSV Sheet:")

        row = layout.row()
        col = layout.column(align=True)
        col.prop(scn.my_tool, "filepathcsv", text="")

        row = layout.row()
        linha=row.operator("object.forensic_cria_botoes", text="Generate Soft Tissue Markers!", icon="EMPTY_SINGLE_ARROW")

        row = layout.row()
        row = layout.row()
        linha=row.operator("object.oculta_nomes", text="Hide Names", icon="HIDE_ON")

        row = layout.row()
        linha=row.operator("mesh.add_linhabase", text="Vertical Center Line", icon="SORT_DESC")
        linha.location=(0,-200,0)

        row = layout.row()
        linha=row.operator("object.engrossa_linha", text="Make Tube Line", icon="OUTLINER_OB_CURVE")

        row = layout.row()
        linha=row.operator("object.forensic_importa_olho", text="Import Eye", icon="HIDE_OFF")

bpy.utils.register_class(FORENSIC_PT_ColocaMarcadores)

bpy.types.Scene.nome_marcador = bpy.props.StringProperty \
  (
    name = "Name",
    description = "Object Size",
    default = "Marker"
  )

bpy.types.Scene.dimensao_marcador = bpy.props.StringProperty \
  (
    name = "Size",
    description = "Object Size",
    default = "None"
  )

class FORENSIC_PT_Musculos(bpy.types.Panel):
    bl_label = "Muscles"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Forensic"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        linha=row.operator("object.forensic_importa_temporalis", text="Temporalis")

        row = layout.row()
        linha=row.operator("object.forensic_importa_masseter", text="Masseter")

        row = layout.row()
        linha=row.operator("object.forensic_importa_orbicularis_oculi", text="Orbicularis Oculi")

        row = layout.row()
        linha=row.operator("object.forensic_importa_elevator_labii_superioris", text="Elevator Labii Superioris")

        row = layout.row()
        linha=row.operator("object.forensic_importa_nasalis", text="Nasalis")

        row = layout.row()
        linha=row.operator("object.forensic_importa_zygomaticus", text="Zygomaticus")

        row = layout.row()
        linha=row.operator("object.forensic_importa_orbicularis_oris", text="Orbicularis Oris")

        row = layout.row()
        linha=row.operator("object.forensic_importa_buccinator", text="Buccinator")

        row = layout.row()
        linha=row.operator("object.forensic_importa_mentalis", text="Mentalis+")

        row = layout.row()
        linha=row.operator("object.forensic_importa_sternocleidomastoid", text="Sternocleidomastoid+")

        row = layout.row()
        row.label(text="Deform Muscle:")

        row = layout.row()
        linha=row.operator("object.forensic_escultura_grab", text="Grab", icon="BRUSH_GRAB")

        row = layout.row()
        linha=row.operator("object.forensic_escultura_smooth", text="Smooth", icon="BRUSH_SMOOTH")

        row = layout.row()
        linha=row.operator("object.forensic_escultura_clay_strips", text="Clay Strips", icon="BRUSH_CLAY_STRIPS")

        row = layout.row()
        linha=row.operator("object.mode_set", text="OK! (Object Mode)", icon="META_CUBE").mode='OBJECT'

        row = layout.row()
        linha=row.operator("object.forensic_copia_espelha", text="Copy & Mirror", icon="MOD_TRIANGULATE")


bpy.utils.register_class(FORENSIC_PT_Musculos)


class FORENSIC_PT_FaceBasica(bpy.types.Panel):
    bl_label = "Basic Face Sculpt"
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Forensic"

    def draw(self, context):
        layout = self.layout

        context = bpy.context
        obj = context.object
        scn = context.scene

        row = layout.row()
        row.label(text="1) Put all structure in the origin of scene.")

        row = layout.row()
        row.label(text="2) Select all interest muscules.")

        row = layout.row()
        row.label(text="3) Create Basic Shape!")

        row = layout.row()
        linha=row.operator("object.forensic_cria_face_basica", text="Create Basic Shape!", icon="MESH_ICOSPHERE")


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

bpy.utils.register_class(FORENSIC_PT_FaceBasica)
