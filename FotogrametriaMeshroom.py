import bpy
import subprocess
import platform
from os.path import expanduser
import shutil
import tempfile
from os import listdir
from os.path import isfile, join
import exifread
import re
import os
import bmesh

from .FerrImgTomo import *

def GeraModeloFotoMeshroomDef(self, context):

    scn = context.scene

    tmpdir = tempfile.mkdtemp()

    homeall = expanduser("~")

# Database

    mypath = scn.my_tool.path  # Tem que ter o / no final
#       mypathFotos = mypath+'*'
#       print("Caminho:"+mypathFotos)

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    FotoTeste = onlyfiles[1]

    try:
        with open(mypath + FotoTeste, 'rb') as f_jpg:
            tags = exifread.process_file(f_jpg, details=True)
            print (tags['Image Model'])
            CamModel = str(tags['Image Model'])
        #print("CamModel:", CamModel)
    except:
        print("Não rolou!")
#                subprocess.call([os.system('cd'+mypath), '&&', homeall+'/Programs/OrtogOnBlender/openMVG/ExifTool.sh'])
        if platform.system() == "Linux":
            os.system('cd '+mypath+' && '+homeall+'/Programs/OrtogOnBlender/openMVG/ExifTool.sh')

        if platform.system() == "Darwin":
            os.system('cd '+mypath+' && /OrtogOnBlender/openMVGMACelcap/ExifTool.sh')

        if platform.system() == "Windows":
            print(mypath)
            subprocess.call(['C:\OrtogOnBlender\ExitTool\exiftool.exe', '-overwrite_original', '-Model="Z00AD"', '-FocalLength=4', mypath+'*']) # Solução colocando o 4 sem as aspas duplas!

        print("Resolvido!")

    with open(mypath + FotoTeste, 'rb') as f_jpg:
        tags = exifread.process_file(f_jpg, details=True)
        print (tags['Image Model'])
        CamModel = str(tags['Image Model'])+";"

# Inscreve no Banco de dados

    if platform.system() == "Linux":
        camDatabase = homeall+"/Programs/OrtogOnBlender/Meshroom/aliceVision/share/aliceVision/cameraSensors.db"
        
    if platform.system() == "Windows":
        camDatabase = "C:/OrtogOnBlender/Meshroom/aliceVision/share/aliceVision/cameraSensors.db"

    infile = open(camDatabase, "r")

    numlines = 0
    found = 0
    for line in infile:
        numlines += 1
        while 1:
            str_found_at = line.find(CamModel)
            if str_found_at == -1:
                # string not found in line ...
                # go to next (ie break out of the while loop)
                break
            else:
                # string found in line
                found += 1
                # more than once in this line?
                # lets strip string and anything prior from line and
                # then go through the testing loop again
                line = line[str_found_at + len(CamModel):]
    infile.close()

    print(CamModel, "was found", found, "times in", numlines, "lines")

    if found == 0:
        print("Nao apareceu!")

        with open(camDatabase, 'a') as file:
            inputCam = CamModel,CamModel, "3.80;devicespecifications"
            print(inputCam)
 #           if platform.system() == "Darwin" or platform.system() == "Windows":
 #              file.write("\n")
            file.write("\n")
            file.writelines(inputCam) # Escreve o modelo de camera no arquivo

