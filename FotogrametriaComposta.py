import bpy
import subprocess
import platform
from os.path import expanduser
import shutil
import tempfile
from os import listdir
from os.path import isfile, join
import exifread
import bmesh

import os

# ERROS

def ERROruntimeFotosDef(self, context):
    self.layout.label("Doesn't have photo path!")

def ERROTermFoto():
     CRED = '\033[91m'
     CEND = '\033[0m'
     print(CRED + "Doesn't have photo path!" + CEND)


def FotogrametriaCompostaDef(self, context):

# OPENMVG -----------------------------------------------------------------------------------

# MODELOS


    
    scn = context.scene
    
    
    #CRIA OU SETA DIETÓRIO TEMPORÁRIO
#    if platform.system() == "Linux":
    tmpdir = tempfile.mkdtemp()
#    else:
#        tmpdir = tempfile.gettempdir()


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


# OPENMVS ----------------------------------------------------------------------------------------------------------------------

        #subprocess.call(OpenMVSPath ,  shell=True)

        if platform.system() == "Linux":

            subprocess.call('cd '+tmpdir+' && mkdir MVS && ~/Programs/OrtogOnBlender/openMVG/./openMVG_main_openMVG2openMVS -i '+tmpdir+'/OpenMVG/reconstruction_sequential/sfm_data.bin -o '+tmpdir+'/MVS/scene.mvs && ~/Programs/OrtogOnBlender/openMVS/./DensifyPointCloud --estimate-normals 1 '+tmpdir+'/MVS/scene.mvs && ~/Programs/OrtogOnBlender/openMVS/./ReconstructMesh -d 16 --smooth 6 '+tmpdir+'/MVS/scene_dense.mvs && ~/Programs/OrtogOnBlender/openMVS/./TextureMesh --export-type obj '+tmpdir+'/MVS/scene_dense_mesh.mvs', shell=True)

        if platform.system() == "Darwin":

            subprocess.call('cd '+tmpdir+' && mkdir MVS && /OrtogOnBlender/openMVGMACelcap/openMVG_main_openMVG2openMVS -i '+tmpdir+'/OpenMVG/reconstruction_sequential/sfm_data.bin -o '+tmpdir+'/MVS/scene.mvs && /OrtogOnBlender/openMVSMACelcap/./DensifyPointCloud --estimate-normals 1 '+tmpdir+'/MVS/scene.mvs && /OrtogOnBlender/openMVSMACelcap/./ReconstructMesh -d 16 --smooth 6 '+tmpdir+'/MVS/scene_dense.mvs && /OrtogOnBlender/openMVSMACelcap/./TextureMesh --export-type obj '+tmpdir+'/MVS/scene_dense_mesh.mvs', shell=True)

        if platform.system() == "Windows":

            subprocess.call('cd '+tmpdir+' && mkdir MVS && C:\OrtogOnBlender\openMVGWin\openMVG_main_openMVG2openMVS -i '+tmpdir+'/OpenMVG/reconstruction_sequential/sfm_data.bin -o '+tmpdir+'/MVS/scene.mvs && C:\OrtogOnBlender\openMVSWin\DensifyPointCloud --estimate-normals 1 '+tmpdir+'/MVS/scene.mvs && C:\OrtogOnBlender\openMVSWin\ReconstructMesh -d 16 --smooth 6 '+tmpdir+'/MVS/scene_dense.mvs && C:\OrtogOnBlender\openMVSWin\TextureMesh --export-type obj '+tmpdir+'/MVS/scene_dense_mesh.mvs', shell=True)

#        else:
#            subprocess.call(OpenMVSPath ,  shell=True)            
            #subprocess.call([ 'meshlabserver', '-i', tmpdir+'scene_dense_mesh_texture.ply', '-o', tmpdir+'scene_dense_mesh_texture.obj', '-om', 'vn', 'wt' ])



        bpy.ops.import_scene.obj(filepath=tmpOBJface, filter_glob="*.obj;*.mtl")

        scene_dense_mesh_texture = bpy.data.objects['scene_dense_mesh_texture']

        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = scene_dense_mesh_texture
        bpy.data.objects['scene_dense_mesh_texture'].select = True


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
            
#        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
        bpy.ops.view3d.view_all(center=False)
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
        bpy.context.object.modifiers["Displace"].strength = 1.7
        bpy.context.object.modifiers["Displace"].mid_level = 0.5
        bpy.context.object.modifiers["Displace"].show_viewport = False

                #Comprime modificadores
        bpy.context.object.modifiers["Smooth"].show_expanded = False
        bpy.context.object.modifiers["Multires"].show_expanded = False
        bpy.context.object.modifiers["Displace"].show_expanded = False

        bpy.ops.object.shade_smooth()

# SMVS -------------------------------------------------------------------------------------------------------------------------------------------
      
#    tmpdir = tempfile.mkdtemp()
    tmpOBJface = tmpdir+'/MVE/scene_dense_mesh_texture2.obj'
