import bpy
import platform

def ImportaMaterial(impMaterial, SelObj):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    if platform.system() == "Linux" or platform.system() == "Darwin":
        dirScript = bpy.utils.user_resource('SCRIPTS')
        
        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Material\\"
        object    = impMaterial
        
    if platform.system() == "Windows":
        dirScript = 'C:/OrtogOnBlender/Blender/2.78/scripts/' 

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Material\\"
        object    = impMaterial

    filepath  = blendfile + section + object
    directory = blendfile + section
    filename  = object

    bpy.ops.wm.append(
        filepath=filepath, 
        filename=filename,
        directory=directory)


#    bpy.context.scene.render.engine = 'CYCLES' # Troca tipo renderização

    # Etapa de importação de material


#    objects = bpy.data.objects


    material_01 = bpy.data.materials[impMaterial] # Informa material à def

    obj = bpy.data.objects[SelObj] # Informa objeto à def

    bpy.ops.object.select_all(action='DESELECT')
    obj.select = True
    bpy.context.scene.objects.active = obj
    bpy.context.object.show_transparent = True


    bpy.ops.object.material_slot_add()
    obj.data.materials[0] = material_01

    mensagem = "Beleza!"

    return mensagem


def ImportaLampXRay():

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    if platform.system() == "Linux" or platform.system() == "Darwin":
        dirScript = bpy.utils.user_resource('SCRIPTS')
        
        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Object\\"
        object    = 'Lamp_X_Ray'
        
    if platform.system() == "Windows":
        dirScript = 'C:/OrtogOnBlender/Blender/2.78/scripts/' 

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Object\\"
        object    = 'Lamp_X_Ray'

    filepath  = blendfile + section + object
    directory = blendfile + section
    filename  = object

    bpy.ops.wm.append(
        filepath=filepath, 
        filename=filename,
        directory=directory)

    bpy.ops.object.select_all(action='DESELECT')

#impMaterial = 'SCATTER_bone'

#SelObj = 'Cube'

#ImportaMaterial(impMaterial, SelObj)


def ImportaCefalo():

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    if platform.system() == "Linux" or platform.system() == "Darwin":
        dirScript = bpy.utils.user_resource('SCRIPTS')
        
        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Group\\"
        object    = '2D_cephalometry_all'
        
    if platform.system() == "Windows":
        dirScript = 'C:/OrtogOnBlender/Blender/2.78/scripts/' 

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Group\\"
        object    = '2D_cephalometry_all'

    filepath  = blendfile + section + object
    directory = blendfile + section
    filename  = object

    bpy.ops.wm.append(
        filepath=filepath, 
        filename=filename,
        directory=directory)

'''
# Apaga objetos a mais
    bpy.ops.object.select_all(action='DESELECT')

    apagar = [bpy.data.objects['PT_2nd_Mol.001'], bpy.data.objects['PT_1st_Mol.001'], bpy.data.objects['PT_Incisor_low_low.001'], bpy.data.objects['PT_Incisor_low_up.001'], bpy.data.objects['PT_Incisor_up_up.001'], bpy.data.objects['PT_Incisor_up_low.001'], bpy.data.objects['PT_Go.001'], bpy.data.objects['PT_Me.001'], bpy.data.objects['PT_N.001'], bpy.data.objects['PT_A.001'], bpy.data.objects['PT_B.001'], bpy.data.objects['PT_Ls.001'], bpy.data.objects['PT_Pg.001'], bpy.data.objects['PT_Po.001'], bpy.data.objects['PT_Or.001'], bpy.data.objects['PT_S.001']]

    a = 0

    NumObj = len(apagar)

    while a < NumObj:
        b = apagar[a].select = True
        print(b)
        print(a)
        a += 1
        
    bpy.context.scene.objects.active = apagar[0]
    bpy.ops.object.delete(use_global=False)
'''

def ImportaCamXray():

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    if platform.system() == "Linux" or platform.system() == "Darwin":
        dirScript = bpy.utils.user_resource('SCRIPTS')
        
        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Group\\"
        object    = 'Cameras_X_Ray'
        
    if platform.system() == "Windows":
        dirScript = 'C:/OrtogOnBlender/Blender/2.78/scripts/' 

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Group\\"
        object    = 'Cameras_X_Ray'

    filepath  = blendfile + section + object
    directory = blendfile + section
    filename  = object

    bpy.ops.wm.append(
        filepath=filepath, 
        filename=filename,
        directory=directory)

def SplitAreaTrabalho():
    context = bpy.context
#    obj = context.active_object
#    scn = context.scene        

    start_areas = context.screen.areas[:]
    bpy.ops.screen.area_split(direction='VERTICAL', factor=0.3)
    for area in context.screen.areas:
        if area not in start_areas:
                area.type = 'VIEW_3D'
    return {'FINISHED'}
