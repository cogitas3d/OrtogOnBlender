import bpy
import math
from .FerrMedidas import *

def CursorToSelectedObj(objeto):

    context = bpy.context
    scn = context.scene

    bpy.ops.object.select_all(action='DESELECT')

    bpy.data.objects[objeto].select_set(True)
    context.view_layer.objects.active = bpy.data.objects[objeto]

    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            ctx = bpy.context.copy()
            ctx['area'] = area
            ctx['region'] = area.regions[-1]
    #        bpy.ops.view3d.view_selected(ctx)
            bpy.ops.view3d.snap_cursor_to_selected(ctx)
            break

def CursorToSelectedObjs(objeto1, objeto2):

    context = bpy.context
    scn = context.scene

    bpy.ops.object.select_all(action='DESELECT')

    bpy.data.objects[objeto1].select_set(True)
    bpy.data.objects[objeto2].select_set(True)
    context.view_layer.objects.active = bpy.data.objects[objeto1]

    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            ctx = bpy.context.copy()
            ctx['area'] = area
            ctx['region'] = area.regions[-1]
    #        bpy.ops.view3d.view_selected(ctx)
            bpy.ops.view3d.snap_cursor_to_selected(ctx)
            break

def ApagarObjeto(objeto):
    context = bpy.context
    scn = context.scene

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[objeto].select_set(True)
    context.view_layer.objects.active = bpy.data.objects[objeto]
    bpy.ops.object.delete(use_global=False)



