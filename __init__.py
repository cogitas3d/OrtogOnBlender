bl_info = {
    "name": "OrtogOnBlender",
    "author": "Cicero Moraes e Everton da Rosa",
    "version": (1, 1, 9),
    "blender": (2, 75, 0),
    "location": "View3D",
    "description": "Planejamento de Cirurgia Ortognática no Blender",
    "warning": "",
    "wiki_url": "",
    "category": "ortog",
    }

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


# COLOCACAO DOS PONTOS

class EventWatcher:
    # Set of watchers
    eventWatchers = set()

    @staticmethod
    def AddWatcher(watcher):
        EventWatcher.eventWatchers.add(watcher)

    @staticmethod
    def RemoveWatcher(watcher):
        EventWatcher.eventWatchers.remove(watcher)

    @staticmethod
    def RemoveAllWatchers():
        EventWatcher.eventWatchers.clear()

    # From 'context', 'path' needs to exist
    # 'comparer' is to compare the previous value of context.path to its new value
    # 'callback' is the cb called if the value if changed
    # 'copyValue' indicates if the value needs to be copied (that can be needed as if not old and new value may point onto the same object)
    def __init__(self, context, path, comparer, callback, copyValue):
        self.context = context
        self.path = path
        self.comparer = comparer
        self.callback = callback
        self.copyValue = copyValue
        self.currentValue = self.GetValue()
        print("QUANDO COMEÇA")

    def GetValue(self):
        #        print("CONSTANTE")
        value = getattr(self.context, self.path)
        if self.copyValue:
            # print("CONSTANTE")
            value = value.copy()
            # print("CONSTANTE")
        return value

    def Fire(self):
        newValue = self.GetValue()
        #        print("CONSTANTE")

        #        for obj in bpy.data.objects:
        A = bpy.context.scene.objects.active
        #            print(obj)

        if self.comparer(self.currentValue, newValue) == False and A.name != "Empty.002":
            self.callback(self, newValue)
            self.currentValue = newValue
            #   bpy.ops.mesh.primitive_cube_add()
            bpy.ops.object.empty_add(type='PLAIN_AXES', radius=1)

            #            bpy.context.object.name = "EMPPonto" #NÃO FUNCIONA!!!
            print("nome", A.name)
        return {'FINISHED'}  # DEU CERTO!


# Global loop on the watchers. This callback responds to scene_update_post global handler
def cb_scene_update(context):
    #    print("FICA CONSTANTE")
    for ew in EventWatcher.eventWatchers:
        ew.Fire()


# To stop the calls at the scene_update_post event level
class StopCallback(bpy.types.Operator):
    bl_idname = "scene.stop_callback"
    bl_label = "Stop Callback"

    @classmethod
    def poll(cls, context):
        #        print("FICA CONSTANTEMENTE")
        return cb_scene_update in bpy.app.handlers.scene_update_post

    def execute(self, context):
        print("ASSIM QUE CLICA NO STOP")
        bpy.app.handlers.scene_update_post.remove(cb_scene_update)
        return {'FINISHED'}


# To start the calls at the scene_update_post event level
class StartCallback(bpy.types.Operator):
    bl_idname = "scene.start_callback"
    bl_label = "Start Callback"

    @classmethod
    def poll(cls, context):
        #        print("PQP") # CONSTANTE, SEM PARAR
        return cb_scene_update not in bpy.app.handlers.scene_update_post

    def execute(self, context):
        bpy.app.handlers.scene_update_post.append(cb_scene_update)
        print("QUANDO CLICA NO START")
        return {'FINISHED'}


# ALINHA MAXILA

def ColocaPontosDef(self, context):
    EventWatcher.AddWatcher(
        EventWatcher(bpy.data.scenes[0], "cursor_location", CompareLocation, CompareLocationCallback, True))
    bpy.ops.scene.start_callback()


class ColocaPontos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.colocapontos"
    bl_label = "Coloca Pontos"

    def execute(self, context):
        ColocaPontosDef(self, context)
        return {'FINISHED'}


