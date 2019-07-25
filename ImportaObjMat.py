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
        dirScript = 'C:/OrtogOnBlender/Blender280/2.80/scripts/' 

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
    obj.select_set(True)
    context.view_layer.objects.active = obj
    bpy.context.object.show_transparent = True


    bpy.ops.object.material_slot_add()
    obj.data.materials[0] = material_01

    mensagem = "Beleza!"

    return mensagem



