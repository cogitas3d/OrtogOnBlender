import bpy
import math

from .CalculaPontos import *

def testeDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.modifier_add(type='WIREFRAME')
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subsurf"].levels = 2

#def calculaAngulo(PT1, PT2, PT3):
    

def CalculaDist(Ponto1, Ponto2):
    Dist = math.sqrt( (Ponto2.location[1] - Ponto1.location[1])**2 + (Ponto2.location[2] - Ponto1.location[2])**2 )
    #print(Dist)
    
    return Dist # Necessario para imprimir e retornar valor


def CalculaAngulo(Lado1, Lado2, Lado3):
    
    Angulo = ((Lado1**2)+(Lado2**2)-(Lado3**2))/(2*Lado1*Lado2)
    
    return Angulo

def CalculaAnguloFalta(Angulo1, Angulo2):
    Lado_1 = float(round(math.degrees(math.acos(-1)),2)) - float(round(math.degrees(math.acos(Angulo1)),2))
    Lado_2 = float(round(math.degrees(math.acos(-1)),2)) - float(round(math.degrees(math.acos(Angulo2)),2))
    Lado_3 = float(round(math.degrees(math.acos(-1)),2)) - Lado_1 - Lado_2
    return Lado_3

def CriaCopiaPonto(objeto):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.select_all(action='DESELECT')
    selecionado = bpy.data.objects[objeto]
    selecionado.select = True
    bpy.context.scene.objects.active = selecionado
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = objeto+".INI"
    bpy.context.object.empty_draw_size = 3
#    bpy.ops.object.duplicate()
#    bpy.context.object.name = objeto+".INI"
#    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')




def CefaloCalculaTudoDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene
    
    CriaCopiaPonto('PT_N')
    CriaCopiaPonto('PT_S')
    CriaCopiaPonto('PT_A')
    CriaCopiaPonto('PT_B')
    CriaCopiaPonto('PT_Gn')
    CriaCopiaPonto('PT_1st_Mol')
    CriaCopiaPonto('PT_2nd_Mol')
    CriaCopiaPonto('PT_Or')
    CriaCopiaPonto('PT_Po')
    CriaCopiaPonto('PT_Go')
    CriaCopiaPonto('PT_Me')
    CriaCopiaPonto('PT_Incisor_low_up')
    CriaCopiaPonto('PT_Incisor_low_low')
    CriaCopiaPonto('PT_Incisor_up_up')
    CriaCopiaPonto('PT_Incisor_up_low')

    PT_N = bpy.data.objects['PT_N.INI']
    PT_S = bpy.data.objects['PT_S.INI']
    PT_A = bpy.data.objects['PT_A.INI']
    PT_B = bpy.data.objects['PT_B.INI']
    PT_Gn = bpy.data.objects['PT_Gn.INI']
    PT_1st_Mol = bpy.data.objects['PT_1st_Mol.INI']
    PT_2nd_Mol = bpy.data.objects['PT_2nd_Mol.INI']
    PT_Or = bpy.data.objects['PT_Or.INI']
    PT_Po = bpy.data.objects['PT_Po.INI']
    PT_Go = bpy.data.objects['PT_Go.INI']
    PT_Me = bpy.data.objects['PT_Me.INI']
    PT_Incisor_low_up = bpy.data.objects['PT_Incisor_low_up.INI']
    PT_Incisor_low_low = bpy.data.objects['PT_Incisor_low_low.INI']
    PT_Incisor_up_up = bpy.data.objects['PT_Incisor_up_up.INI']
    PT_Incisor_up_low = bpy.data.objects['PT_Incisor_up_low.INI']

    dist_N_S = CalculaDist(PT_N, PT_S)

    dist_N_B = CalculaDist(PT_N, PT_B)
    dist_S_B = CalculaDist(PT_S, PT_B)

    dist_N_A = CalculaDist(PT_N, PT_A)
    dist_S_A = CalculaDist(PT_S, PT_A)

    dist_A_B = CalculaDist(PT_A, PT_B)

    dist_S_Gn = CalculaDist(PT_S, PT_Gn)
    dist_N_Gn = CalculaDist(PT_N, PT_Gn)

    dist_S_2nd_Mol = CalculaDist(PT_S, PT_2nd_Mol)
    dist_N_2nd_Mol = CalculaDist(PT_N, PT_2nd_Mol)
    dist_1st_2nd_Mol = CalculaDist(PT_2nd_Mol, PT_1st_Mol)
    dist_S_1st_Mol = CalculaDist(PT_S, PT_1st_Mol)

    dist_Po_Or = CalculaDist(PT_Po, PT_Or)
    dist_Po_Go = CalculaDist(PT_Go, PT_Po)
    dist_Or_Go = CalculaDist(PT_Or, PT_Go)

    dist_Go_Me = CalculaDist(PT_Go, PT_Me)
    dist_Me_Po = CalculaDist(PT_Me, PT_Po)

    dist_Or_In_low_up = CalculaDist(PT_Or, PT_Incisor_low_up)
    dist_Po_In_low_up = CalculaDist(PT_Po, PT_Incisor_low_up)
    dist_In_low_up_In_low_low = CalculaDist(PT_Incisor_low_up, PT_Incisor_low_low)
    dist_Or_In_low_low = CalculaDist(PT_Or, PT_Incisor_low_low)

    dist_Go_In_low_up = CalculaDist(PT_Incisor_low_up, PT_Go)
    dist_Go_In_low_low = CalculaDist(PT_Incisor_low_low, PT_Go)
    dist_Me_In_low_up = CalculaDist(PT_Me, PT_Incisor_low_up)

    dist_In_up_up_In_up_low = CalculaDist(PT_Incisor_up_up, PT_Incisor_up_low)
    dist_In_up_up_S = CalculaDist(PT_Incisor_up_up, PT_S)
    dist_In_up_low_S = CalculaDist(PT_Incisor_up_low, PT_S)
    dist_In_up_low_N = CalculaDist(PT_Incisor_up_low, PT_N)


    Angulo_S_N_A = CalculaAngulo(dist_N_S, dist_N_A, dist_S_A)

    Angulo_S_N_B = CalculaAngulo(dist_N_S, dist_N_B, dist_S_B)

    Angulo_A_N_B = CalculaAngulo(dist_N_A, dist_N_B, dist_A_B)

    Angulo_Y_Cresc = CalculaAngulo(dist_N_S, dist_S_Gn, dist_N_Gn)