def CalcAlinhaMandibulaDef(self, context):
    bpy.ops.scene.stop_callback()

    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['scene_dense_mesh_texture2']
    a.select = True
    bpy.context.scene.objects.active = a

    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    EMP1 = bpy.data.objects['Empty']
    EMP2 = bpy.data.objects['Empty.001']
    EMP3 = bpy.data.objects['Empty.002']

    a = bpy.data.objects['scene_dense_mesh_texture2']
    b = bpy.data.objects['Empty']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

    a = bpy.data.objects['scene_dense_mesh_texture2']
    b = bpy.data.objects['Empty.001']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

    a = bpy.data.objects['scene_dense_mesh_texture2']
    b = bpy.data.objects['Empty.002']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

    # Frontal

    AB = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[2] - EMP1.location[2]) ** 2)

    AC = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP1.location[2] - EMP1.location[2]) ** 2)

    BC = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[2] - EMP2.location[2]) ** 2)

    # Superior

    EF = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[1] - EMP2.location[1]) ** 2)
    DE = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[1] - EMP1.location[1]) ** 2)

    # Valor rotação frontal
    valor = BC / AB

    # Valor rotação superior
    valor2 = EF / DE

    bpy.ops.object.select_all(action='DESELECT')
    #    PT_INCISIVOS = bpy.data.objects['PT_INCISIVOS']
    #    PT_INCISIVOS.select = True
    #    bpy.context.scene.objects.active = PT_INCISIVOS
    #    bpy.ops.view3d.snap_cursor_to_selected()
    #    bpy.context.space_data.pivot_point = 'CURSOR'

    a = bpy.data.objects['scene_dense_mesh_texture2']
    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    bpy.context.scene.objects.active = a

    # Rotação frontal
    if EMP1.location[2] > EMP2.location[2]:
        bpy.ops.transform.rotate(value=valor, axis=(0, -1, 0))

    else:
        bpy.ops.transform.rotate(value=valor, axis=(0, 1, 0))

    # Rotação superior
    if EMP1.location[1] > EMP2.location[1]:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, 1))

    else:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, -1))

    #    bpy.context.space_data.pivot_point = 'MEDIAN_POINT'

    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    # Calcula rotação em X

    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')

    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0

    AB2 = math.sqrt((EMP3.location[1] - EMP1.location[1]) ** 2 + (EMP3.location[2] - EMP1.location[2]) ** 2)

    BC2 = math.sqrt((EMP1.location[1] - EMP3.location[1]) ** 2 + (EMP3.location[2] - EMP3.location[2]) ** 2)

    valor3 = BC2 / AB2

    bpy.ops.transform.rotate(value=valor3, axis=(1, 0, 0))

    # OUTRA VEZ 1

    # Frontal

    AB = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[2] - EMP1.location[2]) ** 2)

    AC = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP1.location[2] - EMP1.location[2]) ** 2)

    BC = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[2] - EMP2.location[2]) ** 2)

    # Superior

    EF = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[1] - EMP2.location[1]) ** 2)
    DE = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[1] - EMP1.location[1]) ** 2)

    # Valor rotação frontal
    valor = BC / AB

    # Valor rotação superior
    valor2 = EF / DE

    bpy.ops.object.select_all(action='DESELECT')
    #    PT_INCISIVOS = bpy.data.objects['PT_INCISIVOS']
    #    PT_INCISIVOS.select = True
    #    bpy.context.scene.objects.active = PT_INCISIVOS
    #    bpy.ops.view3d.snap_cursor_to_selected()
    #    bpy.context.space_data.pivot_point = 'CURSOR'

    a = bpy.data.objects['scene_dense_mesh_texture2']
    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    bpy.context.scene.objects.active = a

    # Rotação frontal
    if EMP1.location[2] > EMP2.location[2]:
        bpy.ops.transform.rotate(value=valor, axis=(0, -1, 0))

    else:
        bpy.ops.transform.rotate(value=valor, axis=(0, 1, 0))

    # Rotação superior
    if EMP1.location[1] > EMP2.location[1]:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, 1))

    else:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, -1))

    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    # Calcula rotação em X

    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')

    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0

    AB2 = math.sqrt((EMP3.location[1] - EMP1.location[1]) ** 2 + (EMP3.location[2] - EMP1.location[2]) ** 2)

    BC2 = math.sqrt((EMP1.location[1] - EMP3.location[1]) ** 2 + (EMP3.location[2] - EMP3.location[2]) ** 2)

    valor3 = BC2 / AB2

    bpy.ops.transform.rotate(value=valor3, axis=(1, 0, 0))

    # OUTRA VEZ 2

    # Frontal

    AB = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[2] - EMP1.location[2]) ** 2)

    AC = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP1.location[2] - EMP1.location[2]) ** 2)

    BC = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[2] - EMP2.location[2]) ** 2)

    # Superior

    EF = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[1] - EMP2.location[1]) ** 2)
    DE = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[1] - EMP1.location[1]) ** 2)

    # Valor rotação frontal
    valor = BC / AB

    # Valor rotação superior
    valor2 = EF / DE

    bpy.ops.object.select_all(action='DESELECT')
    #    PT_INCISIVOS = bpy.data.objects['PT_INCISIVOS']
    #    PT_INCISIVOS.select = True
    #    bpy.context.scene.objects.active = PT_INCISIVOS
    #    bpy.ops.view3d.snap_cursor_to_selected()
    #    bpy.context.space_data.pivot_point = 'CURSOR'

    a = bpy.data.objects['scene_dense_mesh_texture2']
    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    bpy.context.scene.objects.active = a

    # Rotação frontal
    if EMP1.location[2] > EMP2.location[2]:
        bpy.ops.transform.rotate(value=valor, axis=(0, -1, 0))

    else:
        bpy.ops.transform.rotate(value=valor, axis=(0, 1, 0))

    # Rotação superior
    if EMP1.location[1] > EMP2.location[1]:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, 1))

    else:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, -1))

    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    # Calcula rotação em X

    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')

    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0

    AB2 = math.sqrt((EMP3.location[1] - EMP1.location[1]) ** 2 + (EMP3.location[2] - EMP1.location[2]) ** 2)

    BC2 = math.sqrt((EMP1.location[1] - EMP3.location[1]) ** 2 + (EMP3.location[2] - EMP3.location[2]) ** 2)

    valor3 = BC2 / AB2

    bpy.ops.transform.rotate(value=valor3, axis=(1, 0, 0))

    # OUTRA VEZ 3

    # Frontal

    AB = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[2] - EMP1.location[2]) ** 2)

    AC = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP1.location[2] - EMP1.location[2]) ** 2)

    BC = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[2] - EMP2.location[2]) ** 2)

    # Superior

    EF = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[1] - EMP2.location[1]) ** 2)
    DE = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[1] - EMP1.location[1]) ** 2)

    # Valor rotação frontal
    valor = BC / AB

    # Valor rotação superior
    valor2 = EF / DE

    bpy.ops.object.select_all(action='DESELECT')
    #    PT_INCISIVOS = bpy.data.objects['PT_INCISIVOS']
    #    PT_INCISIVOS.select = True
    #    bpy.context.scene.objects.active = PT_INCISIVOS
    #    bpy.ops.view3d.snap_cursor_to_selected()
    #    bpy.context.space_data.pivot_point = 'CURSOR'

    a = bpy.data.objects['scene_dense_mesh_texture2']
    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    bpy.context.scene.objects.active = a

    # Rotação frontal
    if EMP1.location[2] > EMP2.location[2]:
        bpy.ops.transform.rotate(value=valor, axis=(0, -1, 0))

    else:
        bpy.ops.transform.rotate(value=valor, axis=(0, 1, 0))

    # Rotação superior
    if EMP1.location[1] > EMP2.location[1]:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, 1))

    else:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, -1))

    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    # Calcula rotação em X

    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')

    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0

    AB2 = math.sqrt((EMP3.location[1] - EMP1.location[1]) ** 2 + (EMP3.location[2] - EMP1.location[2]) ** 2)

    BC2 = math.sqrt((EMP1.location[1] - EMP3.location[1]) ** 2 + (EMP3.location[2] - EMP3.location[2]) ** 2)

    valor3 = BC2 / AB2

    bpy.ops.transform.rotate(value=valor3, axis=(1, 0, 0))

    # OUTRA VEZ 4

    # Frontal

    AB = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[2] - EMP1.location[2]) ** 2)

    AC = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP1.location[2] - EMP1.location[2]) ** 2)

    BC = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[2] - EMP2.location[2]) ** 2)

    # Superior

    EF = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[1] - EMP2.location[1]) ** 2)
    DE = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[1] - EMP1.location[1]) ** 2)

    # Valor rotação frontal
    valor = BC / AB

    # Valor rotação superior
    valor2 = EF / DE

    bpy.ops.object.select_all(action='DESELECT')
    #    PT_INCISIVOS = bpy.data.objects['PT_INCISIVOS']
    #    PT_INCISIVOS.select = True
    #    bpy.context.scene.objects.active = PT_INCISIVOS
    #    bpy.ops.view3d.snap_cursor_to_selected()
    #    bpy.context.space_data.pivot_point = 'CURSOR'

    a = bpy.data.objects['scene_dense_mesh_texture2']
    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    bpy.context.scene.objects.active = a

    # Rotação frontal
    if EMP1.location[2] > EMP2.location[2]:
        bpy.ops.transform.rotate(value=valor, axis=(0, -1, 0))

    else:
        bpy.ops.transform.rotate(value=valor, axis=(0, 1, 0))

    # Rotação superior
    if EMP1.location[1] > EMP2.location[1]:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, 1))

    else:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, -1))

    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    # Calcula rotação em X

    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')

    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0

    AB2 = math.sqrt((EMP3.location[1] - EMP1.location[1]) ** 2 + (EMP3.location[2] - EMP1.location[2]) ** 2)

    BC2 = math.sqrt((EMP1.location[1] - EMP3.location[1]) ** 2 + (EMP3.location[2] - EMP3.location[2]) ** 2)

    valor3 = BC2 / AB2

    bpy.ops.transform.rotate(value=valor3, axis=(1, 0, 0))

    # OUTRA VEZ 5

    # Frontal

    AB = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[2] - EMP1.location[2]) ** 2)

    AC = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP1.location[2] - EMP1.location[2]) ** 2)

    BC = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[2] - EMP2.location[2]) ** 2)

    # Superior

    EF = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[1] - EMP2.location[1]) ** 2)
    DE = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[1] - EMP1.location[1]) ** 2)

    # Valor rotação frontal
    valor = BC / AB

    # Valor rotação superior
    valor2 = EF / DE

    bpy.ops.object.select_all(action='DESELECT')
    #    PT_INCISIVOS = bpy.data.objects['PT_INCISIVOS']
    #    PT_INCISIVOS.select = True
    #    bpy.context.scene.objects.active = PT_INCISIVOS
    #    bpy.ops.view3d.snap_cursor_to_selected()
    #    bpy.context.space_data.pivot_point = 'CURSOR'

    a = bpy.data.objects['scene_dense_mesh_texture2']
    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    bpy.context.scene.objects.active = a

    # Rotação frontal
    if EMP1.location[2] > EMP2.location[2]:
        bpy.ops.transform.rotate(value=valor, axis=(0, -1, 0))

    else:
        bpy.ops.transform.rotate(value=valor, axis=(0, 1, 0))

    # Rotação superior
    if EMP1.location[1] > EMP2.location[1]:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, 1))

    else:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, -1))

    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    # Calcula rotação em X

    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')

    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0

    AB2 = math.sqrt((EMP3.location[1] - EMP1.location[1]) ** 2 + (EMP3.location[2] - EMP1.location[2]) ** 2)

    BC2 = math.sqrt((EMP1.location[1] - EMP3.location[1]) ** 2 + (EMP3.location[2] - EMP3.location[2]) ** 2)

    valor3 = BC2 / AB2

    bpy.ops.transform.rotate(value=valor3, axis=(1, 0, 0))

    # OUTRA VEZ 6

    # Frontal

    AB = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[2] - EMP1.location[2]) ** 2)

    AC = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP1.location[2] - EMP1.location[2]) ** 2)

    BC = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[2] - EMP2.location[2]) ** 2)

    # Superior

    EF = math.sqrt((EMP2.location[0] - EMP2.location[0]) ** 2 + (EMP1.location[1] - EMP2.location[1]) ** 2)
    DE = math.sqrt((EMP2.location[0] - EMP1.location[0]) ** 2 + (EMP2.location[1] - EMP1.location[1]) ** 2)

    # Valor rotação frontal
    valor = BC / AB

    # Valor rotação superior
    valor2 = EF / DE

    bpy.ops.object.select_all(action='DESELECT')
    #    PT_INCISIVOS = bpy.data.objects['PT_INCISIVOS']
    #    PT_INCISIVOS.select = True
    #    bpy.context.scene.objects.active = PT_INCISIVOS
    #    bpy.ops.view3d.snap_cursor_to_selected()
    #    bpy.context.space_data.pivot_point = 'CURSOR'

    a = bpy.data.objects['scene_dense_mesh_texture2']
    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    bpy.context.scene.objects.active = a

    # Rotação frontal
    if EMP1.location[2] > EMP2.location[2]:
        bpy.ops.transform.rotate(value=valor, axis=(0, -1, 0))

    else:
        bpy.ops.transform.rotate(value=valor, axis=(0, 1, 0))

    # Rotação superior
    if EMP1.location[1] > EMP2.location[1]:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, 1))

    else:
        bpy.ops.transform.rotate(value=valor2, axis=(0, 0, -1))

    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    # Calcula rotação em X

    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')

    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0

    AB2 = math.sqrt((EMP3.location[1] - EMP1.location[1]) ** 2 + (EMP3.location[2] - EMP1.location[2]) ** 2)

    BC2 = math.sqrt((EMP1.location[1] - EMP3.location[1]) ** 2 + (EMP3.location[2] - EMP3.location[2]) ** 2)

    valor3 = BC2 / AB2

    bpy.ops.transform.rotate(value=valor3, axis=(1, 0, 0))

    # CORRIGE ROTAÇÃO

    FACE = bpy.data.objects['scene_dense_mesh_texture2']

    bpy.ops.object.select_all(action='DESELECT')
    EMP1.select = True
    EMP2.select = True
    EMP3.select = True
    bpy.context.scene.objects.active = EMP1

    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

    print("EMP1 Z:", EMP1.location[2])
    print("EMP1 Y:", EMP1.location[1])
    print("EMP3 Z:", EMP3.location[2])
    print("EMP3 Y:", EMP3.location[1])

    bpy.ops.object.select_all(action='DESELECT')

    FACE.select = True
    bpy.context.scene.objects.active = FACE

    if EMP1.location[2] > 0 and EMP1.location[1] < 0 and EMP3.location[2] < 0 and EMP3.location[1] < 0:
        print("Rotação CORRETA")

    if EMP1.location[2] > 0 and EMP1.location[1] > 0 and EMP3.location[2] > 0 and EMP3.location[1] < 0:
        bpy.ops.transform.rotate(value=1.5707963268, axis=(1, 0, 0))
        print("Estava olhando para CIMA")

    if EMP1.location[2] < 0 and EMP1.location[1] > 0 and EMP3.location[2] > 0 and EMP3.location[1] > 0:
        bpy.ops.transform.rotate(value=3.141592, axis=(1, 0, 0))
        print("Estava olhando para TRÁS com olhos baixos")

    if EMP1.location[2] < 0 and EMP1.location[1] < 0 and EMP3.location[2] < 0 and EMP3.location[1] > 0:
        bpy.ops.transform.rotate(value=-1.5707963268, axis=(1, 0, 0))
        print("Estava olhando para BAIXO")

    # Distância intercantal

    l = []
    EMP1EMP2 = [bpy.data.objects['Empty'], bpy.data.objects['Empty.001']]

    for item in EMP1EMP2:
        l.append(item.location)

    medidaAtual2 = math.sqrt((l[0][0] - l[1][0]) ** 2 + (l[0][1] - l[1][1]) ** 2 + (l[0][2] - l[1][2]) ** 2)
    print("Medida atual: ", medidaAtual2)

    medidaReal2 = float(bpy.context.scene.medida_real2)
    print("Medida real: ", medidaReal2)

    # Apaga empties

    bpy.ops.object.select_all(action='DESELECT')
    EMP1.select = True
    EMP2.select = True
    EMP3.select = True
    bpy.context.scene.objects.active = EMP1

    bpy.ops.object.delete(use_global=False)

    # Redimensiona

    fatorEscala2 = medidaReal2 / medidaAtual2

    bpy.ops.object.select_all(action='DESELECT')
    FACE.select = True
    bpy.context.scene.objects.active = FACE
    FACE.scale = (fatorEscala2, fatorEscala2, fatorEscala2)

    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    bpy.ops.view3d.viewnumpad(type='FRONT')
    bpy.ops.view3d.view_selected()


