import bpy
import platform

# IMPORTA SPLINT COM ARMATURE

def ImportaSplintDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene


    if platform.system() == "Linux":

        dirScript = bpy.utils.user_resource('SCRIPTS')

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Group\\"
        object    = "SPLINT"

    if platform.system() == "Darwin":

        dirScript = bpy.utils.user_resource('SCRIPTS')

        blendfile = "/OrtogOnBlender/Blender/blender.app/Contents/Resources/2.78/scripts/addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Group\\"
        object    = "SPLINT"
        
    if platform.system() == "Windows":

        dirScript = 'C:/OrtogOnBlender/Blender/2.78/scripts/'

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Group\\"
        object    = "SPLINT"    


#    if platform.system() == "Darwin":

#        dirScript = bpy.utils.user_resource('SCRIPTS')

#        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
#        section   = "\\Group\\"
#        object    = "SPLINT"


    filepath  = blendfile + section + object
    directory = blendfile + section
    filename  = object

    bpy.ops.wm.append(
        filepath=filepath, 
        filename=filename,
        directory=directory)

# CRIA EMPTIES INTERMEDIÁRIOS

def CriaSplintDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.select_all(action='DESELECT')

    a = bpy.data.objects['EMP11']
    b = bpy.data.objects['EMP41']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP1141"
    bpy.context.object.empty_draw_size = .5
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP1141']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


    # ----------------------------

    a = bpy.data.objects['EMP21']
    b = bpy.data.objects['EMP31']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP2131"
    bpy.context.object.empty_draw_size = .5
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP2131']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    
    # ----------------------------

    a = bpy.data.objects['EMP23']
    b = bpy.data.objects['EMP33']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP2333"
    bpy.context.object.empty_draw_size = .5
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP2333']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    
    # ----------------------------

    a = bpy.data.objects['EMP13']
    b = bpy.data.objects['EMP43']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP1343"
    bpy.context.object.empty_draw_size = .5
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP1343']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    
    # ----------------------------

    a = bpy.data.objects['EMP26']
    b = bpy.data.objects['EMP36']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP2636"
    bpy.context.object.empty_draw_size = .5
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP2636']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    
    # ----------------------------

    a = bpy.data.objects['EMP16']
    b = bpy.data.objects['EMP46']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP1646"
    bpy.context.object.empty_draw_size = .5
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP1646']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    
    # ---------------
    
    bpy.ops.object.importa_splint()
    
    # --------------
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP1646']                 
    a.select = True
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone1646']                 
    a.select = True
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP1343']                 
    a.select = True
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone1343']                 
    a.select = True
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP1141']                 
    a.select = True
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone1141']                 
    a.select = True
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP2131']                 
    a.select = True
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone2131']                 
    a.select = True
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP2333']                 
    a.select = True
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone2333']                 
    a.select = True
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP2636']                 
    a.select = True
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone2636']                 
    a.select = True
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

    
class CriaSplint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_splint"
    bl_label = "Cria Splint"
    
    def execute(self, context):
        CriaSplintDef(self, context)
        return {'FINISHED'}

def ConfSplintDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.select_all(action='DESELECT')

    a = bpy.data.objects['ma']
    b = bpy.data.objects['cm']

    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    
    bpy.ops.object.duplicate()
    bpy.ops.object.join()
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['SPLINT']
    a.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.duplicate()
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['SPLINT']
    a.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.hide_view_set(unselected=False)
        
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['ma.001']
    b = bpy.data.objects['SPLINT.001']
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
#    bpy.ops.view3d.cork_mesh_slicer(method='DIFF')            
