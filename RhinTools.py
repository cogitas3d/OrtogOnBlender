import bpy
from .PontosAnatomicos import *
from .FerrMedidas import *

# PONTOS ANATOMICOS

class Radix_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.radix_pt"
    bl_label = "Radix"

    @classmethod
    def poll(cls, context):

        found = 'Radix' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Radix', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Radix_pt)


# COPIA FACE

def CopiaFaceDef():
    bpy.context.object.name = "SoftTissueDynamic"
    bpy.ops.object.duplicate()
    bpy.context.object.name = "SoftTissueDynamic_COPY"

    FaceCopiada = bpy.data.objects['SoftTissueDynamic_COPY']
    FaceCopiada.hide_viewport=True

    FaceOriginal = bpy.data.objects['SoftTissueDynamic']
    FaceOriginal.select_set(True)
    bpy.context.view_layer.objects.active = FaceOriginal

class CopiaFace(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.copia_face"
    bl_label = "Copy Face"

    @classmethod
    def poll(cls, context):

        found = 'SoftTissueDynamic_COPY' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CopiaFaceDef()
        return {'FINISHED'}

bpy.utils.register_class(CopiaFace)


def CalculaDistsNarizDef():

    bpy.ops.object.mode_set(mode = 'OBJECT')

    ListaPontos = ["Radix", "Tip of Nose", "Subnasale"]

    for i in ListaPontos:
#            print("HÁ O NOME!", i.name)
        bpy.ops.object.select_all(action='DESELECT')

        ObjetoAtual = bpy.data.objects[i]
        ObjetoAtual.select_set(True)
        bpy.context.view_layer.objects.active = ObjetoAtual
        bpy.ops.object.duplicate()
        NovoNome = str(bpy.data.objects[i].name)+"_COPY_MEDIDAS"
        bpy.context.object.name = NovoNome
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        bpy.ops.object.select_all(action='DESELECT')

    try:

        DistRadixTip = DistanciaObjetos("Radix_COPY_MEDIDAS", "Tip of Nose_COPY_MEDIDAS")
        DistTipSub = DistanciaObjetos("Radix_COPY_MEDIDAS", "Subnasale_COPY_MEDIDAS")

        ProporcaoNariz = DistRadixTip / DistTipSub

        bpy.types.Scene.rhin_prop_nariz = bpy.props.StringProperty \
            (
                name = "Nose Proportion",
                description = "Nose Proportion",
                default = str(round(ProporcaoNariz, 2))
            )
    except:
        print("Problemas ao calcular a proporção do nariz.")

    try:

        # CRIA PONTOS PARA CALCULAR ANGULO
        bpy.ops.object.select_all(action='DESELECT')

        ObjetoAtual = bpy.data.objects["Subnasale_COPY_MEDIDAS"]
        ObjetoAtual.select_set(True)
        bpy.context.view_layer.objects.active = ObjetoAtual
        bpy.ops.object.duplicate()
        NovoNome = "Subnasale_ABAIXO"
        bpy.context.object.name = NovoNome
        bpy.ops.transform.translate(value=(0, 0, -80))
        bpy.ops.object.select_all(action='DESELECT')

        # CALCULA ANGULO
        AnguloNasolabial = CalculaAngulo("Tip of Nose_COPY_MEDIDAS", "Subnasale_COPY_MEDIDAS", "Subnasale_ABAIXO")

#        AnguloNasolabial = CalculaAngulo("Radix_COPY_MEDIDAS", "Tip of Nose_COPY_MEDIDAS", "Subnasale_COPY_MEDIDAS")

        bpy.types.Scene.rhin_angulo_nasolabial = bpy.props.StringProperty \
            (
                name = "Nasolabial Angle",
                description = "Nasolabial Angle",
                default = str(AnguloNasolabial) #+"º"
            )

        # Apaga objeto criados

        bpy.ops.object.select_all(action='DESELECT')
        ObjetoAtual = bpy.data.objects["Subnasale_ABAIXO"]
        ObjetoAtual.select_set(True)
        bpy.context.view_layer.objects.active = ObjetoAtual
        bpy.ops.object.delete(use_global=False)

    except:
        print("Não foi possível fazer o cálculo do ângulo nasolabial.")

    # APAGA Pontos criados

    try:
        for i in ListaPontos:
    #            print("HÁ O NOME!", i.name)
            bpy.ops.object.select_all(action='DESELECT')
            NomeAtual = str(bpy.data.objects[i].name)+"_COPY_MEDIDAS"
            ObjetoAtual = bpy.data.objects[NomeAtual]
            ObjetoAtual.select_set(True)
            bpy.context.view_layer.objects.active = ObjetoAtual
            bpy.ops.object.delete(use_global=False)
            bpy.ops.object.select_all(action='DESELECT')

    except:
        print("Houve algum problema ao deletar os pontos.")


class CalculaDistsNariz(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.dist_nariz"
    bl_label = "Nose dists"

    def execute(self, context):
        CalculaDistsNarizDef()
        return {'FINISHED'}

bpy.utils.register_class(CalculaDistsNariz)
