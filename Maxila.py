bl_info = {
    "name": "Adiciona Planos de Corte",
    "author": "Cicero Moraes e Everton da Rosa",
    "version": (1, 0),
    "blender": (2, 77, 0),
    "location": "View3D > Add > Mesh > Planos de Corte",
    "description": "Adicionar Ramo Mandíbula",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
    }


import bpy
from bpy.types import Operator
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

# RAMO

def add_object(self, context):

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


class OBJECT_OT_add_object(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_maxila"
    bl_label = "Add Maxila"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        add_object(self, context)

        return {'FINISHED'}


# Registration

def add_object_button(self, context):
    self.layout.operator(
        OBJECT_OT_add_object.bl_idname,
        text="Maxila",
        icon='VIEW3D')



def register():
    bpy.utils.register_class(OBJECT_OT_add_object)
    bpy.types.INFO_MT_mesh_add.append(add_object_button)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_object)
    bpy.types.INFO_MT_mesh_add.remove(add_object_button)


if __name__ == "__main__":
    register()