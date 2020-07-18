import bpy
import subprocess
import platform
from os.path import expanduser
import shutil
import tempfile
import bmesh
from os import listdir
from os.path import isfile, join

from .FerrImgTomo import *
from .FotogrametriaOpenMVG import *

# ERROS

def ERROruntimeFotosDef(self, context):
    self.layout.label("Doesn't have photo path!")

def ERROTermFoto():
     CRED = '\033[91m'
     CEND = '\033[0m'
     print(CRED + "Doesn't have photo path!" + CEND)

def GeraModeloFotoSMVSDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    tmpdir = tempfile.mkdtemp()
    tmpOBJface = tmpdir+'/scene/scene_dense_mesh_texture2.obj'
#    subprocess.call(['rm /tmp/DIRETORIO_FOTOS.txt'],  shell=True)

    homeall = expanduser("~")

    ConverteHEICtoJPG()

    # Inicia os trabalhos

    if scn.my_tool.path_photo == "":
        ERROTermFoto()
        bpy.context.window_manager.popup_menu(ERROruntimeFotosDef, title="Attention!", icon='INFO')

    else:
        if platform.system() == "Linux":

            with open("/etc/issue") as f:
             Versao = str(f.read().lower().split()[1])

            if Versao == "18.04":

                SMVSPath = homeall+"/Programs/OrtogOnBlender/SMVS/"
                subprocess.call(['rm', '-rf', tmpdir+'/scene'])
                subprocess.call([SMVSPath+'./makescene', '-i', scn.my_tool.path_photo, tmpdir+'/scene'])
                subprocess.call([SMVSPath+'./sfmrecon', tmpdir+'/scene'])
                subprocess.call([SMVSPath+'./smvsrecon', '-s2', tmpdir+'/scene'])
                subprocess.call(['meshlabserver', '-i', tmpdir+'/scene/smvs-B2.ply', '-o', tmpdir+'/scene/meshlab.ply', '-s', SMVSPath+'SMVSmeshlab.mlx', '-om'])
                subprocess.call([SMVSPath+'./texrecon', '--data_term=area', '--skip_global_seam_leveling', '--outlier_removal=gauss_damping', tmpdir+'/scene::undistorted', tmpdir+'/scene/meshlab.ply', tmpdir+'/scene/scene_dense_mesh_texture2'])
                bpy.ops.import_scene.obj(filepath=tmpOBJface, filter_glob="*.obj;*.mtl")
                scene_dense_mesh_texture2 = bpy.data.objects['scene_dense_mesh_texture2']
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = scene_dense_mesh_texture2
                bpy.data.objects['scene_dense_mesh_texture2'].select_set(True)
                bpy.ops.view3d.view_all(center=False)
                bpy.ops.file.pack_all()


            if Versao == "20.04":

                SMVSPath = homeall+"/Programs/OrtogOnBlender/SMVS/"
                subprocess.call(['rm', '-rf', tmpdir+'/scene'])
                subprocess.call([SMVSPath+'./makescene', '-i', scn.my_tool.path_photo, tmpdir+'/scene'])
                subprocess.call([SMVSPath+'./sfmrecon', tmpdir+'/scene'])
                subprocess.call([SMVSPath+'./smvsrecon', '-s2', tmpdir+'/scene'])
                subprocess.call([SMVSPath+'./fssrecon', tmpdir+'/scene/smvs-B2.ply', tmpdir+'/scene/smvs-surface.ply'])
                subprocess.call([SMVSPath+'./meshclean', '-p10', tmpdir+'/scene/smvs-surface.ply', tmpdir+'/scene/smvs-surface-clean.ply'])
                subprocess.call([SMVSPath+'./texrecon', '--data_term=area', '--skip_global_seam_leveling', '--outlier_removal=gauss_damping', tmpdir+'/scene::undistorted', tmpdir+'/scene/smvs-surface-clean.ply', tmpdir+'/scene/scene_dense_mesh_texture2'])
                bpy.ops.import_scene.obj(filepath=tmpOBJface, filter_glob="*.obj;*.mtl")
                scene_dense_mesh_texture2 = bpy.data.objects['scene_dense_mesh_texture2']
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.view_layer.objects.active = scene_dense_mesh_texture2
                bpy.data.objects['scene_dense_mesh_texture2'].select_set(True)
                bpy.ops.view3d.view_all(center=False)
                bpy.ops.file.pack_all()


        if platform.system() == "Windows":
            SMVSPath = 'C:/OrtogOnBlender/SMVS/'
