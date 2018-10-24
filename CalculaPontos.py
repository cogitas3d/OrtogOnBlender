import bpy

def capturaINI(ObjSelecionado):
    bpy.ops.object.select_all(action='DESELECT')
    Objeto = bpy.data.objects[ObjSelecionado]
    Objeto.select = True
    bpy.context.scene.objects.active = Objeto
    print("Está no frame: ",bpy.context.scene.frame_current)
    bpy.ops.object.duplicate()
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
    bpy.context.object.name = ObjSelecionado+".INI"
    
def capturaFIN(ObjSelecionado):
    bpy.ops.object.select_all(action='DESELECT')
    Objeto = bpy.data.objects[ObjSelecionado]
    Objeto.select = True
    bpy.context.scene.objects.active = Objeto
    print("Está no frame: ",bpy.context.scene.frame_current)
    bpy.ops.object.duplicate()
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
    bpy.context.object.name = ObjSelecionado+".FIN" 
    
def apagaObjeto(ObjSelecionado):   
    bpy.ops.object.select_all(action='DESELECT')
    Objeto = bpy.data.objects[ObjSelecionado]
    Objeto.select = True
    bpy.ops.object.delete(use_global=False)
    
    
def capturaINItodosDef(self, context):
    capturaINI('EMP11')
    
def capturaFINtodosDef(self, context):
    capturaFIN('EMP11')

def geraDeslocamentoTODOSDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    EMP11ini = bpy.data.objects['EMP11.INI']
    EMP11fin = bpy.data.objects['EMP11.FIN']
    
    print("Deslocamento em Y: ", EMP11fin.location[1] - EMP11ini.location[1])
    
    
    apagaObjeto('EMP11.INI')
    apagaObjeto('EMP11.FIN')