class CalcAlinhaMandibula(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.calcalinhamand"
    bl_label = "Cálculo de Alinhamento da Mandíbula"

    def execute(self, context):
        CalcAlinhaMandibulaDef(self, context)
        return {'FINISHED'}

# IMPORTA TOMO MOLDES

def GeraModelosTomoArcDef(self, context):
    
    scn = context.scene
    
    tmpdir = tempfile.gettempdir()
    tmpSTLarcada = tmpdir+'/Arcada.stl'

    homeall = expanduser("~")

    try:


        if platform.system() == "Linux":


            dicom2DtlPath = homeall+'/Programs/OrtogOnBlender/Dicom2Mesh/dicom2mesh'
#            dicom2DtlPath = get_dicom2stl_filepath(context)


            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.5', '-s', '-t', '226', '-o', tmpSTLarcada])
	      

            bpy.ops.import_mesh.stl(filepath=tmpSTLarcada, filter_glob="*.stl",  files=[{"name":"Arcada.stl", "name":"Arcada.stl"}], directory=tmpdir)
      


        if platform.system() == "Windows":

            dicom2DtlPath = 'C:/OrtogOnBlender/DicomToMeshWin/dicom2mesh.exe'


            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.5', '-s', '-t', '226', '-o', tmpSTLarcada])
	      

            bpy.ops.import_mesh.stl(filepath=tmpSTLarcada, filter_glob="*.stl",  files=[{"name":"Arcada.stl", "name":"Arcada.stl"}], directory=tmpdir)


        if platform.system() == "Darwin":


            dicom2DtlPath = '/OrtogOnBlender/DicomToMeshMAC/dicom2mesh'

#            dicom2DtlPath = get_dicom2stl_filepath(context)


            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.5', '-s', '-t', '226', '-o', tmpSTLarcada])
	      

            bpy.ops.import_mesh.stl(filepath=tmpSTLarcada, filter_glob="*.stl",  files=[{"name":"Arcada.stl", "name":"Arcada.stl"}], directory=tmpdir)

  
        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
        bpy.ops.view3d.view_all(center=False)

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDICOMDef, title="Atenção!", icon='INFO')


class GeraModelosTomoArc(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_modelos_tomo_arc"
    bl_label = "Gera Tomografia Molde"
    
    def execute(self, context):
        GeraModelosTomoArcDef(self, context)
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

# IMPORTA ARMATURE

def ImportaArmatureDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    if platform.system() == "Linux" or platform.system() == "Darwin":
        dirScript = bpy.utils.user_resource('SCRIPTS')
        
        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Object\\"
        object    = "Armature_Head"
        
    if platform.system() == "Windows":
        dirScript = 'C:/OrtogOnBlender/Blender/2.78/scripts/' 

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Object\\"
        object    = "Armature_Head"

    filepath  = blendfile + section + object
    directory = blendfile + section
    filename  = object

    bpy.ops.wm.append(
        filepath=filepath, 
        filename=filename,
        directory=directory)
        
 #   bpy.ops.wm.append(filename=filename, directory=directory)

    # APAGA OBJETOS EXCEDENTES

    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['Mandibula']
    b = bpy.data.objects['SETA_Corpo_M']
    c = bpy.data.objects['SETA_Maxila']
    d = bpy.data.objects['SETA_Mento']


    a.select = True
    b.select = True
    c.select = True
    d.select = True


    bpy.ops.object.delete(use_global=False)
    

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


def CortaFaceDef(self, context):
    
    context = bpy.context
    obj = context.active_object

    try:

        bpy.context.object.name = "FaceMalha"
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.knife_project(cut_through=True)
        bpy.ops.mesh.separate(type='SELECTED')
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['FaceMalha.001'].select = False
        bpy.data.objects['FaceMalha'].select = True
        bpy.ops.object.delete()
        bpy.data.objects['Circle'].select = True
        bpy.ops.object.delete()
        
    except RuntimeError:
        bpy.context.object.name = "Circle"        
        bpy.context.window_manager.popup_menu(ERROruntimeCorteDef, title="Atenção!", icon='INFO')
         

def AlinhaRostoDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    try:
        
        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')

        bpy.context.object.name = "Rosto"
        bpy.ops.mesh.edge_face_add() # cria face nos pontos selecionados
        bpy.ops.mesh.normals_make_consistent(inside=False)

        bpy.ops.mesh.separate(type='SELECTED') # separa triângulo
        bpy.ops.object.editmode_toggle() #sai do modo de edição
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Rosto.001'].select = True
        bpy.context.scene.objects.active = bpy.data.objects['Rosto.001']
        bpy.ops.object.editmode_toggle() #entra modo edição
        bpy.ops.mesh.select_all(action='TOGGLE') #seleciona tudo

    #    bpy.ops.mesh.flip_normals() # inverte os normals
    #    bpy.ops.mesh.normals_make_consistent(inside=False) # Força normals para fora
        bpy.ops.view3d.viewnumpad(type='TOP', align_active=True) # alinha a vista com a face selecionada

        bpy.ops.object.editmode_toggle() #sai edit mode
    
    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimePontosDef, title="Atenção!", icon='INFO')    
    

# FATOR DE ESCALA

def posicionaEmpties():

    context = bpy.context    
    obj = context.active_object
    v0 = obj.data.vertices[0]
    v1 = obj.data.vertices[1]
    v2 = obj.data.vertices[2]

    co_final0 = obj.matrix_world * v0.co
    co_final1 = obj.matrix_world * v1.co
    co_final2 = obj.matrix_world * v2.co

    # now we can view the location by applying it to an object
    obj_empty0 = bpy.data.objects.new("Dist0", None)
    context.scene.objects.link(obj_empty0)
    obj_empty0.location = co_final0

    obj_empty1 = bpy.data.objects.new("Dist1", None)
    context.scene.objects.link(obj_empty1)
    obj_empty1.location = co_final1

    obj_empty2 = bpy.data.objects.new("Dist2", None)
    context.scene.objects.link(obj_empty2)
    obj_empty2.location = co_final2

def medidaAtual():

    posicionaEmpties()
    
    """ Retorna Média de Três Pontos """
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['Dist0']
    b = bpy.data.objects['Dist1']
    c = bpy.data.objects['Dist2']
    a.select = True
    b.select = True
    c.select = True
    l = []
    for item in bpy.context.selected_objects:
        l.append(item.location)

    distancia1 = sqrt( (l[0][0] - l[2][0])**2 + (l[0][1] - l[2][1])**2 + (l[0][2] - l[2][2])**2)
    distancia2 = sqrt( (l[1][0] - l[2][0])**2 + (l[1][1] - l[2][1])**2 + (l[1][2] - l[2][2])**2)
    distancia3 = sqrt( (l[1][0] - l[0][0])**2 + (l[1][1] - l[0][1])**2 + (l[1][2] - l[0][2])**2)

    print(distancia1)
    print(distancia2)
    print(distancia3)
    
    medidaAtual = min(distancia1, distancia2, distancia3)
    print("A distância menor é:")
    print(medidaAtual)

    medidaReal = float(bpy.context.scene.medida_real)
    print(medidaReal)

    global fatorEscala 
    fatorEscala = medidaReal / medidaAtual
    print(fatorEscala)

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

# ALINHAMENTO ROSTO PARTE 2 - ALINHA OBJETO

def AlinhaRostoDef2(self, context):

    medidaAtual()
    
    bpy.ops.object.select_all(action='DESELECT')
    c = bpy.data.objects['Rosto.001']
    bpy.context.scene.objects.active = c
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.editmode_toggle() #entra edit mode 
    bpy.ops.view3d.snap_cursor_to_selected() # posiciona o cursor ao centro da seleção
#    bpy.ops.mesh.delete(type='EDGE_FACE') # deleta apenas a face e edges selecionadas
    bpy.ops.object.editmode_toggle() #sai edit mode
    
    bpy.ops.object.select_all(action='DESELECT') # desseleciona todos os objetos
    bpy.ops.object.add(radius=1.0, type='EMPTY', view_align=True)
#    bpy.ops.object.empty_add(type='SINGLE_ARROW', view_align=True) # cria um empty single arrow apontando para o view
    bpy.context.object.name = "Alinhador" #renomeia de alinhador

#    bpy.context.object.rotation_euler[0] = 1.5708

# Parenteia objetos
    a = bpy.data.objects['Rosto']
    b = bpy.data.objects['Alinhador']
    c = bpy.data.objects['Rosto.001']


    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = b
    bpy.ops.object.parent_set()
    
    bpy.ops.object.select_all(action='DESELECT')
    c.select = True
    b.select = True 
    bpy.context.scene.objects.active = b
    bpy.ops.object.parent_set() 

# Reseta rotações
    bpy.ops.object.rotation_clear(clear_delta=False)
    
    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    bpy.context.scene.objects.active = a        
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

    bpy.ops.object.select_all(action='DESELECT')
    b.select = True
    bpy.context.scene.objects.active = b
    bpy.ops.object.delete(use_global=False)

    bpy.ops.object.select_all(action='DESELECT')
    c.select = True
    bpy.context.scene.objects.active = c
    bpy.ops.object.delete(use_global=False)

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


    objRedimensionado = bpy.data.objects['Rosto']
    objRedimensionado.scale = ( fatorEscala, fatorEscala, fatorEscala )

   
    bpy.ops.view3d.viewnumpad(type='FRONT')
    bpy.ops.view3d.view_selected(use_all_regions=False)
    
    
    bpy.context.object.name = "Rosto_OK"
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['Dist0']
    b = bpy.data.objects['Dist1']
    c = bpy.data.objects['Dist2']
    a.select = True
    b.select = True
    c.select = True

    bpy.ops.object.delete(use_global=False)

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
    
def ERROruntimeDICOMDef(self, context):
    self.layout.label("Você não indicou a pasta com os DICOMS!")

def ERROruntimeFotosDef(self, context):
    self.layout.label("Você não indicou a pasta com as fotos!")
    
def ERROruntimePontosDef(self, context):
    self.layout.label("Você não selecionou os três pontos!")
    
def ERROruntimeCorteDef(self, context):
    self.layout.label("Você não selecionou o objeto a ser cortado!")