#            shutil.rmtree(tmpdir+'/scene')

            SMVSPathLinux = 'C:/OrtogOnBlender/SMVSlinux/'

            Fotos = str(scn.my_tool.path_photo).replace("\\", "/").replace('\\', "/").replace("C:", "/mnt/c")
            print("FOTOS: ", Fotos)

            Saida = str(tmpdir).replace("\\", "/").replace('\\', "/").replace("C:", "/mnt/c")

            # subprocess.call([SMVSPath+'./makescene', '-i', scn.my_tool.path_photo, tmpdir+'/scene'])
            subprocess.call("wsl \"/mnt/c/OrtogOnBlender/SMVSlinux/makescene\" -i \""+Fotos+"\" \""+Saida+"/scene\"", shell=True)

            #subprocess.call([SMVSPath+'./sfmrecon', tmpdir+'/scene'])
            subprocess.call("wsl \"/mnt/c/OrtogOnBlender/SMVSlinux/sfmrecon\" \""+Saida+"/scene\"", shell=True)

            #subprocess.call([SMVSPath+'./smvsrecon', '-s2', tmpdir+'/scene'])
            subprocess.call("wsl \"/mnt/c/OrtogOnBlender/SMVSlinux/smvsrecon\" -s2 \""+Saida+"/scene\"", shell=True)

            subprocess.call([SMVSPath+'./fssrecon', tmpdir+'/scene/smvs-B2.ply', tmpdir+'/scene/smvs-surface.ply'])
            subprocess.call([SMVSPath+'./meshclean', '-p10', tmpdir+'/scene/smvs-surface.ply', tmpdir+'/scene/smvs-surface-clean.ply'])

            #subprocess.call('C:\OrtogOnBlender\MeshLab\meshlabserver -i '+tmpdir+'/scene/smvs-B2.ply -o '+tmpdir+'/scene/meshlab.ply -s '+SMVSPathLinux+'SMVSmeshlab.mlx', shell=True)


            subprocess.call("wsl \"/mnt/c/OrtogOnBlender/SMVSlinux/texrecon\" \"--data_term=area\" \"--skip_global_seam_leveling\" \"--outlier_removal=gauss_damping\" \""+Saida+"/scene::undistorted\" \""+Saida+"/scene/smvs-surface-clean.ply\" \""+Saida+"/scene/scene_dense_mesh_texture2\"", shell=True)

            bpy.ops.import_scene.obj(filepath=tmpOBJface, filter_glob="*.obj;*.mtl")
            scene_dense_mesh_texture2 = bpy.data.objects['scene_dense_mesh_texture2']
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.view_layer.objects.active = scene_dense_mesh_texture2
            bpy.data.objects['scene_dense_mesh_texture2'].select_set(True)
            bpy.ops.view3d.view_all(center=False)
            bpy.ops.file.pack_all()

            '''
            tmpPLYface = tmpdir+'/scene/smvs-surface-clean.ply'
            bpy.ops.import_mesh.ply(filepath=tmpPLYface, filter_glob="*.ply")
            smvs_surface_clean = bpy.data.objects['smvs-surface-clean']
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.view_layer.objects.active = smvs_surface_clean
            bpy.data.objects['smvs-surface-clean'].select_set(True)
            bpy.ops.view3d.view_all(center=False)
            bpy.ops.file.pack_all()
            '''

        if platform.system() == "Darwin":
            homemac = expanduser("~")
            SMVSPath = homemac+'/Programs/OrtogOnBlender/SMVSMAC/'

            subprocess.call(['rm', '-Rf', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./makescene', '-i', scn.my_tool.path_photo, tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./sfmrecon', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./smvsrecon', '-s2', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./fssrecon', '-s4', tmpdir+'/scene/smvs-B2.ply', tmpdir+'/scene/smvs-surface.ply'])
            subprocess.call([SMVSPath+'./meshclean', '-p10', tmpdir+'/scene/smvs-surface.ply', tmpdir+'/scene/smvs-clean.ply'])
            subprocess.call(['rm', '-Rf', tmpdir+'/scene/tmp'])
            subprocess.call([SMVSPath+'./texrecon', '--data_term=area', '--skip_global_seam_leveling', '--outlier_removal=gauss_damping', tmpdir+'/scene::undistorted', tmpdir+'/scene/smvs-clean.ply', tmpdir+'/scene/scene_dense_mesh_texture2'])

            bpy.ops.import_scene.obj(filepath=tmpOBJface, filter_glob="*.obj;*.mtl")
            scene_dense_mesh_texture2 = bpy.data.objects['scene_dense_mesh_texture2']
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.view_layer.objects.active = scene_dense_mesh_texture2
            bpy.data.objects['scene_dense_mesh_texture2'].select_set(True)
            bpy.ops.view3d.view_all(center=False)
            bpy.ops.file.pack_all()

    bpy.ops.object.modifier_add(type='DECIMATE')
    #bpy.context.object.modifiers["Decimate"].ratio = 0.25
    bpy.context.object.modifiers["Decimate"].ratio = 0.35
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Decimate")


    print("FIX SMVS SURFACE AND MAP")

    photogrammetry_original = bpy.context.active_object

    #bpy.ops.object.duplicate()

    bpy.ops.object.duplicate_move()

    photogrammetry_original.select_set(False)
    photogrammetry_copy = bpy.context.active_object

    print(photogrammetry_original)
    print(photogrammetry_copy)


    # Entra em modo de edição e seleciona todos os vértices
    ob   = bpy.context.active_object

    #Apaga todos os materiais
    for i in range(len(ob.material_slots)):
        bpy.ops.object.material_slot_remove({'object': ob})

    bpy.ops.object.mode_set(mode = 'EDIT')
    mesh = bmesh.from_edit_mesh(ob.data)
    for v in mesh.verts:
        v.select = True

    # Cria UV map com espaço entre os grupos
    bpy.ops.uv.smart_project(island_margin=0.03)
