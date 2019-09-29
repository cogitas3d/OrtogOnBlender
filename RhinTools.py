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

class Anterior_Nostril_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.anterior_nostril_left_pt"
    bl_label = "Anterior Nostril left"

    @classmethod
    def poll(cls, context):

        found = 'Anterior Nostril left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Anterior Nostril left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Anterior_Nostril_left_pt)


class Anterior_Nostril_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.anterior_nostril_right_pt"
    bl_label = "Anterior Nostril right"

    @classmethod
    def poll(cls, context):

        found = 'Anterior Nostril right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Anterior Nostril right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Anterior_Nostril_right_pt)


class Posterior_Nostril_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.posterior_nostril_left_pt"
    bl_label = "Posterior Nostril left"

    @classmethod
    def poll(cls, context):

        found = 'Posterior Nostril left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Posterior Nostril left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Posterior_Nostril_left_pt)


class Posterior_Nostril_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.posterior_nostril_right_pt"
    bl_label = "Posterior Nostril right"

    @classmethod
    def poll(cls, context):

        found = 'Posterior Nostril right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Posterior Nostril right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Posterior_Nostril_right_pt)


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

    try:
        bpy.ops.object.mode_set(mode = 'OBJECT')
    except:
        print("Já em modo objeto.")

    ListaPontos = ["Radix", "Tip of Nose", "Subnasale", "Anterior Nostril left", "Posterior Nostril left", "Anterior Nostril right", "Posterior Nostril right"]

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

        # CRIA PONTOS PARA CALCULAR ANGULO ESQUERDO
        bpy.ops.object.select_all(action='DESELECT')

        ObjetoAtual = bpy.data.objects["Posterior Nostril left_COPY_MEDIDAS"]
        ObjetoAtual.select_set(True)
        bpy.context.view_layer.objects.active = ObjetoAtual
        bpy.ops.object.duplicate()
        NovoNome = "Posterior Nostril left_ABAIXO"
        bpy.context.object.name = NovoNome
        bpy.ops.transform.translate(value=(0, 0, -80))
        bpy.ops.object.select_all(action='DESELECT')

        # CALCULA ANGULO
        AnguloNasolabial = CalculaAngulo("Anterior Nostril left_COPY_MEDIDAS", "Posterior Nostril left_COPY_MEDIDAS", "Posterior Nostril left_ABAIXO")

#        AnguloNasolabial = CalculaAngulo("Radix_COPY_MEDIDAS", "Tip of Nose_COPY_MEDIDAS", "Subnasale_COPY_MEDIDAS")

        bpy.types.Scene.rhin_angulo_nasolabial_esquerdo = bpy.props.StringProperty \
            (
                name = "Nasolabial Angle left",
                description = "Nasolabial Angle left",
                default = str(AnguloNasolabial) #+"º"
            )

        # Apaga objeto criados

        bpy.ops.object.select_all(action='DESELECT')
        ObjetoAtual = bpy.data.objects["Posterior Nostril left_ABAIXO"]
        ObjetoAtual.select_set(True)
        bpy.context.view_layer.objects.active = ObjetoAtual
        bpy.ops.object.delete(use_global=False)

    except:
        print("Não foi possível fazer o cálculo do ângulo nasolabial ESQUERDO.")


    try:

        # CRIA PONTOS PARA CALCULAR ANGULO DIREITO
        bpy.ops.object.select_all(action='DESELECT')

        ObjetoAtual = bpy.data.objects["Posterior Nostril right_COPY_MEDIDAS"]
        ObjetoAtual.select_set(True)
        bpy.context.view_layer.objects.active = ObjetoAtual
        bpy.ops.object.duplicate()
        NovoNome = "Posterior Nostril right_ABAIXO"
        bpy.context.object.name = NovoNome
        bpy.ops.transform.translate(value=(0, 0, -80))
        bpy.ops.object.select_all(action='DESELECT')

        # CALCULA ANGULO
        AnguloNasolabial = CalculaAngulo("Anterior Nostril right_COPY_MEDIDAS", "Posterior Nostril right_COPY_MEDIDAS", "Posterior Nostril right_ABAIXO")

#        AnguloNasolabial = CalculaAngulo("Radix_COPY_MEDIDAS", "Tip of Nose_COPY_MEDIDAS", "Subnasale_COPY_MEDIDAS")

        bpy.types.Scene.rhin_angulo_nasolabial_direito = bpy.props.StringProperty \
            (
                name = "Nasolabial Angle right",
                description = "Nasolabial Angle right",
                default = str(AnguloNasolabial) #+"º"
            )

        # Apaga objeto criados

        bpy.ops.object.select_all(action='DESELECT')
        ObjetoAtual = bpy.data.objects["Posterior Nostril right_ABAIXO"]
        ObjetoAtual.select_set(True)
        bpy.context.view_layer.objects.active = ObjetoAtual
        bpy.ops.object.delete(use_global=False)

    except:
        print("Não foi possível fazer o cálculo do ângulo nasolabial DIREITO.")

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