# CONFIGURA MENTO
def ConfiguraMentoDef(self, context):

    context = bpy.context
    obj = context.active_object
 #   scn = context.scene


    try: 
        ob=bpy.data.objects["Armature_Head"]

        try: 
            ob=bpy.data.objects["cm"]

            bpy.ops.object.mode_set(mode='EDIT')
            mesh=bmesh.from_edit_mesh(bpy.context.object.data)


            for v in mesh.verts:
                v.select = True

            vg = obj.vertex_groups.new(name="me")
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.object.vertex_group_assign()
            bpy.ops.object.mode_set(mode='OBJECT')
            
            activeObject = bpy.context.active_object #Set active object to variable
            mat = bpy.data.materials.new(name="MaterialMento") #set new material to variable
            activeObject.data.materials.append(mat) #add the material to the object
            bpy.context.object.active_material.diffuse_color = (0.8, 0.35, 0.2) #change color
            bpy.context.object.name = "me"

            armatureHead = bpy.data.objects['Armature_Head']
            bpy.ops.object.select_all(action='DESELECT')
            armatureHead.hide=False
            armatureHead.select=True
            bpy.context.scene.objects.active = armatureHead
            bpy.ops.object.posemode_toggle()

         #   bpy.data.objects['me'].select = True
         #   bpy.data.objects['Armature_Head'].select = True
         #   bpy.ops.object.parent_set(type='ARMATURE_NAME')

            bpy.ops.pose.select_all(action='DESELECT')
            o=bpy.context.object
            b=o.data.bones['me']
            b.select=True
            o.data.bones.active=b
         
            bpy.ops.pose.constraint_add(type='CHILD_OF')
            bpy.context.object.pose.bones["me"].constraints["Child Of"].target = bpy.data.objects["me"]

            pbone = bpy.context.active_object.pose.bones["me"] # Bone
            context_copy = bpy.context.copy()
            context_copy["constraint"] = pbone.constraints["Child Of"]
            bpy.ops.constraint.childof_set_inverse(context_copy, constraint="Child Of", owner='BONE')

            bpy.ops.object.posemode_toggle()
            armatureHead.hide=True

            a = bpy.data.objects['cm']
            b = bpy.data.objects['me']

            bpy.ops.object.select_all(action='DESELECT')
            a.select = True
            b.select = True 
            bpy.context.scene.objects.active = a
            bpy.ops.object.parent_set()
        
        except KeyError:
            bpy.context.window_manager.popup_menu(ERROcmDef, title="Atenção!", icon='INFO')

 #   bpy.context.active_object.data.bones.active = pbone.bone


    except KeyError:
        bpy.context.window_manager.popup_menu(ERROarmatureDef, title="Atenção!", icon='INFO')

    except TypeError:
        bpy.context.window_manager.popup_menu(ERROtipoDef, title="Atenção!", icon='INFO')

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDef, title="Atenção!", icon='INFO')

# CONFIGURA RAMO DA MANDÍBULA
def ConfiguraCorpoMandDef(self, context):
    
    context = bpy.context
    obj = context.active_object
 #   scn = context.scene

    try: 
        ob=bpy.data.objects["Armature_Head"]

        bpy.ops.object.mode_set(mode='EDIT')
        mesh=bmesh.from_edit_mesh(bpy.context.object.data)
        for v in mesh.verts:
            v.select = True

        vg = obj.vertex_groups.new(name="Corpo_Mandibular.GUIA")
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.vertex_group_assign()
        bpy.ops.object.mode_set(mode='OBJECT')

        activeObject = bpy.context.active_object #Set active object to variable
        mat = bpy.data.materials.new(name="MaterialCorpoMand") #set new material to variable
        activeObject.data.materials.append(mat) #add the material to the object
        bpy.context.object.active_material.diffuse_color = (0.35, 0.8, 0.4) #change color
        bpy.context.object.name = "cm"

        armatureHead = bpy.data.objects['Armature_Head']
        bpy.ops.object.select_all(action='DESELECT')
        armatureHead.hide=False
        armatureHead.select=True
        bpy.context.scene.objects.active = armatureHead
        bpy.ops.object.posemode_toggle()

    #    bpy.data.objects['cm'].select = True
    #    bpy.data.objects['Armature_Head'].select = True
    #    bpy.ops.object.parent_set(type='ARMATURE_NAME')

        bpy.ops.pose.select_all(action='DESELECT')
        o=bpy.context.object
        b=o.data.bones['Corpo_Mandibular.GUIA']
        b.select=True
        o.data.bones.active=b
     
        bpy.ops.pose.constraint_add(type='CHILD_OF')
        bpy.context.object.pose.bones["Corpo_Mandibular.GUIA"].constraints["Child Of"].target = bpy.data.objects["cm"]

        pbone = bpy.context.active_object.pose.bones["Corpo_Mandibular.GUIA"] # Bone
        context_copy = bpy.context.copy()
        context_copy["constraint"] = pbone.constraints["Child Of"]
        bpy.ops.constraint.childof_set_inverse(context_copy, constraint="Child Of", owner='BONE')


        bpy.ops.object.posemode_toggle()
        armatureHead.hide=True

    except KeyError:
        bpy.context.window_manager.popup_menu(ERROarmatureDef, title="Atenção!", icon='INFO')

    except TypeError:
        bpy.context.window_manager.popup_menu(ERROtipoDef, title="Atenção!", icon='INFO')

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDef, title="Atenção!", icon='INFO') 

# CONFIGURA RAMO DIREITO
def ConfiguraRamoDirDef(self, context):
    
    context = bpy.context
    obj = context.active_object
 #   scn = context.scene

    try: 
        ob=bpy.data.objects["Armature_Head"]

        bpy.ops.object.mode_set(mode='EDIT')
        mesh=bmesh.from_edit_mesh(bpy.context.object.data)
        for v in mesh.verts:
            v.select = True

        vg = obj.vertex_groups.new(name="rd")
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.vertex_group_assign()
        bpy.ops.object.mode_set(mode='OBJECT')

        activeObject = bpy.context.active_object #Set active object to variable
        mat = bpy.data.materials.new(name="MaterialRamoDir") #set new material to variable
        activeObject.data.materials.append(mat) #add the material to the object
        bpy.context.object.active_material.diffuse_color = (0.4, 0.3, 0.8) #change color
        bpy.context.object.name = "rd"

        armatureHead = bpy.data.objects['Armature_Head']
        bpy.ops.object.select_all(action='DESELECT')
        armatureHead.hide=False
        armatureHead.select=True
        bpy.context.scene.objects.active = armatureHead
        bpy.ops.object.posemode_toggle()
    #    bpy.data.objects['rd'].select = True
    #    bpy.data.objects['Armature_Head'].select = True
    #    bpy.ops.object.parent_set(type='ARMATURE_NAME')

        bpy.ops.pose.select_all(action='DESELECT')
        o=bpy.context.object
        b=o.data.bones['rd']
        b.select=True
        o.data.bones.active=b
     
        bpy.ops.pose.constraint_add(type='CHILD_OF')
        bpy.context.object.pose.bones["rd"].constraints["Child Of"].target = bpy.data.objects["rd"]

        pbone = bpy.context.active_object.pose.bones["rd"] # Bone
        context_copy = bpy.context.copy()
        context_copy["constraint"] = pbone.constraints["Child Of"]
        bpy.ops.constraint.childof_set_inverse(context_copy, constraint="Child Of", owner='BONE')

        bpy.ops.object.posemode_toggle()
        armatureHead.hide=True


    except KeyError:
        bpy.context.window_manager.popup_menu(ERROarmatureDef, title="Atenção!", icon='INFO')

    except TypeError:
        bpy.context.window_manager.popup_menu(ERROtipoDef, title="Atenção!", icon='INFO')

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDef, title="Atenção!", icon='INFO')  


# CONFIGURA RAMO ESQUERDO
def ConfiguraRamoEsqDef(self, context):

    context = bpy.context
    obj = context.active_object
 #   scn = context.scene

    try: 
        ob=bpy.data.objects["Armature_Head"]

        bpy.ops.object.mode_set(mode='EDIT')
        mesh=bmesh.from_edit_mesh(bpy.context.object.data)
        for v in mesh.verts:
            v.select = True

        vg = obj.vertex_groups.new(name="re")
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.vertex_group_assign()
        bpy.ops.object.mode_set(mode='OBJECT')
        
        activeObject = bpy.context.active_object #Set active object to variable
        mat = bpy.data.materials.new(name="MaterialRamoEsq") #set new material to variable
        activeObject.data.materials.append(mat) #add the material to the object
        bpy.context.object.active_material.diffuse_color = (0.4, 0.3, 0.8) #change color
        bpy.context.object.name = "re"

        armatureHead = bpy.data.objects['Armature_Head']
        bpy.ops.object.select_all(action='DESELECT')
        armatureHead.hide=False
        armatureHead.select=True
        bpy.context.scene.objects.active = armatureHead
        bpy.ops.object.posemode_toggle()
    #    bpy.data.objects['re'].select = True
    #    bpy.data.objects['Armature_Head'].select = True
    #    bpy.ops.object.parent_set(type='ARMATURE_NAME')

        bpy.ops.pose.select_all(action='DESELECT')
        o=bpy.context.object
        b=o.data.bones['re']
        b.select=True
        o.data.bones.active=b
     
        bpy.ops.pose.constraint_add(type='CHILD_OF')
        bpy.context.object.pose.bones["re"].constraints["Child Of"].target = bpy.data.objects["re"]

        pbone = bpy.context.active_object.pose.bones["re"] # Bone
        context_copy = bpy.context.copy()
        context_copy["constraint"] = pbone.constraints["Child Of"]
        bpy.ops.constraint.childof_set_inverse(context_copy, constraint="Child Of", owner='BONE')

        bpy.ops.object.posemode_toggle()
        armatureHead.hide=True

    except KeyError:
        bpy.context.window_manager.popup_menu(ERROarmatureDef, title="Atenção!", icon='INFO')

    except TypeError:
        bpy.context.window_manager.popup_menu(ERROtipoDef, title="Atenção!", icon='INFO')

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDef, title="Atenção!", icon='INFO') 

# CONFIGURA MAXILA
def ConfiguraMaxilaDef(self, context):

    context = bpy.context
    obj = context.active_object
 #   scn = context.scene

    try: 
        ob=bpy.data.objects["Armature_Head"]

        bpy.ops.object.mode_set(mode='EDIT')
        mesh=bmesh.from_edit_mesh(bpy.context.object.data)
        for v in mesh.verts:
            v.select = True

        vg = obj.vertex_groups.new(name="Maxila.GUIA")
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.vertex_group_assign()
        bpy.ops.object.mode_set(mode='OBJECT')
        
        activeObject = bpy.context.active_object #Set active object to variable
        mat = bpy.data.materials.new(name="MaterialMaxila") #set new material to variable
        activeObject.data.materials.append(mat) #add the material to the object
        bpy.context.object.active_material.diffuse_color = (0.8, 0.3, 0.2) #change color
        bpy.context.object.name = "ma"

        armatureHead = bpy.data.objects['Armature_Head']
        bpy.ops.object.select_all(action='DESELECT')
        armatureHead.hide=False
        armatureHead.select=True
        bpy.context.scene.objects.active = armatureHead
        bpy.ops.object.posemode_toggle()
    #    bpy.data.objects['ma'].select = True
    #    bpy.data.objects['Armature_Head'].select = True
    #    bpy.ops.object.parent_set(type='ARMATURE_NAME')

        bpy.ops.pose.select_all(action='DESELECT')
        o=bpy.context.object
        b=o.data.bones['Maxila.GUIA']
        b.select=True
        o.data.bones.active=b
     
        bpy.ops.pose.constraint_add(type='CHILD_OF')
        bpy.context.object.pose.bones["Maxila.GUIA"].constraints["Child Of"].target = bpy.data.objects["ma"]

        pbone = bpy.context.active_object.pose.bones["Maxila.GUIA"] # Bone
        context_copy = bpy.context.copy()
        context_copy["constraint"] = pbone.constraints["Child Of"]
        bpy.ops.constraint.childof_set_inverse(context_copy, constraint="Child Of", owner='BONE')

        bpy.ops.object.posemode_toggle()
        armatureHead.hide=True
        
    except KeyError:
        bpy.context.window_manager.popup_menu(ERROarmatureDef, title="Atenção!", icon='INFO')

    except TypeError:
        bpy.context.window_manager.popup_menu(ERROtipoDef, title="Atenção!", icon='INFO')

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDef, title="Atenção!", icon='INFO')  

