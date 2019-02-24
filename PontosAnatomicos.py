import bpy
import bmesh
from math import sqrt

# PONTOS NOS DENTES SUPERIORES

def EMP11Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP11"
    bpy.context.object.empty_draw_size = 3
    
'''    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP11']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''    

def EMP21Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP21"
    bpy.context.object.empty_draw_size = 3
    
'''    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP21']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMP13Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP13"
    bpy.context.object.empty_draw_size = 3
    
'''    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP13']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMP23Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP23"
    bpy.context.object.empty_draw_size = 3
    
'''    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP23']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMP16Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP16"
    bpy.context.object.empty_draw_size = 3
    
'''    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP16']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMP26Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP26"
    bpy.context.object.empty_draw_size = 3
    
'''    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP26']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPPalatineDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPPalatine"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMPPalatine']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPUpperIncisorDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPApoint"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMPApoint']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPNasalSpineDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPNasalSpine"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMPNasalSpine']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPPterygoidLDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPPterygoidL"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMPPterygoidL']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPPterygoidRDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPPterygoidR"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMPPterygoidR']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

# PONTOS NOS DENTES INFERIORES

def EMP31Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP31"
    bpy.context.object.empty_draw_size = 3
    
'''    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP31']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMP41Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP41"
    bpy.context.object.empty_draw_size = 3
    
'''    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP41']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMP33Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP33"
    bpy.context.object.empty_draw_size = 3
    
'''    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP33']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMP43Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP43"
    bpy.context.object.empty_draw_size = 3
    
'''    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP43']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMP36Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP36"
    bpy.context.object.empty_draw_size = 3
    
'''    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP36']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMP46Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP46"
    bpy.context.object.empty_draw_size = 3
    
'''    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP46']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPBpointDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPBpoint"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMPBpoint']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

# MENTO

def EMPPogonionDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPPogonion"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['me']
    b = bpy.data.objects['EMPPogonion']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPMentonDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPMenton"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['me']
    b = bpy.data.objects['EMPMenton']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPMentonLDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPMentonL"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['me']
    b = bpy.data.objects['EMPMentonL']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPMentonRDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPMentonR"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['me']
    b = bpy.data.objects['EMPMentonR']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPLSpointDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene


    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPLSpoint"
    bpy.context.object.empty_draw_size = 3
'''
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPLSpoint"
    bpy.context.object.empty_draw_size = 3

    bpy.ops.object.select_all(action='DESELECT')


    a = bpy.data.objects['FaceMalha.001']
    b = bpy.data.objects['EMPLSpoint']

    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a

    bpy.ops.object.editmode_toggle()

    bpy.ops.object.vertex_parent_set()

    bpy.ops.object.editmode_toggle()
'''

def EMPPGpointDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPPGpoint"
    bpy.context.object.empty_draw_size = 3

'''
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPPGpoint"
    bpy.context.object.empty_draw_size = 3

    bpy.ops.object.select_all(action='DESELECT')

    a = bpy.data.objects['FaceMalha.001']
    b = bpy.data.objects['EMPPGpoint']

    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a

    bpy.ops.object.editmode_toggle()

    bpy.ops.object.vertex_parent_set()

    bpy.ops.object.editmode_toggle()
'''

def EMPGonionRDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPGonionR"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['rd']
    b = bpy.data.objects['EMPGonionR']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPGonionLDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPGonionL"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['re']
    b = bpy.data.objects['EMPGonionL']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPEyeRDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPEyeR"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['ca']
    b = bpy.data.objects['EMPEyeR']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPEyeLDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPEyeL"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['ca']
    b = bpy.data.objects['EMPEyeL']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPMeatusRDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPMeatusR"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['ca']
    b = bpy.data.objects['EMPMeatusR']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPMeatusLDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPMeatusL"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['ca']
    b = bpy.data.objects['EMPMeatusL']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPNasionDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPNasion"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['ca']
    b = bpy.data.objects['EMPNasion']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPApointDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPApoint"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMPApoint']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

def EMPSellaTurcicaDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPSellaTurcica"
    bpy.context.object.empty_draw_size = 3

'''
    a = bpy.data.objects['ca']
    b = bpy.data.objects['EMPSellaTurcica']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
'''

# PONTOS NOS DENTES SUPERIORES

