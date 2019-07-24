import bpy


def FechaMoldeSimplesDef(self, context):

    context = bpy.context
    obj = context.object
    scn = context.scene

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_non_manifold()

    bpy.ops.mesh.fill()
    bpy.ops.object.editmode_toggle()


class FechaMoldeSimples(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.fecha_molde_simples"
    bl_label = "Close hole simple"
    
    def execute(self, context):
        FechaMoldeSimplesDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(FechaMoldeSimples)


def ParenteiaObjetosDef():

#    objetos_selecionados = [ o for o in bpy.context.selected_objects ]

#    for i in objetos_selecionados:
#        if i.visible_get() == True:
#            bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
    print("Parenteado!")


class ParenteiaObjetos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.parenteia_objetos"
    bl_label = "Parenteia objetos"
    
    def execute(self, context):
        ParenteiaObjetosDef()
        return {'FINISHED'}

bpy.utils.register_class(ParenteiaObjetos)



def DesparenteiaObjetosDef():

    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
    print("Desparenteado!")


class DesparenteiaObjetos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.desparenteia_objetos"
    bl_label = "Desparenteia objetos"
    
    def execute(self, context):
        DesparenteiaObjetosDef()
        return {'FINISHED'}

bpy.utils.register_class(DesparenteiaObjetos)
