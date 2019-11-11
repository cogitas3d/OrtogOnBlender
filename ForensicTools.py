import bpy
import re
import platform

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


def ForensicImportaMuscleDef(nome, colecao):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    try:
        bpy.ops.object.mode_set(mode='OBJECT')
    except:
        print("Erro com o Object Mode!")


    if platform.system() == "Linux":

        dirScript = bpy.utils.user_resource('SCRIPTS')

        blendfile = dirScript+"addons/OrtogOnBlender-master/ForensicObj.blend"
#        section   = "\\Collection\\"
#        object    = "SPLINT"
        section   = "\\Object\\"
        object    = nome

    if platform.system() == "Darwin":

        dirScript = bpy.utils.user_resource('SCRIPTS')

        blendfile = dirScript+"addons/OrtogOnBlender-master/ForensicObj.blend"
        section   = "\\Object\\"
        object    = nome

    if platform.system() == "Windows":

        dirScript = 'C:/OrtogOnBlender/Blender280/2.80/scripts/'

        blendfile = dirScript+"addons/OrtogOnBlender-master/ForensicObj.blend"
        section   = "\\Object\\"
        object    = nome


    filepath  = blendfile + section + object
    directory = blendfile + section
    filename  = object

    bpy.ops.wm.append(
        filepath=filepath,
        filename=filename,
        directory=directory)

    ObjImportado = bpy.data.objects[nome]


    bpy.ops.object.select_all(action='DESELECT')
    ObjImportado.select_set(True)
    context.view_layer.objects.active = ObjImportado

    # Coloca na camada
    obj2 = bpy.context.view_layer.objects.active

    ListaColl = []

    for i in bpy.data.collections:
        ListaColl.append(i.name)

    if colecao not in ListaColl:

        myCol = bpy.data.collections.new(colecao)
        bpy.context.scene.collection.children.link(myCol)
        bpy.ops.object.collection_link(collection=colecao)
#        mainCol = bpy.data.collections['Collection']
#        bpy.context.scene.collection.children.unlink(mainCol)
        bpy.data.collections['Collection'].objects.unlink(obj2)

    else:
        bpy.ops.object.collection_link(collection=colecao)
#        mainCol = bpy.data.collections['Collection']
#        bpy.context.scene.collection.children.unlink(mainCol)
        bpy.data.collections['Collection'].objects.unlink(obj2)

class ForensicImportaTemporalis(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_temporalis"
    bl_label = "Import Temporalis"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Temporalis' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Temporalis", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaTemporalis)


class ForensicImportaMasseter(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_masseter"
    bl_label = "Import Masseter"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Masseter' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Masseter", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaMasseter)


class ForensicImportaOrbicularisOculi(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_orbicularis_oculi"
    bl_label = "Import Orbicularis Oculi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Orbicularis Oculi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Orbicularis Oculi", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaOrbicularisOculi)


class ForensicImportaElevatorLabiiSuperioris(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_elevator_labii_superioris"
    bl_label = "Import Elevator Labii Superioris"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Elevator Labii Superioris' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Elevator Labii Superioris", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaElevatorLabiiSuperioris)


class ForensicImportaNasalis(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_nasalis"
    bl_label = "Import Nasalis"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Nasalis' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Nasalis", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaNasalis)

class ForensicImportaZygomaticus(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_zygomaticus"
    bl_label = "Import Zygomaticus"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Zygomaticus' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Zygomaticus", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaZygomaticus)


class ForensicImportaOrbicularisOris(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_orbicularis_oris"
    bl_label = "Import Orbicularis Oris"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Orbicularis Oris' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Orbicularis Oris", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaOrbicularisOris)


class ForensicImportaBuccinator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_buccinator"
    bl_label = "Import Buccinator"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Buccinator' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Buccinator", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaBuccinator)


class ForensicImportaMentalis(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_mentalis"
    bl_label = "Import Mentalis"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Mentalis+' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Mentalis+", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaMentalis)


class ForensicImportaSternocleidomastoid(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_sternocleidomastoid"
    bl_label = "Import Sternocleidomastoid"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Sternocleidomastoid+' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Sternocleidomastoid+", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaSternocleidomastoid)


class ForensicImportaOlho(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_olho"
    bl_label = "Import Eye"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Eye' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Eye", "Eyes")
        return {'FINISHED'}


bpy.utils.register_class(ForensicImportaOlho)

def CopiaEspelhaDef():

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

class CopiaEspelha(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_copia_espelha"
    bl_label = "Copy and Mirror"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        CopiaEspelhaDef()
        return {'FINISHED'}

bpy.utils.register_class(CopiaEspelha)

def ForensicEsculturaGrabDef():

    context = bpy.context
    scn = context.scene

#    bpy.context.space_data.shading.type = 'MATERIAL'
    bpy.ops.object.mode_set(mode = 'SCULPT')
    bpy.ops.wm.tool_set_by_id(name="builtin_brush.Grab")
    bpy.context.scene.tool_settings.sculpt.use_symmetry_x = False

class ForensicEsculturaGrab(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_escultura_grab"
    bl_label = "Change to Grab"

    @classmethod
    def poll(cls, context):
        o = context.object
        if o is None:
            return False
        else:
            if o.type == "MESH":
                if bpy.context.mode == 'OBJECT' or bpy.context.mode == 'SCULPT':
                    return True
                else:
                    return False
            else:
                return False

    def execute(self, context):
        ForensicEsculturaGrabDef()
        return {'FINISHED'}

bpy.utils.register_class(ForensicEsculturaGrab)


def ForensicEsculturaSmoothDef():

    context = bpy.context
    scn = context.scene

#    bpy.context.space_data.shading.type = 'MATERIAL'
    bpy.ops.object.mode_set(mode = 'SCULPT')
    bpy.ops.wm.tool_set_by_id(name="builtin_brush.Smooth")
    bpy.context.scene.tool_settings.sculpt.use_symmetry_x = False

class ForensicEsculturaSmooth(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_escultura_smooth"
    bl_label = "Change to Smooth"

    @classmethod
    def poll(cls, context):
        o = context.object
        if o is None:
            return False
        else:
            if o.type == "MESH":
                if bpy.context.mode == 'OBJECT' or bpy.context.mode == 'SCULPT':
                    return True
                else:
                    return False
            else:
                return False

    def execute(self, context):
        ForensicEsculturaSmoothDef()
        return {'FINISHED'}

bpy.utils.register_class(ForensicEsculturaSmooth)
