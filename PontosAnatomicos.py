import bpy

# PONTOS NOS DENTES SUPERIORES

def EMP11Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP11"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP11']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    

def EMP21Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP21"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP21']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


def EMP13Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP13"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP13']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


def EMP23Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP23"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP23']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


def EMP16Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP16"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP16']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


def EMP26Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP26"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP26']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


def EMPPalatineDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPPalatine"
    bpy.context.object.empty_draw_size = 3

    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMPPalatine']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

def EMPUpperIncisorDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPUpperIncisor"
    bpy.context.object.empty_draw_size = 3

    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMPUpperIncisor']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

def EMPNasalSpineDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPNasalSpine"
    bpy.context.object.empty_draw_size = 3

    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMPNasalSpine']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

def EMPPterygoidLDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPPterygoidL"
    bpy.context.object.empty_draw_size = 3

    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMPPterygoidL']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

def EMPPterygoidRDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPPterygoidR"
    bpy.context.object.empty_draw_size = 3

    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMPPterygoidR']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

# PONTOS NOS DENTES INFERIORES

def EMP31Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP31"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP31']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


def EMP41Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP41"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP41']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


def EMP33Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP33"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP33']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


def EMP43Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP43"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP43']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


def EMP36Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP36"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP36']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


def EMP46Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP46"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP46']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


def EMPBpointDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPBpoint"
    bpy.context.object.empty_draw_size = 3

    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMPBpoint']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

# MENTO

def EMPPogonionDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPPogonion"
    bpy.context.object.empty_draw_size = 3

    a = bpy.data.objects['me']
    b = bpy.data.objects['EMPPogonion']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

def EMPMentonDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPMenton"
    bpy.context.object.empty_draw_size = 3

    a = bpy.data.objects['me']
    b = bpy.data.objects['EMPMenton']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

def EMPMentonLDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPMentonL"
    bpy.context.object.empty_draw_size = 3

    a = bpy.data.objects['me']
    b = bpy.data.objects['EMPMentonL']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

def EMPMentonRDef(self, context):
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMPMentonR"
    bpy.context.object.empty_draw_size = 3

    a = bpy.data.objects['me']
    b = bpy.data.objects['EMPMentonR']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