class CalculaTudoUSP(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.calcula_tudo_usp"
    bl_label = "USP Calc All"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.calcula_plano_oclusal_classico()
        CalculaSNADef()
        CalculaSNBDef()
        CalculaANBDef()
        CalculaPlanoMandibularDef()
        CalculaSNGoGnDef()
        CalculaSNGnDef()
        return {'FINISHED'}

bpy.utils.register_class(CalculaTudoUSP)

def CalculaSNGnDef():

    FoundA = 'S point' in bpy.data.objects
    FoundN = 'N point' in bpy.data.objects
    FoundB = 'Gn point' in bpy.data.objects

    context = bpy.context
    objInicial = context.object

    CursorInicial = []

    for i in bpy.context.scene.cursor.location:
        CursorInicial.append(i)

    if FoundA == True and FoundN == True and FoundB == True:
        print("SNGn - Todos os pontos anatômicos presentes!")

        CursorToSelectedObj("S point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoS"
        bpy.context.object.location[0] = 0


        CursorToSelectedObj("N point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoN"
        bpy.context.object.location[0] = 0


        CursorToSelectedObj("Gn point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoGn"
        bpy.context.object.location[0] = 0

        bpy.data.objects["PontoS"].location[0] = 0
        bpy.data.objects["PontoN"].location[0] = 0
        bpy.data.objects["PontoGn"].location[0] = 0

        AnguloSNGn = CalculaAngulo("PontoN", "PontoS", "PontoGn")
        print("Ângulo SNGn:", AnguloSNGn)

        bpy.types.Scene.angulo_sngn = bpy.props.StringProperty \
            (
                name = "SNGn Angle",
                description = "SNGn Angle",
                default = str(AnguloSNGn)
            )

        ApagarObjeto("PontoS")
        ApagarObjeto("PontoN")
        ApagarObjeto("PontoGn")

        context.scene.cursor.location = CursorInicial

        if objInicial != None:
            bpy.ops.object.select_all(action='DESELECT')
            objInicial.select_set(True)
            context.view_layer.objects.active = objInicial

        return str(AnguloSNGn)

    else:
        bpy.types.Scene.angulo_sngn = bpy.props.StringProperty \
            (
                name = "SNGn Angle",
                description = "SNGn Angle",
                default = "NONE"
            )
        print("Falta algum ponto anatômico (SNGn)!")

def CalculaSNGoGnDef():

    FoundS = 'S point' in bpy.data.objects
    FoundN = 'N point' in bpy.data.objects
    FoundGoright = 'Go right' in bpy.data.objects
    FoundGoleft = 'Go left' in bpy.data.objects
    FoundGnpoint = 'Gn point' in bpy.data.objects

    context = bpy.context
    objInicial = context.object

    CursorInicial = []

    for i in bpy.context.scene.cursor.location:
        CursorInicial.append(i)


    if FoundS == True and FoundN == True and FoundGoright == True and FoundGoleft == True and FoundGnpoint == True:
        print("Todos os pontos anatômicos presentes!")

        CursorToSelectedObj("S point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoS"
        bpy.context.object.location[0] = 0

        CursorToSelectedObj("N point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoN"
        bpy.context.object.location[0] = 0

        CursorToSelectedObjs("Go left", "Go left")
        Cursor_Gonios = bpy.context.scene.cursor.location
        print(Cursor_Gonios)

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "Gonios"
        bpy.context.object.location[0] = 0

        CursorToSelectedObj("Gn point")
        Cursor_Gn = bpy.context.scene.cursor.location


        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoGn"
        bpy.context.object.location[0] = 0


        def line_intersection(line1, line2):
            xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
            ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

            def det(a, b):
                return a[0] * b[1] - a[1] * b[0]

            div = det(xdiff, ydiff)
            if div == 0:
               raise Exception('As linhas tê intersecção!')

            d = (det(*line1), det(*line2))
            x = det(d, xdiff) / div
            y = det(d, ydiff) / div
            return x, y

        PontoS = bpy.data.objects['PontoS']
        PontoN = bpy.data.objects['PontoN']
        Gonios = bpy.data.objects['Gonios']
        PontoGn = bpy.data.objects['PontoGn']

        Linha1 = [(PontoS.location[1], PontoS.location[2]), (PontoN.location[1], PontoN.location[2])]
        Linha2 = [(Gonios.location[1], Gonios.location[2]), (PontoGn.location[1],PontoGn.location[2])]

        EncontroYZ = line_intersection(Linha1, Linha2)

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "ProjSNGoGn"
        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = EncontroYZ[0]
        bpy.context.object.location[2] = EncontroYZ[1]


        AnguloSNGoGn = CalculaAngulo("PontoN", "ProjSNGoGn", "PontoGn")

        bpy.types.Scene.angulo_sngogn = bpy.props.StringProperty \
            (
                name = "SNGoGn Angle",
                description = "SNGoGn Angle",
                default = str(AnguloSNGoGn)
            )

        ApagarObjeto("PontoS")
        ApagarObjeto("PontoN")
        ApagarObjeto("Gonios")
        ApagarObjeto("PontoGn")
        ApagarObjeto("ProjSNGoGn")

        context.scene.cursor.location = CursorInicial

        if objInicial != None:
            bpy.ops.object.select_all(action='DESELECT')
            objInicial.select_set(True)
            context.view_layer.objects.active = objInicial

        return str(AnguloSNGoGn)

    else:
        bpy.types.Scene.angulo_sngogn = bpy.props.StringProperty \
            (
                name = "SNGoGn Angle",
                description = "SNGoGn Angle",
                default = "NONE"
            )
        print("Falta algum ponto anatômico (SNGoGn)!")

def CalculaPlanoMaxilaClassicoDef():

    FoundT3 = 'Tooth 3' in bpy.data.objects
    FoundT14 = 'Tooth 14' in bpy.data.objects
    FoundT8 = 'Tooth 8' in bpy.data.objects
    FoundT9 = 'Tooth 9' in bpy.data.objects

    context = bpy.context
    objInicial = context.object

    CursorInicial = []

    for i in bpy.context.scene.cursor.location:
        CursorInicial.append(i)


    if FoundT3 == True and FoundT14 == True and FoundT8 == True and FoundT9 == True:
        print("Todos os pontos anatômicos presentes!")

        CursorToSelectedObjs("Tooth 14", "Tooth 3")
        Cursor_1626 = bpy.context.scene.cursor.location
        print(Cursor_1626)

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "1626"

        CursorToSelectedObjs("Tooth 9", "Tooth 8")
        Cursor_1121 = bpy.context.scene.cursor.location
        print(Cursor_1121)

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "1121"

        #PosicaoX = bpy.data.objects["1121"].location[0]
        #PosicaoY = bpy.data.objects["1626"].location[1]
        #PosicaoZ = bpy.data.objects["1121"].location[2]

        PosicaoX = bpy.data.objects["1121"].location[0]
        PosicaoY = bpy.data.objects["1121"].location[1]
        PosicaoZ = bpy.data.objects["1626"].location[2]

        print(PosicaoX)
        print(PosicaoY)
        print(PosicaoZ)

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(PosicaoX, PosicaoY, PosicaoZ))
        bpy.context.object.name = "Inter_1626_1121"

        bpy.data.objects["1121"].location[0] = 0
        bpy.data.objects["1626"].location[0] = 0
        bpy.data.objects["Inter_1626_1121"].location[0] = 0

        AnguloOcluMaxClass = CalculaAngulo("1121", "1626", "Inter_1626_1121")

        bpy.types.Scene.plano_oclusal_maxila_classico = bpy.props.StringProperty \
            (
                name = "Maxillary Occlusal Angle",
                description = "Classic Max. Occl. Plane",
                default = str(AnguloOcluMaxClass)
            )

        ApagarObjeto("1121")
        ApagarObjeto("1626")
        ApagarObjeto("Inter_1626_1121")

        context.scene.cursor.location = CursorInicial

        if objInicial != None:
            bpy.ops.object.select_all(action='DESELECT')
            objInicial.select_set(True)
            context.view_layer.objects.active = objInicial

        return str(AnguloOcluMaxClass)

    else:
        print("Falta algum ponto anatômico dos dentes!")


def CalculaPlanoMandibularDef():

    FoundGoleft = 'Go left' in bpy.data.objects
    FoundGoright = 'Go right' in bpy.data.objects
    FoundMepoint = 'Me point' in bpy.data.objects

    context = bpy.context
    objInicial = context.object

    CursorInicial = []

    for i in bpy.context.scene.cursor.location:
        CursorInicial.append(i)


    if FoundGoleft == True and FoundGoright == True and FoundMepoint == True:
        print("Todos os pontos anatômicos presentes!")

        CursorToSelectedObjs("Go left", "Go left")
        Cursor_Gonios = bpy.context.scene.cursor.location
        print(Cursor_Gonios)

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "Gonios"

        CursorToSelectedObj("Me point")
        Cursor_Mepoint = bpy.context.scene.cursor.location
        print(Cursor_Mepoint)

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "Mepoint"


        PosicaoX = bpy.data.objects["Gonios"].location[0]
        PosicaoY = bpy.data.objects["Mepoint"].location[1]
        PosicaoZ = bpy.data.objects["Gonios"].location[2]

        print(PosicaoX)
        print(PosicaoY)
        print(PosicaoZ)

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(PosicaoX, PosicaoY, PosicaoZ))
        bpy.context.object.name = "Inter_Gonios_Me"

        bpy.data.objects["Gonios"].location[0] = 0
        bpy.data.objects["Mepoint"].location[0] = 0
        bpy.data.objects["Inter_Gonios_Me"].location[0] = 0

        AnguloOcluMandUsp = CalculaAngulo("Inter_Gonios_Me", "Gonios", "Mepoint")

        bpy.types.Scene.plano_mandibula_usp = bpy.props.StringProperty \
            (
                name = "Mandibular Plane",
                description = "Mandibular Plane",
                default = str(AnguloOcluMandUsp)
            )

        ApagarObjeto("Gonios")
        ApagarObjeto("Mepoint")
        ApagarObjeto("Inter_Gonios_Me")

        context.scene.cursor.location = CursorInicial

        if objInicial != None:
            bpy.ops.object.select_all(action='DESELECT')
            objInicial.select_set(True)
            context.view_layer.objects.active = objInicial

        return str(AnguloOcluMandUsp)

    else:
        print("Falta algum ponto anatômico na mandíbula!")

def CalculaANBDef():

    FoundA = 'A point' in bpy.data.objects
    FoundN = 'N point' in bpy.data.objects
    FoundB = 'B point' in bpy.data.objects

    context = bpy.context
    objInicial = context.object

    CursorInicial = []

    for i in bpy.context.scene.cursor.location:
        CursorInicial.append(i)

    if FoundA == True and FoundN == True and FoundB == True:
        print("SNA - Todos os pontos anatômicos presentes!")

        CursorToSelectedObj("A point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoA"
        bpy.context.object.location[0] = 0


        CursorToSelectedObj("N point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoN"
        bpy.context.object.location[0] = 0


        CursorToSelectedObj("B point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoB"
        bpy.context.object.location[0] = 0

        bpy.data.objects["PontoA"].location[0] = 0
        bpy.data.objects["PontoN"].location[0] = 0
        bpy.data.objects["PontoB"].location[0] = 0

        AnguloANB = CalculaAngulo("PontoA", "PontoN", "PontoB")
        print("Ângulo ANB:", AnguloANB)

        bpy.types.Scene.angulo_anb = bpy.props.StringProperty \
            (
                name = "ANB Angle",
                description = "ANB Angle",
                default = str(AnguloANB)
            )

        ApagarObjeto("PontoA")
        ApagarObjeto("PontoN")
        ApagarObjeto("PontoB")

        context.scene.cursor.location = CursorInicial

        if objInicial != None:
            bpy.ops.object.select_all(action='DESELECT')
            objInicial.select_set(True)
            context.view_layer.objects.active = objInicial

        return str(AnguloANB)

    else:
        bpy.types.Scene.angulo_anb = bpy.props.StringProperty \
            (
                name = "ANB Angle",
                description = "ANB Angle",
                default = "NONE"
            )
        print("Falta algum ponto anatômico (ANB)!")

def CalculaSNADef():

    FoundS = 'S point' in bpy.data.objects
    FoundN = 'N point' in bpy.data.objects
    FoundA = 'A point' in bpy.data.objects

    context = bpy.context
    objInicial = context.object

    CursorInicial = []

    for i in bpy.context.scene.cursor.location:
        CursorInicial.append(i)


    if FoundS == True and FoundN == True and FoundA == True:
        print("SNA - Todos os pontos anatômicos presentes!")

        CursorToSelectedObj("S point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoS"
        bpy.context.object.location[0] = 0


        CursorToSelectedObj("N point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoN"
        bpy.context.object.location[0] = 0


        CursorToSelectedObj("A point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoA"
        bpy.context.object.location[0] = 0

        bpy.data.objects["PontoS"].location[0] = 0
        bpy.data.objects["PontoN"].location[0] = 0
        bpy.data.objects["PontoA"].location[0] = 0

        AnguloSNA = CalculaAngulo("PontoS", "PontoN", "PontoA")
        print("Ângulo SNA:", AnguloSNA)

        bpy.types.Scene.angulo_sna = bpy.props.StringProperty \
            (
                name = "SNA Angle",
                description = "SNA Angle",
                default = str(AnguloSNA)
            )

        ApagarObjeto("PontoS")
        ApagarObjeto("PontoN")
        ApagarObjeto("PontoA")

        context.scene.cursor.location = CursorInicial

        if objInicial != None:
            bpy.ops.object.select_all(action='DESELECT')
            objInicial.select_set(True)
            context.view_layer.objects.active = objInicial


        return str(AnguloSNA)

    else:
        bpy.types.Scene.angulo_sna = bpy.props.StringProperty \
            (
                name = "SNA Angle",
                description = "SNA Angle",
                default = "NONE"
            )
        print("Falta algum ponto anatômico (SNA)!")


def CalculaSNBDef():

    FoundS = 'S point' in bpy.data.objects
    FoundN = 'N point' in bpy.data.objects
    FoundB = 'B point' in bpy.data.objects

    context = bpy.context
    objInicial = context.object

    CursorInicial = []

    for i in bpy.context.scene.cursor.location:
        CursorInicial.append(i)


    if FoundS == True and FoundN == True and FoundB == True:
        print("SNB - Todos os pontos anatômicos presentes!")

        CursorToSelectedObj("S point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoS"
        bpy.context.object.location[0] = 0


        CursorToSelectedObj("N point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoN"
        bpy.context.object.location[0] = 0


        CursorToSelectedObj("B point")
        Cursor_S = bpy.context.scene.cursor.location

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
        bpy.context.object.name = "PontoB"
        bpy.context.object.location[0] = 0

        bpy.data.objects["PontoS"].location[0] = 0
        bpy.data.objects["PontoN"].location[0] = 0
        bpy.data.objects["PontoB"].location[0] = 0

        AnguloSNB = CalculaAngulo("PontoS", "PontoN", "PontoB")
        print("Ângulo SNB:", AnguloSNB)

        bpy.types.Scene.angulo_snb = bpy.props.StringProperty \
            (
                name = "SNB Angle",
                description = "SNB Angle",
                default = str(AnguloSNB)
            )

        ApagarObjeto("PontoS")
        ApagarObjeto("PontoN")
        ApagarObjeto("PontoB")

        context.scene.cursor.location = CursorInicial

        if objInicial != None:
            bpy.ops.object.select_all(action='DESELECT')
            objInicial.select_set(True)
            context.view_layer.objects.active = objInicial

        return str(AnguloSNB)

    else:
        bpy.types.Scene.angulo_snb = bpy.props.StringProperty \
            (
                name = "SNB Angle",
                description = "SNB Angle",
                default = "NONE"
            )
        print("Falta algum ponto anatômico (SNB)!")


class CalculaPlanoMaxilaClassico(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.calcula_plano_oclusal_classico"
    bl_label = "Calc. Max. Occl. Plane Classic"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        CalculaPlanoMaxilaClassicoDef()
        return {'FINISHED'}

bpy.utils.register_class(CalculaPlanoMaxilaClassico)


def CalculaAnguloOclusao():
    found_U6_Oc = 'U6 Occlusal' in bpy.data.objects
    found_U1_Tp = 'U1 Tip' in bpy.data.objects

    context = bpy.context
    objInicial = context.object

    CursorInicial = []

    for i in bpy.context.scene.cursor.location:
        CursorInicial.append(i)


    if found_U6_Oc == True and found_U1_Tp == True:
        print("U6 Occlusal e U1 Tip presentes!")

        PT_U6_Oc = bpy.data.objects['U6 Occlusal']

        PT_U1_Tp = bpy.data.objects['U1 Tip']

        Distancia1 = math.sqrt( (PT_U6_Oc.location[1] - PT_U1_Tp.location[1])**2 + (PT_U6_Oc.location[2] - PT_U1_Tp.location[2])**2 )

        print("Distancia1:", Distancia1)

        Distancia2= ( math.sqrt( (PT_U1_Tp.location[1] - PT_U6_Oc.location[1])**2 + ((PT_U1_Tp.location[2]-Distancia1) - PT_U6_Oc.location[2])**2 ) )/2

        print("Distancia2:", Distancia2)

        CosLinOc = (Distancia2 / Distancia1)

        Grau1 = float(round(math.degrees(math.acos(CosLinOc)),2))

        GrauOclusao = 180 - (Grau1*2)

        print(GrauOclusao)

        bpy.types.Scene.plano_oclusal_maxila = bpy.props.StringProperty \
        (
            name = "Maxillary Occlusal Plane",
            description = "Maxillary Occlusal Plane",
            default = str(GrauOclusao)+"º"
        )

        context.scene.cursor.location = CursorInicial

        if objInicial != None:
            bpy.ops.object.select_all(action='DESELECT')
            objInicial.select_set(True)
            context.view_layer.objects.active = objInicial

        return str(GrauOclusao)+"º"

    else:
        print("Veja se os pontos U6 Occlusal e U1 Tip foram adicionados corretamente.")




def CalculaAnguloNasolabial():
    found_Columella = 'Columella' in bpy.data.objects
    found_Subnasale = 'Subnasale' in bpy.data.objects
    found_UpperLip = 'Upper Lip' in bpy.data.objects


    if found_Columella == True and found_Subnasale == True and found_UpperLip == True:
        print("Columella, Subnasale e Upper Lip presentes!")

        # Copia os 3

        Objetos = [bpy.data.objects['Columella'], bpy.data.objects['Subnasale'], bpy.data.objects['Upper Lip']]

        for item in Objetos:

            bpy.ops.object.select_all(action='DESELECT')
            item.select_set(True)
            bpy.context.view_layer.objects.active = item
            bpy.ops.object.duplicate_move()
            bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')




        # Calcula

        Columella = bpy.data.objects['Columella.001']
        Subnasale = bpy.data.objects['Subnasale.001']
        UpperLip = bpy.data.objects['Upper Lip.001']

        SC = math.sqrt( (Columella.location[1] - Subnasale.location[1])**2 + (Columella.location[2] - Subnasale.location[2])**2 )
        print("SC", SC)

        SU = math.sqrt( (UpperLip.location[1] - Subnasale.location[1])**2 + (UpperLip.location[2] - Subnasale.location[2])**2 )
        print("SU", SU)

        UC = math.sqrt( (UpperLip.location[1] - Columella.location[1])**2 + (UpperLip.location[2] - Columella.location[2])**2 )
        print("UC", UC)

        GrauNasolabial = (SC**2 + SU**2 - UC**2) / (2 * SC * SU)

        AnguloNasolabial = float(round(math.degrees(math.acos(GrauNasolabial)),2))

        print("Ângulo Nasolabial:", AnguloNasolabial)

        bpy.types.Scene.angulo_nasolabial = bpy.props.StringProperty \
        (
            name = "Nasolabial Angle",
            description = "Nasolabial Angle",
            default = str(AnguloNasolabial)+"º"
        )

        # Apaga objetos

        bpy.ops.object.select_all(action='DESELECT')

        ObjetosCopias = [bpy.data.objects['Columella.001'], bpy.data.objects['Subnasale.001'], bpy.data.objects['Upper Lip.001']]

        for item in ObjetosCopias:

            bpy.ops.object.select_all(action='DESELECT')
            item.select_set(True)
            bpy.ops.object.delete(use_global=False)


        return str(AnguloNasolabial)+"º"

def CalculaAnguloGbSnPog():
    found_ST_Glabella = 'ST Glabella' in bpy.data.objects
    found_Subnasale = 'Subnasale' in bpy.data.objects
    found_ST_Pogonion = 'ST Pogonion' in bpy.data.objects


    if found_ST_Glabella == True and found_Subnasale == True and found_ST_Pogonion == True:
        print("ST Glabella, Subnasale e ST Pogonion presentes!")

        AnguloBase = GeraAnguloViewX('Subnasale', 'ST Glabella', 'ST Pogonion')

        Gn = bpy.data.objects['ST Glabella']
        Pog = bpy.data.objects['ST Pogonion']
        Sn = bpy.data.objects['Subnasale']

        # Acha posição do Y no meio entre Gn e Pog'
        PosicaoMeioY = (Gn.location[1] + Pog.location[1])/2
        print("PosicaoMeioY", PosicaoMeioY)

        if PosicaoMeioY > Sn.location[1]:
            print("Maior! Valor:", AnguloBase)

            bpy.types.Scene.angulo_GbSnPog = bpy.props.StringProperty \
            (
                name = "Gb', Sn, Pog' Angle",
                description = "Gb', Sn, Pog' Angle",
                default = str(AnguloBase)+"º"
            )

        if PosicaoMeioY < Sn.location[1]:
            print("Menor", 360 - AnguloBase)

            bpy.types.Scene.angulo_GbSnPog = bpy.props.StringProperty \
            (
                name = "Gb', Sn, Pog' Angle",
                description = "Gb', Sn, Pog' Angle",
                default = str(360 - AnguloBase)+"º"
            )

        if PosicaoMeioY == Sn.location[1]:
            print("Igual", 180)

            bpy.types.Scene.angulo_GbSnPog = bpy.props.StringProperty \
            (
                name = "Gb', Sn, Pog' Angle",
                description = "Gb', Sn, Pog' Angle",
                default = '180º'
            )

def GeraAnguloViewX(Obj1, Obj2, Obj3):

    A = bpy.data.objects[Obj1]
    B = bpy.data.objects[Obj2]
    C = bpy.data.objects[Obj3]

    AB = math.sqrt( (B.location[1] - A.location[1])**2 + (B.location[2] - A.location[2])**2 )
    print("AB", AB)

    AC = math.sqrt( (C.location[1] - A.location[1])**2 + (C.location[2] - A.location[2])**2 )
    print("AC", AC)

    BC = math.sqrt( (C.location[1] - B.location[1])**2 + (C.location[2] - B.location[2])**2 )
    print("BC", BC)

    AnguloCos = (AB**2 + AC**2 - BC**2) / (2 * AB * AC)

    AnguloGraus = float(round(math.degrees(math.acos(AnguloCos)),2))
    print("Ângulo em graus:", AnguloGraus)

    return AnguloGraus

#GeraAnguloViewX("U1 Tip", "U1 Root", "U6 Occlusal")

#GeraAnguloViewX("L1 Tip", "L1 Root", "L6 Occlusal")

#GeraAnguloViewX("Subnasale", "ST Glabella", "ST Pogonion")

# G' SN POG'

def DistanciaDupla(ObjDir, ObjEsq, ObjBase, Eixo):

    found_ObjDir = str(ObjDir) in bpy.data.objects
    found_ObjEsq = str(ObjEsq) in bpy.data.objects
    found_ObjBase = str(ObjBase) in bpy.data.objects

    if found_ObjDir == True and found_ObjEsq == True and found_ObjBase == True:



        def ApagaTudo():

            bpy.ops.object.select_all(action='DESELECT')
            ObjetosCopias = [Direita , Esquerda, Base]

            for item in ObjetosCopias:
                bpy.ops.object.select_all(action='DESELECT')
                item.select_set(True)
                bpy.context.view_layer.objects.active = item
                bpy.ops.object.delete(use_global=False)


        # Copia os 3

        Objetos = [bpy.data.objects[ObjDir], bpy.data.objects[ObjEsq], bpy.data.objects[ObjBase]]


        for item in Objetos:

            bpy.ops.object.select_all(action='DESELECT')
            item.select_set(True)
            bpy.ops.object.duplicate_move()
            bpy.context.view_layer.objects.active = item # Se não tiver dá erro!
            bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')


        Direita = bpy.data.objects[ObjDir+'.001']
        Esquerda = bpy.data.objects[ObjEsq+'.001']
        Base = bpy.data.objects[ObjBase+'.001']



        PontoCentral = ( Direita.location[Eixo] + Esquerda.location[Eixo] ) / 2

        Distancia = abs( PontoCentral - Base.location[Eixo] )


        # Calcula Posicao
        if PontoCentral > Base.location[Eixo]:
            DistanciaFinal = Distancia * -1
            print("DistanciaFinal", DistanciaFinal)
            print("")
            ApagaTudo()

            return DistanciaFinal

        if PontoCentral < Base.location[Eixo]:
            DistanciaFinal = Distancia
            print("DistanciaFinal", DistanciaFinal)
            print("")
            ApagaTudo()

            return DistanciaFinal

        if PontoCentral == Base.location[Eixo]:
            DistanciaFinal = Distancia
            print("DistanciaFinal", DistanciaFinal)
            print("")
            ApagaTudo()

            return DistanciaFinal


    else:
        print( "Não calculou. Algum objeto faltante:", ObjDir,",", ObjEsq, ",", ObjBase)


def DistanciaUnica(ObjDist, ObjBase, Eixo):

    found_ObjDist = str(ObjDist) in bpy.data.objects
    found_ObjBase = str(ObjBase) in bpy.data.objects

    if found_ObjDist == True and found_ObjBase == True:


        def ApagaTudo():

            bpy.ops.object.select_all(action='DESELECT')

            for item in ObjetosCopias:
                bpy.ops.object.select_all(action='DESELECT')
                item.select_set(True)
                bpy.context.view_layer.objects.active = item
                bpy.ops.object.delete(use_global=False)


        # Copia os 2

        Objetos = [bpy.data.objects[ObjDist], bpy.data.objects[ObjBase]]

        MedidasEixo = []
        ObjetosCopias = []

        for item in Objetos:
            print("OBJETO", item)
            bpy.ops.object.select_all(action='DESELECT')
            item.select_set(True)
            bpy.context.view_layer.objects.active = item
            bpy.ops.object.duplicate_move()

            print("CAMADONA")
            bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

            ObjetoAtual = bpy.context.selected_objects[0]
            MedidaAtual = ObjetoAtual.location[Eixo]

            MedidasEixo.append(MedidaAtual)
            ObjetosCopias.append(ObjetoAtual)

        Distancia = abs( MedidasEixo[0] - MedidasEixo[1] )


        # Calcula Posicao
        if MedidasEixo[1] < MedidasEixo[0]:
            DistanciaFinal = Distancia * -1
            print("DistanciaFinal", DistanciaFinal)
            print("")
            ApagaTudo()

            return DistanciaFinal

        if MedidasEixo[1] > MedidasEixo[0]:
            DistanciaFinal = Distancia
            print("DistanciaFinal", DistanciaFinal)
            print("")
            ApagaTudo()

            return DistanciaFinal

        if MedidasEixo[1] == MedidasEixo[0]:
            DistanciaFinal = Distancia
            print("DistanciaFinal", DistanciaFinal)
            print("")
            ApagaTudo()

            return DistanciaFinal


    else:
        print( "Não calculou. Algum objeto faltante:", ObjDist,",", ObjBase)



def CalculaTudoCefalometriaDef(self, context):

    CalculaAnguloOclusao()
    CalculaAnguloNasolabial()
    CalculaAnguloGbSnPog()


    try:
        glabella_tvl = str(float(round(DistanciaUnica("ST Glabella", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_glabella_tvl = bpy.props.StringProperty \
            (
                name = "Glabella - TVL",
                description = "Glabella - TVL",
                default = glabella_tvl
            )
    except:
        print("Algum ponto faltante!")



    try:
        rima_or_tvl = str(float(round(DistanciaDupla("OR right", "OR left", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_rima_or_tvl = bpy.props.StringProperty \
            (
                name = "OR' - TVL",
                description = "OR' - TVL",
                default = rima_or_tvl
            )
    except:
        print("Algum ponto faltante!")


    try:
        rima_or_tvl = str(float(round(DistanciaDupla("Cheekbone right", "Cheekbone left", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_cheekbone_tvl = bpy.props.StringProperty \
            (
                name = "Cheekbone - TVL",
                description = "Cheekbone - TVL",
                default = rima_or_tvl
            )
    except:
        print("Algum ponto faltante!")


    try:
        subpupilar_tvl = str(float(round(DistanciaDupla("Subpupil right", "Subpupil left", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_subpupil_tvl = bpy.props.StringProperty \
            (
                name = "Subpupil - TVL",
                description = "Subpupil - TVL",
                default = subpupilar_tvl
            )
    except:
        print("Algum ponto faltante!")

    '''
    try:
        proj_nasal_tvl = str(float(round(DistanciaDupla("Tip of Nose", "Tip of Nose", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_proj_nasal_tvl = bpy.props.StringProperty \
            (
                name = "Tip of Nose - TVL",
                description = "Tip of Nose - TVL",
                default = proj_nasal_tvl
            )
    except:
        print("Algum ponto faltante!")


    '''
    try:
        base_nasal_tvl = str(float(round(DistanciaDupla("AB right", "AB left", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_base_nasal_tvl = bpy.props.StringProperty \
            (
                name = "AB - TVL",
                description = "AB - TVL",
                default = base_nasal_tvl
            )
    except:
        print("Algum ponto faltante!")

    '''
    try:
        a_mole_tvl = str(float(round(DistanciaDupla("ST A point", "ST A point", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_a_mole_tvl = bpy.props.StringProperty \
            (
                name = "A' - TVL",
                description = "A' - TVL",
                default = a_mole_tvl
            )
    except:
        print("Algum ponto faltante!")


    try:
        labio_superior_tvl = str(float(round(DistanciaDupla("Upper Lip", "Upper Lip", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_labio_superior_tvl = bpy.props.StringProperty \
            (
                name = "Upper Lip - TVL",
                description = "Upper Lip - TVL",
                default = labio_superior_tvl
            )
    except:
        print("Algum ponto faltante!")


    try:
        l1_tvl = str(float(round(DistanciaDupla("L1 Tip", "L1 Tip", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_l1_tvl = bpy.props.StringProperty \
            (
                name = "L1 Tip - TVL",
                description = "L1 Tip - TVL",
                default = l1_tvl
            )
    except:
        print("Algum ponto faltante!")


    try:
        u1_tvl = str(float(round(DistanciaDupla("U1 Tip", "U1 Tip", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_u1_tvl = bpy.props.StringProperty \
            (
                name = "U1 Tip - TVL",
                description = "U1 Tip - TVL",
                default = u1_tvl
            )
    except:
        print("Algum ponto faltante!")


    try:
        labio_inferior_tvl = str(float(round(DistanciaDupla("Lower Lip", "Lower Lip", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_labio_inferior_tvl = bpy.props.StringProperty \
            (
                name = "Lower Lip - TVL",
                description = "Lower Lip - TVL",
                default = labio_inferior_tvl
            )
    except:
        print("Algum ponto faltante!")

    try:
        b_mole_tvl = str(float(round(DistanciaDupla("ST B point", "ST B point", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_b_mole_tvl = bpy.props.StringProperty \
            (
                name = "ST B point - TVL",
                description = "ST B point - TVL",
                default = b_mole_tvl
            )
    except:
        print("Algum ponto faltante!")


    try:
        pog_mole_tvl = str(float(round(DistanciaDupla("ST Pogonion", "ST Pogonion", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_pog_mole_tvl = bpy.props.StringProperty \
            (
                name = "ST Pogonion - TVL",
                description = "ST Pogonion - TVL",
                default = pog_mole_tvl
            )
    except:
        print("Algum ponto faltante!")


    try:
        pescoco_garganta_tvl = str(float(round(DistanciaDupla("Throat point", "Throat point", "Subnasale", 1),2)))+" mm"

        bpy.types.Scene.dist_pescoco_garganta_tvl = bpy.props.StringProperty \
            (
                name = "Throat point - TVL",
                description = "Throat point - TVL",
                default = pescoco_garganta_tvl
            )
    except:
        print("Algum ponto faltante!")

    '''

class CalculaTudoCefalometria(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.calcula_tudo_cefalo"
    bl_label = "Cephalometry cal all"

    def execute(self, context):
        CalculaTudoCefalometriaDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(CalculaTudoCefalometria)


def CalculaDistanciaObjetos(ObjA, ObjB):

    A = bpy.data.objects[ObjA]
    B = bpy.data.objects[ObjB]

    Distancia = math.sqrt(( (B.location[0] - A.location[0])**2 ) + ( (B.location[1] - A.location[1])**2 ) + ( (B.location[2] - A.location[2])**2 ))

    print("A distância entre '"+ObjA+"' e '"+ObjB+"' é de", round(Distancia, 2))

    return round(Distancia, 2)