# Cálculo SN PlO
    Angulo_N_S_2nd_Mol = CalculaAngulo(dist_N_S, dist_S_2nd_Mol, dist_N_2nd_Mol)
    Angulo_2nd_S_1st_Mol = CalculaAngulo(dist_S_2nd_Mol, dist_1st_2nd_Mol, dist_S_1st_Mol)

    SNPLlo_lado_3 = CalculaAnguloFalta(Angulo_N_S_2nd_Mol, Angulo_2nd_S_1st_Mol)

# Cálculo FMA
    Angulo_Po_Or_Go = CalculaAngulo(dist_Po_Go, dist_Po_Or, dist_Or_Go)
    Angulo_Go_Me_Po = CalculaAngulo(dist_Go_Me, dist_Po_Go, dist_Me_Po)

    FMA_lado_3 = CalculaAnguloFalta(Angulo_Po_Or_Go, Angulo_Go_Me_Po)

# Cálculo FMIA
    Angulo_Or_Po_In_low_up = CalculaAngulo(dist_Po_Or, dist_Or_In_low_up, dist_Po_In_low_up)
    Angulo_In_low_up_Or_In_low_low = CalculaAngulo(dist_Or_In_low_up, dist_In_low_up_In_low_low, dist_Or_In_low_low)

    FMIA_lado_3 = CalculaAnguloFalta(Angulo_Or_Po_In_low_up, Angulo_In_low_up_Or_In_low_low)

# Cálculo IMPA

    Angulo_In_low_up_Go_In_low_low = CalculaAngulo(dist_Go_In_low_up, dist_In_low_up_In_low_low, dist_Go_In_low_low)
    Angulo_Go_In_low_up_Me = CalculaAngulo(dist_Go_In_low_up, dist_Go_Me, dist_Me_In_low_up)

    IMPA_lado_3 = abs(CalculaAnguloFalta(Angulo_In_low_up_Go_In_low_low, Angulo_Go_In_low_up_Me))

