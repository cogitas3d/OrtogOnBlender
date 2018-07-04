import bpy
import subprocess
import platform
from os.path import expanduser
import shutil
import tempfile
from os import listdir
from os.path import isfile, join
import exifread

import os

# ERROS

def ERROruntimeFotosDef(self, context):
    self.layout.label("Doesn't have photo path!")

def ERROTermFoto():
     CRED = '\033[91m'
     CEND = '\033[0m'
     print(CRED + "Doesn't have photo path!" + CEND)

# MODELOS

def GeraModeloFotoDef(self, context):
    
    scn = context.scene
    
    tmpdir = tempfile.gettempdir()

    homeall = expanduser("~")

    # TESTA CAMERA

    if scn.my_tool.path == "":
        ERROTermFoto()        
        bpy.context.window_manager.popup_menu(ERROruntimeFotosDef, title="Attention!", icon='INFO')

    else:


        mypath = scn.my_tool.path  # Tem que ter o / no final
 #       mypathFotos = mypath+'*'
 #       print("Caminho:"+mypathFotos)

        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        FotoTeste = onlyfiles[0]
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
                print("Ainda não implementado")

            print("Resolvido!")

        with open(mypath + FotoTeste, 'rb') as f_jpg:
            tags = exifread.process_file(f_jpg, details=True)
            print (tags['Image Model'])
            CamModel = str(tags['Image Model'])



        # TESTA MODELO CAMERA

        if platform.system() == "Linux":
            camDatabase = homeall+"/Programs/OrtogOnBlender/openMVG/sensor_width_camera_database.txt"

        if platform.system() == "Darwin":
            camDatabase = "/OrtogOnBlender/openMVGMACelcap/sensor_width_camera_database.txt"


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
                inputCam = CamModel, "; 3.80"
                print(inputCam)
     #           if platform.system() == "Darwin" or platform.system() == "Windows":
     #              file.write("\n")
                file.write("\n")
                file.writelines(inputCam) # Escreve o modelo de camera no arquivo



        # GERA FOTOGRAMETRIA

    #    try:

    #    if scn.my_tool.path == "":
    #        ERROTermFoto()        
    #        bpy.context.window_manager.popup_menu(ERROruntimeFotosDef, title="Attention!", icon='INFO')

    #    else:

        OpenMVGtmpDir = tmpdir+'/OpenMVG'
        tmpOBJface = tmpdir+'/MVS/scene_dense_mesh_texture2.obj'

                
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
            OpenMVGPath = '/OrtogOnBlender/openMVGMACelcap/SfM_SequentialPipeline.py' 
            OpenMVSPath = '/OrtogOnBlender/openMVSMACelcap/openMVSMAC.sh'

            shutil.rmtree(tmpdir+'/OpenMVG', ignore_errors=True)
            shutil.rmtree(tmpdir+'/MVS', ignore_errors=True)

            #    if os.name=='posix':
            #    	shutil.rmtree(tmpdir+'/OpenMVG')
            #    	shutil.rmtree(tmpdir+'/MVS')

            #    if os.name=='nt':
            #    	subprocess.call(['rmdir', '/Q', '/S', tmpdir+'/OpenMVG'])
            #    	subprocess.call(['rmdir', '/Q', '/S', tmpdir+'/MVS'])


        if platform.system() == "Linux":
            subprocess.call(['python', OpenMVGPath , scn.my_tool.path ,  OpenMVGtmpDir])

                    
        if platform.system() == "Windows":
            subprocess.call(['C:/OrtogOnBlender/Python27/python', OpenMVGPath , scn.my_tool.path ,  OpenMVGtmpDir])

        if platform.system() == "Darwin":
            subprocess.call(['python', OpenMVGPath , scn.my_tool.path ,  OpenMVGtmpDir])


        subprocess.call(OpenMVSPath ,  shell=True)

            #    subprocess.call([ 'meshlabserver', '-i', tmpdir+'scene_dense_mesh_texture.ply', '-o', tmpdir+'scene_dense_mesh_texture2.obj', '-om', 'vn', 'wt' ])



        bpy.ops.import_scene.obj(filepath=tmpOBJface, filter_glob="*.obj;*.mtl")

        scene_dense_mesh_texture2 = bpy.data.objects['scene_dense_mesh_texture2']

        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = scene_dense_mesh_texture2
        bpy.data.objects['scene_dense_mesh_texture2'].select = True


        bpy.context.object.data.use_auto_smooth = False
        bpy.context.object.active_material.specular_hardness = 60
        bpy.context.object.active_material.diffuse_intensity = 0.6
        bpy.context.object.active_material.specular_intensity = 0.3
        bpy.context.object.active_material.specular_color = (0.233015, 0.233015, 0.233015)
            #    bpy.ops.object.modifier_add(type='SMOOTH')
            #    bpy.context.object.modifiers["Smooth"].factor = 2
            #    bpy.context.object.modifiers["Smooth"].iterations = 3
            #    bpy.ops.object.convert(target='MESH')
            #    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Smooth")    
            
        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
        bpy.ops.view3d.view_all(center=False)
        bpy.ops.file.pack_all()
                
        bpy.ops.object.modifier_add(type='SMOOTH')
        bpy.context.object.modifiers["Smooth"].factor = 2
        bpy.context.object.modifiers["Smooth"].iterations = 3
        bpy.context.object.modifiers["Smooth"].show_viewport = False

                #bpy.ops.object.convert(target='MESH')

                # MutRes
        bpy.ops.object.modifier_add(type='MULTIRES')
        bpy.context.object.modifiers["Multires"].show_viewport = False
        bpy.ops.object.multires_subdivide(modifier="Multires")

        context = bpy.context
        obj = context.active_object

        heightTex = bpy.data.textures.new('Texture name', type='IMAGE')
        heightTex.image = bpy.data.images['scene_dense_mesh_texture2_material_0_map_Kd.jpg']
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

