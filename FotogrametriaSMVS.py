import bpy
import subprocess
import platform
from os.path import expanduser
import shutil
import tempfile

# ERROS

def ERROruntimeFotosDef(self, context):
    self.layout.label("Doesn't have photo path!")

def ERROTermFoto():
     CRED = '\033[91m'
     CEND = '\033[0m'
     print(CRED + "Doesn't have photo path!" + CEND)

def GeraModeloFotoSMVSDef(self, context):

    scn = context.scene
        
    tmpdir = tempfile.gettempdir()
    tmpOBJface = tmpdir+'/scene/scene_dense_mesh_texture2.obj'
#    subprocess.call(['rm /tmp/DIRETORIO_FOTOS.txt'],  shell=True)

    homeall = expanduser("~")
    
    if scn.my_tool.path == "":
        ERROTermFoto()        
        bpy.context.window_manager.popup_menu(ERROruntimeFotosDef, title="Attention!", icon='INFO')

    else:
        if platform.system() == "Linux":
            SMVSPath = homeall+"/Programs/OrtogOnBlender/SMVS/"
            subprocess.call(['rm', '-rf', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./makescene', '-i', scn.my_tool.path, tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./sfmrecon', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./smvsrecon', '-s2', tmpdir+'/scene'])
            subprocess.call(['meshlabserver', '-i', tmpdir+'/scene/smvs-B2.ply', '-o', tmpdir+'/scene/meshlab.ply', '-s', SMVSPath+'SMVSmeshlab.mlx', '-om'])
            subprocess.call([SMVSPath+'./texrecon', '--data_term=area', '--skip_global_seam_leveling', '--outlier_removal=gauss_damping', tmpdir+'/scene::undistorted', tmpdir+'/scene/meshlab.ply', tmpdir+'/scene/scene_dense_mesh_texture2'])
            bpy.ops.import_scene.obj(filepath=tmpOBJface, filter_glob="*.obj;*.mtl")
            scene_dense_mesh_texture2 = bpy.data.objects['scene_dense_mesh_texture2']
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.scene.objects.active = scene_dense_mesh_texture2
            bpy.data.objects['scene_dense_mesh_texture2'].select = True
            bpy.ops.view3d.view_all(center=False)
            bpy.ops.file.pack_all()


        if platform.system() == "Windows":
            SMVSPath = 'C:/OrtogOnBlender/SMVS/'
#            shutil.rmtree(tmpdir+'/scene')
            subprocess.call([SMVSPath+'./makescene', '-i', scn.my_tool.path, tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./sfmrecon', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./smvsrecon', '-s2', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./fssrecon', tmpdir+'/scene/smvs-B2.ply', tmpdir+'/scene/smvs-surface.ply'])
            subprocess.call([SMVSPath+'./meshclean', '-p10', tmpdir+'/scene/smvs-surface.ply', tmpdir+'/scene/smvs-surface-clean.ply'])
            tmpPLYface = tmpdir+'/scene/smvs-surface-clean.ply'        
            bpy.ops.import_mesh.ply(filepath=tmpPLYface, filter_glob="*.ply")
            smvs_surface_clean = bpy.data.objects['smvs-surface-clean']
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.scene.objects.active = smvs_surface_clean
            bpy.data.objects['smvs-surface-clean'].select = True
            bpy.ops.view3d.view_all(center=False)
            bpy.ops.file.pack_all()        


        if platform.system() == "Darwin":
            homemac = expanduser("~")
            SMVSPath = '/OrtogOnBlender/SMVSMAC/'

            subprocess.call(['rm', '-Rf', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./makescene', '-i', scn.my_tool.path, tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./sfmrecon', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./smvsrecon', '-s2', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./fssrecon', '-s4', tmpdir+'/scene/smvs-B2.ply', tmpdir+'/scene/smvs-surface.ply'])
            subprocess.call([SMVSPath+'./meshclean', '-p10', tmpdir+'/scene/smvs-surface.ply', tmpdir+'/scene/smvs-clean.ply'])
            subprocess.call(['rm', '-Rf', tmpdir+'/scene/tmp'])
            subprocess.call([SMVSPath+'./texrecon', '--data_term=area', '--skip_global_seam_leveling', '--outlier_removal=gauss_damping', tmpdir+'/scene::undistorted', tmpdir+'/scene/smvs-clean.ply', tmpdir+'/scene/scene_dense_mesh_texture2'])

            bpy.ops.import_scene.obj(filepath=tmpOBJface, filter_glob="*.obj;*.mtl")
            scene_dense_mesh_texture2 = bpy.data.objects['scene_dense_mesh_texture2']
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.scene.objects.active = scene_dense_mesh_texture2
            bpy.data.objects['scene_dense_mesh_texture2'].select = True
            bpy.ops.view3d.view_all(center=False)
            bpy.ops.file.pack_all()
