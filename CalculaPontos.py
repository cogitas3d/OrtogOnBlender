import bpy

def capturaINI(ObjSelecionado):
    bpy.ops.object.select_all(action='DESELECT')
    Objeto = bpy.data.objects[ObjSelecionado]
    Objeto.select_set(True)
    bpy.context.view_layer.objects.active = Objeto
    print("Está no frame: ",bpy.context.scene.frame_current)
    bpy.ops.object.duplicate()
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
    bpy.context.object.name = ObjSelecionado+".INI"
    
def capturaFIN(ObjSelecionado):
    bpy.ops.object.select_all(action='DESELECT')
    Objeto = bpy.data.objects[ObjSelecionado]
    Objeto.select_set(True)
    bpy.context.view_layer.objects.active = Objeto
    print("Está no frame: ",bpy.context.scene.frame_current)
    bpy.ops.object.duplicate()
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
    bpy.context.object.name = ObjSelecionado+".FIN" 
    
def apagaObjeto(ObjSelecionado):   
    bpy.ops.object.select_all(action='DESELECT')
    Objeto = bpy.data.objects[ObjSelecionado]
    Objeto.select_set(True)
    bpy.ops.object.delete(use_global=False)

  
    
def capturaINItodosDef():

    # ATUALIZADO?
    ListaPontos = ['Orbital right', 'Orbital left', 'N point', 'Po right', 'Po left', 'Pt right', 'Pt left', 'Ba point', 'S point', 'U1 Tip', 'U1 Labial Gengival Border', 'U1 Lingual Gengival Border', 'M U6', 'D U6', 'U6 Occlusal', 'PNS point', 'A point', 'ANS point', 'U1 Root', 'L1 Tip', 'L1 Root', 'L1 Labial Gengival Border', 'L1 Lingual Gengival Border', 'B point', 'M L6', 'L6 Occlusal', 'D L6', 'Mid Ramus right', 'Mid Ramus left', 'R right', 'R left', 'Go right', 'Go left', 'Ar right', 'Ar left', 'Sigmoid right', 'Sigmoid left', 'Co right', 'Co left', 'Pg point', 'Gn point', 'Me point', 'ST Glabella', 'ST Nasion', 'Bridge of Nose', 'Tip of Nose', 'Cheekbone right', 'Cheekbone left', 'Columella', 'Subnasale', 'Subpupil right', 'Subpupil left', 'ST A point', 'Upper Lip', 'Stomion Superius', 'Stomion Inferius', 'Lower Lip', 'ST B point', 'ST Pogonion', 'ST Gnathion', 'ST Menton', 'Throat point', 'CB right', 'CB left', 'OR right', 'OR left', 'SP right', 'SP left', 'AB right', 'AB left', 'Tooth 8', 'Tooth 9', 'Tooth 6', 'Tooth 11', 'Tooth 3', 'Tooth 14', 'Tooth 24', 'Tooth 25', 'Tooth 22', 'Tooth 27', 'Tooth 19', 'Tooth 30']

    ObjetosCena = bpy.data.objects

    for ob in ListaPontos:
        if ob in ObjetosCena:
            capturaINI(ob)

def capturaFINtodosDef():

    # ATUALIZADO?
    ListaPontos = ['Orbital right', 'Orbital left', 'N point', 'Po right', 'Po left', 'Pt right', 'Pt left', 'Ba point', 'S point', 'U1 Tip', 'U1 Labial Gengival Border', 'U1 Lingual Gengival Border', 'M U6', 'D U6', 'U6 Occlusal', 'PNS point', 'A point', 'ANS point', 'U1 Root', 'L1 Tip', 'L1 Root', 'L1 Labial Gengival Border', 'L1 Lingual Gengival Border', 'B point', 'M L6', 'L6 Occlusal', 'D L6', 'Mid Ramus right', 'Mid Ramus left', 'R right', 'R left', 'Go right', 'Go left', 'Ar right', 'Ar left', 'Sigmoid right', 'Sigmoid left', 'Co right', 'Co left', 'Pg point', 'Gn point', 'Me point', 'ST Glabella', 'ST Nasion', 'Bridge of Nose', 'Tip of Nose', 'Cheekbone right', 'Cheekbone left', 'Columella', 'Subnasale', 'Subpupil right', 'Subpupil left', 'ST A point', 'Upper Lip', 'Stomion Superius', 'Stomion Inferius', 'Lower Lip', 'ST B point', 'ST Pogonion', 'ST Gnathion', 'ST Menton', 'Throat point', 'CB right', 'CB left', 'OR right', 'OR left', 'SP right', 'SP left', 'AB right', 'AB left', 'Tooth 8', 'Tooth 9', 'Tooth 6', 'Tooth 11', 'Tooth 3', 'Tooth 14', 'Tooth 24', 'Tooth 25', 'Tooth 22', 'Tooth 27', 'Tooth 19', 'Tooth 30']

    ObjetosCena = bpy.data.objects

    for ob in ListaPontos:
        if ob in ObjetosCena:
            capturaFIN(ob)



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
    

def obj_pre(frame):
    bpy.context.scene.frame_set(frame)
    print("frame:", frame)
    capturaINItodosDef()
        
