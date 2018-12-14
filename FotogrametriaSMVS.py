import bpy
import subprocess
import platform
from os.path import expanduser
import shutil
import tempfile
import bmesh

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

# Simplifica, gera UVMap único e Displacement
def DisplaceSMVSDef(self, context):

    scn = context.scene

    photogrammetry_original = bpy.context.active_object

    #bpy.ops.object.duplicate()

    bpy.ops.object.duplicate_move()

    photogrammetry_original.select=True
    photogrammetry_copy = bpy.context.active_object

    print(photogrammetry_original)
    print(photogrammetry_copy)

    bpy.ops.object.modifier_add(type='DECIMATE')
    #bpy.context.object.modifiers["Decimate"].ratio = 0.25
    bpy.context.object.modifiers["Decimate"].ratio = 0.50
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Decimate")


    # Entra em modo de edição e seleciona todos os vértices
    ob   = bpy.context.active_object
    bpy.ops.object.mode_set(mode = 'EDIT')
    mesh = bmesh.from_edit_mesh(ob.data)
    for v in mesh.verts:
        v.select = True

    # Cria UV map com espaço entre os grupos    
    bpy.ops.uv.smart_project(island_margin=0.3)


    # Faz o bake	
    #bpy.context.scene.render.use_bake_selected_to_active = True
    #bpy.context.scene.render.bake_type = 'TEXTURE'
    #bpy.context.scene.render.bake_margin = 4
    #bpy.ops.object.bake_image()

    #Cria imagem
    bpy.ops.image.new(name='UV_FACE', width=4096, height=4096, color=(0.5, 0.5, 0.5, 1), alpha=True, generated_type='BLANK', float=False, gen_context='NONE', use_stereo_3d=False)

    # BAKE
    bpy.context.scene.render.bake_margin = 2
    bpy.context.scene.render.use_bake_selected_to_active = True

    ob.data.uv_textures['UVMap'].active = True

    bpy.data.scenes["Scene"].render.bake_type = "TEXTURE"

    bpy.ops.object.mode_set(mode='OBJECT')

    for d in ob.data.uv_textures['UVMap'].data:
        d.image = bpy.data.images['UV_FACE']

    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.mesh.select_all(action='SELECT')

    bpy.ops.object.bake_image()

    bpy.ops.object.mode_set(mode='OBJECT')

    # Oculta original
    photogrammetry_original.hide=True

    # MODIFICADORES

    # Smooth
    bpy.ops.object.modifier_add(type='SMOOTH')
    bpy.context.object.modifiers["Smooth"].factor = 2
    bpy.context.object.modifiers["Smooth"].iterations = 3
    bpy.context.object.modifiers["Smooth"].show_viewport = False

    # MultRes
    bpy.ops.object.modifier_add(type='MULTIRES')
    bpy.context.object.modifiers["Multires"].show_viewport = False
    bpy.ops.object.multires_subdivide(modifier="Multires")

    context = bpy.context
    obj = context.active_object

    heightTex = bpy.data.textures.new('Texture name', type='IMAGE')
    heightTex.image = bpy.data.images['UV_FACE']
    dispMod = obj.modifiers.new("Displace", type='DISPLACE')
    dispMod.texture = heightTex
    bpy.context.object.modifiers["Displace"].texture_coords = 'UV'
    bpy.context.object.modifiers["Displace"].strength = 1.7
    bpy.context.object.modifiers["Displace"].mid_level = 0.5
    bpy.context.object.modifiers["Displace"].show_viewport = False

    #Comprime modificadores
    bpy.context.object.modifiers["Smooth"].show_expanded = False
    bpy.context.object.modifiers["Multires"].show_expanded = False
    bpy.context.object.modifiers["Displace"].show_expanded = False

    bpy.ops.object.shade_smooth()

    bpy.ops.file.pack_all()
