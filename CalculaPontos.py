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
    capturaINI('EMP21')
    capturaINI('EMP13')
    capturaINI('EMP23')
    capturaINI('EMP16')
    capturaINI('EMP26')
    capturaINI('EMPPalatine')
    capturaINI('EMPApoint')
    capturaINI('EMPNasalSpine')
    capturaINI('EMPPterygoidL')
    capturaINI('EMPPterygoidR')
    capturaINI('EMP31')
    capturaINI('EMP41')
    capturaINI('EMP33')
    capturaINI('EMP43')
    capturaINI('EMP36')
    capturaINI('EMP46')
    capturaINI('EMPBpoint')
    capturaINI('EMPPogonion')
    capturaINI('EMPMenton')
    capturaINI('EMPMentonL')
    capturaINI('EMPMentonR')
    
def capturaFINtodosDef(self, context):
    capturaFIN('EMP11')
    capturaFIN('EMP21')
    capturaFIN('EMP13')
    capturaFIN('EMP23')
    capturaFIN('EMP16')
    capturaFIN('EMP26')
    capturaFIN('EMPPalatine')
    capturaFIN('EMPApoint')
    capturaFIN('EMPNasalSpine')
    capturaFIN('EMPPterygoidL')
    capturaFIN('EMPPterygoidR')
    capturaFIN('EMP31')
    capturaFIN('EMP41')
    capturaFIN('EMP33')
    capturaFIN('EMP43')
    capturaFIN('EMP36')
    capturaFIN('EMP46')
    capturaFIN('EMPBpoint')
    capturaFIN('EMPPogonion')
    capturaFIN('EMPMenton')
    capturaFIN('EMPMentonL')
    capturaFIN('EMPMentonR')

def calculaDeslocamento(obj, obj1, obj2):
    objini = bpy.data.objects[obj1]
    objfin = bpy.data.objects[obj2]
    
    SRED = '\033[91m'
    SGREEN = '\033[92m'
    SBLUE = '\033[94m'

    BHEAD = '\033[95m'

    BEND = '\033[0m'


#    if bpy.data.objects.get(obj) is not None:
    Xdes = SRED + "X: " + str(round(objfin.location[0] - objini.location[0], 2)) + BEND
    Ydes = SGREEN + "Y: " + str(round(objfin.location[1] - objini.location[1], 2)) + BEND
    Zdes = SBLUE + "Z: " + str(round(objfin.location[2] - objini.location[2], 2)) + BEND

    a = '{} {} {} {} '.format(obj, Xdes, Ydes, Zdes)
    print(a)
    

def geraDeslocamentoTODOSDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    SYEL = '\33[45m'
    BOLD = '\033[1m'
    BEND = '\033[0m'

    print(" ")
    print(" ")
    print(BOLD + SYEL + "MAXILLA" + BEND)
    calculaDeslocamento('Teeth 8 (11) : ', 'EMP11.INI', 'EMP11.FIN')
    calculaDeslocamento('Teeth 9 (21) : ', 'EMP21.INI', 'EMP21.FIN')
    calculaDeslocamento('Teeth 6 (13) : ', 'EMP13.INI', 'EMP13.FIN')
    calculaDeslocamento('Teeth 11 (23) :', 'EMP16.INI', 'EMP16.FIN')    
    calculaDeslocamento('Teeth 3 (16) : ', 'EMP26.INI', 'EMP26.FIN')
    calculaDeslocamento('Palatine :     ', 'EMPPalatine.INI', 'EMPPalatine.FIN')
    calculaDeslocamento('A Point :      ', 'EMPApoint.INI', 'EMPApoint.FIN')
    calculaDeslocamento('Nasal Spine :  ', 'EMPNasalSpine.INI', 'EMPNasalSpine.FIN')
    calculaDeslocamento('Pterygoid (L) :', 'EMPPterygoidL.INI', 'EMPPterygoidL.FIN')
    calculaDeslocamento('Pterygoid (R) :', 'EMPPterygoidR.INI', 'EMPPterygoidR.FIN')
    print(" ")
    print(BOLD + SYEL + "MANDIBLE BODY" + BEND)
    calculaDeslocamento('Teeth 24 (31) :', 'EMP31.INI', 'EMP31.FIN')
    calculaDeslocamento('Teeth 25 (41) :', 'EMP41.INI', 'EMP41.FIN')
    calculaDeslocamento('Teeth 22 (33) :', 'EMP33.INI', 'EMP33.FIN')
    calculaDeslocamento('Teeth 27 (43) :', 'EMP43.INI', 'EMP43.FIN')
    calculaDeslocamento('Teeth 19 (36) :', 'EMP36.INI', 'EMP36.FIN')
    calculaDeslocamento('Teeth 30 (46) :', 'EMP46.INI', 'EMP46.FIN')
    calculaDeslocamento('B Point or Up: ', 'EMPBpoint.INI', 'EMPBpoint.FIN')
    print(" ")
    print(BOLD + SYEL + "CHIN" + BEND)
    calculaDeslocamento('Pogonion:      ', 'EMPPogonion.INI', 'EMPPogonion.FIN')
    calculaDeslocamento('Menton:        ', 'EMPMenton.INI', 'EMPMenton.FIN')
    calculaDeslocamento('Menton (L):    ', 'EMPMentonL.INI', 'EMPMentonL.FIN')
    calculaDeslocamento('Menton (R) :   ', 'EMPMentonR.INI', 'EMPMentonR.FIN')
    
    apagaObjeto('EMP11.INI')
    apagaObjeto('EMP11.FIN')
    apagaObjeto('EMP21.INI')
    apagaObjeto('EMP21.FIN')
    apagaObjeto('EMP13.INI')
    apagaObjeto('EMP13.FIN')
    apagaObjeto('EMP23.INI')
    apagaObjeto('EMP23.FIN')
    apagaObjeto('EMP16.INI')
    apagaObjeto('EMP16.FIN')
    apagaObjeto('EMP26.INI')
    apagaObjeto('EMP26.FIN')
    apagaObjeto('EMPPalatine.INI')
    apagaObjeto('EMPPalatine.FIN')
    apagaObjeto('EMPApoint.INI')
    apagaObjeto('EMPApoint.FIN')
    apagaObjeto('EMPNasalSpine.INI')
    apagaObjeto('EMPNasalSpine.FIN')
    apagaObjeto('EMPPterygoidL.INI')
    apagaObjeto('EMPPterygoidR.FIN')
    apagaObjeto('EMP31.INI')
    apagaObjeto('EMP31.FIN')
    apagaObjeto('EMP41.INI')
    apagaObjeto('EMP41.FIN')
    apagaObjeto('EMP33.INI')
    apagaObjeto('EMP33.FIN')
    apagaObjeto('EMP43.INI')
    apagaObjeto('EMP43.FIN')
    apagaObjeto('EMP36.INI')
    apagaObjeto('EMP36.FIN')
    apagaObjeto('EMP46.INI')
    apagaObjeto('EMP46.FIN')
    apagaObjeto('EMPBpoint.INI')
    apagaObjeto('EMPBpoint.FIN')
    apagaObjeto('EMPPogonion.INI')
    apagaObjeto('EMPPogonion.FIN')
    apagaObjeto('EMPMenton.INI')
    apagaObjeto('EMPMenton.FIN')
    apagaObjeto('EMPMentonL.INI')
    apagaObjeto('EMPMentonL.FIN')
    apagaObjeto('EMPMentonR.INI')
    apagaObjeto('EMPMentonR.FIN')