def obj_pos(frame):
    bpy.context.scene.frame_set(frame)
    print("frame:", frame)
    capturaFINtodosDef()

def geraDeslocamentoTODOSDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

# Mostra resultados

    frame1 = bpy.data.scenes["Scene"].frame_start

    obj_pre(frame1)


    frame2 = bpy.data.scenes["Scene"].frame_end

    obj_pos(frame2)

    SYEL = '\33[45m'
    BOLD = '\033[1m'
    BEND = '\033[0m'

    print(" ")
    print(" ")
    print(BOLD + SYEL + "MAXILLA" + BEND)

    # ATUALIZADO?
    ListaPontos = ['Orbital right', 'Orbital left', 'N point', 'Po right', 'Po left', 'Pt right', 'Pt left', 'Ba point', 'S point', 'U1 Tip', 'U1 Labial Gengival Border', 'U1 Lingual Gengival Border', 'M U6', 'D U6', 'U6 Occlusal', 'PNS point', 'A point', 'ANS point', 'U1 Root', 'L1 Tip', 'L1 Root', 'L1 Labial Gengival Border', 'L1 Lingual Gengival Border', 'B point', 'M L6', 'L6 Occlusal', 'D L6', 'Mid Ramus right', 'Mid Ramus left', 'R right', 'R left', 'Go right', 'Go left', 'Ar right', 'Ar left', 'Sigmoid right', 'Sigmoid left', 'Co right', 'Co left', 'Pg point', 'Gn point', 'Me point', 'ST Glabella', 'ST Nasion', 'Bridge of Nose', 'Tip of Nose', 'Cheekbone right', 'Cheekbone left', 'Columella', 'Subnasale', 'Subpupil right', 'Subpupil left', 'ST A point', 'Upper Lip', 'Stomion Superius', 'Stomion Inferius', 'Lower Lip', 'ST B point', 'ST Pogonion', 'ST Gnathion', 'ST Menton', 'Throat point', 'CB right', 'CB left', 'OR right', 'OR left', 'SP right', 'SP left', 'AB right', 'AB left', 'Tooth 8', 'Tooth 9', 'Tooth 6', 'Tooth 11', 'Tooth 3', 'Tooth 14', 'Tooth 24', 'Tooth 25', 'Tooth 22', 'Tooth 27', 'Tooth 19', 'Tooth 30']

    ObjetosCena = bpy.data.objects

    Collection_Head = bpy.data.collections['Anatomical Points - Head'].all_objects
    Collection_Maxilla = bpy.data.collections['Anatomical Points - Maxilla'].all_objects
    Collection_Teeth = bpy.data.collections['Anatomical Points - Teeth'].all_objects
    Collection_Mandible = bpy.data.collections['Anatomical Points - Mandible'].all_objects
    Collection_SoftTissue = bpy.data.collections['Anatomical Points - Soft Tissue'].all_objects

    '''
    for ob in ListaPontos:
        if ob in ObjetosCena:
            calculaDeslocamento( ob+' : ', ob+'.INI', ob+'.FIN')
    '''


    print(BOLD + SYEL + "HEAD" + BEND)

    for ob in ListaPontos:
        if ob in Collection_Head:
            calculaDeslocamento( ob+' : ', ob+'.INI', ob+'.FIN')

    print(" ")
    print(BOLD + SYEL + "MAXILLA" + BEND)

    for ob in ListaPontos:
        if ob in Collection_Maxilla:
            calculaDeslocamento( ob+' : ', ob+'.INI', ob+'.FIN')

    print(" ")
    print(BOLD + SYEL + "TEETH" + BEND)

    for ob in ListaPontos:
        if ob in Collection_Teeth:
            calculaDeslocamento( ob+' : ', ob+'.INI', ob+'.FIN')

    print(" ")
    print(BOLD + SYEL + "MANDIBLE" + BEND)

    for ob in ListaPontos:
        if ob in Collection_Mandible:
            calculaDeslocamento( ob+' : ', ob+'.INI', ob+'.FIN')

    print(" ")
    print(BOLD + SYEL + "SOFT TISSUE" + BEND)

    for ob in ListaPontos:
        if ob in Collection_SoftTissue:
            calculaDeslocamento( ob+' : ', ob+'.INI', ob+'.FIN')

    # Apaga
    for ob in ListaPontos:
        if ob in ObjetosCena:
            apagaObjeto(ob+'.INI')
            apagaObjeto(ob+'.FIN')
    

# Calcula Pontos
'''
class capturaINItodos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.captura_ini_todos"
    bl_label = "Captura todos objetos inicio"

    def execute(self, context):
        capturaINItodosDef(self, context)
        return {'FINISHED'}


class capturaFINtodos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.captura_fin_todos"
    bl_label = "Captura todos objetos final"

    def execute(self, context):
        capturaFINtodosDef(self, context)
        return {'FINISHED'}
'''
class geraDeslocamentoTODOS(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_deslocamento_todos"
    bl_label = "Gera deslocamento de todos"

    def execute(self, context):
        geraDeslocamentoTODOSDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(geraDeslocamentoTODOS)
