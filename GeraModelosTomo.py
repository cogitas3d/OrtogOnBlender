import bpy
import platform
import tempfile
from os.path import expanduser
import subprocess

# GERA MODELO CABEÇA

def GeraModelosTomoDef(self, context):
    
    scn = context.scene
    
    tmpdir = tempfile.gettempdir()
    tmpSTLossos = tmpdir+'/ossos.stl'
    tmpSTLmole = tmpdir+'/mole.stl'

    homeall = expanduser("~")

    try:


        if platform.system() == "Linux":

            dicom2DtlPath = homeall+'/Programs/OrtogOnBlender/Dicom2Mesh/dicom2mesh'
#            dicom2DtlPath = get_dicom2stl_filepath(context)


            interesseOssos = bpy.context.scene.interesse_ossos
            interesseMole = bpy.context.scene.interesse_mole


            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', interesseOssos, '-o', tmpSTLossos])
	      

            bpy.ops.import_mesh.stl(filepath=tmpSTLossos, filter_glob="*.stl",  files=[{"name":"ossos.stl", "name":"ossos.stl"}], directory=tmpdir)
		
            bpy.ops.view3d.view_all(center=False)

            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', interesseMole, '-o', tmpSTLmole])

# CASO DIDATICO
#            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', '65', '-o', tmpSTLmole])

            bpy.ops.import_mesh.stl(filepath=tmpSTLmole, filter_glob="*.stl",  files=[{"name":"mole.stl", "name":"mole.stl"}], directory=tmpdir)


        if platform.system() == "Windows":

            dicom2DtlPath = 'C:/OrtogOnBlender/DicomToMeshWin/dicom2mesh.exe'

            interesseOssos = bpy.context.scene.interesse_ossos
            interesseMole = bpy.context.scene.interesse_mole


            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', interesseOssos, '-o', tmpSTLossos])
	      

            bpy.ops.import_mesh.stl(filepath=tmpSTLossos, filter_glob="*.stl",  files=[{"name":"ossos.stl", "name":"ossos.stl"}], directory=tmpdir)
		
            bpy.ops.view3d.view_all(center=False)
	      

            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', interesseMole, '-o', tmpSTLmole])

            bpy.ops.import_mesh.stl(filepath=tmpSTLmole, filter_glob="*.stl",  files=[{"name":"mole.stl", "name":"mole.stl"}], directory=tmpdir)


        if platform.system() == "Darwin":


            dicom2DtlPath = '/OrtogOnBlender/DicomToMeshMAC/dicom2mesh'

            interesseOssos = bpy.context.scene.interesse_ossos
            interesseMole = bpy.context.scene.interesse_mole

#            dicom2DtlPath = get_dicom2stl_filepath(context)


            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', interesseOssos, '-o', tmpSTLossos])
	      

            bpy.ops.import_mesh.stl(filepath=tmpSTLossos, filter_glob="*.stl",  files=[{"name":"ossos.stl", "name":"ossos.stl"}], directory=tmpdir)
		
            bpy.ops.view3d.view_all(center=False)
	      

            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', interesseMole, '-o', tmpSTLmole])

            bpy.ops.import_mesh.stl(filepath=tmpSTLmole, filter_glob="*.stl",  files=[{"name":"mole.stl", "name":"mole.stl"}], directory=tmpdir)


        a = bpy.data.objects['Ossos']
        b = bpy.data.objects['Mole']

        bpy.ops.object.select_all(action='DESELECT')
        a.select = True
        bpy.context.scene.objects.active = a
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

        bpy.ops.object.select_all(action='DESELECT')
        b.select = True
        bpy.context.scene.objects.active = b
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

        bpy.ops.object.select_all(action='DESELECT')
        a.select = True
        b.select = True 
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

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDICOMDef, title="Atenção!", icon='INFO')

# GERA MODELO ARCADA

def GeraModelosTomoArcDef(self, context):
    
    scn = context.scene
    
    tmpdir = tempfile.gettempdir()
    tmpSTLarcada = tmpdir+'/Arcada.stl'

    homeall = expanduser("~")

    try:


        if platform.system() == "Linux":


            dicom2DtlPath = homeall+'/Programs/OrtogOnBlender/Dicom2Mesh/dicom2mesh'
#            dicom2DtlPath = get_dicom2stl_filepath(context)


            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.5', '-s', '-t', '226', '-o', tmpSTLarcada])
	      

            bpy.ops.import_mesh.stl(filepath=tmpSTLarcada, filter_glob="*.stl",  files=[{"name":"Arcada.stl", "name":"Arcada.stl"}], directory=tmpdir)
      


        if platform.system() == "Windows":

            dicom2DtlPath = 'C:/OrtogOnBlender/DicomToMeshWin/dicom2mesh.exe'


            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.5', '-s', '-t', '226', '-o', tmpSTLarcada])
	      

            bpy.ops.import_mesh.stl(filepath=tmpSTLarcada, filter_glob="*.stl",  files=[{"name":"Arcada.stl", "name":"Arcada.stl"}], directory=tmpdir)


        if platform.system() == "Darwin":


            dicom2DtlPath = '/OrtogOnBlender/DicomToMeshMAC/dicom2mesh'

#            dicom2DtlPath = get_dicom2stl_filepath(context)


            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.5', '-s', '-t', '226', '-o', tmpSTLarcada])
	      

            bpy.ops.import_mesh.stl(filepath=tmpSTLarcada, filter_glob="*.stl",  files=[{"name":"Arcada.stl", "name":"Arcada.stl"}], directory=tmpdir)

  
        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
        bpy.ops.view3d.view_all(center=False)

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDICOMDef, title="Atenção!", icon='INFO')
