bl_info = {
    "name": "OrtogOnBlender",
    "author": "Cicero Moraes and Everton da Rosa",
    "version": (1, 0),
    "blender": (2, 7, 8),
    "location": "Tool Shelf",
    "description": "Interface to use Cork library for advanced boolean operations",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"}

import bpy

text = bpy.data.texts['Ramo.py']
ctx = bpy.context.copy()
ctx['edit_text'] = text
bpy.ops.text.run_script(ctx)

text2 = bpy.data.texts['PreparaImpressao.py']
ctx2 = bpy.context.copy()
ctx2['edit_text'] = text2
bpy.ops.text.run_script(ctx2)

text3 = bpy.data.texts['Mento.py']
ctx3 = bpy.context.copy()
ctx3['edit_text'] = text3
bpy.ops.text.run_script(ctx3)

text4 = bpy.data.texts['Maxila.py']
ctx4 = bpy.context.copy()
ctx4['edit_text'] = text4
bpy.ops.text.run_script(ctx4)

text5 = bpy.data.texts['CriaEspessura.py']
ctx5 = bpy.context.copy()
ctx5['edit_text'] = text5
bpy.ops.text.run_script(ctx5)

text6 = bpy.data.texts['CriaAreasDeformacao.py']
ctx6 = bpy.context.copy()
ctx6['edit_text'] = text6
bpy.ops.text.run_script(ctx6)

text7 = bpy.data.texts['AreasInfluencia.py']
ctx7 = bpy.context.copy()
ctx7['edit_text'] = text7
bpy.ops.text.run_script(ctx7)

# APAGA TUDO
class LimparCena(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Limpar Cena"
    bl_idname = "limpar_cena"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("object.select_all", text="Selecionar tudo", icon="HAND")
        
        row = layout.row()
        row.operator("object.delete", text="Apagar", icon="X")
        
        
#IMPORTA STL
  
class OOB_import_stl(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Importar Reconstrução Tomo"
    bl_idname = "import_stl"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("import_mesh.stl", text="Importa STL", icon="IMPORT")
        
        row = layout.row()
        row.operator("view3d.view_all", text="Centraliza Zoom", icon="VIEWZOOM").center=False

        
#IMPORTA OBJ
   
class OOB_import_obj(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Importar Fotogrametria"
    bl_idname = "import_obj"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("import_scene.obj", text="Importa OBJ", icon="MOD_MASK")
        #ORIGINAL bpy.ops.import_mesh.stl()
        
        row = layout.row()
        circle=row.operator("mesh.primitive_circle_add", text="Círculo de Corte", icon="MESH_CIRCLE")
        circle.radius=200
        circle.vertices=100
        circle.location=(85,-185,0)
        circle.rotation=(0,1.5708,0)
        
        row = layout.row()
        knife=row.operator("mesh.knife_project", text="Cortar!", icon="META_PLANE")
        knife.cut_through=True
        
        row = layout.row()
        circle=row.operator("mesh.separate", text="Separa Face", icon="GROUP_VERTEX")
        circle.type='SELECTED'
 
            
# IMPORTA CEFALOMETRIA

class ImportaCefalometria(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Importar Cefalometria"
    bl_idname = "Importa_Cefalometria"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("import_image.to_plane", text="Importa Imagem", icon="FILE_IMAGE")

#ALINHA FACES

class AlinhaFaces(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Alinha Faces"
    bl_idname = "alinha_faces"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("object.align_picked_points", text="Alinha por Pontos", icon="PARTICLE_TIP")

        row = layout.row()
        row.operator("object.align_icp", text="Alinha ICP", icon="PARTICLE_PATH")
    

# OSTEOTOMIA

class Osteotomia(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Osteotomia"
    bl_idname = "Object_Name"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        
        obj = context.object
        
        
        row = layout.row()
        circle=row.operator("mesh.add_mento", text="Plano Mento", icon="TRIA_DOWN")
        circle.location=(0,-35,-81)
        
        row = layout.row()
        circle=row.operator("mesh.add_ramo", text="Plano Ramo Esquerdo", icon="TRIA_RIGHT")
        circle.location=(36, -4, -45)
        
        row = layout.row()
        circle=row.operator("mesh.add_ramo", text="Plano Ramo Direito", icon="TRIA_LEFT")
        circle.location=(-36, -4, -45)
        
        row = layout.row()
        circle=row.operator("mesh.add_maxila", text="Plano Maxila", icon="TRIA_UP")
        circle.location=(0, -45, -31)
 
        row = layout.row()
        circle=row.operator("object.join", text="Junta Tudo", icon="GROUP")
    
        
        row = layout.row()
        circle=row.operator("object.cria_espessura", text="Cria Espessura", icon="MOD_SOLIDIFY")
               
        row = layout.row()
        #circle=row.operator("import_image.to_plane", text="Habilita Planos de Corte", icon="BONE_DATA")
        circle=row.operator("view3d.cork_mesh_slicer", text="Boolean Cortes", icon="MOD_BOOLEAN")
        circle.method='DIFF'
        
        # Não é necessário estar em Object Mode
        row = layout.row()
        circle=row.operator("mesh.separate", text="Separa Osteotomia", icon="GROUP_VERTEX")
        circle.type='LOOSE'
        
        row = layout.row()
        #row.label(text="Nome Atual: " + obj.name)
        row = layout.row()
        row.prop(obj, "name", text="Renomear ")
        
        

        
class DinamicaMole(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Dinâmica do Mole"
    bl_idname = "Dinamica_Mole"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        
        obj = context.object
              
        row = layout.row()
        circle=row.operator("object.areas_influencia", text="Gera Grupos Influêcia", icon="GROUP_VCOL")
        
        row = layout.row()
        circle=row.operator("object.cria_areas_deformacao", text="Cria Áreas de Deformação", icon="STYLUS_PRESSURE")
        
        row = layout.row()
        circle=row.operator("object.convert", text="Aplica Deformação", icon="FILE_TICK").target='MESH'

        row = layout.row()
        circle=row.operator("object.parent_set", text="Parentear Estrutura", icon="BONE_DATA").type='ARMATURE'



class CriaSplint(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Criação do Splint"
    bl_idname = "Cria_Splint"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        
        obj = context.object
        
        row = layout.row()
        circle=row.operator("view3d.cork_mesh_slicer", text="Boolean Splint", icon="MOD_BOOLEAN")
        circle.method='DIFF'
        
        row = layout.row()
        row.operator("object.prepara_impressao", text="Prepara Impressão 3D", icon="MOD_REMESH")
        #row.prop(obj.modifiers["Remesh"], "octree_depth", text="Subdivisão")
        
        row = layout.row()
        row.operator("export_mesh.stl", text="Exporta STL", icon="EXPORT")


def register():
    bpy.utils.register_class(LimparCena)
    bpy.utils.register_class(OOB_import_stl)
    bpy.utils.register_class(OOB_import_obj)
    bpy.utils.register_class(ImportaCefalometria)
    bpy.utils.register_class(AlinhaFaces)
    bpy.utils.register_class(Osteotomia)
    bpy.utils.register_class(DinamicaMole)
    bpy.utils.register_class(CriaSplint)



def unregister():
    bpy.utils.unregister_class(LimparCena)
    bpy.utils.unregister_class(OOB_import_stl)
    bpy.utils.unregister_class(OOB_import_obj)
    bpy.utils.unregister_class(ImportaCefalometria)
    bpy.utils.unregister_class(AlinhaFaces)
    bpy.utils.unregister_class(Osteotomia)
    bpy.utils.unregister_class(DinamicaMole)
    bpy.utils.unregister_class(CriaSplint)


if __name__ == "__main__":
    register()