# Cálculo 1NS

    Angulo_In_up_low_In_up_up_S = CalculaAngulo(dist_In_up_up_In_up_low, dist_In_up_low_S, dist_In_up_up_S)
    Angulo_S_N_In_up_up = CalculaAngulo(dist_N_S, dist_In_up_low_S, dist_In_up_low_N)

    NS_lado_3 = abs(CalculaAnguloFalta(Angulo_In_up_low_In_up_up_S, Angulo_S_N_In_up_up))

    print("Angulo_In_up_low_In_up_up_S")
    print(Angulo_In_up_low_In_up_up_S)
    print(" ")
    print("Angulo_S_N_In_up_up")
    print(Angulo_S_N_In_up_up)
    print(" ")
    print("1NS:")
    print(NS_lado_3)

    bpy.types.Scene.angulo_SNA = bpy.props.StringProperty \
      (
        name = "SNA",
        description = "Ângulo SNA",
        default = str(round(math.degrees(math.acos(Angulo_S_N_A)),2))
      )

    bpy.types.Scene.angulo_SNB = bpy.props.StringProperty \
      (
        name = "SNB",
        description = "Ângulo SNB",
        default = str(round(math.degrees(math.acos(Angulo_S_N_B)),2))
      )

    bpy.types.Scene.angulo_ANB = bpy.props.StringProperty \
      (
        name = "ANB",
        description = "Ângulo SNB",
        default = str(round(math.degrees(math.acos(Angulo_A_N_B)),2))
      )
    bpy.types.Scene.angulo_Y_Cresc = bpy.props.StringProperty \
      (
        name = "Y Growing",
        description = "Ângulo Y de Screscimento",
        default = str(round(math.degrees(math.acos(Angulo_Y_Cresc)),2))
      )
    bpy.types.Scene.angulo_SNPlO = bpy.props.StringProperty \
      (
        name = "SNPlO",
        description = "ANgulo SN Molares",
        default = str(int(SNPLlo_lado_3)+float(str(SNPLlo_lado_3-int(SNPLlo_lado_3))[1:4])) # Para mostrar apenas duas casas decimais
      )
    bpy.types.Scene.angulo_FMA = bpy.props.StringProperty \
      (
        name = "FMA",
        description = "Ângulo FMA",
        default = str(int(FMA_lado_3)+float(str(FMA_lado_3-int(FMA_lado_3))[1:4]))
      )
    bpy.types.Scene.angulo_FMIA = bpy.props.StringProperty \
      (
        name = "FMIA",
        description = "Ângulo FMA",
        default = str(int(FMIA_lado_3)+float(str(FMIA_lado_3-int(FMIA_lado_3))[1:4]))
      )
    bpy.types.Scene.angulo_IMPA = bpy.props.StringProperty \
      (
        name = "IMPA",
        description = "Ângulo IMPA",
        default = str(int(IMPA_lado_3)+float(str(IMPA_lado_3-int(IMPA_lado_3))[1:4]))
      )
    bpy.types.Scene.angulo_NS = bpy.props.StringProperty \
      (
        name = "1NS",
        description = "Ângulo 1NS",
        default = str(int(NS_lado_3)+float(str(NS_lado_3-int(NS_lado_3))[1:4]))
      )

    apagaObjeto('PT_N.INI')
    apagaObjeto('PT_S.INI')
    apagaObjeto('PT_A.INI')
    apagaObjeto('PT_B.INI')
    apagaObjeto('PT_Gn.INI')
    apagaObjeto('PT_1st_Mol.INI')
    apagaObjeto('PT_2nd_Mol.INI')
    apagaObjeto('PT_Or.INI')
    apagaObjeto('PT_Po.INI')
    apagaObjeto('PT_Go.INI')
    apagaObjeto('PT_Me.INI')
    apagaObjeto('PT_Incisor_low_up.INI')
    apagaObjeto('PT_Incisor_low_low.INI')
    apagaObjeto('PT_Incisor_up_up.INI')
    apagaObjeto('PT_Incisor_up_low.INI')
