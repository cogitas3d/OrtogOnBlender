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

    #DistRadixTip = DistanciaObjetos("Radix", "Tip of Nose")

    try:
        AnguloNasolabial = CalculaAngulo("Radix", "Tip of Nose", "Subnasale")

        bpy.types.Scene.rhin_angulo_nasolabial = bpy.props.StringProperty \
            (
                name = "Nasolabial Angle",
                description = "Nasolabial Angle",
                default = str(AnguloNasolabial)+"º"
            )

    except:
        print("Não foi possível fazer o cálculo do ângulo nasolabial.")
#    return DistRadixTip, AnguloNasolabial


class CalculaDistsNariz(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.dist_nariz"
    bl_label = "Nose dists"

    def execute(self, context):
        CalculaDistsNarizDef()
        return {'FINISHED'}

bpy.utils.register_class(CalculaDistsNariz)
