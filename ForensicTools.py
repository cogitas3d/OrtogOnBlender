import bpy
import re

from .PontosAnatomicos import *

def AdicionaMarcadorDef(nome, distancia):

    bpy.ops.object.empty_add(type='SINGLE_ARROW', view_align=False)
    bpy.context.object.empty_display_size = distancia

    bpy.context.object.name = nome


    context = bpy.context
    obj = context.object
    scn = context.scene

    Marcador_EMP = obj
#    Marcador_EMP.select_set(True)
#    bpy.context.view_layer.objects.active = Marcador_EMP

    Marcador_EMP.location = bpy.context.scene.cursor.location
    Marcador_EMP.rotation_euler = bpy.context.scene.cursor.rotation_euler

#    bpy.context.scene.tool_settings.snap_elements = {'FACE'}
#    bpy.context.scene.tool_settings.use_snap_align_rotation = True

#    bpy.ops.wm.tool_set_by_id(name="builtin.rotate")

#    bpy.context.scene.transform_orientation_slots[0].type = 'NORMAL'

#    bpy.ops.view3d.view_selected(use_all_regions=False)

#    bpy.ops.view3d.view_center_cursor()

class AdicionaMarcador(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.adiciona_marcador"
    bl_label = "Add Soft Tissue Marker"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        NomePonto = bpy.context.scene.nome_marcador
        DistPonto = float(bpy.context.scene.dimensao_marcador)
        AdicionaMarcadorDef(NomePonto, DistPonto)
        return {'FINISHED'}

bpy.utils.register_class(AdicionaMarcador)


#-----------------------------------
# Cria Botões Marcadores Tecido mole

'''
with open('/home/linux3dcs/prj/Arc-Team_Santo/planilha.csv', 'r') as f:
    fileLines = f.readlines()

for i in range(len(fileLines)):
    limpaFinalLinha = fileLines[i].strip()
    separa = limpaFinalLinha.split(',')
    print(separa)
'''


def CriaBotoesDef():

    context = bpy.context
    #obj = context.object
    scn = context.scene

    bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT' # Tem que estar assim senão o alinhamento dá errado!


#        with open('/home/linux3dcs/prj/Arc-Team_Santo/planilha.csv', 'r') as f:
    with open(scn.my_tool.filepathcsv, 'r') as f:
        fileLines = f.readlines()

    posicaoZ = 0

    for i in range(len(fileLines))[::-1]:
        limpaFinalLinha = fileLines[i].strip()
        separa = limpaFinalLinha.split(',')
        #print(separa)

        # Cria def do botão
        Nome = "Mk "+separa[0]
        NomeClass = Nome.replace(" ", "")
        NomeMin = "object."+Nome.lower().replace(" ", "_")

        bpy.ops.object.empty_add(type='SINGLE_ARROW', view_align=False, location=(-150, 0, posicaoZ))
        bpy.context.object.name = Nome
        bpy.context.object.empty_display_size = float(separa[1])
        bpy.context.object.show_name = True
        bpy.ops.transform.rotate(value=1.5708, orient_axis='Y')
        posicaoZ += 10

    # ENVIA COLLECTION

        obj2 = bpy.context.view_layer.objects.active

        ListaColl = []

        for i in bpy.data.collections:
            ListaColl.append(i.name)

        if "Soft Tissue Markers" not in ListaColl:

            myCol = bpy.data.collections.new("Soft Tissue Markers")
            bpy.context.scene.collection.children.link(myCol)
            bpy.ops.object.collection_link(collection='Soft Tissue Markers')
    #        mainCol = bpy.data.collections['Collection']
    #        bpy.context.scene.collection.children.unlink(mainCol)
            bpy.data.collections['Collection'].objects.unlink(obj2)

        else:
            bpy.ops.object.collection_link(collection='Soft Tissue Markers')
    #        mainCol = bpy.data.collections['Collection']
    #        bpy.context.scene.collection.children.unlink(mainCol)
            bpy.data.collections['Collection'].objects.unlink(obj2)

    bpy.context.scene.tool_settings.snap_elements = {'FACE'}
    bpy.context.scene.tool_settings.use_snap_align_rotation = True




class CriaBotoes(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_cria_botoes"
    bl_label = "Cria Botões"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        CriaBotoesDef()
        return {'FINISHED'}

bpy.utils.register_class(CriaBotoes)

def OcultaNomesDef():
    context = bpy.context
    #obj = context.object
    scn = context.scene

    for i in bpy.context.selected_objects:
        i.show_name = False

class OcultaNomes(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.oculta_nomes"
    bl_label = "Hide Names"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        OcultaNomesDef()
        return {'FINISHED'}

bpy.utils.register_class(OcultaNomes)

def EngrossaLinhaDef():
    context = bpy.context
    #obj = context.object
    scn = context.scene

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.convert(target='CURVE')
    bpy.context.object.data.bevel_depth = 0.84

class EngrossaLinha(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.engrossa_linha"
    bl_label = "Make Tube Line"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        EngrossaLinhaDef()
        return {'FINISHED'}

bpy.utils.register_class( EngrossaLinha)