class EMP11(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp11"
    bl_label = "EMP11"
    
    def execute(self, context):
        EMP11Def(self, context)
        return {'FINISHED'}

  
class EMP21(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp21"
    bl_label = "EMP21"
    
    def execute(self, context):
        EMP21Def(self, context)
        return {'FINISHED'}
    
   
class EMP13(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp13"
    bl_label = "EMP1"
    
    def execute(self, context):
        EMP13Def(self, context)
        return {'FINISHED'}
    
 
class EMP23(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp23"
    bl_label = "EMP23"
    
    def execute(self, context):
        EMP23Def(self, context)
        return {'FINISHED'}
    

class EMP16(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp16"
    bl_label = "EMP16"
    
    def execute(self, context):
        EMP16Def(self, context)
        return {'FINISHED'}
    
   
class EMP26(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp26"
    bl_label = "EMP26"
    
    def execute(self, context):
        EMP26Def(self, context)
        return {'FINISHED'}


class EMPPterygoidL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pterygoidl"
    bl_label = "EMPPterygoidL"

    def execute(self, context):
        EMPPterygoidLDef(self, context)
        return {'FINISHED'}

class EMPPterygoidR(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pterygoidr"
    bl_label = "EMPPterygoidR"

    def execute(self, context):
        EMPPterygoidRDef(self, context)
        return {'FINISHED'}

class EMPPalatine(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.palatine"
    bl_label = "EMPPalatine"

    def execute(self, context):
        EMPPalatineDef(self, context)
        return {'FINISHED'}


class EMPUpperIncisor(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.upperincisor"
    bl_label = "EMPUpperIncisor"

    def execute(self, context):
        EMPUpperIncisorDef(self, context)
        return {'FINISHED'}

class EMPNasalSpine(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.nasalspine"
    bl_label = "EMPNasalSpine"

    def execute(self, context):
        EMPNasalSpineDef(self, context)
        return {'FINISHED'}

class EMPPogonion(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pogonion"
    bl_label = "EMPPogonion"

    def execute(self, context):
        EMPPogonionDef(self, context)
        return {'FINISHED'}

class EMPMenton(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.menton"
    bl_label = "EMPMenton"

    def execute(self, context):
        EMPMentonDef(self, context)
        return {'FINISHED'}

class EMPMentonL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.mentonl"
    bl_label = "EMPMentonL"

    def execute(self, context):
        EMPMentonLDef(self, context)
        return {'FINISHED'}

class EMPMentonR(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.mentonr"
    bl_label = "EMPMentonR"

    def execute(self, context):
        EMPMentonRDef(self, context)
        return {'FINISHED'}

class EMPMeatusR(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.meatusr"
    bl_label = "EMPMeatusR"

    def execute(self, context):
        EMPMeatusRDef(self, context)
        return {'FINISHED'}

class EMPMeatusL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.meatusl"
    bl_label = "EMPMeatusL"

    def execute(self, context):
        EMPMeatusLDef(self, context)
        return {'FINISHED'}

# PONTOS NOS DENTES INFERIORES

class EMP31(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp31"
    bl_label = "EMP31"
    
    def execute(self, context):
        EMP31Def(self, context)
        return {'FINISHED'}


class EMP41(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp41"
    bl_label = "EMP41"
    
    def execute(self, context):
        EMP41Def(self, context)
        return {'FINISHED'}
    
class EMP33(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp33"
    bl_label = "EMP33"
    
    def execute(self, context):
        EMP33Def(self, context)
        return {'FINISHED'}
    
class EMP43(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp43"
    bl_label = "EMP43"
    
    def execute(self, context):
        EMP43Def(self, context)
        return {'FINISHED'}
    

class EMP36(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp36"
    bl_label = "EMP36"
    
    def execute(self, context):
        EMP36Def(self, context)
        return {'FINISHED'}
    

class EMP46(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp46"
    bl_label = "EMP46"
    
    def execute(self, context):
        EMP46Def(self, context)
        return {'FINISHED'}


class EMPBpoint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.bpoint"
    bl_label = "EMPBpoint"

    def execute(self, context):
        EMPBpointDef(self, context)
        return {'FINISHED'}

# EMPTIES MOLES

class EMPLSpoint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.lspoint"
    bl_label = "EMPLSpoint"
    
    def execute(self, context):
        EMPLSpointDef(self, context)
        return {'FINISHED'}

class EMPPGpoint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pgpoint"
    bl_label = "EMPPGpoint"
    
    def execute(self, context):
        EMPPGpointDef(self, context)
        return {'FINISHED'}

class EMPGonionR(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gonionr"
    bl_label = "EMPGonionR"
    
    def execute(self, context):
        EMPGonionRDef(self, context)
        return {'FINISHED'}

class EMPGonionL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gonionl"
    bl_label = "EMPGonionL"
    
    def execute(self, context):
        EMPGonionLDef(self, context)
        return {'FINISHED'}

class EMPEyeR(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.eyer"
    bl_label = "EMPEyeR"
    
    def execute(self, context):
        EMPEyeRDef(self, context)
        return {'FINISHED'}

class EMPEyeL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.eyel"
    bl_label = "EMPEyeL"
    
    def execute(self, context):
        EMPEyeLDef(self, context)
        return {'FINISHED'}

class EMPNasion(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.nasion"
    bl_label = "EMPNasion"
    
    def execute(self, context):
        EMPNasionDef(self, context)
        return {'FINISHED'}

class EMPApoint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.apoint"
    bl_label = "EMPApoint"
    
    def execute(self, context):
        EMPApointDef(self, context)
        return {'FINISHED'}

class EMPSellaTurcica(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.sella"
    bl_label = "SellaTurcica"
    
    def execute(self, context):
        EMPSellaTurcicaDef(self, context)
        return {'FINISHED'}

# Funcao parenteia pontos
 
def ParenteiaPonto(ponto):

    listaDist = []

    osteotomias = [bpy.data.objects["ca"], bpy.data.objects["ma"], bpy.data.objects["cm"], bpy.data.objects["me"], bpy.data.objects["rd"], bpy.data.objects["re"]]

#    for item in bpy.data.objects:
    for item in osteotomias:
#        if item.hide == False and item.type == 'MESH':

            obj = bpy.data.objects[item.name]
            # print("OBJETO ATUAL", obj)

            # Lista os vértices do objeto
            if obj.mode == 'EDIT':
                bm = bmesh.from_edit_mesh(obj.data)
                vertices = bm.verts

            else:
                vertices = obj.data.vertices

            # Todos os vértices por vetor
            verts = [obj.matrix_world * vert.co for vert in vertices] 

            # Captura vetor do objeto

            referencia = bpy.data.objects[ponto].location



            # Calcula distância pontos

            def DistanciaObjs(obj1, obj2):

                objA = bpy.data.objects[obj1].location
                objB = obj2
                
                distancia = sqrt( (objB[0] - objA[0])**2 + (objB[1] - objA[1])**2 + (objB[2] - objA[2])**2 )
                
                return distancia
                


            for i in range(len(verts)):

                vertAtual = verts[i]

                distanciaVert = DistanciaObjs(ponto, vertAtual)

                listaDist.append([distanciaVert, obj.name])
                
                

    listaFin = sorted(listaDist)
    print("MAIS PRÓXIMO!", listaFin[0])

    bpy.ops.object.select_all(action='DESELECT')
    ObjPai = bpy.data.objects[listaFin[0][1]]
    ObjFilho = bpy.data.objects[ponto]
    ObjPai.select = True
    ObjFilho.select = True
    bpy.context.scene.objects.active = ObjPai
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

def testaPontosDef(self, context):
		def ERROPonto(self, context):
			self.layout.label("Doesn't have the object above!")
			
		def OKPonto(self, context):
			self.layout.label("All points OK!!!")

		def TestaPontos(ponto):
			try:
				ob_act = bpy.data.objects[ponto]
			except:
				bpy.context.window_manager.popup_menu(ERROPonto, title="--> "+ponto+" <--", icon='INFO')
	

		pontosAnat = ["EMP11", "EMP21","EMP13","EMP23","EMP16","EMP26","EMPPalatine","EMPApoint","EMPNasalSpine","EMPPterygoidR","EMPPterygoidL","EMP31","EMP41","EMP33","EMP43","EMP36","EMP46","EMPBpoint","EMPPogonion","EMPMenton","EMPMentonR","EMPMentonL","EMPNasion","EMPEyeR","EMPEyeL","EMPMeatusR","EMPMeatusL","EMPSellaTurcica","EMPGonionR","EMPGonionL", "EMPLSpoint", "EMPPGpoint","FaceMalha.001" ]

		for i in pontosAnat:
			TestaPontos(i)
		#bpy.context.window_manager.popup_menu(OKPonto, title="Great!", icon='INFO')
		
# PARENTEIA PONTO MOLE

def ParenteiaPontoMole(ponto):

    listaDist = []

    obj = bpy.data.objects["FaceMalha.001"]
            # print("OBJETO ATUAL", obj)

            # Lista os vértices do objeto
    if obj.mode == 'EDIT':
        bm = bmesh.from_edit_mesh(obj.data)
        vertices = bm.verts

    else:
        vertices = obj.data.vertices

            # Todos os vértices por vetor
    verts = [obj.matrix_world * vert.co for vert in vertices] 

            # Captura vetor do objeto

    referencia = bpy.data.objects[ponto].location
    
            # Calcula distância pontos

    def DistanciaObjs(obj1, obj2):
        objA = bpy.data.objects[obj1].location
        objB = obj2
                
        distancia = sqrt( (objB[0] - objA[0])**2 + (objB[1] - objA[1])**2 + (objB[2] - objA[2])**2 )
                
        return distancia
                

    for i in range(len(verts)):

        vertAtual = verts[i]
            
        distanciaVert = DistanciaObjs(ponto, vertAtual)

        listaDist.append([distanciaVert, i])
                
                

    listaFin = sorted(listaDist)
    print("MAIS PRÓXIMO!", listaFin[0])
    


    bpy.ops.object.select_all(action='DESELECT')
    obj.select = True
    bpy.context.scene.objects.active = obj

    bpy.ops.object.mode_set(mode = 'EDIT') 
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set(mode = 'OBJECT')
    obj.data.vertices[listaFin[0][1]].select = True
    bpy.ops.object.mode_set(mode = 'EDIT')
    
    bpy.ops.object.mode_set(mode = 'OBJECT')            

    bpy.ops.object.select_all(action='DESELECT')

    b = bpy.data.objects[ponto]

    obj.select = True
    b.select = True
    bpy.context.scene.objects.active = obj

    bpy.ops.object.editmode_toggle()
    bpy.ops.object.vertex_parent_set()
    bpy.ops.object.editmode_toggle()  

class testaPontos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.testa_pontos"
    bl_label = "TestaPontos"
    
    def execute(self, context):
        testaPontosDef(self, context)
        return {'FINISHED'}

    
def ParenteiaEMPDef(self, context):

	# Maxilla
	ParenteiaPonto("EMP11")
	ParenteiaPonto("EMP21")
	ParenteiaPonto("EMP13")
	ParenteiaPonto("EMP23")
	ParenteiaPonto("EMP16")
	ParenteiaPonto("EMP26")
	ParenteiaPonto("EMPPalatine")
	ParenteiaPonto("EMPApoint")
	ParenteiaPonto("EMPNasalSpine")
	ParenteiaPonto("EMPPterygoidR")
	ParenteiaPonto("EMPPterygoidL")

		# Mandible body
	ParenteiaPonto("EMP31")
	ParenteiaPonto("EMP41")
	ParenteiaPonto("EMP33")
	ParenteiaPonto("EMP43")
	ParenteiaPonto("EMP36")
	ParenteiaPonto("EMP46")
	ParenteiaPonto("EMPBpoint")

		# Chin
	ParenteiaPonto("EMPPogonion")
	ParenteiaPonto("EMPMenton")
	ParenteiaPonto("EMPMentonR")
	ParenteiaPonto("EMPMentonL")

		# Soft Tissue

	ParenteiaPontoMole("EMPLSpoint")
	ParenteiaPontoMole("EMPPGpoint")

		# Others
	ParenteiaPonto("EMPNasion")
	ParenteiaPonto("EMPEyeR")
	ParenteiaPonto("EMPEyeL")
	ParenteiaPonto("EMPMeatusR")
	ParenteiaPonto("EMPMeatusL")
	ParenteiaPonto("EMPSellaTurcica")
	ParenteiaPonto("EMPGonionR")
	ParenteiaPonto("EMPGonionL")

	
class ParenteiaEMP(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.parenteia_emp"
    bl_label = "ParenteiaEMP"
    
    def execute(self, context):
        ParenteiaEMPDef(self, context)
        return {'FINISHED'}
