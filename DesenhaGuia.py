import bpy
import fnmatch
import bmesh

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
    bpy.ops.mesh.select_non_manifold(use_non_contiguous=False)


#    bpy.ops.object.triangle_fill(res_mode='MAX')
        

def FechaBuracoDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene    
    
    bpy.ops.object.triangle_fill(res_mode = 'MAX')

def DesenhaLinhaCorteDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    Osso = bpy.context.active_object


# Lista todos os layers

    LayerOriginal = []
    for i in bpy.context.scene.layers:
         LayerOriginal.append(i)
   

    for i in range(20):
         bpy.context.scene.layers[i] = True

# Apaga todas as linhas

    bpy.ops.object.select_all(action='DESELECT')    
    Pontos = [obj for obj in bpy.context.scene.objects if fnmatch.fnmatchcase(obj.name, "GP_Laye*")]
    for i in Pontos:
        i.select=True
    bpy.ops.object.delete(use_global=False)

# Volta aos layers originais

    ListNum = 0

    for i in LayerOriginal:
         bpy.context.scene.layers[ListNum] = i
         ListNum += 1

# Seleciona o desenho

    bpy.ops.gpencil.convert(type='CURVE', timing_mode='LINEAR', use_timing_data=False)
    bpy.ops.gpencil.layer_remove()

    Linha = bpy.data.objects['GP_Layer']

    bpy.ops.object.select_all(action='DESELECT')
    Linha.select = True
#    Linha.select = True
    bpy.context.scene.objects.active = Linha

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.curve.make_segment()
    bpy.ops.curve.select_all(action='TOGGLE')
    bpy.ops.curve.select_all(action='TOGGLE')
    bpy.ops.curve.handle_type_set(type='AUTOMATIC')
    bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.modifier_add(type='SHRINKWRAP')
    bpy.context.object.modifiers["Shrinkwrap"].use_keep_above_surface = True
    bpy.context.object.modifiers["Shrinkwrap"].target = Osso
    bpy.context.object.modifiers["Shrinkwrap"].offset = 2
    bpy.ops.object.modifier_add(type='SMOOTH')
    bpy.context.object.modifiers["Smooth"].factor = 2
    bpy.context.object.modifiers["Smooth"].iterations = 3
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.mode_set(mode='EDIT')    
    bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.remove_doubles(threshold=2)
    bpy.ops.mesh.fill()
    bpy.ops.mesh.extrude_region()
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(3.72529e-09, 7.91624e-09, 0.3), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})

    bpy.ops.object.editmode_toggle()
 
    bpy.context.object.name = "Corte"    
    Linha = bpy.data.objects['Corte']

    bpy.ops.object.select_all(action='DESELECT')
    Linha.select = True
    Osso.select = True
    bpy.context.scene.objects.active = Osso

# Se não duplicar não funciona!
    bpy.ops.object.duplicate()

    bpy.ops.object.booleana_osteo()
 
# Apaga os objetos anteriores   
    bpy.ops.object.select_all(action='DESELECT')
    Linha.select = True
    Osso.select = True
    bpy.ops.object.delete(use_global=False)



class DesenhaLinhaCorte(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.desenha_linha_corte"
    bl_label = "Desenha Linha Corte"
    
    def execute(self, context):
        DesenhaLinhaCorteDef(self, context)
        return {'FINISHED'}

def DesenhaLinhaVertexDef(self, context):

    global Osso

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    Osso = bpy.context.active_object


# Lista todos os layers

    LayerOriginal = []
    for i in bpy.context.scene.layers:
         LayerOriginal.append(i)
   

    for i in range(20):
         bpy.context.scene.layers[i] = True

# Apaga todas as linhas

    bpy.ops.object.select_all(action='DESELECT')    
    Pontos = [obj for obj in bpy.context.scene.objects if fnmatch.fnmatchcase(obj.name, "GP_Laye*")]
    for i in Pontos:
        i.select=True
    bpy.ops.object.delete(use_global=False)

# Volta aos layers originais

    ListNum = 0

    for i in LayerOriginal:
         bpy.context.scene.layers[ListNum] = i
         ListNum += 1

# Seleciona o desenho

    bpy.ops.gpencil.convert(type='CURVE', timing_mode='LINEAR', use_timing_data=False)
    bpy.ops.gpencil.layer_remove()

    Linha = bpy.data.objects['GP_Layer']

    bpy.ops.object.select_all(action='DESELECT')
    Linha.select = True
#    Linha.select = True
    bpy.context.scene.objects.active = Linha

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.curve.make_segment()
    bpy.ops.curve.select_all(action='TOGGLE')
    bpy.ops.curve.select_all(action='TOGGLE')
    bpy.ops.curve.handle_type_set(type='AUTOMATIC')
    bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.modifier_add(type='SHRINKWRAP')
    bpy.context.object.modifiers["Shrinkwrap"].use_keep_above_surface = True
    bpy.context.object.modifiers["Shrinkwrap"].target = Osso
    bpy.context.object.modifiers["Shrinkwrap"].offset = 2
    bpy.ops.object.modifier_add(type='SMOOTH')
    bpy.context.object.modifiers["Smooth"].factor = 2
    bpy.context.object.modifiers["Smooth"].iterations = 3
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.mode_set(mode='EDIT')    
    bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.remove_doubles(threshold=2)

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.object.name = "Linha_"+Osso.name

    bpy.ops.object.mode_set(mode='EDIT')    

class DesenhaLinhaVertex(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.desenha_linha_vertex"
    bl_label = "Desenha Linha Corte"
    
    def execute(self, context):
        DesenhaLinhaVertexDef(self, context)
        return {'FINISHED'}

def DesenhaLinhaVertexFinDef(self, context):

    context = bpy.context
    scn = context.scene

    Linha = context.active_object

    bpy.ops.object.mode_set(mode='EDIT')

# É NECESSÁRIO SELECIONAR OS EDGES!!! NÃO OS VÉRTICES!
    mesh = bmesh.from_edit_mesh(Linha.data)
    for e in mesh.edges:
        e.select = True
    # trigger viewport update
    bpy.context.scene.objects.active = bpy.context.scene.objects.active

    bpy.ops.mesh.fill()
    bpy.ops.mesh.extrude_region()
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(3.72529e-09, 7.91624e-09, 0.3), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})

    bpy.ops.object.editmode_toggle()
 
#    bpy.context.object.name = "Corte"    
#    Linha = bpy.data.objects['Corte']

    Osso = bpy.data.objects[str(Linha.name.strip("Linha_"))]

    bpy.ops.object.select_all(action='DESELECT')
    Linha.select = True
    Osso.select = True
    bpy.context.scene.objects.active = Osso

# Se não duplicar não funciona!
    bpy.ops.object.duplicate()

    bpy.ops.object.booleana_osteo()
 
# Apaga os objetos anteriores   
    bpy.ops.object.select_all(action='DESELECT')
    Linha.select = True
    Osso.select = True
    bpy.ops.object.delete(use_global=False)


class DesenhaLinhaVertexFin(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.desenha_linha_vertex_fin"
    bl_label = "Desenha Linha Corte"
    
    def execute(self, context):
        DesenhaLinhaVertexFinDef(self, context)
        return {'FINISHED'}