#    subprocess.call(['rm /tmp/DIRETORIO_FOTOS.txt'],  shell=True)

#    homeall = expanduser("~")
    
    if platform.system() == "Linux":
        subprocess.call('cd '+tmpdir+' && '+homeall+'/Programs/OrtogOnBlender/openMVG/./openMVG_main_openMVG2MVE2 -i '+tmpdir+'/OpenMVG/reconstruction_sequential/sfm_data.bin -o '+tmpdir, shell=True)
        SMVSPath = homeall+"/Programs/OrtogOnBlender/SMVS/"
        subprocess.call(['rm', '-rf', tmpdir+'/scene'])
#            subprocess.call([SMVSPath+'./makescene', '-i', scn.my_tool.path, tmpdir+'/scene'])
#            subprocess.call([SMVSPath+'./sfmrecon', tmpdir+'/scene'])
        subprocess.call([SMVSPath+'./smvsrecon', '-s2', tmpdir+'/MVE'])
        subprocess.call(['meshlabserver', '-i', tmpdir+'/MVE/smvs-B2.ply', '-o', tmpdir+'/MVE/meshlab.ply', '-s', SMVSPath+'SMVSmeshlab.mlx', '-om'])
        subprocess.call([SMVSPath+'./texrecon', '--data_term=area', '--skip_global_seam_leveling', '--outlier_removal=gauss_damping', tmpdir+'/MVE::undistorted', tmpdir+'/MVE/meshlab.ply', tmpdir+'/MVE/scene_dense_mesh_texture2'])
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


    print("FIX SMVS SURFACE AND MAP")

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
    bpy.ops.uv.smart_project(island_margin=0.03)
#    bpy.ops.uv.smart_project(island_margin=0.3)


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
    bpy.context.object.modifiers["Displace"].strength = 2.2
    bpy.context.object.modifiers["Displace"].mid_level = 0.5
    bpy.context.object.modifiers["Displace"].show_viewport = False

    #Comprime modificadores
    bpy.context.object.modifiers["Smooth"].show_expanded = False
    bpy.context.object.modifiers["Multires"].show_expanded = False
    bpy.context.object.modifiers["Displace"].show_expanded = False

    bpy.ops.object.shade_smooth()

#    bpy.ops.file.unpack_item(id_name="UV_FACE")
#    bpy.data.images["UV_FACE"].filepath = tmpdir+'/UV_FACE.png'
#    bpy.data.images["UV_FACE"].save()

#    bpy.ops.file.pack_all()
    bpy.data.images["UV_FACE"].pack(as_png=True)


# IMPORTA CAMERA ---------------------------------------------------------------------------------------------------------------------------------

    if platform.system() == "Linux":
        subprocess.call('~/Programs/OrtogOnBlender/openMVG/./openMVG_main_openMVG2PMVS -i '+tmpdir+'/OpenMVG/reconstruction_sequential/sfm_data.bin -o '+tmpdir+'/ && mkdir '+tmpdir+'/PMVS/bundle && cp '+tmpdir+'/PMVS/bundle.rd.out '+tmpdir+'/PMVS/bundle/bundle.out && cp -v '+mypath+'/* '+tmpdir+'/PMVS/', shell=True)

        bpy.ops.bundle.out(filepath=tmpdir+"/PMVS/bundle/bundle.out", filter_glob="bundle.out")
        
        print("BUNDLE IMPORTED")


    if platform.system() == "Windows":
                subprocess.call('C:\\OrtogOnBlender\\openMVGWin\\openMVG_main_openMVG2PMVS.exe -i '+tmpdir+'\\OpenMVG\\reconstruction_sequential\\sfm_data.bin -o '+tmpdir+'\\ &&  mkdir '+tmpdir+'\\PMVS\\bundle && copy '+tmpdir+'\\PMVS\\bundle.rd.out '+tmpdir+'\\PMVS\\bundle\\bundle.out && copy '+mypath+'\\* '+tmpdir+'\\PMVS\\', shell=True)

                bpy.ops.bundle.out(filepath=tmpdir+"\\PMVS\\bundle\\bundle.out", filter_glob="bundle.out")
        

    if platform.system() == "Darwin":
                subprocess.call('/OrtogOnBlender/openMVGMAC/./openMVG_main_openMVG2PMVS -i '+tmpdir+'/OpenMVG/reconstruction_sequential/sfm_data.bin -o '+tmpdir+' && mkdir '+tmpdir+'/PMVS/bundle && cp '+tmpdir+'/PMVS/bundle.rd.out '+tmpdir+'/PMVS/bundle/bundle.out && cp -v '+mypath+'/* '+tmpdir+'/PMVS/', shell=True)

                bpy.ops.bundle.out(filepath=tmpdir+"/PMVS/bundle/bundle.out", filter_glob="bundle.out")

    bpy.ops.object.select_all(action='SELECT')
    bpy.context.scene.objects.active = scene_dense_mesh_texture
#        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    bpy.ops.object.parent_set(type='OBJECT', xmirror=False, keep_transform=True)