# GERA FOTOGRAMETRIA

    if platform.system() == "Linux":

        
        subprocess.call('mkdir '+tmpdir+'/JPG && cd '+mypath+' && for i in *; do cp $i '+tmpdir+'/JPG/; done ', shell=True)


        subprocess.call('~/Programs/OrtogOnBlender/Meshroom/meshroom_photogrammetry --input '+tmpdir+'/JPG/ --output '+tmpdir+' --scale 2 --save '+tmpdir+'/PipelineOrtogOnBlender.txt', shell=True)


    if platform.system() == "Windows":

        print("TENTA COPIAR")
        subprocess.call('mkdir '+tmpdir+'\JPG & cd '+mypath+' & for %f in (*) do copy %f '+tmpdir+'\JPG', shell=True)

        print("TENTA RODAR MESHROOM")
        subprocess.call('C:/OrtogOnBlender/Meshroom/meshroom_photogrammetry --input '+tmpdir+'/JPG/ --output '+tmpdir+' --scale 2 --save '+tmpdir+'/PipelineOrtogOnBlender.txt', shell=True)
        


    with open(tmpdir+'/PipelineOrtogOnBlender.txt', 'r') as fd:
        txt = fd.read()

        txt = txt.replace('"iterations": 5','"iterations": 16')
        txt = txt.replace('"maxInputPoints": 50000000','"maxInputPoints": 5000000', 1)
        txt = txt.replace('"maxPoints": 5000000','"maxPoints": 500000', 1)

    with open(tmpdir+'/PipelineOrtogOnBlender.txt', 'w') as fd:
        fd.write(txt)
    
    print("ARQUIVO CRIADO!")

    if platform.system() == "Linux":

        subprocess.call('~/Programs/OrtogOnBlender/Meshroom/meshroom_photogrammetry --input '+tmpdir+'/JPG/ --output '+tmpdir+' --scale 2 --pipeline '+tmpdir+'/PipelineOrtogOnBlender.txt', shell=True)


    if platform.system() == "Windows":

        subprocess.call('C:/OrtogOnBlender/Meshroom/meshroom_photogrammetry --input '+tmpdir+'/JPG/ --output '+tmpdir+' --scale 2 --pipeline '+tmpdir+'/PipelineOrtogOnBlender.txt', shell=True)


    tmpOBJface = tmpdir+'/texturedMesh.obj'

    bpy.ops.import_scene.obj(filepath=tmpOBJface, filter_glob="*.obj;*.mtl")

    texturedMesh = bpy.data.objects['texturedMesh']

    bpy.ops.object.select_all(action='DESELECT')
    texturedMesh.select_set(True)
    bpy.context.view_layer.objects.active = texturedMesh

    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
    bpy.ops.view3d.view_all(center=False)
    bpy.ops.file.pack_all()


# UNIFICA UV MAP

    print("FIX MESHROOM SURFACE AND MAP")

    ob   = bpy.context.active_object

    me = ob.data
    Faces = len(me.polygons)
    Fator = 500000 / Faces

    bpy.ops.object.modifier_add(type='DECIMATE')
    bpy.context.object.modifiers["Decimate"].ratio = Fator
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Decimate")



    photogrammetry_original = bpy.context.active_object

    #bpy.ops.object.duplicate()

    bpy.ops.object.duplicate_move()

    photogrammetry_original.select_set(False)
    photogrammetry_copy = bpy.context.active_object

    print(photogrammetry_original)
    print(photogrammetry_copy)



    # Entra em modo de edição e seleciona todos os vértices
    ob   = bpy.context.active_object

# FATOR DECIMATE

    me = ob.data
    Faces = len(me.polygons)
    Fator = 100000 / Faces

    bpy.ops.object.modifier_add(type='DECIMATE')
    bpy.context.object.modifiers["Decimate"].ratio = Fator
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Decimate")

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

    bpy.data.images['UV_FACE'].pack()
    bpy.ops.file.pack_all()
    
    # Oculta original
    photogrammetry_original.hide_viewport=True



    # MODIFICADORES

    bpy.ops.object.modifier_add(type='SMOOTH')
    bpy.context.object.modifiers["Smooth"].factor = 2
    bpy.context.object.modifiers["Smooth"].iterations = 3
    bpy.context.object.modifiers["Smooth"].show_viewport = False

            #bpy.ops.object.convert(target='MESH')

            # MultRes
    bpy.ops.object.modifier_add(type='MULTIRES')
    bpy.context.object.modifiers["Multires"].show_viewport = False
    bpy.ops.object.multires_subdivide(modifier="Multires")

    context = bpy.context
    obj = context.active_object

    heightTex = bpy.data.textures.new('Texture name', type='IMAGE')
   # heightTex.image = bpy.data.images['scene_dense_mesh_texture_material_0_map_Kd.jpg']
    heightTex.image = bpy.data.images['UV_FACE']
    dispMod = obj.modifiers.new("Displace", type='DISPLACE')
    dispMod.texture = heightTex
    bpy.context.object.modifiers["Displace"].texture_coords = 'UV'
    bpy.context.object.modifiers["Displace"].strength = 3.2
    bpy.context.object.modifiers["Displace"].mid_level = 0.5
    bpy.context.object.modifiers["Displace"].show_viewport = False

            #Comprime modificadores
    bpy.context.object.modifiers["Smooth"].show_expanded = False
    bpy.context.object.modifiers["Multires"].show_expanded = False
    bpy.context.object.modifiers["Displace"].show_expanded = False

    bpy.ops.object.shade_smooth()

    bpy.context.space_data.shading.type = 'MATERIAL'


class GeraModeloFotoMeshroom(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_modelo_foto_meshroom"
    bl_label = "Gera Modelos Foto Meshroom"
    
    def execute(self, context):
        GeraModeloFotoMeshroomDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(GeraModeloFotoMeshroom)




