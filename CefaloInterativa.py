import bpy
from math import sqrt

#context = bpy.context
#obj = context.active_object
#scn = context.scene

def PontosCasa(objPonto, objEmpty):

    bpy.ops.object.select_all(action='DESELECT')

    ponto = bpy.data.objects[objPonto]
    empty = bpy.data.objects[objEmpty]

    ponto.select = True
    print("Selected")
    bpy.context.scene.objects.active = ponto
    print("Actived")

    bpy.ops.object.constraint_add(type='COPY_LOCATION')
    bpy.context.object.constraints["Copy Location"].target = empty
    bpy.context.object.constraints["Copy Location"].use_x = False


def CopiaRotacao(objFilho, objPai):

    bpy.ops.object.select_all(action='DESELECT')

    filho = bpy.data.objects[objFilho]
    pai = bpy.data.objects[objPai]

    filho.select = True
    print("Selected")
    bpy.context.scene.objects.active = filho
    print("Actived")

    bpy.ops.object.constraint_add(type='COPY_ROTATION')
    bpy.context.object.constraints["Copy Rotation"].target = pai
    bpy.context.object.constraints["Copy Rotation"].use_y = False


def CriaPontoMeio(emp1, emp2, empNovo, objPai):

    bpy.ops.object.select_all(action='DESELECT')

    emptyDireito = bpy.data.objects[emp1]
    emptyEsquerdo = bpy.data.objects[emp2]
    objetoPai = bpy.data.objects[objPai]

    emptyDireito.select = True
    emptyEsquerdo.select = True
#    bpy.context.scene.objects.active = emptyEsquerdo

    l = []
    for item in bpy.context.selected_objects:
        l.append(item.location)

#    distancia = sqrt( (l[0][0] - l[1][0])**2 + (l[0][1] - l[1][1])**2 + (l[0][2] - l[1][2])**2)

#    print(distancia)
    
    valorX = (l[0][0] + l[1][0]) / 2
    print("Valor X: ", valorX)
    
    valorY = (l[0][1] + l[1][1]) / 2
    print("Valor Y: ", valorY)
    
    valorZ = (l[0][2] + l[1][2]) / 2
    print("Valor Z: ", valorZ)
    
    bpy.ops.object.empty_add(type='PLAIN_AXES', radius=1, view_align=False, location=(valorX, valorY, valorZ))
    bpy.context.object.empty_draw_size = 3
    
    bpy.context.object.name = empNovo
    
    bpy.ops.object.select_all(action='DESELECT')
    
    emptyNovo = bpy.data.objects[empNovo]
    
    emptyNovo.select = True    
    objetoPai.select = True 
    bpy.context.scene.objects.active = objetoPai
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

def CefaloInterativaDef (self, context):
    CriaPontoMeio('EMP11', 'EMP21', 'EMPIncisivesUp', 'ma')
    PontosCasa('PT_Incisor_up_low', 'EMPIncisivesUp')

    CriaPontoMeio('EMP31', 'EMP41', 'EMPIncisivesDown', 'cm')
    PontosCasa('PT_Incisor_low_up', 'EMPIncisivesDown')

    CriaPontoMeio('EMPMeatusR', 'EMPMeatusL', 'EMPMeatus', 'ca')
    PontosCasa('PT_Po', 'EMPMeatus')

    CriaPontoMeio('EMP16', 'EMP26', 'EMPlin1', 'ma')
    PontosCasa('PT_2nd_Mol', 'EMPlin1')

    CriaPontoMeio('EMP13', 'EMP23', 'EMPlin2', 'ma')
    PontosCasa('PT_1st_Mol', 'EMPlin2')

    CriaPontoMeio('EMPEyeR', 'EMPEyeL', 'EMPEyes', 'ca')
    PontosCasa('PT_Or', 'EMPEyes')

    CriaPontoMeio('EMPEyeR', 'EMPEyeL', 'EMPEyes', 'ca')
    PontosCasa('PT_Or', 'EMPEyes')

    CriaPontoMeio('EMPGonionR', 'EMPGonionL', 'EMPGonion', 'ca')
    PontosCasa('PT_Go', 'EMPGonion')

    PontosCasa('PT_A', 'EMPApoint')
    PontosCasa('PT_B', 'EMPBpoint')
    PontosCasa('PT_Me', 'EMPMenton')
    PontosCasa('PT_Gn', 'EMPPogonion')
    PontosCasa('PT_N', 'EMPNasion')
    PontosCasa('PT_Ls', 'EMPLSpoint')
    PontosCasa('PT_Pg', 'EMPPGpoint')
    PontosCasa('PT_S', 'EMPSellaTurcica')

    CopiaRotacao('PT_Incisor_up_low', 'ma')
    CopiaRotacao('PT_Incisor_low_up', 'cm')

class CefaloInterativa(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cefalo_interativa"
    bl_label = "Cefalo Interativa"
    
    def execute(self, context):
        CefaloInterativaDef(self, context)
        return {'FINISHED'}
