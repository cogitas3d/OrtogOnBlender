bl_info = {
    "name": "OrtogOnBlender",
    "author": "Cicero Moraes e Everton da Rosa",
    "version": (1, 1, 11),
    "blender": (2, 75, 0),
    "location": "View3D",
    "description": "Planejamento de Cirurgia Ortognática no Blender",
    "warning": "",
    "wiki_url": "",
    "category": "ortog",
    }

if "bpy" in locals():
    import imp
    imp.reload(ImportaArmature)
#    imp.reload(GeraModelosTomo)
    print("Reloaded multifiles")
else:
    from .CefaloInterativa import *
    from .DesenhaGuia import *
    from .ImportaArmature import *
    from .GeraModelosTomo import *
    from .AlinhaRedimFotogrametria import *
    from .DinamicaMole import *
    from .ConfiguraOsteotomias import *
    from .FotogrametriaOpenMVG import *
    from .FotogrametriaOpenMVGCam import *
    from .FotogrametriaSMVS import *
    from .PontosAnatomicos import *
    from .CriaSplint import *
    from .FerramentasRefeMedidas import *
    from .FerramentasCorte import *
    from .CefaloMedidas import *
    from .AjustaTomo import *
    from .CalculaPontos import *
    from .AtualizaScript import *
    from .FotogrametriaComposta import *
#    from . import mycube, mysphere, mycylinder
    print("Imported all OrtogOnBlender modules")

import bpy
import os
import sys
import subprocess
import tempfile
import bmesh
import shutil
import platform


from bpy_extras.object_utils import AddObjectHelper, object_data_add

from bpy.props import (StringProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )

#from mathutils import Vector
from mathutils import Matrix, Vector
from math import sqrt
from bpy import context
from os.path import expanduser
import math

from os import listdir
from os.path import isfile, join
import exifread


# Desenha Guia