# CONFIGURA CABEÇA
def ConfiguraCabecaDef(self, context):

    context = bpy.context
    obj = context.active_object
 #   scn = context.scene


    try: 
        ob=bpy.data.objects["Armature_Head"]
        
        bpy.ops.object.mode_set(mode='EDIT')
        mesh=bmesh.from_edit_mesh(bpy.context.object.data)
        for v in mesh.verts:
            v.select = True

        vg = obj.vertex_groups.new(name="ca")
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.vertex_group_assign()
        bpy.ops.object.mode_set(mode='OBJECT')
        
        activeObject = bpy.context.active_object #Set active object to variable
        mat = bpy.data.materials.new(name="MaterialCabeca") #set new material to variable
        activeObject.data.materials.append(mat) #add the material to the object
        bpy.context.object.active_material.diffuse_color = (0.8, 0.75, 0.2) #change color
        bpy.context.object.name = "ca"

        armatureHead = bpy.data.objects['Armature_Head']
        bpy.ops.object.select_all(action='DESELECT')
        armatureHead.hide=False
        armatureHead.select=True
        bpy.context.scene.objects.active = armatureHead
        bpy.ops.object.posemode_toggle()
    #    bpy.data.objects['ca'].select = True
    #    bpy.data.objects['Armature_Head'].select = True
    #    bpy.ops.object.parent_set(type='ARMATURE_NAME')

        bpy.ops.pose.select_all(action='DESELECT')
        o=bpy.context.object
        b=o.data.bones['ca']
        b.select=True
        o.data.bones.active=b
     
        bpy.ops.pose.constraint_add(type='CHILD_OF')
        bpy.context.object.pose.bones["ca"].constraints["Child Of"].target = bpy.data.objects["ca"]

        pbone = bpy.context.active_object.pose.bones["ca"] # Bone
        context_copy = bpy.context.copy()
        context_copy["constraint"] = pbone.constraints["Child Of"]
        bpy.ops.constraint.childof_set_inverse(context_copy, constraint="Child Of", owner='BONE')

        bpy.ops.object.posemode_toggle()
        armatureHead.hide=True        
        
    except KeyError:
        bpy.context.window_manager.popup_menu(ERROarmatureDef, title="Atenção!", icon='INFO')

    except TypeError:
        bpy.context.window_manager.popup_menu(ERROtipoDef, title="Atenção!", icon='INFO')

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDef, title="Atenção!", icon='INFO')



def AreasInfluenciaDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    #vg = obj.vertex_groups.new(name=slot.material.name)
    bpy.ops.object.mode_set(mode='EDIT')
#    bpy.ops.object.editmode_toggle()
    mesh=bmesh.from_edit_mesh(bpy.context.object.data)
    for v in mesh.verts:
        v.select = True


    # CORPO MANDÍBULA

    vg = obj.vertex_groups.new(name="cm")
        
    scn.tool_settings.vertex_group_weight=0

    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.vertex_group_assign()


    # MAXILA

    vg = obj.vertex_groups.new(name="ma")
        
    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.vertex_group_assign()


    # MENTO

    vg = obj.vertex_groups.new(name="me")
        
    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.vertex_group_assign()


    # CABEÇA

    vg = obj.vertex_groups.new(name="ca")
        
    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.vertex_group_assign()


    # RAMO DIREITO
        
    vg = obj.vertex_groups.new(name="rd")
        
    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.vertex_group_assign()


    # RAMO ESQUERDO

    vg = obj.vertex_groups.new(name="re")
        
    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.vertex_group_assign()


    bpy.ops.object.mode_set(mode='OBJECT') # Depois de fazer tudo voltar ao modo de Objeto


def CriaAreasDeformacaoDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene


    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "me"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["me"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 25
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 3
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'SHARP'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Mento"
    bpy.context.object.modifiers["Mento"].show_expanded = False

    
    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "cm"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["cm"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 35
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 12
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'SHARP'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Corpo Mandibula"
    bpy.context.object.modifiers["Corpo Mandibula"].show_expanded = False
    
    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "re"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["re"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 35
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 12
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'SHARP'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Ramo Esquerdo"
    bpy.context.object.modifiers["Ramo Esquerdo"].show_expanded = False
    
    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "rd"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["rd"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 35
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 12
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'SHARP'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Ramo Direito"
    bpy.context.object.modifiers["Ramo Direito"].show_expanded = False
    
    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "ma"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["ma"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 37
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 9.5
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'SHARP'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Maxila"
    bpy.context.object.modifiers["Maxila"].show_expanded = False
    
    bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
    bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "ca"
    bpy.context.object.modifiers["VertexWeightProximity"].target = bpy.data.objects["ca"]
    bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
    bpy.context.object.modifiers["VertexWeightProximity"].min_dist = 90
    bpy.context.object.modifiers["VertexWeightProximity"].max_dist = 0
    bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'SHARP'
    bpy.context.object.modifiers["VertexWeightProximity"].name = "Cabeça"
    bpy.context.object.modifiers["Cabeça"].show_expanded = False

def GeraModelosTomoDef(self, context):
    
    scn = context.scene
    
    tmpdir = tempfile.gettempdir()
    tmpSTLossos = tmpdir+'/ossos.stl'
    tmpSTLmole = tmpdir+'/mole.stl'

    homeall = expanduser("~")

    try:


        if platform.system() == "Linux":


            dicom2DtlPath = get_dicom2stl_filepath(context)


            interesseOssos = bpy.context.scene.interesse_ossos
            interesseMole = bpy.context.scene.interesse_mole


            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', interesseOssos, '-o', tmpSTLossos])
	      

            bpy.ops.import_mesh.stl(filepath=tmpSTLossos, filter_glob="*.stl",  files=[{"name":"ossos.stl", "name":"ossos.stl"}], directory=tmpdir)
		
            bpy.ops.view3d.view_all(center=False)

            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', interesseMole, '-o', tmpSTLmole])

# CASO DIDATICO
#            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', '65', '-o', tmpSTLmole])

            bpy.ops.import_mesh.stl(filepath=tmpSTLmole, filter_glob="*.stl",  files=[{"name":"mole.stl", "name":"mole.stl"}], directory=tmpdir)


        if platform.system() == "Windows":

            dicom2DtlPath = 'C:/OrtogOnBlender/DicomToMeshWin/dicom2mesh.exe'

            interesseOssos = bpy.context.scene.interesse_ossos
            interesseMole = bpy.context.scene.interesse_mole


            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', interesseOssos, '-o', tmpSTLossos])
	      

            bpy.ops.import_mesh.stl(filepath=tmpSTLossos, filter_glob="*.stl",  files=[{"name":"ossos.stl", "name":"ossos.stl"}], directory=tmpdir)
		
            bpy.ops.view3d.view_all(center=False)
	      

            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', interesseMole, '-o', tmpSTLmole])

            bpy.ops.import_mesh.stl(filepath=tmpSTLmole, filter_glob="*.stl",  files=[{"name":"mole.stl", "name":"mole.stl"}], directory=tmpdir)


        if platform.system() == "Darwin":


            dicom2DtlPath = '/OrtogOnBlender/DicomToMeshMAC/dicom2mesh'

            interesseOssos = bpy.context.scene.interesse_ossos
            interesseMole = bpy.context.scene.interesse_mole

#            dicom2DtlPath = get_dicom2stl_filepath(context)


            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', interesseOssos, '-o', tmpSTLossos])
	      

            bpy.ops.import_mesh.stl(filepath=tmpSTLossos, filter_glob="*.stl",  files=[{"name":"ossos.stl", "name":"ossos.stl"}], directory=tmpdir)
		
            bpy.ops.view3d.view_all(center=False)
	      

            subprocess.call([dicom2DtlPath, '-i',  scn.my_tool.path, '-r', '0.9', '-s', '-t', interesseMole, '-o', tmpSTLmole])

            bpy.ops.import_mesh.stl(filepath=tmpSTLmole, filter_glob="*.stl",  files=[{"name":"mole.stl", "name":"mole.stl"}], directory=tmpdir)


        a = bpy.data.objects['Ossos']
        b = bpy.data.objects['Mole']

        bpy.ops.object.select_all(action='DESELECT')
        a.select = True
        bpy.context.scene.objects.active = a
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

        bpy.ops.object.select_all(action='DESELECT')
        b.select = True
        bpy.context.scene.objects.active = b
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

        bpy.ops.object.select_all(action='DESELECT')
        a.select = True
        b.select = True 
        bpy.context.scene.objects.active = a
        bpy.ops.object.parent_set()

        bpy.ops.transform.rotate(value=3.14159, axis=(0, 1, 0), constraint_axis=(False, True, False),
                                 constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED',
                                 proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.transform.rotate(value=3.14159, axis=(0, 0, 1), constraint_axis=(False, False, True),
                                 constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED',
                                 proportional_edit_falloff='SMOOTH', proportional_size=1)
                                 
        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = 0
        bpy.context.object.location[2] = 0

        bpy.ops.view3d.view_all(center=False)

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDICOMDef, title="Atenção!", icon='INFO')

def GeraModeloFotoDef(self, context):
    
    scn = context.scene
    
    tmpdir = tempfile.gettempdir()

    homeall = expanduser("~")

    try:

        OpenMVGtmpDir = tmpdir+'/OpenMVG'
        tmpOBJface = tmpdir+'/MVS/scene_dense_mesh_texture2.obj'

        
        if platform.system() == "Linux":
            OpenMVGPath = homeall+'/Programs/OrtogOnBlender/openMVG/software/SfM/SfM_SequentialPipeline.py'
            OpenMVSPath = homeall+'/Programs/OrtogOnBlender/openMVS/OpenMVS'
            
        if platform.system() == "Windows":
            OpenMVGPath = 'C:/OrtogOnBlender/openMVGWin/software/SfM/SfM_SequentialPipeline.py' 
            OpenMVSPath = 'C:/OrtogOnBlender/openMVSWin/OpenMVS.bat' 

        if platform.system() == "Darwin":
   #         if platform.release() == '15.6.0':
#                OpenMVGPath = '/OrtogOnBlender/openMVGMACelcap/SfM_SequentialPipeline.py' 
#                OpenMVSPath = '/OrtogOnBlender/openMVSMACelcap/openMVSMAC.sh' 
#            if platform.release() == '17.5.0':
#                OpenMVGPath = '/OrtogOnBlender/openMVGMACelcap/SfM_SequentialPipeline.py' 
#                OpenMVSPath = '/OrtogOnBlender/openMVSMACelcap/openMVSMAC.sh'                       
#            else:
#                OpenMVGPath = '/OrtogOnBlender/openMVGMAC/SfM_SequentialPipeline.py' 
#                OpenMVSPath = '/OrtogOnBlender/openMVSMAC/openMVSMAC.sh'
            OpenMVGPath = '/OrtogOnBlender/openMVGMACelcap/SfM_SequentialPipeline.py' 
            OpenMVSPath = '/OrtogOnBlender/openMVSMACelcap/openMVSMAC.sh'

        shutil.rmtree(tmpdir+'/OpenMVG', ignore_errors=True)
        shutil.rmtree(tmpdir+'/MVS', ignore_errors=True)

    #    if os.name=='posix':
    #    	shutil.rmtree(tmpdir+'/OpenMVG')
    #    	shutil.rmtree(tmpdir+'/MVS')

    #    if os.name=='nt':
    #    	subprocess.call(['rmdir', '/Q', '/S', tmpdir+'/OpenMVG'])
    #    	subprocess.call(['rmdir', '/Q', '/S', tmpdir+'/MVS'])


        if platform.system() == "Linux":
            subprocess.call(['python', OpenMVGPath , scn.my_tool.path ,  OpenMVGtmpDir])
            
        if platform.system() == "Windows":
            subprocess.call(['C:/OrtogOnBlender/Python27/python', OpenMVGPath , scn.my_tool.path ,  OpenMVGtmpDir])

        if platform.system() == "Darwin":
            subprocess.call(['python', OpenMVGPath , scn.my_tool.path ,  OpenMVGtmpDir])

        subprocess.call(OpenMVSPath ,  shell=True)

    #    subprocess.call([ 'meshlabserver', '-i', tmpdir+'scene_dense_mesh_texture.ply', '-o', tmpdir+'scene_dense_mesh_texture2.obj', '-om', 'vn', 'wt' ])



        bpy.ops.import_scene.obj(filepath=tmpOBJface, filter_glob="*.obj;*.mtl")

        scene_dense_mesh_texture2 = bpy.data.objects['scene_dense_mesh_texture2']

        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = scene_dense_mesh_texture2
        bpy.data.objects['scene_dense_mesh_texture2'].select = True


        bpy.context.object.data.use_auto_smooth = False
        bpy.context.object.active_material.specular_hardness = 60
        bpy.context.object.active_material.diffuse_intensity = 0.6
        bpy.context.object.active_material.specular_intensity = 0.3
        bpy.context.object.active_material.specular_color = (0.233015, 0.233015, 0.233015)
    #    bpy.ops.object.modifier_add(type='SMOOTH')
    #    bpy.context.object.modifiers["Smooth"].factor = 2
    #    bpy.context.object.modifiers["Smooth"].iterations = 3
    #    bpy.ops.object.convert(target='MESH')
    #    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Smooth")    
    
        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
        bpy.ops.view3d.view_all(center=False)
        bpy.ops.file.pack_all()
        
        bpy.ops.object.modifier_add(type='SMOOTH')
        bpy.context.object.modifiers["Smooth"].factor = 2
        bpy.context.object.modifiers["Smooth"].iterations = 4
        
    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeFotosDef, title="Atenção!", icon='INFO')


def GeraModeloFotoSMVSDef(self, context):

    scn = context.scene
        
    tmpdir = tempfile.gettempdir()
    tmpOBJface = tmpdir+'/scene/scene_dense_mesh_texture2.obj'
#    subprocess.call(['rm /tmp/DIRETORIO_FOTOS.txt'],  shell=True)
    


    try:

        if platform.system() == "Linux":
            SMVSPath = get_SMVS_filepath(context)
            subprocess.call(['rm', '-rf', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./makescene', '-i', scn.my_tool.path, tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./sfmrecon', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./smvsrecon', '-s2', tmpdir+'/scene'])
            subprocess.call(['meshlabserver', '-i', tmpdir+'/scene/smvs-B2.ply', '-o', tmpdir+'/scene/meshlab.ply', '-s', SMVSPath+'SMVSmeshlab.mlx', '-om'])
            subprocess.call([SMVSPath+'./texrecon', '--data_term=area', '--skip_global_seam_leveling', '--outlier_removal=gauss_damping', tmpdir+'/scene::undistorted', tmpdir+'/scene/meshlab.ply', tmpdir+'/scene/scene_dense_mesh_texture2'])
            bpy.ops.import_scene.obj(filepath=tmpOBJface, filter_glob="*.obj;*.mtl")
            scene_dense_mesh_texture2 = bpy.data.objects['scene_dense_mesh_texture2']
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.scene.objects.active = scene_dense_mesh_texture2
            bpy.data.objects['scene_dense_mesh_texture2'].select = True
            bpy.ops.view3d.view_all(center=False)
            bpy.ops.file.pack_all()


        if platform.system() == "Windows":
            SMVSPath = 'C:/OrtogOnBlender/SMVS/'
#            shutil.rmtree(tmpdir+'/scene')
            subprocess.call([SMVSPath+'./makescene', '-i', scn.my_tool.path, tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./sfmrecon', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./smvsrecon', '-s2', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./fssrecon', tmpdir+'/scene/smvs-B2.ply', tmpdir+'/scene/smvs-surface.ply'])
            subprocess.call([SMVSPath+'./meshclean', '-p10', tmpdir+'/scene/smvs-surface.ply', tmpdir+'/scene/smvs-surface-clean.ply'])
            tmpPLYface = tmpdir+'/scene/smvs-surface-clean.ply'        
            bpy.ops.import_mesh.ply(filepath=tmpPLYface, filter_glob="*.ply")
            smvs_surface_clean = bpy.data.objects['smvs-surface-clean']
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.scene.objects.active = smvs_surface_clean
            bpy.data.objects['smvs-surface-clean'].select = True
            bpy.ops.view3d.view_all(center=False)
            bpy.ops.file.pack_all()        


        if platform.system() == "Darwin":
            homemac = expanduser("~")
            SMVSPath = '/OrtogOnBlender/SMVSMAC/'

            subprocess.call(['rm', '-Rf', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./makescene', '-i', scn.my_tool.path, tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./sfmrecon', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./smvsrecon', '-s2', tmpdir+'/scene'])
            subprocess.call([SMVSPath+'./fssrecon', '-s4', tmpdir+'/scene/smvs-B2.ply', tmpdir+'/scene/smvs-surface.ply'])
            subprocess.call([SMVSPath+'./meshclean', '-p10', tmpdir+'/scene/smvs-surface.ply', tmpdir+'/scene/smvs-clean.ply'])
            subprocess.call(['rm', '-Rf', tmpdir+'/scene/tmp'])
            subprocess.call([SMVSPath+'./texrecon', '--data_term=area', '--skip_global_seam_leveling', '--outlier_removal=gauss_damping', tmpdir+'/scene::undistorted', tmpdir+'/scene/smvs-clean.ply', tmpdir+'/scene/scene_dense_mesh_texture2'])

            bpy.ops.import_scene.obj(filepath=tmpOBJface, filter_glob="*.obj;*.mtl")
            scene_dense_mesh_texture2 = bpy.data.objects['scene_dense_mesh_texture2']
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.scene.objects.active = scene_dense_mesh_texture2
            bpy.data.objects['scene_dense_mesh_texture2'].select = True
            bpy.ops.view3d.view_all(center=False)
            bpy.ops.file.pack_all()


    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeFotosDef, title="Atenção!", icon='INFO')

# ------------------------

def ConfiguraDinamicaMoleDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.areas_influencia()
    bpy.ops.object.cria_areas_deformacao()
    bpy.ops.object.convert(target='MESH')


#    a = bpy.data.objects['FaceMalha.001']
    armatureHead = bpy.data.objects['Armature_Head']

    armatureHead.hide=False

    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.scene.objects.active = armatureHead
    bpy.data.objects['FaceMalha.001'].select = True
    bpy.data.objects['Armature_Head'].select = True
    bpy.ops.object.parent_set(type='ARMATURE_NAME')

    armatureHead.hide=True

class CortaFace(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.corta_face"
    bl_label = "Corta Face"
    
    def execute(self, context):
        CortaFaceDef(self, context)
        return {'FINISHED'}


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

    def end_ui(self, context):            
        context.area.header_text_set()
        context.window.cursor_modal_restore()
        
    def cleanup(self, context, cleantype=''):
        '''
        remove temporary object
        '''
        if cleantype == 'commit':
            pass

        elif cleantype == 'cancel':
            pass

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

class ConfiguraDinamicaMole(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_dinamica_mole"
    bl_label = "Configura Dinâmica do Mole"
    
    def execute(self, context):
        ConfiguraDinamicaMoleDef(self, context)
        return {'FINISHED'}

# IMPORTA SPLINT COM ARMATURE

def ImportaSplintDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene


    if platform.system() == "Linux":

        dirScript = bpy.utils.user_resource('SCRIPTS')

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Group\\"
        object    = "SPLINT"

    if platform.system() == "Darwin":

        dirScript = bpy.utils.user_resource('SCRIPTS')

        blendfile = "/OrtogOnBlender/Blender/blender.app/Contents/Resources/2.78/scripts/addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Group\\"
        object    = "SPLINT"
        
    if platform.system() == "Windows":

        dirScript = 'C:/OrtogOnBlender/Blender/2.78/scripts/'

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Group\\"
        object    = "SPLINT"    


#    if platform.system() == "Darwin":

#        dirScript = bpy.utils.user_resource('SCRIPTS')

#        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
#        section   = "\\Group\\"
#        object    = "SPLINT"


    filepath  = blendfile + section + object
    directory = blendfile + section
    filename  = object

    bpy.ops.wm.append(
        filepath=filepath, 
        filename=filename,
        directory=directory)
        

class ImportaSplint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.importa_splint"
    bl_label = "Importa Splint com Armature"
    
    def execute(self, context):
        ImportaSplintDef(self, context)
        return {'FINISHED'}

# PONTOS NOS DENTES SUPERIORES

def EMP11Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP11"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP11']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    

class EMP11(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp11"
    bl_label = "EMP11"
    
    def execute(self, context):
        EMP11Def(self, context)
        return {'FINISHED'}

def EMP21Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP21"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP21']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    

class EMP21(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp21"
    bl_label = "EMP21"
    
    def execute(self, context):
        EMP21Def(self, context)
        return {'FINISHED'}
    
def EMP13Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP13"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP13']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    

class EMP13(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp13"
    bl_label = "EMP1"
    
    def execute(self, context):
        EMP13Def(self, context)
        return {'FINISHED'}
    
def EMP23Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP23"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP23']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    

class EMP23(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp23"
    bl_label = "EMP23"
    
    def execute(self, context):
        EMP23Def(self, context)
        return {'FINISHED'}
    
def EMP16Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP16"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP16']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    

class EMP16(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp16"
    bl_label = "EMP16"
    
    def execute(self, context):
        EMP16Def(self, context)
        return {'FINISHED'}
    
def EMP26Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP26"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['ma']
    b = bpy.data.objects['EMP26']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    

class EMP26(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp26"
    bl_label = "EMP26"
    
    def execute(self, context):
        EMP26Def(self, context)
        return {'FINISHED'}

# PONTOS NOS DENTES INFERIORES

def EMP31Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP31"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP31']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    

class EMP31(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp31"
    bl_label = "EMP31"
    
    def execute(self, context):
        EMP31Def(self, context)
        return {'FINISHED'}

def EMP41Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP41"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP41']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    

class EMP41(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp41"
    bl_label = "EMP41"
    
    def execute(self, context):
        EMP41Def(self, context)
        return {'FINISHED'}
    
def EMP33Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP33"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP33']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    

class EMP33(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp33"
    bl_label = "EMP33"
    
    def execute(self, context):
        EMP33Def(self, context)
        return {'FINISHED'}
    
def EMP43Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP43"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP43']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    

class EMP43(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp43"
    bl_label = "EMP43"
    
    def execute(self, context):
        EMP43Def(self, context)
        return {'FINISHED'}
    
def EMP36Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP36"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP36']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    

class EMP36(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp36"
    bl_label = "EMP36"
    
    def execute(self, context):
        EMP36Def(self, context)
        return {'FINISHED'}
    
def EMP46Def(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP46"
    bpy.context.object.empty_draw_size = 3
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP46']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    

class EMP46(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp46"
    bl_label = "EMP46"
    
    def execute(self, context):
        EMP46Def(self, context)
        return {'FINISHED'}
    
# CRIA EMPTIES INTERMEDIÁRIOS

def CriaSplintDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.select_all(action='DESELECT')

    a = bpy.data.objects['EMP11']
    b = bpy.data.objects['EMP41']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP1141"
    bpy.context.object.empty_draw_size = .5
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP1141']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')


    # ----------------------------

    a = bpy.data.objects['EMP21']
    b = bpy.data.objects['EMP31']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP2131"
    bpy.context.object.empty_draw_size = .5
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP2131']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    
    # ----------------------------

    a = bpy.data.objects['EMP23']
    b = bpy.data.objects['EMP33']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP2333"
    bpy.context.object.empty_draw_size = .5
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP2333']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    
    # ----------------------------

    a = bpy.data.objects['EMP13']
    b = bpy.data.objects['EMP43']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP1343"
    bpy.context.object.empty_draw_size = .5
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP1343']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    
    # ----------------------------

    a = bpy.data.objects['EMP26']
    b = bpy.data.objects['EMP36']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP2636"
    bpy.context.object.empty_draw_size = .5
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP2636']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    
    # ----------------------------

    a = bpy.data.objects['EMP16']
    b = bpy.data.objects['EMP46']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP1646"
    bpy.context.object.empty_draw_size = .5
    
    
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP1646']

    bpy.ops.object.select_all(action='DESELECT')
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    
    # ---------------
    
    bpy.ops.object.importa_splint()
    
    # --------------
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP1646']                 
    a.select = True
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone1646']                 
    a.select = True
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP1343']                 
    a.select = True
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone1343']                 
    a.select = True
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP1141']                 
    a.select = True
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone1141']                 
    a.select = True
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP2131']                 
    a.select = True
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone2131']                 
    a.select = True
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP2333']                 
    a.select = True
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone2333']                 
    a.select = True
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP2636']                 
    a.select = True
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone2636']                 
    a.select = True
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

    
class CriaSplint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_splint"
    bl_label = "Cria Splint"
    
    def execute(self, context):
        CriaSplintDef(self, context)
        return {'FINISHED'}

def ConfSplintDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.select_all(action='DESELECT')

    a = bpy.data.objects['ma']
    b = bpy.data.objects['cm']

    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
    
    bpy.ops.object.duplicate()
    bpy.ops.object.join()
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['SPLINT']
    a.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.duplicate()
    
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['SPLINT']
    a.select = True
    bpy.context.scene.objects.active = a
    bpy.ops.object.hide_view_set(unselected=False)
        
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['ma.001']
    b = bpy.data.objects['SPLINT.001']
    a.select = True
    b.select = True 
    bpy.context.scene.objects.active = a
#    bpy.ops.view3d.cork_mesh_slicer(method='DIFF')            
    
class ConfSplint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.conf_splint"
    bl_label = "Boolean Splint"
    
    def execute(self, context):
        ConfSplintDef(self, context)
        return {'FINISHED'}

#IMPORTA TOMO

class CapturaLocal(PropertyGroup):

    path = StringProperty(
        name="",
        description="Path to Directory",
        default="",
        maxlen=1024,
        subtype='DIR_PATH')

class ImportaTomo(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Importa Tomo"
    bl_idname = "importa_tomo"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        scn = context.scene
        obj = context.object 
        
        row = layout.row()
        row.label(text="Reconstrução da Tomografia:")

        col = layout.column(align=True)
        col.prop(scn.my_tool, "path", text="")

        col = self.layout.column(align = True)
        col.prop(context.scene, "interesse_ossos")

        col = self.layout.column(align = True)
        col.prop(context.scene, "interesse_mole")

        row = layout.row()
        row.operator("object.gera_modelos_tomo", text="Converte DICOM para 3D", icon="SNAP_FACE")
        

        row = layout.row()
        row.label(text="Referências Gráficas:")

        row = layout.row()
        linha=row.operator("mesh.add_linhabase", text="Linha Central Ver", icon="PAUSE")
        linha.location=(0,-200,0)

        row = layout.row()
        linha=row.operator("mesh.add_linhabase", text="Linha Central Hor", icon="ZOOMOUT")
        linha.location=(0,-200,0)
        linha.rotation=(0,1.5708,0)
        
        row = layout.row()
        linha=row.operator("mesh.add_linhabase", text="Linha Lateral Hor", icon="ZOOMOUT")
        linha.location=(200,30,0)
        linha.rotation=(1.5708,0,0)

        row = layout.row()
        row.label(text="Segmentação Mandíbula:")
        
        row = layout.row()
        linha=row.operator("mesh.select_more", text="Sel. Mais", icon="ZOOMIN")
        
        linha=row.operator("mesh.select_less", text="Sel. Menos", icon="ZOOMOUT")     
  
        row = layout.row()
        row.label(text="Importação das Arcadas:")

        col = layout.column(align=True)
        col.prop(scn.my_tool, "path", text="")
 
        row = layout.row()
        row.operator("object.gera_modelos_tomo_arc", text="Gera Arcada", icon="SNAP_FACE")

        row = layout.row()
        row.operator("import_mesh.stl", text="Importa STL", icon="IMPORT")
        
        row = layout.row()
        row.operator("object.align_picked_points", text="Alinha Mode Pontos", icon="PARTICLE_TIP")

        row = layout.row()
        row.operator("object.align_icp", text="Alinha Molde ICP", icon="PARTICLE_PATH")
        
        row = layout.row()
        circle=row.operator("object.join", text="Junta com Molde", icon="GROUP")       


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

# FOTOGRAMETRIA

class CriaFotogrametria(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Cria Fotogrametria"
    bl_idname = "cria_fotogrametria"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"


    def draw(self, context):
        layout = self.layout
        scn = context.scene
        obj = context.object 
        
        col = layout.column(align=True)
        col.prop(scn.my_tool, "path", text="")
 
        row = layout.row()
        row.operator("object.gera_modelo_foto", text="Iniciar Fotogrametria", icon="IMAGE_DATA")

        row = layout.row()
        row.operator("object.gera_modelo_foto_smvs", text="SMVS+Meshlab", icon="IMAGE_DATA")

        
#       print (scn.my_tool.path)
 

      
#IMPORTA OBJ
   
class OOB_import_obj(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Importar Fotogrametria"
    bl_idname = "import_obj"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("import_scene.obj", text="Importa OBJ", icon="MOD_MASK")
        #ORIGINAL bpy.ops.import_mesh.stl()
        
        row = layout.row()
        circle=row.operator("mesh.primitive_circle_add", text="Círculo de Corte", icon="MESH_CIRCLE")
        circle.radius=200
        circle.vertices=100
        circle.location=(85,-185,0)
        circle.rotation=(0,1.5708,0)

        row = layout.row()
        knife=row.operator("object.corta_face", text="Cortar!", icon="META_PLANE")
        
        
        
            
# IMPORTA CEFALOMETRIA

class ImportaCefalometria(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Importar Cefalometria"
    bl_idname = "Importa_Cefalometria"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("import_image.to_plane", text="Importa Imagem", icon="FILE_IMAGE")

#ALINHA FACES

class AlinhaMaxila(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Alinha Face (Novo)"
    bl_idname = "Alinha Face 2"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("object.colocapontos", text="3 Pontos", icon="CURSOR")

        col = self.layout.column(align = True)
        col.prop(context.scene, "medida_real2")

        row = layout.row()
        row.operator("object.calcalinhamand", text="Alinhar e Redimensionar", icon="FILE_TICK")

class AlinhaFaces(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Alinha Face (Antigo)"
    bl_idname = "alinha_faces"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()        
        row.label(text="Alinhamento e Redimensionamento:")
        layout.operator("object.alinha_rosto", text="1 - Alinha com a Camera", icon="MANIPUL")
        col = self.layout.column(align = True)
        col.prop(context.scene, "medida_real")  
        layout.operator("object.alinha_rosto2", text="2 - Alinha e Redimensiona", icon="LAMP_POINT")
        
        row = layout.row()
        row.operator("object.rotaciona_z", text="Flip Z", icon="FORCE_MAGNETIC")

        row = layout.row()
        row.label(text="Alinhamento por Pontos:")

        row = layout.row()
        row.operator("object.align_picked_points", text="Alinha por Pontos", icon="PARTICLE_TIP")

        row = layout.row()
        row.operator("object.align_icp", text="Alinha ICP", icon="PARTICLE_PATH")
    

# OSTEOTOMIA

class Osteotomia(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Osteotomia"
    bl_idname = "Object_Name"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        
        obj = context.object
       
        row = layout.row()
        circle=row.operator("mesh.add_mento", text="Plano Mento", icon="TRIA_DOWN")
        circle.location=(0,-35,-81)
        
        row = layout.row()
        circle=row.operator("mesh.add_ramo", text="Plano Ramo Esquerdo", icon="TRIA_RIGHT")
        circle.location=(36, -4, -45)
        
        row = layout.row()
        circle=row.operator("mesh.add_ramo", text="Plano Ramo Direito", icon="TRIA_LEFT")
        circle.location=(-36, -4, -45)
        
        row = layout.row()
        circle=row.operator("mesh.add_maxila", text="Plano Maxila", icon="TRIA_UP")
        circle.location=(0, -45, -31)
 
        row = layout.row()
        circle=row.operator("object.join", text="Junta Tudo", icon="GROUP")
    
        
        row = layout.row()
        circle=row.operator("object.cria_espessura", text="Cria Espessura", icon="MOD_SOLIDIFY")
               
        row = layout.row()
        circle=row.operator("view3d.cork_mesh_slicer", text="Boolean Cortes", icon="MOD_BOOLEAN")
        circle.method='DIFF'
        
        # Não é necessário estar em Object Mode
        row = layout.row()
        circle=row.operator("mesh.separate", text="Separa Osteotomia", icon="GROUP_VERTEX")
        circle.type='LOOSE'
        
        row = layout.row()
        circle=row.operator("object.importa_armature", text="Configura Armature", icon="GROUP_BONE")        

        row = layout.row()        
        row.label(text="Configura Peças:")

        row = layout.row()
        row.operator("object.configura_cabeca", text="Configura Cabeça")

        row = layout.row()
        row.operator("object.configura_maxila", text="Configura Maxila")

        row = layout.row()
        row.operator("object.configura_ramo_dir", text="Configura Ramo Direito")

        row = layout.row()
        row.operator("object.configura_ramo_esq", text="Configura Ramo Esquerdo")

        row = layout.row()
        row.operator("object.configura_corpo_mand", text="Configura Corpo Mandíbula")

        row = layout.row()
        row.operator("object.configura_mento", text="Configura Mento")

        
class DinamicaMole(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Dinâmica do Mole"
    bl_idname = "Dinamica_Mole"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        
        obj = context.object
              

        row = layout.row()
        circle=row.operator("object.configura_dinamica_mole", text="Configura Dinâmica Mole", icon="STYLUS_PRESSURE")
       
        row = layout.row()
        circle=row.operator("view3d.clip_border", text="Filete de Visualização", icon="UV_FACESEL")

# SPLINT

class CriaSplintPanel(bpy.types.Panel):
    """Planejamento de cirurgia ortognática no Blender"""
    bl_label = "Criação do Splint"
    bl_idname = "Cria_Splint"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Ortog"

    def draw(self, context):
        layout = self.layout
        
        obj = context.object
        
        row = layout.row()
        row.operator("screen.frame_jump", text="Inicio", icon="REW").end=False
        row.operator("screen.animation_play", text="", icon="PLAY_REVERSE").reverse=True
        row.operator("anim.animalocrot", text="", icon="CLIP")
        row.operator("screen.animation_play", text="", icon="PLAY")
        row.operator("screen.frame_jump", text="Final", icon="FF").end=True
        
        row = layout.row()        
        row.label(text="Arcada Superior:")

        row = layout.row()
        row.operator("object.emp11", text="Dente 11", icon="X")

        row = layout.row()
        row.operator("object.emp21", text="Dente 21", icon="X")
        
        row = layout.row()
        row.operator("object.emp13", text="Dente 13", icon="X")       

        row = layout.row()
        row.operator("object.emp23", text="Dente 23", icon="X") 
        
        row = layout.row()
        row.operator("object.emp16", text="Dente 16", icon="X")
        
        row = layout.row()
        row.operator("object.emp26", text="Dente 26", icon="X")
        
        row = layout.row()        
        row.label(text="Arcada Inferior:") 

        row = layout.row()
        row.operator("object.emp31", text="Dente 31", icon="X")
        
        row = layout.row()
        row.operator("object.emp41", text="Dente 41", icon="X")
        
        row = layout.row()
        row.operator("object.emp33", text="Dente 33", icon="X")

        row = layout.row()
        row.operator("object.emp43", text="Dente 43", icon="X")
        
        row = layout.row()
        row.operator("object.emp36", text="Dente 36", icon="X")
        
        row = layout.row()
        row.operator("object.emp46", text="Dente 46", icon="X")

        row = layout.row()        
        row.label(text="Configuração do Splint:") 

        row = layout.row()
        row.operator("object.cria_splint", text="Cria Splint", icon="OUTLINER_OB_CURVE")

        row = layout.row()
        row.operator("object.conf_splint", text="Prepara Boolean", icon="RECOVER_AUTO")        
        
        row = layout.row()
        circle=row.operator("view3d.cork_mesh_slicer", text="Boolean Cortes", icon="MOD_BOOLEAN")
        circle.method='DIFF'    

#        row = layout.row()
#        circle=row.operator("object.convert", text="Aplica Deformação", icon="FILE_TICK").target='MESH'
    
        row = layout.row()
        row.operator("object.prepara_impressao", text="Prepara Impressão 3D", icon="MOD_REMESH")
        
        row = layout.row()
        row.operator("export_mesh.stl", text="Exporta STL", icon="EXPORT")


def register():
    bpy.utils.register_class(StartCallback)
    bpy.utils.register_class(StopCallback)
    bpy.types.Scene.medida_real2 = bpy.props.StringProperty \
      (
        name = "Medida Real",
        description = "Medida real distância cantal",
        default = "1"
      )
    bpy.utils.register_class(ColocaPontos)
    bpy.utils.register_class(CalcAlinhaMandibula)
    bpy.utils.register_class(ortogPreferences)
#    bpy.utils.register_class(ortogPreferences2)
    bpy.utils.register_class(CriaMento)
    bpy.types.INFO_MT_mesh_add.append(add_object_button)
    bpy.utils.register_class(CortaFace)
    bpy.utils.register_class(AlinhaRosto)
#    bpy.utils.register_class(MedidaReal)
    bpy.types.Scene.medida_real = bpy.props.StringProperty \
      (
        name = "Medida Real",
        description = "Medida real distância cantal",
        default = "1"
      )
    bpy.utils.register_class(AlinhaRosto2)
    bpy.utils.register_class(AnimaLocRot)
    bpy.utils.register_class(rotacionaZ)
    bpy.utils.register_class(GeraModelosTomoArc)
    bpy.utils.register_class(LinhaBase)
    bpy.utils.register_class(ImportaArmature)
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
        name = "Fator Ossos",
        description = "Fatos interesse ossos",
        default = "200"
      )
    bpy.types.Scene.interesse_mole = bpy.props.StringProperty \
      (
        name = "Fator Mole",
        description = "Fatos interesse mole",
        default = "-300"
      )
    bpy.utils.register_class(GeraModelosTomo)
    bpy.utils.register_class(GeraModeloFoto)
    bpy.utils.register_class(GeraModeloFotoSMVS)
    bpy.utils.register_class(ConfiguraDinamicaMole)
    bpy.utils.register_class(ImportaTomo)
    bpy.utils.register_class(ZoomCena)
    bpy.utils.register_class(CriaFotogrametria)
    bpy.utils.register_class(AlinhaMaxila)
    bpy.utils.register_class(AlinhaFaces)
    bpy.utils.register_class(OOB_import_obj)
    bpy.utils.register_class(ImportaCefalometria)
    bpy.utils.register_class(Osteotomia)
    bpy.utils.register_class(DinamicaMole)
    bpy.utils.register_class(CriaSplint)
    bpy.utils.register_class(CapturaLocal)
    bpy.types.Scene.my_tool = PointerProperty(type=CapturaLocal)
    bpy.utils.register_class(ImportaSplint)
    bpy.utils.register_class(EMP11)
    bpy.utils.register_class(EMP21)
    bpy.utils.register_class(EMP13)
    bpy.utils.register_class(EMP23)
    bpy.utils.register_class(EMP16)
    bpy.utils.register_class(EMP26)
    bpy.utils.register_class(EMP31)
    bpy.utils.register_class(EMP41)
    bpy.utils.register_class(EMP33)
    bpy.utils.register_class(EMP43)
    bpy.utils.register_class(EMP36)
    bpy.utils.register_class(EMP46)
    bpy.utils.register_class(CriaSplintPanel)
    bpy.utils.register_class(ConfSplint)


def unregister():
    bpy.utils.unregister_class(StartCallback)
    bpy.utils.unregister_class(StopCallback)
    del bpy.types.Scene.medida_real
    bpy.utils.register_class(ColocaPontos)
    bpy.utils.register_class(CalcAlinhaMandibula)
    bpy.utils.unregister_class(AlinhaMaxila)
    bpy.utils.unregister_class(ortogPreferences)
#    bpy.utils.unregister_class(ortogPreferences2)
    bpy.utils.unregister_class(CortaFace)
    bpy.utils.unregister_class(AlinhaRosto)
#    bpy.utils.register_class(MedidaReal)
    del bpy.types.Scene.medida_real
    bpy.utils.unregister_class(AlinhaRosto2)
    bpy.utils.unregister_class(AnimaLocRot)
    bpy.utils.unregister_class(rotacionaZ)
    bpy.utils.unregister_class(GeraModelosTomoArc)
    bpy.utils.unregister_class(LinhaBase)
    bpy.utils.unregister_class(ImportaArmature)
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
    del bpy.types.Scene.interesse_ossos
    del bpy.types.Scene.interesse_mole
    bpy.utils.unregister_class(ImportaTomo)
    bpy.utils.unregister_class(ZoomCena)
    bpy.utils.unregister_class(CriaFotogrametria)
    bpy.utils.unregister_class(AlinhaFaces)
    bpy.utils.unregister_class(OOB_import_obj)
    bpy.utils.unregister_class(ImportaCefalometria)
    bpy.utils.unregister_class(Osteotomia)
    bpy.utils.unregister_class(DinamicaMole)
    bpy.utils.unregister_class(CapturaLocal)
    bpy.utils.unregister_class(CriaSplint)
    bpy.utils.unregister_class(ImportaSplint)
    bpy.utils.unregister_class(EMP11)
    bpy.utils.unregister_class(EMP21)
    bpy.utils.unregister_class(EMP13)
    bpy.utils.unregister_class(EMP23)
    bpy.utils.unregister_class(EMP16)
    bpy.utils.unregister_class(EMP26)
    bpy.utils.unregister_class(EMP31)
    bpy.utils.unregister_class(EMP41)
    bpy.utils.unregister_class(EMP33)
    bpy.utils.unregister_class(EMP43)
    bpy.utils.unregister_class(EMP36)
    bpy.utils.unregister_class(EMP46)
    bpy.utils.unregister_class(CriaSplintPanel)
    bpy.utils.unregister_class(ConfSplint)

if __name__ == "__main__":
    register()

#Example:

#The comparaison (for cursor location, it is a vector comparison)
def CompareLocation( l1, l2 ):
    return l1 == l2

#The callback to execute when the cursor's location changes
def CompareLocationCallback( watcher, newValue ):
    print( 'New value', newValue )

#Install the watcher which will run the callback
#EventWatcher.AddWatcher( EventWatcher( bpy.data.scenes[0], "cursor_location", CompareLocation, CompareLocationCallback, True ) )