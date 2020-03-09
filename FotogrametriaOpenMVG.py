import bpy
import subprocess
import platform
from os.path import expanduser
import shutil
import tempfile
from os import listdir
from os.path import isfile, join
import multiprocessing
import exifread
import re
import os


# MENSAGENS

class MessageFaltaFotos(bpy.types.Operator):
    bl_idname = "object.dialog_operator_falta_foto"
    bl_label = "Doesn't have photo path!"

    def execute(self, context):
        message = ("Doesn't have photo path!")
        self.report({'INFO'}, message)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

bpy.utils.register_class(MessageFaltaFotos)

'''
# ERROS

def ERROruntimeFotosDef(self, context):
    self.layout.label("Doesn't have photo path!")

def ERROTermFoto():
     CRED = '\033[91m'
     CEND = '\033[0m'
     print(CRED + "Doesn't have photo path!" + CEND)
'''

# PREPARA CENA

def PreparaCenaFotogramDef(self, context):
    try:
        bpy.ops.object.select_all(action='SELECT')

        objetos_selecionados = [ o for o in bpy.context.scene.objects if o.select_get() == True ]

        for i in objetos_selecionados:
            i.hide_viewport = True
    except:
        print("Cena já preparada.")

class PreparaCenaFotogram(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.prepara_cena_fotogram"
    bl_label = "Photogrammetry Scene Setup"

    def execute(self, context):
        PreparaCenaFotogramDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(PreparaCenaFotogram)

# MODELOS

def GeraModeloFotoDef(self, context):

    scn = context.scene


    #CRIA OU SETA DIRETÓRIO TEMPORÁRIO
#    if platform.system() == "Linux":
    tmpdir = tempfile.mkdtemp()
#    else:
#        tmpdir = tempfile.gettempdir()

    dFactor = scn.d_factor
    smoothFactor = scn.smooth_factor

    homeall = expanduser("~")

	# TESTA ARQUIVOS
    mypath = scn.my_tool.path_photo
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    FotoTeste = onlyfiles[1]

    TestaHEIC = ".HEIC" in FotoTeste

    if TestaHEIC == True:
        if platform.system() == "Linux":
            subprocess.call('mkdir '+tmpdir+'/JPG && cd '+mypath+' && for i in *; do heif-convert $i $i.jpg; done && mv *.jpg '+tmpdir+'/JPG/', shell=True)
            scn.my_tool.path_photo = tmpdir+'/JPG/'

        if platform.system() == "Darwin":
            subprocess.call('mkdir '+tmpdir+'/JPG && cd '+mypath+' && mogrify -format jpg *.HEIC && mv *.jpg '+tmpdir+'/JPG/', shell=True)
            scn.my_tool.path_photo = tmpdir+'/JPG/'

    Testajpeg = ".jpeg" in FotoTeste

    if Testajpeg == True:
        if platform.system() == "Linux" or platform.system() == "Darwin":
            subprocess.call('mkdir '+tmpdir+'/JPG && cd '+mypath+' && for i in *; do cp $i $i.jpg; done && mv *.jpg '+tmpdir+'/JPG/', shell=True)
            scn.my_tool.path_photo = tmpdir+'/JPG/'

        if platform.system() == "Windows" :

            subprocess.call('mkdir '+tmpdir+'\JPG & cd '+mypath+' & for %f in (*) do copy %f %f.jpg & move *.jpg '+tmpdir+'\JPG', shell=True)
            scn.my_tool.path_photo = tmpdir+'\JPG\\' # Se não colocar as duas barras não funciona!


    TestaJPEG = ".JPEG" in FotoTeste

    if TestaJPEG == True:
        if platform.system() == "Linux" or platform.system() == "Darwin":
            subprocess.call('mkdir '+tmpdir+'/JPG && cd '+mypath+' && for i in *; do cp $i $i.jpg; done && mv *.jpg '+tmpdir+'/JPG/', shell=True)
            scn.my_tool.path_photo = tmpdir+'/JPG/'

        if platform.system() == "Windows" :

            subprocess.call('mkdir '+tmpdir+'\JPG & cd '+mypath+' & for %f in (*) do copy %f %f.jpg & move *.jpg '+tmpdir+'\JPG', shell=True)
            scn.my_tool.path_photo = tmpdir+'\JPG\\' # Se não colocar as duas barras não funciona!

    # REDUZ FOTOS

    print("REDUZ FOTOS")
    print("bpy.context.scene.my_tool.path_photo", bpy.context.scene.my_tool.path_photo)

    tmpdirFotos = tempfile.mkdtemp()

    Origem = bpy.context.scene.my_tool.path_photo

    # Copia imagens para temporário
    ListaImagens = sorted(os.listdir(Origem))

    ImagContador = 0

    for ImagemAtual in ListaImagens:
        shutil.copyfile(Origem+ImagemAtual, tmpdirFotos+"/"+str(ImagContador)+".jpg")
        ImagContador += 1


        print("Copiando:", Origem+ImagemAtual, "para:", tmpdirFotos+"/"+str(ImagContador)+".jpg")

    bpy.context.scene.my_tool.path_photo = Origem

    # Reduz imagens
    ListaArquivos = sorted(os.listdir(tmpdirFotos))

#    print("ORIGEM:", Origem)

    print("FOOOOOOOOOOOOOOOOI")

    tmpdirIMagemgick = tempfile.mkdtemp()


    for ArquivoAtual in ListaArquivos:

        print("Reduzindo",ArquivoAtual)

        bpy.ops.image.open(filepath=tmpdirFotos+ArquivoAtual, directory=tmpdirFotos, files=[{"name":ArquivoAtual, "name":ArquivoAtual}], relative_path=False, show_multiview=False)

        ImgDim0 = bpy.data.images[ArquivoAtual].size[0]
        ImgDim1 = bpy.data.images[ArquivoAtual].size[1]

        LadoMaior = max(ImgDim0, ImgDim1)


        CpuNum = multiprocessing.cpu_count()

        if CpuNum >= 8:
            FatorPixel = 2536

        if CpuNum == 4:
            FatorPixel = 2400

        if CpuNum == 2:
            FatorPixel = 2200

        if CpuNum == 1:
            FatorPixel = 2200

        if LadoMaior > FatorPixel:
            print("Maior que "+str(FatorPixel)+"!")
            FatorDivisao = LadoMaior/FatorPixel
#            bpy.data.images[ArquivoAtual].scale( int(ImgDim0/FatorDivisao), int(ImgDim1/FatorDivisao) )

            if platform.system() == "Linux" or platform.system() == "Darwin":
                    subprocess.call('convert -resize '+str(100/FatorDivisao)+'% '+tmpdirFotos+"/"+ArquivoAtual+' '+tmpdirIMagemgick+"/"+ArquivoAtual, shell=True)

        #bpy.data.images[ArquivoAtual].save()

            bpy.context.scene.my_tool.path_photo = tmpdirIMagemgick+"/"


            if platform.system() == "Windows":
                    subprocess.call('C:\OrtogOnBlender\ImageMagick\convert -resize '+str(100/FatorDivisao)+'% '+tmpdirFotos+'\\'+ArquivoAtual+' '+tmpdirIMagemgick+'\\'+ArquivoAtual, shell=True) # O convert zoa os dados do EXIF no Windows!

        #bpy.data.images[ArquivoAtual].save()

            bpy.context.scene.my_tool.path_photo = tmpdirIMagemgick+"/"


    # TESTA CAMERA


#    if platform.system() == "Windows":
    if bpy.context.scene.my_tool.path_photo == "":
        bpy.ops.object.dialog_operator_falta_foto('INVOKE_DEFAULT')


    else:


        mypath = scn.my_tool.path_photo  # Tem que ter o / no final
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
                os.system('cd '+mypath+' && '+homeall+'/Programs/OrtogOnBlender/openMVGMACelcap/ExifTool.sh')

            if platform.system() == "Windows":
                print(mypath)

                subprocess.call(['C:\OrtogOnBlender\ExitTool\exiftool.exe', '-all=', mypath]) # Necessário pq o convert zoa os dados do EXIF no Windows!
                print("Exif apagado tudo!")
                subprocess.call(['C:\OrtogOnBlender\ExitTool\exiftool.exe', '-overwrite_original', '-Model=Z00AD', '-FocalLength=4', mypath+'*']) # Solução colocando o 4 sem as aspas duplas!

            print("Resolvido!")

        with open(mypath + FotoTeste, 'rb') as f_jpg:
            tags = exifread.process_file(f_jpg, details=True)
            print (tags['Image Model'])
            CamModel = str(tags['Image Model'])+";"


        # TESTA MODELO CAMERA

        if platform.system() == "Linux":
            camDatabase = homeall+"/Programs/OrtogOnBlender/openMVG/sensor_width_camera_database.txt"

        if platform.system() == "Darwin":
            camDatabase = homeall+"/Programs/OrtogOnBlender/openMVGMACelcap/sensor_width_camera_database.txt"


        if platform.system() == "Windows":
            camDatabase = "C:/OrtogOnBlender/openMVGWIN/sensor_width_camera_database.txt"



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
                inputCam = CamModel, " 3.80"
                print(inputCam)
     #           if platform.system() == "Darwin" or platform.system() == "Windows":
     #              file.write("\n")
                file.write("\n")
                file.writelines(inputCam) # Escreve o modelo de camera no arquivo



        # GERA FOTOGRAMETRIA

    #    try:

    #    if scn.my_tool.path_photo == "":
    #        ERROTermFoto()
    #        bpy.context.window_manager.popup_menu(ERROruntimeFotosDef, title="Attention!", icon='INFO')

    #    else:


        OpenMVGtmpDir = tmpdir+'/OpenMVG'
        tmpOBJface = tmpdir+'/MVS/scene_dense_mesh_texture.obj'


        if platform.system() == "Linux":
            OpenMVGPath = homeall+'/Programs/OrtogOnBlender/openMVG/software/SfM/SfM_SequentialPipeline.py'
            OpenMVSPath = homeall+'/Programs/OrtogOnBlender/openMVS/OpenMVS'
            print("É Linux")

        if platform.system() == "Windows":
            OpenMVGPath = 'C:/OrtogOnBlender/openMVGWin/software/SfM/SfM_SequentialPipeline.py'
            OpenMVSPath = 'C:/OrtogOnBlender/openMVSWin/OpenMVS.bat'

        if platform.system() == "Darwin":
           #         if platform.release() == '15.6.0':
        #                OpenMVGPath = '/OrtogOnBlender/openMVGMACelcap/SfM_SequentialPipeline.py'
        #                OpenMVSPath = '/OrtogOnBlender/openMVSMACelcap/openMVSMAC.sh'
        #            if platform.release() == '17.5.0':
        #                OpenMVGPath = '/OrtogOnBlender/openMVGMACelcap/SfM_SequentialPipeline.py'
        #                OpenMVSPath = '/OrtogOnBlender/openMVSMACelcap/openMVSMAC.sh'
        #            else:
        #                OpenMVGPath = '/OrtogOnBlender/openMVGMAC/SfM_SequentialPipeline.py'
        #                OpenMVSPath = '/OrtogOnBlender/openMVSMAC/openMVSMAC.sh'
            OpenMVGPath = homeall+'/Programs/OrtogOnBlender/openMVGMACelcap/SfM_SequentialPipeline.py'
            OpenMVSPath = homeall+'/Programs/OrtogOnBlender/openMVSMACelcap/openMVSMAC.sh'

            shutil.rmtree(tmpdir+'/OpenMVG', ignore_errors=True)
            shutil.rmtree(tmpdir+'/MVS', ignore_errors=True)

            #    if os.name=='posix':
            #    	shutil.rmtree(tmpdir+'/OpenMVG')
            #    	shutil.rmtree(tmpdir+'/MVS')

            #    if os.name=='nt':
            #    	subprocess.call(['rmdir', '/Q', '/S', tmpdir+'/OpenMVG'])
            #    	subprocess.call(['rmdir', '/Q', '/S', tmpdir+'/MVS'])


        if platform.system() == "Linux":
            subprocess.call(['python', OpenMVGPath , scn.my_tool.path_photo ,  OpenMVGtmpDir])


        if platform.system() == "Windows":
            subprocess.call(['C:/OrtogOnBlender/Python27/python', OpenMVGPath , scn.my_tool.path_photo ,  OpenMVGtmpDir])

        if platform.system() == "Darwin":
            subprocess.call(['python', OpenMVGPath , scn.my_tool.path_photo ,  OpenMVGtmpDir])


        #subprocess.call(OpenMVSPath ,  shell=True)

        if platform.system() == "Linux":

            subprocess.call('cd '+tmpdir+' && mkdir MVS && ~/Programs/OrtogOnBlender/openMVG/./openMVG_main_openMVG2openMVS -i '+tmpdir+'/OpenMVG/reconstruction_sequential/sfm_data.bin -o '+tmpdir+'/MVS/scene.mvs && ~/Programs/OrtogOnBlender/openMVS/./DensifyPointCloud --estimate-normals 1 '+tmpdir+'/MVS/scene.mvs && ~/Programs/OrtogOnBlender/openMVS/./ReconstructMesh -d '+dFactor+' --smooth '+smoothFactor+' '+tmpdir+'/MVS/scene_dense.mvs && ~/Programs/OrtogOnBlender/openMVS/./TextureMesh --export-type obj '+tmpdir+'/MVS/scene_dense_mesh.mvs', shell=True)

        if platform.system() == "Darwin":

            subprocess.call('cd '+tmpdir+' && mkdir MVS && '+homeall+'/Programs/OrtogOnBlender/openMVGMACelcap/openMVG_main_openMVG2openMVS -i '+tmpdir+'/OpenMVG/reconstruction_sequential/sfm_data.bin -o '+tmpdir+'/MVS/scene.mvs && '+homeall+'/Programs/OrtogOnBlender/openMVSMACelcap/./DensifyPointCloud --estimate-normals 1 '+tmpdir+'/MVS/scene.mvs && '+homeall+'/Programs/OrtogOnBlender/openMVSMACelcap/./ReconstructMesh -d '+dFactor+' --smooth '+smoothFactor+' '+tmpdir+'/MVS/scene_dense.mvs && '+homeall+'/Programs/OrtogOnBlender/openMVSMACelcap/./TextureMesh --export-type obj '+tmpdir+'/MVS/scene_dense_mesh.mvs', shell=True)

        if platform.system() == "Windows":

            subprocess.call('cd '+tmpdir+' && mkdir MVS && C:\OrtogOnBlender\openMVGWin\openMVG_main_openMVG2openMVS -i '+tmpdir+'/OpenMVG/reconstruction_sequential/sfm_data.bin -o '+tmpdir+'/MVS/scene.mvs && C:\OrtogOnBlender\openMVSWin\DensifyPointCloud --estimate-normals 1 '+tmpdir+'/MVS/scene.mvs && C:\OrtogOnBlender\openMVSWin\ReconstructMesh -d '+dFactor+' --smooth '+smoothFactor+' '+tmpdir+'/MVS/scene_dense.mvs && C:\OrtogOnBlender\openMVSWin\TextureMesh --export-type obj '+tmpdir+'/MVS/scene_dense_mesh.mvs', shell=True)

#        else:
#            subprocess.call(OpenMVSPath ,  shell=True)
            #subprocess.call([ 'meshlabserver', '-i', tmpdir+'scene_dense_mesh_texture.ply', '-o', tmpdir+'scene_dense_mesh_texture.obj', '-om', 'vn', 'wt' ])



        bpy.ops.import_scene.obj(filepath=tmpOBJface, filter_glob="*.obj;*.mtl")

        scene_dense_mesh_texture = bpy.data.objects['scene_dense_mesh_texture']

        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = scene_dense_mesh_texture
        bpy.data.objects['scene_dense_mesh_texture'].select_set(True)


        bpy.context.object.data.use_auto_smooth = False
#        bpy.context.object.active_material.specular_hardness = 60
#        bpy.context.object.active_material.diffuse_intensity = 0.6
#        bpy.context.object.active_material.specular_intensity = 0.3
        bpy.context.object.active_material.specular_color = (0.233015, 0.233015, 0.233015)
            #    bpy.ops.object.modifier_add(type='SMOOTH')
            #    bpy.context.object.modifiers["Smooth"].factor = 2
            #    bpy.context.object.modifiers["Smooth"].iterations = 3
            #    bpy.ops.object.convert(target='MESH')
            #    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Smooth")

        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
        #bpy.ops.view3d.view_all(center=False)

        # Centraliza zoom
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {'area': area, 'region': region, 'edit_object': bpy.context.edit_object}
                        bpy.ops.view3d.view_all(override)


        bpy.ops.file.pack_all()

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
        heightTex.image = bpy.data.images['scene_dense_mesh_texture_material_0_map_Kd.jpg']
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

        bpy.context.space_data.shading.type = 'SOLID'
        bpy.context.space_data.shading.color_type = 'TEXTURE'



class GeraModeloFoto(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_modelo_foto"
    bl_label = "Gera Modelos Foto"

    def execute(self, context):
        GeraModeloFotoDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(GeraModeloFoto)
