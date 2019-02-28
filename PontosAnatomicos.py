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

# Dente 11
class EMP11(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp11"
    bl_label = "EMP11"

    @classmethod
    def poll(cls, context):

        found = 'EMP11' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    
    def execute(self, context):
        EMP11Def(self, context)
        return {'FINISHED'}

# Dente 21  
class EMP21(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp21"
    bl_label = "EMP21"

    @classmethod
    def poll(cls, context):

        found = 'EMP21' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMP21Def(self, context)
        return {'FINISHED'}
    

# Dente 13   
class EMP13(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp13"
    bl_label = "EMP1"

    @classmethod
    def poll(cls, context):

        found = 'EMP13' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMP13Def(self, context)
        return {'FINISHED'}
    
# Dente 23 
class EMP23(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp23"
    bl_label = "EMP23"

    @classmethod
    def poll(cls, context):

        found = 'EMP23' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMP23Def(self, context)
        return {'FINISHED'}
    
# Dente 16
class EMP16(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp16"
    bl_label = "EMP16"

    @classmethod
    def poll(cls, context):

        found = 'EMP16' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMP16Def(self, context)
        return {'FINISHED'}
    
# Dente 26   
class EMP26(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp26"
    bl_label = "EMP26"

    @classmethod
    def poll(cls, context):

        found = 'EMP26' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMP26Def(self, context)
        return {'FINISHED'}

# Terigoide L
class EMPPterygoidL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pterygoidl"
    bl_label = "EMPPterygoidL"

    @classmethod
    def poll(cls, context):

        found = 'EMPPterygoidL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        EMPPterygoidLDef(self, context)
        return {'FINISHED'}

# Perigoide R
class EMPPterygoidR(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pterygoidr"
    bl_label = "EMPPterygoidR"

    @classmethod
    def poll(cls, context):

        found = 'EMPPterygoidR' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        EMPPterygoidRDef(self, context)
        return {'FINISHED'}

# Palatina
class EMPPalatine(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.palatine"
    bl_label = "EMPPalatine"

    @classmethod
    def poll(cls, context):

        found = 'EMPPalatine' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        EMPPalatineDef(self, context)
        return {'FINISHED'}

# Incisivo Superior
class EMPUpperIncisor(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.upperincisor"
    bl_label = "EMPUpperIncisor"

    @classmethod
    def poll(cls, context):

        found = 'EMPUpperIncisor' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        EMPUpperIncisorDef(self, context)
        return {'FINISHED'}

# Espinha Nasal
class EMPNasalSpine(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.nasalspine"
    bl_label = "EMPNasalSpine"

    @classmethod
    def poll(cls, context):

        found = 'EMPNasalSpine' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        EMPNasalSpineDef(self, context)
        return {'FINISHED'}

# Pogonion
class EMPPogonion(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pogonion"
    bl_label = "EMPPogonion"

    @classmethod
    def poll(cls, context):

        found = 'EMPPogonion' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        EMPPogonionDef(self, context)
        return {'FINISHED'}

# Mento
class EMPMenton(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.menton"
    bl_label = "EMPMenton"

    @classmethod
    def poll(cls, context):

        found = 'EMPMenton' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        EMPMentonDef(self, context)
        return {'FINISHED'}

# Mento L
class EMPMentonL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.mentonl"
    bl_label = "EMPMentonL"

    @classmethod
    def poll(cls, context):

        found = 'EMPMentonL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        EMPMentonLDef(self, context)
        return {'FINISHED'}

# Mento R
class EMPMentonR(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.mentonr"
    bl_label = "EMPMentonR"

    @classmethod
    def poll(cls, context):

        found = 'EMPMentonR' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        EMPMentonRDef(self, context)
        return {'FINISHED'}

# Meato R
class EMPMeatusR(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.meatusr"
    bl_label = "EMPMeatusR"

    @classmethod
    def poll(cls, context):

        found = 'EMPMeatusR' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        EMPMeatusRDef(self, context)
        return {'FINISHED'}

#Meato L
class EMPMeatusL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.meatusl"
    bl_label = "EMPMeatusL"

    @classmethod
    def poll(cls, context):

        found = 'EMPMeatusL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        EMPMeatusLDef(self, context)
        return {'FINISHED'}

# PONTOS NOS DENTES INFERIORES

# Dente 31
class EMP31(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp31"
    bl_label = "EMP31"

    @classmethod
    def poll(cls, context):

        found = 'EMP31' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMP31Def(self, context)
        return {'FINISHED'}

# Dente 41
class EMP41(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp41"
    bl_label = "EMP41"

    @classmethod
    def poll(cls, context):

        found = 'EMP41' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMP41Def(self, context)
        return {'FINISHED'}

# Dente 33    
class EMP33(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp33"
    bl_label = "EMP33"

    @classmethod
    def poll(cls, context):

        found = 'EMP33' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMP33Def(self, context)
        return {'FINISHED'}

# Dente 43    
class EMP43(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp43"
    bl_label = "EMP43"

    @classmethod
    def poll(cls, context):

        found = 'EMP43' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMP43Def(self, context)
        return {'FINISHED'}
    
# Dente 36
class EMP36(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp36"
    bl_label = "EMP36"

    @classmethod
    def poll(cls, context):

        found = 'EMP36' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMP36Def(self, context)
        return {'FINISHED'}
    
# Dente 46
class EMP46(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp46"
    bl_label = "EMP46"

    @classmethod
    def poll(cls, context):

        found = 'EMP46' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMP46Def(self, context)
        return {'FINISHED'}

# Ponto B
class EMPBpoint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.bpoint"
    bl_label = "EMPBpoint"

    @classmethod
    def poll(cls, context):

        found = 'EMPBpoint' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        EMPBpointDef(self, context)
        return {'FINISHED'}

# EMPTIES MOLES


# Ponto LS
class EMPLSpoint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.lspoint"
    bl_label = "EMPLSpoint"

    @classmethod
    def poll(cls, context):

        found = 'EMPLSpoint' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMPLSpointDef(self, context)
        return {'FINISHED'}

# Ponto PG
class EMPPGpoint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pgpoint"
    bl_label = "EMPPGpoint"

    @classmethod
    def poll(cls, context):

        found = 'EMPPGpoint' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMPPGpointDef(self, context)
        return {'FINISHED'}

# Gonio R
class EMPGonionR(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gonionr"
    bl_label = "EMPGonionR"

    @classmethod
    def poll(cls, context):

        found = 'EMPGonionR' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMPGonionRDef(self, context)
        return {'FINISHED'}

# Gonio L
class EMPGonionL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gonionl"
    bl_label = "EMPGonionL"

    @classmethod
    def poll(cls, context):

        found = 'EMPGonionL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMPGonionLDef(self, context)
        return {'FINISHED'}

# Olho R
class EMPEyeR(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.eyer"
    bl_label = "EMPEyeR"

    @classmethod
    def poll(cls, context):

        found = 'EMPEyeR' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMPEyeRDef(self, context)
        return {'FINISHED'}

# Olho L
class EMPEyeL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.eyel"
    bl_label = "EMPEyeL"

    @classmethod
    def poll(cls, context):

        found = 'EMPEyeL' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMPEyeLDef(self, context)
        return {'FINISHED'}

# Nasio
class EMPNasion(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.nasion"
    bl_label = "EMPNasion"

    @classmethod
    def poll(cls, context):

        found = 'EMPNasion' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMPNasionDef(self, context)
        return {'FINISHED'}

# Ponto A
class EMPApoint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.apoint"
    bl_label = "EMPApoint"

    @classmethod
    def poll(cls, context):

        found = 'EMPApoint' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
    def execute(self, context):
        EMPApointDef(self, context)
        return {'FINISHED'}

# Sela Turcica
class EMPSellaTurcica(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.sella"
    bl_label = "EMPSellaTurcica"

    @classmethod
    def poll(cls, context):

        found = 'EMPSellaTurcica' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    
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

# Separa lincados

def SegmentaLinkedDef(self, context):

    listaDist = []

    ponto = bpy.context.scene.cursor_location

    obj = bpy.context.scene.objects.active
    
    # Duplica objeto
    bpy.ops.object.duplicate()
    
    # Joga outro layer
    bpy.ops.object.move_to_layer(layers=(False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False))

    bpy.ops.object.select_all(action='DESELECT')
    obj.select = True
    bpy.context.scene.objects.active = obj

            # Lista os vértices do objeto
    if obj.mode == 'EDIT':
        bm = bmesh.from_edit_mesh(obj.data)
        vertices = bm.verts

    else:
        vertices = obj.data.vertices

            # Todos os vértices por vetor
    verts = [obj.matrix_world * vert.co for vert in vertices] 

            # Captura vetor do objeto

    referencia = bpy.context.scene.cursor_location
    
            # Calcula distância pontos

    def DistanciaObjs(obj1, obj2):
        objA = referencia
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
    
    bpy.ops.mesh.select_linked()
    
    bpy.ops.mesh.select_all(action='INVERT')

    bpy.ops.mesh.delete(type='VERT')

    bpy.ops.object.mode_set(mode = 'OBJECT')


class SegmentaLinked(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.segmenta_linked"
    bl_label = "SegmentaLinked"
    
    def execute(self, context):
        SegmentaLinkedDef(self, context)
        return {'FINISHED'}


# Segmentação por pintura - Apaga Azul

def MantemPintadoDef(self, context):
    bpy.ops.object.mode_set(mode = 'OBJECT')

    bpy.context.object.name = "ObjSplint"

    # Seleciona área interesse

    # Which group to find?
    groupName = 'Group'

    # Use the active object
    obj = bpy.context.active_object

    # Make sure you're in edit mode
    bpy.ops.object.mode_set(mode='EDIT')

    # Deselect all verts
    bpy.ops.mesh.select_all(action='DESELECT')

    # Make sure the active group is the one we want
    bpy.ops.object.vertex_group_set_active(group=groupName)

    # Select the verts
    bpy.ops.object.vertex_group_select()


    bpy.ops.object.vertex_group_assign()
    bpy.ops.mesh.select_all(action='INVERT')

    bpy.ops.mesh.delete(type='VERT')
    bpy.ops.object.mode_set(mode = 'OBJECT')

class MantemPintado(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.mantem_pintado"
    bl_label = "MantemPintado"
    
    def execute(self, context):
        MantemPintadoDef(self, context)
        return {'FINISHED'}

# Segmentação por pintura - Apaga Vermelho

def ApagaPintadoDef(self, context):
    bpy.ops.object.mode_set(mode = 'OBJECT')

    bpy.context.object.name = "ObjSplint"

    # Seleciona área interesse

    # Which group to find?
    groupName = 'Group'

    # Use the active object
    obj = bpy.context.active_object

    # Make sure you're in edit mode
    bpy.ops.object.mode_set(mode='EDIT')

    # Deselect all verts
    bpy.ops.mesh.select_all(action='DESELECT')

    # Make sure the active group is the one we want
    bpy.ops.object.vertex_group_set_active(group=groupName)

    # Select the verts
    bpy.ops.object.vertex_group_select()


    bpy.ops.object.vertex_group_assign()
#    bpy.ops.mesh.select_all(action='INVERT')

    bpy.ops.mesh.delete(type='VERT')
    bpy.ops.object.mode_set(mode = 'OBJECT')

class ApagaPintado(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.apaga_pintado"
    bl_label = "ApagaPintado"
    
    def execute(self, context):
        ApagaPintadoDef(self, context)
        return {'FINISHED'}