class DesenhaGuia(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.teste"
    bl_label = "Teste"
    
    def execute(self, context):
        DesenhaGuiaDef(self, context)
        return {'FINISHED'}

# Corte de acabamento

class Acabamento(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.acabamento"
    bl_label = "Acabamento"
    
    def execute(self, context):
        AcabamentoDef(self, context)
        return {'FINISHED'} 

# Acabamento

class Acabamento(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.acabamento"
    bl_label = "Acabamento"
    
    def execute(self, context):
        AcabamentoDef(self, context)
        return {'FINISHED'} 

# Fecha Buraco

class FechaBuraco(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.fecha_buraco"
    bl_label = "Fecha Buraco"
    
    def execute(self, context):
        FechaBuracoDef(self, context)
        return {'FINISHED'}  

# Fotogrametria composta

class FotogrametriaComposta(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.fotogrametria_composta"
    bl_label = "Fotogrametria Composta"

    def execute(self, context):
        FotogrametriaCompostaDef(self, context)
        return {'FINISHED'}

# Importa cameras

class ImportaCameras(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.importa_cameras"
    bl_label = "Atualiza Script"

    def execute(self, context):
        ImportaCamerasDef(self, context)
        return {'FINISHED'}

# Atualiza Scripts

class AtualizaScript(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.atualiza_script"
    bl_label = "Atualiza Script"

    def execute(self, context):
        AtualizaScriptDef(self, context)
        return {'FINISHED'}

#ABRE TEMPORARIO

class AbreTMP(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.abre_tmp"
    bl_label = "Abre TMP"

    def execute(self, context):
        AbreTMPDef(self, context)
        return {'FINISHED'}

#CORRIGE DICOM

class CorrigeDicom(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.corrige_dicom"
    bl_label = "Corrige DICOM"

    def execute(self, context):
        CorrigeDicomDef(self, context)
        return {'FINISHED'}

# AJUSTA TOMO

class AjustaTomo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.ajusta_tomo"
    bl_label = "Ajusta Tomo"

    def execute(self, context):
        AjustaTomoDef(self, context)
        return {'FINISHED'}



# IMPORTA TOMO MOLDES

class GeraModelosTomoArc(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_modelos_tomo_arc"
    bl_label = "Gera Tomografia Molde"
    
    def execute(self, context):
        GeraModelosTomoArcDef(self, context)
        return {'FINISHED'}

#PONTO VISTA RAIO-X
class CameraXRayView(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.camera_xray_view"
    bl_label = "Visualiza Camera Raio-X"
    
    def execute(self, context):
        CameraXRayViewDef(self, context)
        return {'FINISHED'}

#PONTO VISTA PANORAMICA
class CameraPanoramic(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.camera_panoramic"
    bl_label = "Visualiza Camera Raio-X"
    
    def execute(self, context):
        CameraPanoramicDef(self, context)
        return {'FINISHED'}

# CONFIGURA EXECUTÁVEIS E SCRIPTS

class ortogPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    dicom2stl_filepath = StringProperty(
        name="Dicom2STL Path",
        description="Location of Dicom2Mesh Python file",
        subtype="FILE_PATH",
        default="",
        )


#    OpenMVG_filepath = StringProperty(
#        name="OpenMVG Path",
#        description="Location of OpenMVG Python file",
#        subtype="FILE_PATH",
#        default="",
#        )


 #   OpenMVS_filepath = StringProperty(
 #       name="OpenMVS Path",
 #       description="Location of OpenMVS script",
 #       subtype="FILE_PATH",
 #       default="",
 #       )



    SMVS_filepath = StringProperty(
        name="SMVS Path",
        description="Location of SMVS script",
        subtype="FILE_PATH",
        default="",
        )


    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.prop(self, "dicom2stl_filepath")
        #print(dicom2stl_filepath)

        row = layout.row()
        row.prop(self, "OpenMVG_filepath")
        #print(dicom2stl_filepath)

        row = layout.row()
        row.prop(self, "OpenMVS_filepath")

        row = layout.row()
        row.prop(self, "SMVS_filepath")

def get_dicom2stl_filepath(context):
    """preference set in the addon"""
#    addon = get_addon_name()
    preferences = context.user_preferences.addons["OrtogOnBlender-master"].preferences
    return preferences.dicom2stl_filepath

def get_OpenMVG_filepath(context):
    """preference set in the addon"""
#    addon = get_addon_name()
    preferences = context.user_preferences.addons["OrtogOnBlender-master"].preferences
    return preferences.OpenMVG_filepath

def get_OpenMVS_filepath(context):
    """preference set in the addon"""
#    addon = get_addon_name()
    preferences = context.user_preferences.addons["OrtogOnBlender-master"].preferences
    return preferences.OpenMVS_filepath


def get_SMVS_filepath(context):
    """preference set in the addon"""
#    addon = get_addon_name()
    preferences = context.user_preferences.addons["OrtogOnBlender-master"].preferences
    return preferences.SMVS_filepath

# TOMOGRAFIAS SELECAO

#HELICAL

def TomoHeliDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.context.scene.interesse_ossos = "200"
    bpy.context.scene.interesse_mole = "-300"
    bpy.context.scene.interesse_dentes = "1760"

class TomoHeli(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tomo_heli"
    bl_label = "Objeto Teste" # Tem que ter nome diferente
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "teste"
    
    def execute(self, context):
        TomoHeliDef(self, context)
        return {'FINISHED'}

#CONEBEAM
    
def TomoConeDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.context.scene.interesse_ossos = "585"
    bpy.context.scene.interesse_mole = "-300"
    bpy.context.scene.interesse_dentes = "1195"

class TomoCone(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tomo_cone"
    bl_label = "Objeto Teste" # Tem que ter nome diferente
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "teste"
    
    def execute(self, context):
        TomoConeDef(self, context)
        return {'FINISHED'}


# ROTACIONA/FLIP Z

def rotacionaZDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.transform.rotate(value=3.14159, axis=(0, 0, 1))

class rotacionaZ(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.rotaciona_z"
    bl_label = "Rotaciona "
    
    def execute(self, context):
        rotacionaZDef(self, context)
        return {'FINISHED'}

#------------------------------------

# LINHA BASE

def LinhaBaseDef(self, context):

    verts = [Vector((0, 0, 125)),
             Vector((0, 0, -125)),
            ]

    edges = [[0,1]]
    
    faces = []


    mesh = bpy.data.meshes.new(name="LinhaBase")
    mesh.from_pydata(verts, edges, faces)
    object_data_add(context, mesh, operator=self)

class LinhaBase(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_linhabase"
    bl_label = "Add Linha Base"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        LinhaBaseDef(self, context)

        return {'FINISHED'}

def add_object_button(self, context):
    self.layout.operator(
        RhinLinhaBase.bl_idname,
        text="LinhaBase",
        icon='VIEW3D')

class BooleanCortes(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "mesh.boolean_cortes"
    bl_label = "Boolean Cortes"
    
    def execute(self, context):
        BooleanCortesDef(self, context)
        return {'FINISHED'}


class ImportaArmature(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.importa_armature"
    bl_label = "Importa estrutura de bones"
    
    def execute(self, context):
        ImportaArmatureDef(self, context)
        return {'FINISHED'}

# -----------------------------------

def CriaEsperssuraDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    bpy.ops.object.modifier_add(type='SOLIDIFY') 
    bpy.context.object.modifiers["Solidify"].thickness = 0.3
    bpy.context.object.modifiers["Solidify"].offset = 0
   

# ANIMA LOCAL E ROTAÇÃO

def AnimaLocRotDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene
    bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')

class AnimaLocRot(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "anim.animalocrot"
    bl_label = "Anima Localização e Rotação"
    
    def execute(self, context):
        AnimaLocRotDef(self, context)
        return {'FINISHED'}

#-------------------------------------


class AlinhaRosto(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.alinha_rosto"
    bl_label = "Prepara Impressao"
    
    def execute(self, context):
        AlinhaRostoDef(self, context)
        return {'FINISHED'}

class MedidaReal(bpy.types.Panel):
    
    bl_idname = "ActiveObject"
    bl_label = "Object Info ..."
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context) :
        col = self.layout.column(align = True)
        col.prop(context.scene, "medida_real")        

class AlinhaRosto2(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.alinha_rosto2"
    bl_label = "Prepara Impressao"
    
    def execute(self, context):
        AlinhaRostoDef2(self, context)
        return {'FINISHED'}        


def PreparaImpressaoDef(self, context):
    
    context = bpy.context
    obj = context.active_object

    bpy.ops.object.modifier_add(type='REMESH') 
    bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
    bpy.context.object.modifiers["Remesh"].octree_depth = 8

def CriaMentoDef(self, context):

    verts = [Vector((-34, 22.5, 0)),
             Vector((34, 22.5, 0)),
             Vector((34, -22.5, 0)),
             Vector((-34, -22.5, 0)),
            ]

    edges = []
    faces = [[0, 1, 2, 3]]

    mesh = bpy.data.meshes.new(name="Mento")
    mesh.from_pydata(verts, edges, faces)
    object_data_add(context, mesh, operator=self)

    bpy.ops.object.modifier_add(type='SOLIDIFY') 
    bpy.context.object.modifiers["Solidify"].thickness = 0.3
    bpy.context.object.modifiers["Solidify"].offset = 0


def CriaMaxilaDef(self, context):

    verts = [Vector((-34, 30, 0)),
             Vector((-34, -30, 0)),
             Vector((-4, -30, 10)),
             Vector((-4, 30, 10)),
             Vector((4, 30, 10)),
             Vector((4, -30, 10)),
             Vector((34, -30, 0)),
             Vector((34, 30, 0)),
            ]

    edges = []
    faces = [[0, 1, 2, 3],[4, 5, 6, 7]]

    mesh = bpy.data.meshes.new(name="Maxila")
    mesh.from_pydata(verts, edges, faces)
    object_data_add(context, mesh, operator=self)

    bpy.ops.object.modifier_add(type='SOLIDIFY') 
    bpy.context.object.modifiers["Solidify"].thickness = 0.3
    bpy.context.object.modifiers["Solidify"].offset = 0

# MENSAGENS DE ERRO

def ERROarmatureDef(self, context):
    self.layout.label("Você não configurou a Armature!")

def ERROtipoDef(self, context):
    self.layout.label("Você não selecionou o objeto correto!")

def ERROruntimeDef(self, context):
    self.layout.label("Você não selecionou nenhum objeto!")

def ERROcmDef(self, context):
    self.layout.label("Você não configurou o Ramo da Mandíbula!")
    
def ERROruntimePontosDef(self, context):
    self.layout.label("Você não selecionou os três pontos!")
    
def ERROruntimeCorteDef(self, context):
    self.layout.label("Você não selecionou o objeto a ser cortado!")

# CRIA CIRCULO DE CORTE

class CriaCirculoCorte(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_circulo_corte"
    bl_label = "Cria Circulo de Corte"

    def execute(self, context):
        CriaCirculoCorteDef(self, context)
        return {'FINISHED'}


# CORTA FACE

class CortaFace(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.corta_face"
    bl_label = "Corta Face"
    
    def execute(self, context):
        CortaFaceDef(self, context)
        return {'FINISHED'}

# CRIA CIRCULO DE CORTE ARCADA

class CriaCirculoCorteArc(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_circulo_corte_arc"
    bl_label = "Cria Circulo de Corte"

    def execute(self, context):
        CriaCirculoCorteArcDef(self, context)
        return {'FINISHED'}

# CORTA ARCADA DENTRO

class CortaArcada(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.corta_arcada"
    bl_label = "Corta Arcada"
    
    def execute(self, context):
        CortaArcadaDef(self, context)
        return {'FINISHED'}

# CORTA OSSOS DENTRO

class CortaOssos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.corta_ossos"
    bl_label = "Corta ossos"
    
    def execute(self, context):
        CortaOssosDef(self, context)
        return {'FINISHED'}

# SEGMENTA DESENHO

class SegmentaDesenho(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.segmenta_desenho"
    bl_label = "Segmenta Desenho"
    
    def execute(self, context):
        SegmentaDesenhoDef(self, context)
        return {'FINISHED'}

# FECHA BURACOS

class FechaBuracos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.fecha_buracos"
    bl_label = "Fecha Buracos"
    
    def execute(self, context):
        FechaBuracosDef(self, context)
        return {'FINISHED'}

# CRIA ESPESSURA

class CriaEspessura(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_espessura"
    bl_label = "Cria Espessura"
    
    def execute(self, context):
        CriaEsperssuraDef(self, context)
        return {'FINISHED'}

class PreparaImpressao(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.prepara_impressao"
    bl_label = "Prepara Impressao"
    
    def execute(self, context):
        PreparaImpressaoDef(self, context)
        return {'FINISHED'}

class CriaMento(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_mento"
    bl_label = "Add Mento"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        CriaMentoDef(self, context)

        return {'FINISHED'}

def add_object_button(self, context):
    self.layout.operator(
        CriaMento.bl_idname,
        text="Mento",
        icon='VIEW3D')

def CriaRamoDef(self, context):

    verts = [Vector((0, -22.5, 29.5)),
             Vector((0, 22.5, 29.5)),
             Vector((0, 22.5, -29.5)),
             Vector((0, -22.5, -29.5)),
            ]

    edges = []
    faces = [[0, 1, 2, 3]]

    mesh = bpy.data.meshes.new(name="Ramo")
    mesh.from_pydata(verts, edges, faces)
    object_data_add(context, mesh, operator=self)

    bpy.ops.object.modifier_add(type='SOLIDIFY') 
    bpy.context.object.modifiers["Solidify"].thickness = 0.3
    bpy.context.object.modifiers["Solidify"].offset = 0


class CriaRamo(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_ramo"
    bl_label = "Add Ramo"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        CriaRamoDef(self, context)

        return {'FINISHED'}


def add_object_button(self, context):
    self.layout.operator(
        CriaRamo.bl_idname,
        text="Ramo",
        icon='VIEW3D')


class CriaMaxila(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_maxila"
    bl_label = "Add Maxila"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        CriaMaxilaDef(self, context)

        return {'FINISHED'}


def add_object_button(self, context):
    self.layout.operator(
        CriaMaxila.bl_idname,
        text="Maxila",
        icon='VIEW3D')

class ConfiguraMento(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_mento"
    bl_label = "Configura Mento"
    
    def execute(self, context):
        ConfiguraMentoDef(self, context)
        return {'FINISHED'}


class ConfiguraCorpoMand(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_corpo_mand"
    bl_label = "Configura Mento"
    
    def execute(self, context):
        ConfiguraCorpoMandDef(self, context)
        return {'FINISHED'}

class ConfiguraRamoDir(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_ramo_dir"
    bl_label = "Configura Ramo Direito"
    
    def execute(self, context):
        ConfiguraRamoDirDef(self, context)
        return {'FINISHED'}

class ConfiguraRamoEsq(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_ramo_esq"
    bl_label = "Configura Ramo Esquerdo"
    
    def execute(self, context):
        ConfiguraRamoEsqDef(self, context)
        return {'FINISHED'}

class ConfiguraMaxila(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_maxila"
    bl_label = "Configura Maxila"
    
    def execute(self, context):
        ConfiguraMaxilaDef(self, context)
        return {'FINISHED'}

class ConfiguraCabeca(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_cabeca"
    bl_label = "Configura Cabeça"
    
    def execute(self, context):
        ConfiguraCabecaDef(self, context)
        return {'FINISHED'}

class AreasInfluencia(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.areas_influencia"
    bl_label = "Áreas de Influência - Dinâmica de Tecidos Moles"
    
    def execute(self, context):
        AreasInfluenciaDef(self, context)
        return {'FINISHED'}

class CriaAreasDeformacao(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_areas_deformacao"
    bl_label = "Cria Areas Deformação"
    
    def execute(self, context):
        CriaAreasDeformacaoDef(self, context)
        return {'FINISHED'}

class GeraModelosTomo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_modelos_tomo"
    bl_label = "Prepara Impressao"
    
    def execute(self, context):
        GeraModelosTomoDef(self, context)
        return {'FINISHED'}

class GeraModeloFoto(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_modelo_foto"
    bl_label = "Gera Modelos Foto"
    
    def execute(self, context):
        GeraModeloFotoDef(self, context)
        return {'FINISHED'}

class GeraModeloFotoSMVS(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_modelo_foto_smvs"
    bl_label = "Gera Modelos Foto"
    
    def execute(self, context):
        GeraModeloFotoSMVSDef(self, context)
        return {'FINISHED'}

class DisplaceSMVS(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.displace_smvs"
    bl_label = "Displace SMVS"
    
    def execute(self, context):
        DisplaceSMVSDef(self, context)
        return {'FINISHED'}

class ConfiguraDinamicaMole(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_dinamica_mole"
    bl_label = "Configura Dinâmica do Mole"
    
    def execute(self, context):
        ConfiguraDinamicaMoleDef(self, context)
        return {'FINISHED'}

# IMPORTA SPLINT COM ARMATURE

      
class ImportaSplint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.importa_splint"
    bl_label = "Importa Splint com Armature"
    
    def execute(self, context):
        ImportaSplintDef(self, context)
        return {'FINISHED'}


# CRIA EMPTIES INTERMEDIÁRIOS

    
class ConfSplint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.conf_splint"
    bl_label = "Boolean Splint"
    
    def execute(self, context):
        ConfSplintDef(self, context)
        return {'FINISHED'}

# FERRAMENTAS DE MEDIDAS

class MedidasVerDentes(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.medver"
    bl_label = "Medidas Verticais"
    
    def execute(self, context):
        MedidasVerDentesDef(self, context)
        return {'FINISHED'}


class ChangeSolidXRay(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.change_solid_xray"
    bl_label = "Change Solid/X-Ray"
    
    def execute(self, context):
        ChangeSolidXRayDef(self, context)
        return {'FINISHED'}

class ChangeRenderEngine(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.change_engine_render"
    bl_label = "Change Engine Render"
    
    def execute(self, context):
        ChangeRenderEngineDef(self, context)
        return {'FINISHED'}


class ConfiguraCefalo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_cefalo"
    bl_label = "Configura Cefalometria"
    
    def execute(self, context):
        ConfiguraCefaloDef(self, context)
        return {'FINISHED'}  


# IMPORTA TOMO

class CapturaLocal(PropertyGroup):

    path = StringProperty(
        name="",
        description="Path to Directory",
        default="",
        maxlen=1024,
        subtype='DIR_PATH')

#ATUALIZA VERSAO
class PainelAtualiza(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Upgrade OrtogOnBlender"
    bl_idname = "painel_atualiza"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        scn = context.scene
        obj = context.object 
		
        row = layout.row()
        row.label(text="VERSION: 20181231a")

        row = layout.row()
        row.operator("object.atualiza_script", text="UPGRADE ORTOG!", icon="RECOVER_LAST")
		
        if platform.system() == "Windows":
            row = layout.row()
            row.operator("wm.console_toggle", text="Open Terminal?", icon="CONSOLE")
		
# IMPORTA TOMO
class ImportaTomo(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Import CT-Scan"
    bl_idname = "importa_tomo"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        scn = context.scene
        obj = context.object 

        row = layout.row()
        row.label(text="CT-Scan Preparing:")

        col = layout.column(align=True)
        col.prop(scn.my_tool, "path", text="")

        if platform.system() == "Windows":
            row = layout.row()
            row.operator("wm.console_toggle", text="Open Terminal?", icon="CONSOLE")
		
        row = layout.row()
        row.operator("object.ajusta_tomo", text="Organize", icon="NODETREE")


        row = layout.row()
        row.label(text="CT-Scan Fix:")

        if platform.system() == "Linux":
            col = layout.column(align=True)
            col.prop(scn.my_tool, "path", text="")

            row = layout.row()
            row.operator("object.corrige_dicom", text="Fix it!", icon="FILE_TICK")


        row = layout.row()
        row.label(text="CT-Scan Reconstruction:")

        col = layout.column(align=True)
        col.prop(scn.my_tool, "path", text="")

        row = layout.row()
        row.operator("object.tomo_heli", text="CT-Scan")
        row.operator("object.tomo_cone", text="CBCT")

        col = self.layout.column(align = True)
        col.prop(context.scene, "interesse_ossos")

        col = self.layout.column(align = True)
        col.prop(context.scene, "interesse_mole")

        col = self.layout.column(align = True)
        col.prop(context.scene, "interesse_dentes")

        if platform.system() == "Windows":
            row = layout.row()
            row.operator("wm.console_toggle", text="Open Terminal?", icon="CONSOLE")

        row = layout.row()
        row.operator("object.gera_modelos_tomo", text="Convert DICOM to 3D", icon="SNAP_FACE")

      
        row = layout.row()
        row.label(text="Graphic References:")

        row = layout.row()
        linha=row.operator("mesh.add_linhabase", text="Vertical Center Line", icon="PAUSE")
        linha.location=(0,-200,0)

        row = layout.row()
        linha=row.operator("mesh.add_linhabase", text="Horizontal Center Line", icon="ZOOMOUT")
        linha.location=(0,-200,0)
        linha.rotation=(0,1.5708,0)
        
        row = layout.row()
        linha=row.operator("mesh.add_linhabase", text="Horizontal Side Line", icon="ZOOMOUT")
        linha.location=(200,30,0)
        linha.rotation=(1.5708,0,0)

        row = layout.row()
        row.label(text="Segmentation:")

        row = layout.row()
        
        row = layout.row()
        row.operator("gpencil.draw", icon='LINE_DATA', text="Draw Line").mode = 'DRAW_POLY'

        row = layout.row()
        linha=row.operator("object.segmenta_desenho", text="Cut Draw!", icon="FCURVE")

        row = layout.row()

        row = layout.row()
        linha=row.operator("mesh.select_more", text="Sel. More", icon="ZOOMIN")
        
        linha=row.operator("mesh.select_less", text="Sel. Less", icon="ZOOMOUT")     
  
        row = layout.row()
        row.label(text="Arch Teeth Import:")

        col = layout.column(align=True)
        col.prop(scn.my_tool, "path", text="")
 
        row = layout.row()
        row.operator("object.gera_modelos_tomo_arc", text="Archs Generator", icon="SNAP_FACE")

        row = layout.row()
        row.operator("import_mesh.stl", text="Import STL", icon="IMPORT")

        row = layout.row()
        row.label(text="Archs Lines")
        
        row = layout.row()
        row.label(text="ALIGN ON MISC!")
    #    row.operator("object.align_picked_points", text="Align by Points", icon="PARTICLE_TIP")

    #    row = layout.row()
    #    row.operator("object.align_icp", text="Align by ICP", icon="PARTICLE_PATH")

        row = layout.row()
        row.label(text="Archs/Skull Targeting:")

        row = layout.row()
        row.operator("object.cria_circulo_corte_arc", text="Create Cut Ellipse", icon="META_ELLIPSOID")

        row = layout.row()
        row.operator("object.corta_arcada", text="Delet Out", icon="META_PLANE")

        row = layout.row()
        row.operator("object.corta_ossos", text="Delet In", icon="MOD_WIREFRAME")
     
        row = layout.row()
        circle=row.operator("object.join", text="Joint Arch + Bone", icon="GROUP")

        row = layout.row()        
        row.label(text="Mesh Adjustments:")

        row = layout.row()
        circle=row.operator("object.fecha_buracos", text="Close Holes", icon="MOD_MESHDEFORM")

        row = layout.row()
        circle=row.operator("object.convert", text="Apply!", icon="SAVE_AS") .target='MESH'

'''      
# ZOOM
class ZoomCena(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Zoom Cena"
    bl_idname = "zoom_cena"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object


        row = layout.row()
        row.operator("view3d.viewnumpad", text="Frente").type='FRONT'
        row.operator("view3d.viewnumpad", text="Atrás").type='BACK'
        
        row = layout.row()
        row.operator("view3d.viewnumpad", text="Direita").type='RIGHT'
        row.operator("view3d.viewnumpad", text="Esquerda").type='LEFT'
        
        row = layout.row()
        row.operator("view3d.viewnumpad", text="Cima").type='TOP'
        row.operator("view3d.viewnumpad", text="Baixo").type='BOTTOM'
        
        row = layout.row()
        row.operator("opr.pan_down_view1", text="Pan", icon="TRIA_UP")
        row.operator("opr.pan_up_view1", text="Pan", icon="TRIA_DOWN")
        row.operator("opr.pan_right_view1", text="Pan", icon="TRIA_LEFT")
        row.operator("opr.pan_left_view1", text="Pan", icon="TRIA_RIGHT")

        row = layout.row()
        row.operator("opr.orbit_down_view1", text="Orb", icon="FILE_PARENT")
        row.operator("opr.orbit_up_view1", text="Orb", icon="FILE_REFRESH")
        row.operator("opr.orbit_right_view1", text="Orb", icon="LOOP_BACK")
        row.operator("opr.orbit_left_view1", text="Orb", icon="LOOP_FORWARDS")

        
        row = layout.row()
        row.operator("view3d.view_persportho", text="Persp/Orto")
        row.operator("view3d.view_all", text="Centraliza Zoom", icon="VIEWZOOM").center=False    

'''

# FOTOGRAMETRIA

class CriaFotogrametria(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Create Photogrammetry"
    bl_idname = "cria_fotogrametria"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"


    def draw(self, context):
        layout = self.layout
        scn = context.scene
        obj = context.object 

        row = layout.row()
        row.operator("object.abre_tmp", text="Open Temporary Dir?", icon="FILESEL")

        col = layout.column(align=True)
        col.prop(scn.my_tool, "path", text="")

        if platform.system() == "Windows":
            row = layout.row()
            row.operator("wm.console_toggle", text="Open Terminal?", icon="CONSOLE")

        row = layout.row()
        row.operator("object.gera_modelo_foto", text="Start Photogrammetry!", icon="IMAGE_DATA")

        row = layout.row()
        row = layout.row()

        row = layout.row()
        row.operator("object.importa_cameras", text="OpenMVG+MVS with Cameras", icon="CAMERA_DATA")

        row = layout.row()
        row = layout.row()

        row = layout.row()
        row.operator("object.gera_modelo_foto_smvs", text="SMVS+Meshlab", icon="IMAGE_DATA")

        row = layout.row()
        row = layout.row()

        if platform.system() == "Linux":
            row = layout.row()
            row.operator("object.fotogrametria_composta", text="Compose Photogrammetry", icon="FULLSCREEN_EXIT")

        row = layout.row()
        row = layout.row()

        row = layout.row()
        row.operator("object.displace_smvs", text="Fix Model and UVMap!", icon="FILE_TICK")
        
#       print (scn.my_tool.path)
 

      
#IMPORTA OBJ
   
class OOB_import_obj(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Import/Cut Photogrammetry"
    bl_idname = "import_obj"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("import_scene.obj", text="Import OBJ", icon="MOD_MASK")
        #ORIGINAL bpy.ops.import_mesh.stl()
        
        row = layout.row()
        row.operator("object.cria_circulo_corte", text="Cutting circle", icon="MESH_CIRCLE")
#        circle=row.operator("mesh.primitive_circle_add", text="Círculo de Corte", icon="MESH_CIRCLE")
#        circle.radius=200
#        circle.vertices=100
#        circle.location=(85,-185,0)
#        circle.rotation=(0,1.5708,0)

        row = layout.row()
        knife=row.operator("object.corta_face", text="Cut!", icon="META_PLANE")
        
        
        
            
# IMPORTA CEFALOMETRIA

class ImportaCefalometria(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Import Cephalometry"
    bl_idname = "Importa_Cefalometria"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("import_image.to_plane", text="Import Image", icon="FILE_IMAGE")

#ALINHA FACES

class AlinhaFaces(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Align Face"
    bl_idname = "alinha_faces"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()        
        row.label(text="Align and Resize:")
        layout.operator("object.alinha_rosto", text="1 - Align with the Camera", icon="MANIPUL")
        col = self.layout.column(align = True)
        col.prop(context.scene, "medida_real")  
        layout.operator("object.alinha_rosto2", text="3 - Align and Resize", icon="LAMP_POINT")
        
        row = layout.row()
        row.operator("object.rotaciona_z", text="Flip Z", icon="FORCE_MAGNETIC")

        row = layout.row()
        row.label(text="Align by Points:")

        row = layout.row()
        row.label(text="ALIGN ON MISC!")
#        row.operator("object.align_picked_points", text="Align by Points", icon="PARTICLE_TIP")

#        row = layout.row()
#        row.operator("object.align_icp", text="Align by ICP", icon="PARTICLE_PATH")
    


# OSTEOTOMIA

class Osteotomia(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Osteotomy"
    bl_idname = "Object_Name"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        
        obj = context.object
       
        row = layout.row()
        circle=row.operator("mesh.add_mento", text="Chin Plane", icon="TRIA_DOWN")
        circle.location=(0,-35,-81)
        
        row = layout.row()
        circle=row.operator("mesh.add_ramo", text="Left Ramus Plane", icon="TRIA_RIGHT")
        circle.location=(36, -4, -45)
        
        row = layout.row()
        circle=row.operator("mesh.add_ramo", text="Right Ramus Plane", icon="TRIA_LEFT")
        circle.location=(-36, -4, -45)
        
        row = layout.row()
        circle=row.operator("mesh.add_maxila", text="Maxilla Plane", icon="TRIA_UP")
        circle.location=(0, -45, -31)
 
        row = layout.row()
        circle=row.operator("object.join", text="Joint All", icon="GROUP")
    
        
        row = layout.row()
        circle=row.operator("object.cria_espessura", text="Create Thickness", icon="MOD_SOLIDIFY")
               
        row = layout.row()
        circle=row.operator("view3d.cork_mesh_slicer", text="Cut Boolean", icon="MOD_BOOLEAN")
        circle.method='DIFF'
        
        # Não é necessário estar em Object Mode
        row = layout.row()
        circle=row.operator("mesh.separate", text="Separate Osteotomy", icon="GROUP_VERTEX")
        circle.type='LOOSE'
        
        row = layout.row()
        circle=row.operator("object.importa_armature", text="Setup Armature", icon="GROUP_BONE")        

        row = layout.row()        
        row.label(text="Setup Pieces:")

        row = layout.row()
        row.operator("object.configura_cabeca", text="Setup Head")

        row = layout.row()
        row.operator("object.configura_maxila", text="Setup Maxilla")

        row = layout.row()
        row.operator("object.configura_ramo_dir", text="Setup Right Ramus")

        row = layout.row()
        row.operator("object.configura_ramo_esq", text="Setup Left Ramus")

        row = layout.row()
        row.operator("object.configura_corpo_mand", text="Setup Mandible Body")

        row = layout.row()
        row.operator("object.configura_mento", text="Setup Chin")

        
class DinamicaMole(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Soft Tissue Dynamics"
    bl_idname = "Dinamica_Mole"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        
        obj = context.object
              

        row = layout.row()
        circle=row.operator("object.configura_dinamica_mole", text="Setup Soft Tissue Dynamics", icon="STYLUS_PRESSURE")
       
        row = layout.row()
        circle=row.operator("view3d.clip_border", text="Clipping Border", icon="UV_FACESEL")

# PONTOS ANATÔMICOS

class PontosAnatomicos(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Anatomical Points"
    bl_idname = "Pontos_Anatomicos"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        
        obj = context.object

        row = layout.row()        
        row.label(text="Maxilla:")

        row = layout.row()
        row.operator("object.emp11", text="Tooth 8 (11)", icon="X")

        row = layout.row()
        row.operator("object.emp21", text="Tooth 9 (21)", icon="X")
        
        row = layout.row()
        row.operator("object.emp13", text="Tooth 6 (13)", icon="X")       

        row = layout.row()
        row.operator("object.emp23", text="Tooth 11 (23)", icon="X") 
        
        row = layout.row()
        row.operator("object.emp16", text="Tooth 3 (16)", icon="X")
        
        row = layout.row()
        row.operator("object.emp26", text="Tooth 14 (26)", icon="X")

        row = layout.row()
        row.operator("object.palatine", text="Palatine", icon="X")

        row = layout.row()
        row.operator("object.apoint", text="A Point (Subspinale)", icon="X")

#        row = layout.row()
#        row.operator("object.upperincisor", text="A Point (Subspinale)", icon="X")

        row = layout.row()
        row.operator("object.nasalspine", text="Nasal Spine", icon="X")

        row = layout.row()
        row.operator("object.pterygoidl", text="Pterygoid Process (L)", icon="X")

        row = layout.row()
        row.operator("object.pterygoidr", text="Pterygoid Process (R)", icon="X")

        row = layout.row()        
        row.label(text="Mandible Body:")

        row = layout.row()
        row.operator("object.emp31", text="Tooth 24 (31)", icon="X")
        
        row = layout.row()
        row.operator("object.emp41", text="Tooth 25 (41)", icon="X")
        
        row = layout.row()
        row.operator("object.emp33", text="Tooth 22 (33)", icon="X")

        row = layout.row()
        row.operator("object.emp43", text="Tooth 27 (43)", icon="X")
        
        row = layout.row()
        row.operator("object.emp36", text="Tooth 19 (36)", icon="X")
        
        row = layout.row()
        row.operator("object.emp46", text="Tooth 30 (46)", icon="X")

        row = layout.row()
        row.operator("object.bpoint", text="B Point", icon="X")

        row = layout.row()
        row.label(text="Chin:")

        row = layout.row()
        row.operator("object.pogonion", text="Pogonion or Up", icon="X")

        row = layout.row()
        row.operator("object.menton", text="Menton", icon="X")

        row = layout.row()
        row.operator("object.mentonl", text="Menton Left", icon="X")

        row = layout.row()
        row.operator("object.mentonr", text="Menton Right", icon="X")

        row = layout.row()
        row.label(text="Soft Tissue:")

        row = layout.row()
        row.operator("object.lspoint", text="Ls Point (Edit)", icon="X")

        row = layout.row()
        row.operator("object.pgpoint", text="Pg Point (Edit)", icon="X")

        row = layout.row()
        row.label(text="Others:")

        row = layout.row()
        row.operator("object.nasion", text="Nasion", icon="X")

        row = layout.row()
        row.operator("object.eyer", text="Orbit Right", icon="X")

        row = layout.row()
        row.operator("object.eyel", text="Orbit Left", icon="X")

        row = layout.row()
        row.operator("object.meatusr", text="Meatus Right", icon="X")

        row = layout.row()
        row.operator("object.meatusl", text="Meatus Left", icon="X")

        row = layout.row()
        row.operator("object.sella", text="Sella Turcica", icon="X")

        row = layout.row()
        row.operator("object.gonionr", text="Gonion Right", icon="X")

        row = layout.row()
        row.operator("object.gonionl", text="Gonion Left", icon="X")

        row = layout.row()
        row.label(text="Cephalometry:")

        row = layout.row()
        row.operator("object.configura_cefalo", text="Setup Cephalometry", icon="SETTINGS")

        row = layout.row()
        row.operator("object.cefalo_interativa", text="Interactive Cephalometry", icon="LAMP_POINT")
        

        row = layout.row()
        row.label(text="Render:")

        row = layout.row()
        row.operator("object.change_solid_xray", text="Change Solid/X-Ray", icon="MOD_WIREFRAME")

        row = layout.row()
        row.operator("object.change_engine_render", text="Change Render Engine", icon="SCENE")
        
        row = layout.row()
        row.label(text="Viewpoint Cameras:")

        row = layout.row()
        row.operator("object.camera_xray_view", text="Cephalometry View", icon="RESTRICT_VIEW_OFF")


        row = layout.row()
        row.operator("object.camera_panoramic", text="Panoramic View", icon="RESTRICT_VIEW_OFF") 


# FERRAMENTAS DE MEDIDAS

class FerramentasRefMedidas(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Measuring Tools"
    bl_idname = "feramentas_medidas"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        scn = context.scene
        obj = context.object 
        
        row = layout.row()
        row.label(text="Vertical Measurements:")

        row = layout.row()
        row.operator("object.medver", text="Create Vertical Measurements", icon="LAMP_SUN")

        row = layout.row()
        row.operator("measureit.runopenglbutton", text="Show/Hide Measurements", icon="GHOST_ENABLED")

# ANIMAÇÃO

class CinematicaPanel(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Kinematic"
    bl_idname = "cinematica"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        
        obj = context.object

        row = layout.row()
        row.label(text="Controllers:")

        row = layout.row()
        row.operator("screen.frame_jump", text="Start", icon="REW").end=False
        row.operator("screen.animation_play", text="", icon="PLAY_REVERSE").reverse=True
        row.operator("anim.animalocrot", text="", icon="CLIP")
        row.operator("screen.animation_play", text="", icon="PLAY")
        row.operator("screen.frame_jump", text="End", icon="FF").end=True

        row = layout.row()
        row.label(text="Capturing:")

 #       row = layout.row()
 #       row.operator("object.captura_ini_todos", text="Start Cap", icon="TRIA_LEFT_BAR")
 #       row.operator("object.captura_fin_todos", text="End Cap", icon="TRIA_RIGHT_BAR")

        row = layout.row()
        row.operator("object.gera_deslocamento_todos", text="Generate Data Action", icon="FULLSCREEN_ENTER")

# SPLINT

class CriaSplintPanel(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Splint Creation"
    bl_idname = "Cria_Splint"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        
        obj = context.object
        
        row = layout.row()
        row.label(text="Automatic Splint Creation:")
    
#        row = layout.row()        
#        row.label(text="Configuração do Splint:") 

        row = layout.row()
        row.operator("object.cria_splint", text="Create Splint", icon="OUTLINER_OB_CURVE")

        row = layout.row()
        row.operator("object.conf_splint", text="Prepare Boolean", icon="RECOVER_AUTO")
        
        row = layout.row()
        circle=row.operator("view3d.cork_mesh_slicer", text="Boolean Cuts", icon="MOD_BOOLEAN")
        circle.method='DIFF'    

#        row = layout.row()
#        circle=row.operator("object.convert", text="Aplica Deformação", icon="FILE_TICK").target='MESH'
    
        row = layout.row()
        row.operator("object.prepara_impressao", text="Prepares 3D Printing", icon="MOD_REMESH")
        
        row = layout.row()
        row.operator("export_mesh.stl", text="Export STL", icon="EXPORT")

# Botões desenhar splint

        row = layout.row()
        row.label(text="Manual Draw Splint:")

        if context.space_data.type == 'VIEW_3D':
                propname = "gpencil_stroke_placement_view3d"
        elif context.space_data.type == 'SEQUENCE_EDITOR':
                propname = "gpencil_stroke_placement_sequencer_preview"
        elif context.space_data.type == 'IMAGE_EDITOR':
                propname = "gpencil_stroke_placement_image_editor"
        else:
                propname = "gpencil_stroke_placement_view2d"

        ts = context.tool_settings

        col = layout.column(align=True)

        col.label(text="Stroke Placement:")

        row = col.row(align=True)
        row.prop_enum(ts, propname, 'VIEW')
        row.prop_enum(ts, propname, 'CURSOR')

        if context.space_data.type == 'VIEW_3D':
            row = col.row(align=True)
            row.prop_enum(ts, propname, 'SURFACE')
            row.prop_enum(ts, propname, 'STROKE')

            row = col.row(align=False)
            row.active = getattr(ts, propname) in {'SURFACE', 'STROKE'}
            row.prop(ts, "use_gpencil_stroke_endpoints")        

# -------------------------------------
        row = layout.row()
        row.label(text="Create Solid:")

        row = layout.row()
        row.operator("object.teste", text="DO SOLID!", icon="SURFACE_NCYLINDER")
        
        row = layout.row()
        row.operator("btool.direct_union", text="Union - ALL", icon="SEQ_SEQUENCER") 
             
        row = layout.row()
        row.operator("gpencil.draw", icon='LINE_DATA', text="Draw Line").mode = 'DRAW_POLY'

        row = layout.row()
        row.operator("object.acabamento", icon='MOD_MULTIRES', text="Cut Line!")

        row = layout.row()
        row.operator("object.fecha_buraco", icon='FACESEL', text="Fill Hole")

# Botões boolean
        row = layout.row()
        row.label(text="Boolean Opetations:")
        col = layout.column()
        col.operator("view3d.cork_mesh_slicer", text="Union").method="UNION"
        col.operator("view3d.cork_mesh_slicer", text="Difference").method="DIFF"
        col.operator("view3d.cork_mesh_slicer", text="Intersect").method="INTERSECT"
        col.operator("view3d.cork_mesh_slicer", text="XOR").method="XOR"
        col.operator("view3d.cork_mesh_slicer", text="Resolve").method="RESOLVE"
        col.separator()
        col.operator("view3d.cork_mesh_slicer", text="", icon='QUESTION', emboss=False).show_help = True

class FerrZoom(bpy.types.Header):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Criação do Splint"
    bl_idname = "Cria_Splint"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row = layout.row()
        row.operator("view3d.viewnumpad", text="Front").type='FRONT'
        row.operator("view3d.viewnumpad", text="Back").type='BACK'
        row.operator("view3d.viewnumpad", text="Right").type='RIGHT'
        row.operator("view3d.viewnumpad", text="Left").type='LEFT'
        row.operator("view3d.viewnumpad", text="Top").type='TOP'
        row.operator("view3d.viewnumpad", text="Bottom").type='BOTTOM'
        
        row = layout.row()
        row.operator("opr.pan_down_view1", text="", icon="TRIA_UP")
        row.operator("opr.pan_up_view1", text="", icon="TRIA_DOWN")
        row.operator("opr.pan_right_view1", text="", icon="TRIA_LEFT")
        row.operator("opr.pan_left_view1", text="", icon="TRIA_RIGHT")

        row = layout.row()
        row.operator("opr.orbit_down_view1", text="", icon="FILE_PARENT")
        row.operator("opr.orbit_up_view1", text="", icon="FILE_REFRESH")
        row.operator("opr.orbit_right_view1", text="", icon="LOOP_BACK")
        row.operator("opr.orbit_left_view1", text="", icon="LOOP_FORWARDS")

        
        row = layout.row()
        row.operator("view3d.view_persportho", text="Persp/Ortho")
        row.operator("view3d.view_all", text="Center Zoom", icon="VIEWZOOM").center=False    


# Cefalometria Medidas

class CefaloTeste(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cefalodel"
    bl_label = "Objeto Teste" # Tem que ter nome diferente
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ortog"
    
    def execute(self, context):
        testeDef(self, context)
        return {'FINISHED'}

class CefaloCalculaTudo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cefalo_calc_tudo"
    bl_label = "Cefalo Calcula Tudo" # Tem que ter nome diferente
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ortog"
    
    def execute(self, context):
        CefaloCalculaTudoDef(self, context)
        return {'FINISHED'}


class CefaloTeste1(bpy.types.Panel):
    """Apenas um teste 1"""
    bl_label = "Cephalometry"
    bl_idname = "cefalo_but"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

#        row = layout.row()
#        row.operator("mesh.primitive_monkey_add", text="Add monkey", icon="MESH_MONKEY")

#        row = layout.row()
#        row.operator("object.teste", text="Modificadores", icon="MOD_SUBSURF")

        row = layout.row()
        row.operator("object.cefalo_calc_tudo", text="Calculate All!", icon="SCRIPTWIN")

#        col = self.layout.column(align = True)
        row = layout.row(align = True)
#        split = row.split(percentage=0.5)
        row.prop(context.scene, "angulo_SNA")
        row.label(text="80º - 84º")


        row = layout.row(align = True)
        row.prop(context.scene, "angulo_SNB")
        row.label(text="78º - 82º")  

        row = layout.row(align = True)
        row.prop(context.scene, "angulo_ANB")
        row.label(text="0º - 4º")

        row = layout.row(align = True)
        row.prop(context.scene, "angulo_Y_Cresc")
        row.label(text="65º - 69º") 

        row = layout.row(align = True)
        row.prop(context.scene, "angulo_SNPlO")
        row.label(text="12º - 16º")

        row = layout.row(align = True)
        row.prop(context.scene, "angulo_FMA")
        row.label(text="23º - 27º")

        row = layout.row(align = True)
        row.prop(context.scene, "angulo_FMIA")
        row.label(text="66º - 70º")

        row = layout.row(align = True)
        row.prop(context.scene, "angulo_IMPA")
        row.label(text="85º - 89º")

        row = layout.row(align = True)
        row.prop(context.scene, "angulo_NS")
        row.label(text="101º - 105º")


def register():
    bpy.utils.register_class(DesenhaGuia)
    bpy.utils.register_class(Acabamento)
    bpy.utils.register_class(FechaBuraco)
    bpy.utils.register_class(FotogrametriaComposta)
    bpy.utils.register_class(ortogPreferences)
#    bpy.utils.register_class(ortogPreferences2)
    bpy.utils.register_class(ImportaCameras)
    bpy.utils.register_class(AtualizaScript)
    bpy.utils.register_class(CorrigeDicom)
#    bpy.utils.register_class(capturaINItodos)
#    bpy.utils.register_class(capturaFINtodos)
    bpy.utils.register_class(geraDeslocamentoTODOS)
    bpy.utils.register_class(AbreTMP)
    bpy.utils.register_class(AjustaTomo)
    bpy.utils.register_class(CriaMento)
    bpy.types.INFO_MT_mesh_add.append(add_object_button)
    bpy.utils.register_class(CortaFace)
    bpy.utils.register_class(AlinhaRosto)
    bpy.utils.register_class(CriaCirculoCorte)
#    bpy.utils.register_class(MedidaReal)
    bpy.types.Scene.medida_real = bpy.props.StringProperty \
      (
        name = "2 - Actual Measure",
        description = "Medida real distância cantal",
        default = "0"
      )
    bpy.utils.register_class(AlinhaRosto2)
    bpy.utils.register_class(AnimaLocRot)
    bpy.utils.register_class(TomoHeli)
    bpy.utils.register_class(TomoCone)
    bpy.utils.register_class(rotacionaZ)
    bpy.utils.register_class(GeraModelosTomoArc)
    bpy.utils.register_class(CameraXRayView)
    bpy.utils.register_class(CameraPanoramic)
    bpy.utils.register_class(LinhaBase)
    bpy.utils.register_class(ImportaArmature)
    bpy.utils.register_class(CriaCirculoCorteArc)
    bpy.utils.register_class(CortaArcada)
    bpy.utils.register_class(CortaOssos)
    bpy.utils.register_class(SegmentaDesenho)
    bpy.utils.register_class(FechaBuracos)
    bpy.utils.register_class(CriaEspessura)
    bpy.utils.register_class(PreparaImpressao)
    bpy.utils.register_class(CriaRamo)
    bpy.types.INFO_MT_mesh_add.append(add_object_button)
    bpy.utils.register_class(CriaMaxila)
    bpy.types.INFO_MT_mesh_add.append(add_object_button)
    bpy.utils.register_class(ConfiguraMento)
    bpy.utils.register_class(ConfiguraCorpoMand)
    bpy.utils.register_class(ConfiguraRamoEsq)
    bpy.utils.register_class(ConfiguraRamoDir)
    bpy.utils.register_class(ConfiguraMaxila)
    bpy.utils.register_class(ConfiguraCabeca)
    bpy.utils.register_class(AreasInfluencia)
    bpy.utils.register_class(CriaAreasDeformacao)
    bpy.types.Scene.interesse_ossos = bpy.props.StringProperty \
      (
        name = "Bone Factor",
        description = "Fatos interesse ossos",
        default = "200"
      )
    bpy.types.Scene.interesse_mole = bpy.props.StringProperty \
      (
        name = "Soft Factor",
        description = "Fatos interesse mole",
        default = "-300"
      )
    bpy.types.Scene.interesse_dentes = bpy.props.StringProperty \
      (
        name = "Teeth Factor",
        description = "Fatos interesse dentes",
        default = "1760"
      )
    bpy.utils.register_class(GeraModelosTomo)
    bpy.utils.register_class(GeraModeloFoto)
    bpy.utils.register_class(GeraModeloFotoSMVS)
    bpy.utils.register_class(DisplaceSMVS)
    bpy.utils.register_class(ConfiguraDinamicaMole)
    bpy.utils.register_class(PainelAtualiza)
    bpy.utils.register_class(ImportaTomo)
#    bpy.utils.register_class(ZoomCena)
    bpy.utils.register_class(CriaFotogrametria)
    bpy.utils.register_class(AlinhaFaces)
    bpy.utils.register_class(OOB_import_obj)
    bpy.utils.register_class(ImportaCefalometria)
    bpy.utils.register_class(Osteotomia)
    bpy.utils.register_class(DinamicaMole)
    bpy.utils.register_class(PontosAnatomicos)
    bpy.utils.register_class(FerramentasRefMedidas)
    bpy.utils.register_class(CriaSplint)
    bpy.utils.register_class(MedidasVerDentes)
    bpy.utils.register_class(ChangeSolidXRay)
    bpy.utils.register_class(ChangeRenderEngine)
    bpy.utils.register_class(ConfiguraCefalo)
    bpy.utils.register_class(CapturaLocal)
    bpy.types.Scene.my_tool = PointerProperty(type=CapturaLocal)
    bpy.utils.register_class(ImportaSplint)
    bpy.utils.register_class(EMP11)
    bpy.utils.register_class(EMP21)
    bpy.utils.register_class(EMP13)
    bpy.utils.register_class(EMP23)
    bpy.utils.register_class(EMP16)
    bpy.utils.register_class(EMP26)
    bpy.utils.register_class(EMPUpperIncisor)
    bpy.utils.register_class(EMPPalatine)
    bpy.utils.register_class(EMPNasalSpine)
    bpy.utils.register_class(EMPPterygoidL)
    bpy.utils.register_class(EMPPterygoidR)
    bpy.utils.register_class(EMP31)
    bpy.utils.register_class(EMP41)
    bpy.utils.register_class(EMP33)
    bpy.utils.register_class(EMP43)
    bpy.utils.register_class(EMP36)
    bpy.utils.register_class(EMP46)
    bpy.utils.register_class(EMPBpoint)
    bpy.utils.register_class(EMPMenton)
    bpy.utils.register_class(EMPPogonion)
    bpy.utils.register_class(EMPMentonL)
    bpy.utils.register_class(EMPMentonR)
    bpy.utils.register_class(EMPLSpoint)
    bpy.utils.register_class(EMPPGpoint)
    bpy.utils.register_class(EMPGonionR)
    bpy.utils.register_class(EMPGonionL)
    bpy.utils.register_class(EMPEyeR)
    bpy.utils.register_class(EMPEyeL)
    bpy.utils.register_class(EMPMeatusR)
    bpy.utils.register_class(EMPMeatusL)
    bpy.utils.register_class(EMPNasion)
    bpy.utils.register_class(EMPApoint)
    bpy.utils.register_class(EMPSellaTurcica)
    bpy.utils.register_class(CefaloInterativa)
    bpy.utils.register_class(CinematicaPanel)
    bpy.utils.register_class(CriaSplintPanel)
    bpy.utils.register_class(ConfSplint)
    bpy.utils.register_class(FerrZoom)
    bpy.utils.register_class(CefaloTeste)
    bpy.utils.register_class(CefaloTeste1)
    bpy.types.Scene.angulo_SNA = bpy.props.StringProperty \
      (
        name = "SNA",
        description = "Ângulo SNA",
        default = "NONE"
      )
    bpy.types.Scene.angulo_SNB = bpy.props.StringProperty \
      (
        name = "SNB",
        description = "Ângulo SNB",
        default = "NONE"
      )

    bpy.types.Scene.angulo_ANB = bpy.props.StringProperty \
      (
        name = "ANB",
        description = "Ângulo ANB",
        default = "NONE"
      )
    bpy.types.Scene.angulo_Y_Cresc = bpy.props.StringProperty \
      (
        name = "Y Growing",
        description = "Ângulo Y de Screscimento",
        default = "NONE"
      )
    bpy.types.Scene.angulo_SNPlO = bpy.props.StringProperty \
      (
        name = "SNPlO",
        description = "ANgulo SN Molares",
        default = "NONE"
      )
    bpy.types.Scene.angulo_FMA = bpy.props.StringProperty \
      (
        name = "FMA",
        description = "Ângulo FMA",
        default = "NONE"
      )
    bpy.types.Scene.angulo_FMIA = bpy.props.StringProperty \
      (
        name = "FMIA",
        description = "Ângulo FMA",
        default = "NONE"
      )
    bpy.types.Scene.angulo_IMPA = bpy.props.StringProperty \
      (
        name = "IMPA",
        description = "Ângulo IMPA",
        default = "NONE"
      )
    bpy.types.Scene.angulo_NS = bpy.props.StringProperty \
      (
        name = "1NS",
        description = "Ângulo 1NS",
        default = "NONE"
      )
    bpy.utils.register_class(CefaloCalculaTudo)


def unregister():
    del bpy.types.Scene.medida_real
    bpy.utils.unregister_class(DesenhaGuia)
    bpy.utils.unregister_class(Acabamento)
    bpy.utils.unregister_class(FechaBuraco)
    bpy.utils.unregister_class(FotogrametriaComposta)
    bpy.utils.unregister_class(ImportaCameras)
    bpy.utils.unregister_class(AtualizaScript)
    bpy.utils.unregister_class(CorrigeDicom)
#    bpy.utils.unregister_class(capturaINItodos)
#    bpy.utils.unregister_class(capturaFINtodos)
    bpy.utils.unregister_class(geraDeslocamentoTODOS)
    bpy.utils.unregister_class(AbreTMP)
    bpy.utils.unregister_class(AjustaTomo)
    bpy.utils.unregister_class(ortogPreferences)
#    bpy.utils.unregister_class(ortogPreferences2)
    bpy.utils.unregister_class(CortaFace)
    bpy.utils.unregister_class(AlinhaRosto)
    bpy.utils.unregister_class(CriaCirculoCorte)
#    bpy.utils.register_class(MedidaReal)
    del bpy.types.Scene.medida_real
    bpy.utils.unregister_class(AlinhaRosto2)
    bpy.utils.unregister_class(AnimaLocRot)
    bpy.utils.unregister_class(TomoHeli)
    bpy.utils.unregister_class(TomoCone)
    bpy.utils.unregister_class(rotacionaZ)
    bpy.utils.unregister_class(GeraModelosTomoArc)
    bpy.utils.unregister_class(CameraXRayView)
    bpy.utils.unregister_class(CameraPanoramic)
    bpy.utils.unregister_class(LinhaBase)
    bpy.utils.unregister_class(ImportaArmature)
    bpy.utils.unregister_class(CriaCirculoCorteArc)
    bpy.utils.unregister_class(CortaArcada)
    bpy.utils.unregister_class(CortaOssos)
    bpy.utils.unregister_class(FechaBuracos)
    bpy.utils.unregister_class(SegmentaDesenho)
    bpy.utils.unregister_class(CriaEspessura)
    bpy.utils.unregister_class(CriaMento)
    bpy.types.INFO_MT_mesh_add.remove(add_object_button)
    bpy.utils.unregister_class(PreparaImpressao)
    bpy.utils.unregister_class(CriaRamo)
    bpy.types.INFO_MT_mesh_add.remove(add_object_button)
    bpy.utils.unregister_class(CriaMaxila)
    bpy.types.INFO_MT_mesh_add.remove(add_object_button)
    bpy.utils.unregister_class(ConfiguraMento)
    bpy.utils.unregister_class(ConfiguraCorpoMand)
    bpy.utils.unregister_class(ConfiguraRamoDir)
    bpy.utils.unregister_class(ConfiguraRamoEsq)
    bpy.utils.unregister_class(ConfiguraMaxila)
    bpy.utils.unregister_class(ConfiguraCabeca)
    bpy.utils.unregister_class(AreasInfluencia)
    bpy.utils.unregister_class(CriaAreasDeformacao)
    bpy.utils.unregister_class(ConfiguraDinamicaMole)
    bpy.utils.unregister_class(GeraModelosTomo)
    bpy.utils.unregister_class(GeraModeloFoto)
    bpy.utils.unregister_class(GeraModeloFotoSMVS)
    bpy.utils.unregister_class(DisplaceSMVS)
    del bpy.types.Scene.interesse_ossos
    del bpy.types.Scene.interesse_mole
    del bpy.types.Scene.interesse_dentes
    bpy.utils.unregister_class(ImportaTomo)
    bpy.utils.unregister_class(PainelAtualiza)
#    bpy.utils.unregister_class(ZoomCena)
    bpy.utils.unregister_class(CriaFotogrametria)
    bpy.utils.unregister_class(AlinhaFaces)
    bpy.utils.unregister_class(OOB_import_obj)
    bpy.utils.unregister_class(ImportaCefalometria)
    bpy.utils.unregister_class(Osteotomia)
    bpy.utils.unregister_class(DinamicaMole)
    bpy.utils.unregister_class(PontosAnatomicos)
    bpy.utils.unregister_class(FerramentasRefMedidas)
    bpy.utils.unregister_class(CapturaLocal)
    bpy.utils.unregister_class(CriaSplint)
    bpy.utils.unregister_class(ImportaSplint)
    bpy.utils.unregister_class(EMP11)
    bpy.utils.unregister_class(EMP21)
    bpy.utils.unregister_class(EMP13)
    bpy.utils.unregister_class(EMP23)
    bpy.utils.unregister_class(EMP16)
    bpy.utils.unregister_class(EMP26)
    bpy.utils.unregister_class(EMPPalatine)
    bpy.utils.unregister_class(EMPUpperIncisor)
    bpy.utils.unregister_class(EMPNasalSpine)
    bpy.utils.unregister_class(EMPPterygoidL)
    bpy.utils.unregister_class(EMPPterygoidR)
    bpy.utils.unregister_class(EMP31)
    bpy.utils.unregister_class(EMP41)
    bpy.utils.unregister_class(EMP33)
    bpy.utils.unregister_class(EMP43)
    bpy.utils.unregister_class(EMP36)
    bpy.utils.unregister_class(EMP46)
    bpy.utils.unregister_class(EMPBpoint)
    bpy.utils.unregister_class(EMPMenton)
    bpy.utils.unregister_class(EMPPogonion)
    bpy.utils.unregister_class(EMPMentonL)
    bpy.utils.unregister_class(EMPMentonR)
    bpy.utils.unregister_class(EMPLSpoint)
    bpy.utils.unregister_class(EMPPGpoint)
    bpy.utils.unregister_class(EMPGonionR)
    bpy.utils.unregister_class(EMPGonionL)
    bpy.utils.unregister_class(EMPGonionR)
    bpy.utils.unregister_class(EMPEyeR)
    bpy.utils.unregister_class(EMPEyeL)
    bpy.utils.unregister_class(EMPMeatusR)
    bpy.utils.unregister_class(EMPMeatusL)
    bpy.utils.unregister_class(EMPNasion)
    bpy.utils.unregister_class(EMPApoint)
    bpy.utils.unregister_class(EMPSellaTurcica)
    bpy.utils.unregister_class(CefaloInterativa)
    bpy.utils.unregister_class(CinematicaPanel)
    bpy.utils.unregister_class(CriaSplintPanel)
    bpy.utils.unregister_class(ConfSplint)
    bpy.utils.unregister_class(MedidasVerDentes)
    bpy.utils.unregister_class(ChangeSolidXRay)
    bpy.utils.unregister_class(ChangeRenderEngine)
    bpy.utils.unregister_class(ConfiguraCefalo)
    bpy.utils.unregister_class(FerrZoom)
    bpy.utils.unregister_class(CefaloTeste)
    bpy.utils.unregister_class(CefaloTeste1)
    del bpy.types.Scene.angulo_SNA
    bpy.utils.unregister_class(CefaloCalculaTudo)

if __name__ == "__main__":
    register()
