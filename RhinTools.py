import bpy
from .PontosAnatomicos import *

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
