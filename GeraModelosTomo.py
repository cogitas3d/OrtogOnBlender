import bpy
import platform
import tempfile
import subprocess
from os.path import expanduser

from .ImportaObjMat import *

# ERROS

def ERROruntimeDICOMDef(self, context):
    self.layout.label("Doesn't have DICOM path!")

def ERROTermDICOM():
     CRED = '\033[91m'
     CEND = '\033[0m'
     print(CRED + "Doesn't have DICOM path!" + CEND)

# FUNÇÃO RECONSTRUÇÃO

def ReconTomo(pathdir, interes, saida, simplif):

    context = bpy.context
    obj = context.object
    scn = context.scene
    
#    tmpdir = tempfile.gettempdir()

    tmpdir = tempfile.mkdtemp()

    tmpSTL = tmpdir+'/'+saida+'.stl'

    homeall = expanduser("~")


    if scn.my_tool.path == "":
        ERROTermDICOM()
        bpy.context.window_manager.popup_menu(ERROruntimeDICOMDef, title="Attention!", icon='INFO')

    else:


        if platform.system() == "Linux":


            dicom2DtlPath = homeall+'/Programs/OrtogOnBlender/Dicom2Mesh/dicom2mesh'
    


        if platform.system() == "Windows":

            dicom2DtlPath = 'C:/OrtogOnBlender/DicomToMeshWin/dicom2mesh.exe'



        if platform.system() == "Darwin":

            dicom2DtlPath = '/OrtogOnBlender/DicomToMeshMAC/dicom2mesh'


        subprocess.call([dicom2DtlPath, '-i',  pathdir, '-r', simplif, '-s', '-t', interes, '-o', tmpSTL])
        bpy.ops.import_mesh.stl(filepath=tmpSTL, filter_glob="*.stl",  files=[{"name":saida+".stl", "name":saida+".stl"}], directory=tmpdir)
  
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        bpy.ops.view3d.view_all(center=False)

# GERA MODELO CABEÇA

def GeraModelosTomoDef(self, context):

    context = bpy.context
    obj = context.object
    scn = context.scene

    interesseOssos = bpy.context.scene.interesse_ossos
    interesseMole = bpy.context.scene.interesse_mole
    interesseDentes = bpy.context.scene.interesse_dentes

    ReconTomo(scn.my_tool.path, interesseOssos, 'Bones','0.90')
    ReconTomo(scn.my_tool.path, interesseMole, 'SoftTissue','0.90')
    ReconTomo(scn.my_tool.path, interesseDentes, 'Teeth','0.90')


    a = bpy.data.objects['Bones']
    b = bpy.data.objects['SoftTissue']
    c = bpy.data.objects['Teeth']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    bpy.ops.object.select_all(action='DESELECT')
    b.select = True
    bpy.context.scene.objects.active = b
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')


    bpy.ops.object.select_all(action='DESELECT')
    c.select = True
    bpy.context.scene.objects.active = c
    bpy.ops.object.shade_smooth()
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    c.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()

    bpy.ops.transform.rotate(value=3.14159, axis=(0, 1, 0), constraint_axis=(False, True, False),
                                 constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED',
                                 proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=3.14159, axis=(0, 0, 1), constraint_axis=(False, False, True),
                                 constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED',
                                 proportional_edit_falloff='SMOOTH', proportional_size=1)
                                 
    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0

    bpy.ops.view3d.view_all(center=False)

    impMaterial = 'SCATTER_bone'
    SelObj = 'Bones'
    ImportaMaterial(impMaterial, SelObj)

    impMaterial = 'SCATTER_skin'
    SelObj = 'SoftTissue'
    ImportaMaterial(impMaterial, SelObj)

    impMaterial = 'SCATTER_teeth'
    SelObj = 'Teeth'
    ImportaMaterial(impMaterial, SelObj)

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    bpy.context.scene.objects.active = a

class GeraModelosTomo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_modelos_tomo"
    bl_label = "Prepara Impressao"
    
    def execute(self, context):
        GeraModelosTomoDef(self, context)
        return {'FINISHED'}

# CEFALOMETRIA

