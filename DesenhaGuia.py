import bpy


def DesenhaGuiaDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.gpencil.convert(type='PATH')

    bpy.ops.gpencil.layer_remove()

    # Adiciona MBall
    bpy.ops.object.metaball_add(type='BALL', radius=1)

    Linha = bpy.data.objects['GP_Layer']

    bpy.ops.object.select_all(action='DESELECT')
    Linha.select = True
    bpy.context.scene.objects.active = Linha

#    bpy.context.space_data.context = 'DATA'
    bpy.context.object.data.fill_mode = 'FULL'
    bpy.context.object.data.bevel_depth = 10

    bpy.ops.object.convert(target='MESH')
    
    bpy.ops.object.modifier_add(type='REMESH')
    bpy.context.object.modifiers["Remesh"].use_remove_disconnected = False
    bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
    bpy.context.object.modifiers["Remesh"].octree_depth = 6

    bpy.ops.object.convert(target='MESH')

#    bpy.context.space_data.context = 'PARTICLES'
    bpy.ops.object.particle_system_add()
    bpy.data.particles["ParticleSettings"].type = 'HAIR'
    bpy.data.particles["ParticleSettings"].render_type = 'OBJECT'
    bpy.data.particles["ParticleSettings"].count = 2000
    bpy.data.particles["ParticleSettings"].dupli_object = bpy.data.objects["Mball"]
    bpy.data.particles["ParticleSettings"].particle_size = 0.6
    bpy.data.particles["ParticleSettings"].name = "DELETE" # Senão não funciona, pois usa o nome anterior
    
    bpy.ops.object.select_all(action='DESELECT')
    Linha.select = True
    bpy.context.scene.objects.active = Linha
    bpy.ops.object.delete(use_global=False)

    Guia = bpy.data.objects['Mball']

    bpy.ops.object.select_all(action='DESELECT')
    Guia.select = True
    bpy.context.scene.objects.active = Guia
    bpy.context.object.name = "CirGuide"
    
    bpy.ops.object.convert(target='MESH')
    
    bpy.ops.object.modifier_add(type='SMOOTH')
    bpy.context.object.modifiers["Smooth"].factor = 2
    bpy.context.object.modifiers["Smooth"].iterations = 120
    
    bpy.ops.object.modifier_add(type='DECIMATE')
    bpy.context.object.modifiers["Decimate"].ratio = 0.1

    
    bpy.ops.object.convert(target='MESH')


def AcabamentoDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    GuiaParte = bpy.context.active_object

    bpy.ops.gpencil.convert(type='PATH')
    bpy.ops.gpencil.layer_remove()

    Linha = bpy.data.objects['GP_Layer']
#    Linha.select = True
#    bpy.context.scene.objects.active = Linha
#    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.select_all(action='DESELECT')
    GuiaParte.select = True
    Linha.select = True
    bpy.context.scene.objects.active = GuiaParte
    
    bpy.ops.object.corta_ossos()
    
    bpy.ops.object.select_all(action='DESELECT')   
    Linha.select = True
    bpy.context.scene.objects.active = Linha
    bpy.ops.object.delete(use_global=False)   
    
    ObjAcabamento = bpy.data.objects['OssoPronto']    
    bpy.ops.object.select_all(action='DESELECT')   
    ObjAcabamento.select = True
    bpy.context.scene.objects.active = ObjAcabamento
    
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='DESELECT')

    bpy.ops.mesh.select_mode(type="EDGE")
    
    bpy.ops.mesh.select_non_manifold()

#    bpy.ops.object.triangle_fill(res_mode='MAX')
        

def FechaBuracoDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene    
    
    bpy.ops.object.triangle_fill(res_mode = 'MAX') 
