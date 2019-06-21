import bpy

from mathutils import Matrix, Vector

from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )
from bpy_extras.object_utils import AddObjectHelper, object_data_add

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

class CriaMento(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_mento"
    bl_label = "Add Mento"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        CriaMentoDef(self, context)

        return {'FINISHED'}


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

class CriaMaxila(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_maxila"
    bl_label = "Add Maxila"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        CriaMaxilaDef(self, context)

        return {'FINISHED'}

# MALHA ALINHA ORIGEM

def CriaMeshAlinhOrigDef(self, context):
    
    context = bpy.context

    vec0 = bpy.data.objects['EMP1a'].location
    vec1 = bpy.data.objects['EMP2a'].location
    vec2 = bpy.data.objects['EMP3a'].location

    verts = [Vector((vec0)),
             Vector((vec1)),
             Vector((vec2)),
            ]

    edges = []
    faces = [[0, 1, 2]]

    mesh = bpy.data.meshes.new(name="MeshAlignOrigi")
    mesh.from_pydata(verts, edges, faces)
    object_data_add(context, mesh, operator=self)



class CriaMeshAlinhOrig(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_mesh_alinha_origi"
    bl_label = "Add Mesh Align Origin"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        CriaMeshAlinhOrigDef(self, context)
        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = 0
        bpy.context.object.location[2] = 0
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')

        return {'FINISHED'}

# MALHA ALINHA ORIGEM

def CriaMeshAlinhAlinhDef(self, context):
    
    context = bpy.context

    vec0 = bpy.data.objects['EMP1b'].location
    vec1 = bpy.data.objects['EMP2b'].location
    vec2 = bpy.data.objects['EMP3b'].location

    verts = [Vector((vec0)),
             Vector((vec1)),
             Vector((vec2)),
            ]

    edges = []
    faces = [[0, 1, 2]]

    mesh = bpy.data.meshes.new(name="MeshAlignAlign")
    mesh.from_pydata(verts, edges, faces)
    object_data_add(context, mesh, operator=self)



class CriaMeshAlinhAlinh(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_mesh_alinha_alinha"
    bl_label = "Add Mesh Align Align"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        CriaMeshAlinhAlinhDef(self, context)
        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = 0
        bpy.context.object.location[2] = 0
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')

        return {'FINISHED'}

bpy.utils.register_class(CriaMeshAlinhOrig)
bpy.utils.register_class(CriaMeshAlinhAlinh)
