import fnmatch

from .PontosAnatomicos import *

# Pontos

class Cut_Point_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cut_point_pt"
    bl_label = "Condyle Rotation Point"
    bl_options = {'REGISTER', 'UNDO'}

    '''
    @classmethod
    def poll(cls, context):

        found = 'Condyle Rotation Point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False
    '''

    def execute(self, context):
        CriaPontoDef('CutPoint', 'Cut Points')
        #TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Cut_Point_pt)

# Gera medidas

def CriaCotaCut(Objeto1, Objeto2):

    context = bpy.context
    scn = context.scene

    bpy.ops.measureit.runopengl()

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[Objeto1].select_set(True)
    bpy.data.objects[Objeto2].select_set(True)
    context.view_layer.objects.active = bpy.data.objects[Objeto1]
    bpy.ops.measureit.addlink()
    bpy.ops.object.select_all(action='DESELECT')


def AtribuiCotasCut():

    ListaCutPoints = []

    for i in bpy.data.objects:
        if fnmatch.fnmatchcase(i.name, "CutPoint.0*"):
            ListaCutPoints.append(i.name)

    ListaCutPoints.append("CutPoint")

    #print("Lista:", ListaCutPoints)

    TamanhoLista = len(ListaCutPoints)
    print(TamanhoLista)

    ItemLista = 0
    #ListaPares = []

    for i in range(TamanhoLista):
        try:
            print("valor",i)
            print(ListaCutPoints[ItemLista], ListaCutPoints[ItemLista+1])
            CriaCotaCut(ListaCutPoints[ItemLista], ListaCutPoints[ItemLista+1])
            #ListaPares.append([ListaCutPoints[ItemLista], ListaCutPoints[ItemLista+1]])
            ItemLista += 1
        except:
            print("Finalizado!")
            #print("ListaPares:", ListaPares)


class CriaCotasBotao(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_cotas_botao"
    bl_label = "Create Measure on Cut Poins"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        AtribuiCotasCut()
        return {'FINISHED'}

bpy.utils.register_class(CriaCotasBotao)

# Cria bones

def CriaBonesDef():

    ListaCutPoints = []

    for i in bpy.data.objects:
        if fnmatch.fnmatchcase(i.name, "CutPoint.0*"):
            ListaCutPoints.append(i.name)

    ListaCutPoints.append("CutPoint")


    TamanhoLista = len(ListaCutPoints)
    print(TamanhoLista)

    ItemLista = 0

    bpy.context.scene.cursor.location = 0,0,0
    bpy.ops.object.armature_add(radius=1, view_align=False, enter_editmode=True)

    for i in range(TamanhoLista):
        try:
            print("AQUIIIII")
            print("ITEM LISTA LOCARION:", bpy.data.objects[ListaCutPoints[ItemLista]].location)
            print("ITEM LISTA LOCARION:", bpy.data.objects[ListaCutPoints[ItemLista+1]].location)

            bpy.context.scene.cursor.location = bpy.data.objects[ListaCutPoints[ItemLista]].location
            bpy.ops.armature.bone_primitive_add()
            bpy.context.object.data.edit_bones["Bone"].name = ListaCutPoints[ItemLista]
            print("INTEMLISTA: ", ListaCutPoints[ItemLista])
            bpy.context.object.data.edit_bones[ListaCutPoints[ItemLista]].head = bpy.data.objects[ListaCutPoints[ItemLista+1]].location
            print(bpy.data.objects[ListaCutPoints[ItemLista+1]].location)
            bpy.context.object.data.edit_bones[ListaCutPoints[ItemLista]].tail = bpy.data.objects[ListaCutPoints[ItemLista]].location
            print(bpy.data.objects[ListaCutPoints[ItemLista]].location)

            ItemLista += 1
        except:
            print("Finalizado!")
            #print("ListaPares:", ListaPares)

    bpy.ops.object.mode_set(mode='OBJECT') # Volta ao modo de objeto


class CriaBones(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_bones_fibula"
    bl_label = "Create Fibula Bones"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        CriaBonesDef()
        return {'FINISHED'}

bpy.utils.register_class(CriaBones)