def ConfiguraCefaloDef(self, context):
    
    scn = context.scene

    ImportaLampXRay()

    bpy.context.scene.render.engine = 'CYCLES' # Troca tipo renderização

    bpy.context.scene.cycles.transparent_max_bounces = 32 # Não permite áreas escuras na renderização!
    bpy.context.scene.world.horizon_color = (0, 0, 0)
    bpy.context.scene.cycles.preview_samples = 5
    bpy.context.scene.cycles.samples = 5
    bpy.context.space_data.show_relationship_lines = False
#        bpy.context.space_data.display_mode = 'GROUPS' # Erro
    ImportaCefalo()
    ImportaCamXray()
    bpy.context.scene.render.resolution_y = 1920
    bpy.context.scene.render.resolution_percentage = 100

# Cria grupo de linhas
'''
    bpy.ops.object.select_all(action='DESELECT')

    listaGrupoLinhas = [bpy.data.objects['Line_Occlusal'], bpy.data.objects['Line_Insisor_lower'], bpy.data.objects['Line_Insisor_upper'], bpy.data.objects['Line_Me_Go'], bpy.data.objects['Line_N_A'], bpy.data.objects['Line_N_B'], bpy.data.objects['Line_Pg_Ls'], bpy.data.objects['Line_Or_Po'], bpy.data.objects['Line_NS']]

    a = 0

    NumObj = len(listaGrupoLinhas)

    while a < NumObj:
        b = listaGrupoLinhas[a].select = True
        a += 1

    bpy.context.scene.objects.active = listaGrupoLinhas[0]
    bpy.ops.group.create(name="2D_cephalometry_lines")

    bpy.ops.object.select_all(action='DESELECT')

#    SplitAreaTrabalho()

#    except RuntimeError:
#        bpy.context.window_manager.popup_menu(ERROruntimeDICOMDef, title="Atenção!", icon='INFO')

'''

# GERA MODELO ARCADA

def GeraModelosTomoArcDef(self, context):
    
    scn = context.scene
    
    tmpdir = tempfile.gettempdir()
    tmpSTLarcada = tmpdir+'/Arcada.stl'

    homeall = expanduser("~")


    if scn.my_tool.path == "":
        ERROTermDICOM()
        bpy.context.window_manager.popup_menu(ERROruntimeDICOMDef, title="Attention!", icon='INFO')

    else:


        if platform.system() == "Linux":


            dicom2DtlPath = homeall+'/Programs/OrtogOnBlender/Dicom2Mesh/dicom2mesh'
    


        if platform.system() == "Windows":

            dicom2DtlPath = 'C:/OrtogOnBlender/DicomToMeshWin/dicom2mesh.exe'



        if platform.system() == "Darwin":

            dicom2DtlPath = '/OrtogOnBlender/DicomToMeshMAC/dicom2mesh'


        subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.5', '-s', '-t', '226', '-o', tmpSTLarcada])
        bpy.ops.import_mesh.stl(filepath=tmpSTLarcada, filter_glob="*.stl",  files=[{"name":"Arcada.stl", "name":"Arcada.stl"}], directory=tmpdir)
  
        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
        bpy.ops.view3d.view_all(center=False)

#    except RuntimeError:
#        bpy.context.window_manager.popup_menu(ERROruntimeDICOMDef, title="Atenção!", icon='INFO')

def ChangeSolidXRayDef(self, context):
    
    scn = context.scene

    if bpy.context.scene.render.engine == 'BLENDER_RENDER':
        bpy.context.scene.render.engine = 'CYCLES'
#        print("Está Blender")
    
    elif bpy.context.scene.render.engine == 'CYCLES':
        bpy.context.scene.render.engine = 'BLENDER_RENDER'
#        print("Está Cycles")

def ChangeRenderEngineDef(self, context):
    
    scn = context.scene

    if bpy.context.scene.render.engine == 'BLENDER_RENDER':
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.space_data.viewport_shade = 'RENDERED'
        print("Blender render")

#        print("Está Blender")
    
    elif bpy.context.scene.render.engine == 'CYCLES':
        bpy.context.scene.render.engine = 'BLENDER_RENDER'
        bpy.context.space_data.viewport_shade = 'SOLID'
        print("Renderizado")
#        print("Está Cycles")
