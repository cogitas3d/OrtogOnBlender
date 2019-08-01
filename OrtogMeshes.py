import bpy

from random import randint
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

    bpy.context.object.show_wire = True

    context = bpy.context
    activeObject = context.object

    mat = bpy.data.materials.new(name='Mat_'+activeObject.name) #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    activeObject.active_material.diffuse_color = (randint(20, 100)*.01, randint(20, 100)*.01, randint(20, 100)*.01, 1)


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

    bpy.context.object.show_wire = True

    context = bpy.context
    activeObject = context.object

    mat = bpy.data.materials.new(name='Mat_'+activeObject.name) #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    activeObject.active_material.diffuse_color = (randint(20, 100)*.01, randint(20, 100)*.01, randint(20, 100)*.01, 1)


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
    faces = [[0, 1, 2, 3],[5,4,3,2],[4, 5, 6, 7]]

    mesh = bpy.data.meshes.new(name="Maxila")
    mesh.from_pydata(verts, edges, faces)
    object_data_add(context, mesh, operator=self)

    bpy.ops.object.modifier_add(type='SOLIDIFY') 
    bpy.context.object.modifiers["Solidify"].thickness = 0.3
    bpy.context.object.modifiers["Solidify"].offset = 0

    bpy.context.object.show_wire = True

    context = bpy.context
    activeObject = context.object

    mat = bpy.data.materials.new(name='Mat_'+activeObject.name) #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    activeObject.active_material.diffuse_color = (randint(20, 100)*.01, randint(20, 100)*.01, randint(20, 100)*.01, 1)


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



def AdicionaPlanosCorteAutoDef():

    context = bpy.context
    obj = context.object
    scn = context.scene

    # Plano Maxila

    try:
        ListaPontos1 = [ 'Orbital right', 'Orbital left', 'A point' ]

        bpy.ops.object.select_all(action='DESELECT')

        for i in ListaPontos1:
            bpy.data.objects[i].select_set(True)
            context.view_layer.objects.active = bpy.data.objects[i]
            

        # Cursor to selected

        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                ctx = bpy.context.copy()
                ctx['area'] = area
                ctx['region'] = area.regions[-1]
        #        bpy.ops.view3d.view_selected(ctx)
                bpy.ops.view3d.snap_cursor_to_selected(ctx)
                break
            
        CursorLoc = bpy.context.scene.cursor.location
            
        bpy.ops.mesh.add_maxila(location=(CursorLoc))
        bpy.ops.transform.translate(value=(0, 0, -10))
    except:
        print("Pode estar faltando algum ponto para o plano da Maxila.")
        
    # Plano Mento

    try:
        ListaPontos1 = [ 'B point', 'Me point' ]

        bpy.ops.object.select_all(action='DESELECT')

        for i in ListaPontos1:
            bpy.data.objects[i].select_set(True)
            context.view_layer.objects.active = bpy.data.objects[i]
            

        # Cursor to selected

        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                ctx = bpy.context.copy()
                ctx['area'] = area
                ctx['region'] = area.regions[-1]
        #        bpy.ops.view3d.view_selected(ctx)
                bpy.ops.view3d.snap_cursor_to_selected(ctx)
                break
            
        CursorLoc = bpy.context.scene.cursor.location
            
        bpy.ops.mesh.add_mento(location=(CursorLoc))
    except:
        print("Pode estar faltando algum ponto para o plano do Mento.")
        
    # Ramo Esquerdo

    try:
        ListaPontos1 = [ 'Tooth 19', 'Go left' ]

        bpy.ops.object.select_all(action='DESELECT')

        for i in ListaPontos1:
            bpy.data.objects[i].select_set(True)
            context.view_layer.objects.active = bpy.data.objects[i]
            

        # Cursor to selected

        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                ctx = bpy.context.copy()
                ctx['area'] = area
                ctx['region'] = area.regions[-1]
        #        bpy.ops.view3d.view_selected(ctx)
                bpy.ops.view3d.snap_cursor_to_selected(ctx)
                break
            
        CursorLoc = bpy.context.scene.cursor.location
            
        bpy.ops.mesh.add_ramo(location=(CursorLoc))
    except:
        print("Pode estar faltando algum ponto para o plano do Ramo Esquerdo.")

        
    # Ramo Direito

    try:
        ListaPontos1 = [ 'Tooth 30', 'Go right' ]

        bpy.ops.object.select_all(action='DESELECT')

        for i in ListaPontos1:
            bpy.data.objects[i].select_set(True)
            context.view_layer.objects.active = bpy.data.objects[i]
            

        # Cursor to selected

        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                ctx = bpy.context.copy()
                ctx['area'] = area
                ctx['region'] = area.regions[-1]
        #        bpy.ops.view3d.view_selected(ctx)
                bpy.ops.view3d.snap_cursor_to_selected(ctx)
                break
            
        CursorLoc = bpy.context.scene.cursor.location
            
        bpy.ops.mesh.add_ramo(location=(CursorLoc))
    except:
        print("Pode estar faltando algum ponto para o plano do Ramo Direito.")

class AdicionaPlanosCorteAuto(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "object.adiciona_planos_corte_auto"
    bl_label = "Add Cut Planes Auto"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        AdicionaPlanosCorteAutoDef()

        return {'FINISHED'}

bpy.utils.register_class(AdicionaPlanosCorteAuto)