#    bpy.ops.uv.smart_project(island_margin=0.3)

    bpy.ops.object.mode_set(mode='OBJECT')


    #Cria imagem
    bpy.ops.image.new(name='UV_FACE', width=2048, height=2048, color=(0.5, 0.5, 0.5, 1), alpha=True, generated_type='BLANK', float=False, use_stereo_3d=False)

    #Cria material


    m = Material()
    m.set_cycles()
    # from chapter 1 of [DRM protected book, could not copy author/title]
    m.make_material("FaceUVunic")

    ImageTexture = m.makeNode('ShaderNodeTexImage', 'Image Texture')
    ImageTexture.image = bpy.data.images['UV_FACE']

    diffuseBSDF = m.nodes['Principled BSDF']
    diffuseBSDF.inputs[5].default_value = 0

    m.link(ImageTexture, 'Color', diffuseBSDF, 'Base Color')

    bpy.ops.object.material_slot_remove()
    bpy.ops.object.material_slot_add()

    bpy.data.objects[bpy.context.view_layer.objects.active.name].active_material = bpy.data.materials["FaceUVunic"]


    # BAKE

    ob.data.uv_layers['UVMap'].active = True


#    bpy.data.scenes["Scene"].cycles.bake_type = 'UV'
    bpy.context.scene.cycles.bake_type = 'DIFFUSE'
    bpy.context.scene.render.bake.use_pass_direct = False
    bpy.context.scene.render.bake.use_pass_indirect = False

    bpy.context.scene.render.bake.use_selected_to_active = True
    bpy.context.scene.render.bake.margin = 2
    bpy.context.scene.render.bake.cage_extrusion = 0.32

    photogrammetry_original.select_set(True)

    bpy.ops.object.bake(type='DIFFUSE')

    # Oculta original
    photogrammetry_original.hide_viewport=True



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
#    heightTex.image = bpy.data.images['scene_dense_mesh_texture2_material0000_map_Kd.png']
    dispMod = obj.modifiers.new("Displace", type='DISPLACE')
    dispMod.texture = heightTex
    bpy.context.object.modifiers["Displace"].texture_coords = 'UV'
    bpy.context.object.modifiers["Displace"].strength = 2.2
    bpy.context.object.modifiers["Displace"].mid_level = 0.5
    bpy.context.object.modifiers["Displace"].show_viewport = False

    #Comprime modificadores
    bpy.context.object.modifiers["Smooth"].show_expanded = False
    bpy.context.object.modifiers["Multires"].show_expanded = False
    bpy.context.object.modifiers["Displace"].show_expanded = False

    bpy.ops.object.shade_flat()

    bpy.context.space_data.shading.type = 'MATERIAL'


    if platform.system() == "Linux" or platform.system() == "Darwin":
        bpy.data.images['UV_FACE'].pack()
        print("Empacotou as imagens!")

    if platform.system() == "Windows":
        bpy.data.images['UV_FACE'].pack(as_png=True)
        print("Empacotou as imagens!")


    bpy.ops.file.pack_all()



class GeraModeloFotoSMVS(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_modelo_foto_smvs"
    bl_label = "Gera Modelos Foto"

    def execute(self, context):
        GeraModeloFotoSMVSDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(GeraModeloFotoSMVS)

class DisplaceSMVS(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.displace_smvs"
    bl_label = "Displace SMVS"

    def execute(self, context):
        DisplaceSMVSDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(DisplaceSMVS)
