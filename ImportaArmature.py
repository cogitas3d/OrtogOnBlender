import bpy
import platform

# IMPORTA ARMATURE

def ImportaArmatureDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    if platform.system() == "Linux" or platform.system() == "Darwin":
        dirScript = bpy.utils.user_resource('SCRIPTS')
        
        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Object\\"
        object    = "Armature_Head"
        
    if platform.system() == "Windows":
        dirScript = 'C:/OrtogOnBlender/Blender/2.78/scripts/' 

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Object\\"
        object    = "Armature_Head"

    filepath  = blendfile + section + object
    directory = blendfile + section
    filename  = object

    bpy.ops.wm.append(
        filepath=filepath, 
        filename=filename,
        directory=directory)
        
 #   bpy.ops.wm.append(filename=filename, directory=directory)

    # APAGA OBJETOS EXCEDENTES

    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['Mandibula']
    b = bpy.data.objects['SETA_Corpo_M']
    c = bpy.data.objects['SETA_Maxila']
    d = bpy.data.objects['SETA_Mento']


    a.select = True
    b.select = True
    c.select = True
    d.select = True


    bpy.ops.object.delete(use_global=False)
