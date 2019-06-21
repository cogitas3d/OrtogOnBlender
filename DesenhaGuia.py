import bpy
import fnmatch
import bmesh
import time

def DesenhaGuiaDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

#    bpy.ops.gpencil.convert(type='PATH')
#    bpy.ops.gpencil.layer_remove()

    bpy.ops.gpencil.convert_old_files()
    bpy.ops.gpencil.paintmode_toggle()
    bpy.ops.gpencil.paintmode_toggle()
    bpy.ops.gpencil.convert(type='POLY', use_timing_data=True)

    # Seleciona linha e converte em mesh
    bpy.ops.object.select_all(action='DESELECT')
    linha = bpy.data.objects['Note']
    linha.select_set(True)
#    linha = bpy.context.view_layer.objects.active
    bpy.context.view_layer.objects.active = bpy.data.objects['Note']
#    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.convert(target='CURVE')

    # Adiciona MBall
    bpy.ops.object.metaball_add(type='BALL', radius=1)

    Linha = bpy.data.objects['Note']

    bpy.ops.object.select_all(action='DESELECT')
    Linha.select_set(True)
    bpy.context.view_layer.objects.active = Linha

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
#    bpy.data.particles["ParticleSettings"].dupli_object = bpy.data.objects["Mball"]
    bpy.data.particles["ParticleSettings"].instance_object = bpy.data.objects["Mball"]

    bpy.data.particles["ParticleSettings"].particle_size = 0.6
    bpy.data.particles["ParticleSettings"].name = "DELETE" # Senão não funciona, pois usa o nome anterior

    
    Guia = bpy.data.objects['Mball']

    bpy.ops.object.select_all(action='DESELECT')
    Guia.select_set(True)
    bpy.context.view_layer.objects.active = Guia
    bpy.context.object.name = "CirGuide"
    
    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.modifier_add(type='REMESH')
    bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
    bpy.context.object.modifiers["Remesh"].octree_depth = 6 # antes 8 = muito pesado

   
    bpy.ops.object.modifier_add(type='SMOOTH')
    bpy.context.object.modifiers["Smooth"].factor = 2
    bpy.context.object.modifiers["Smooth"].iterations = 20 # Antes 50 = muito arredondado para o 6

    
#    bpy.ops.object.modifier_add(type='DECIMATE')
#    bpy.context.object.modifiers["Decimate"].ratio = 0.1

    GuiaCopia = bpy.data.objects['CirGuide.001']
    bpy.ops.object.select_all(action='DESELECT')
    GuiaCopia.select_set(True)
    bpy.context.view_layer.objects.active = GuiaCopia
    
    
    bpy.ops.object.convert(target='MESH')


    bpy.ops.object.select_all(action='DESELECT')
    Linha.select_set(True)
    bpy.context.view_layer.objects.active = Linha
    bpy.ops.object.delete(use_global=False)

    bpy.ops.object.select_all(action='DESELECT')
    GuiaCopia.select_set(True)
    bpy.context.view_layer.objects.active = GuiaCopia



class DesenhaGuia(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.desenha_guia"
    bl_label = "Desenha_Guia"
    
    def execute(self, context):
        DesenhaGuiaDef(self, context)
        return {'FINISHED'}


bpy.utils.register_class(DesenhaGuia)
