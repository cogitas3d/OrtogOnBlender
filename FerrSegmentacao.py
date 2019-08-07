
import bpy
import bmesh
from math import sqrt

def SegmentaLinkedDef(self, context):

    listaDist = []

#    ponto = bpy.context.scene.cursor_location

    ponto = bpy.context.scene.cursor.location

#    obj = bpy.context.scene.objects.active

    obj = bpy.context.view_layer.objects.active
    
    # Duplica objeto
    bpy.ops.object.duplicate()
    obj2 = bpy.context.view_layer.objects.active
    
    # Joga outro layer

    #TESTA SE HÁ Copied_Objects


    ListaColl = []

    for i in bpy.data.collections:
        ListaColl.append(i.name)

    if "Copied_Objects" not in ListaColl:

        myCol = bpy.data.collections.new("Copied_Objects")
        bpy.context.scene.collection.children.link(myCol)
        bpy.ops.object.collection_link(collection='Copied_Objects')
#        mainCol = bpy.data.collections['Collection']
#        bpy.context.scene.collection.children.unlink(mainCol)
        bpy.data.collections['Collection'].objects.unlink(obj2)

    else:
        bpy.ops.object.collection_link(collection='Copied_Objects')
#        mainCol = bpy.data.collections['Collection']
#        bpy.context.scene.collection.children.unlink(mainCol)
        bpy.data.collections['Collection'].objects.unlink(obj2)

    bpy.data.collections['Copied_Objects'].hide_viewport=True

#    bpy.ops.object.move_to_layer(layers=(False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False))

    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

            # Lista os vértices do objeto
    if obj.mode == 'EDIT':
        bm = bmesh.from_edit_mesh(obj.data)
        vertices = bm.verts

    else:
        vertices = obj.data.vertices

            # Todos os vértices por vetor
#    verts = [obj.matrix_world * vert.co for vert in vertices]
    verts = [obj.matrix_world @ vert.co for vert in vertices] 

            # Captura vetor do objeto

    referencia = bpy.context.scene.cursor.location
    
            # Calcula distância pontos

    def DistanciaObjs(obj1, obj2):
        objA = referencia
        objB = obj2
                
        distancia = sqrt( (objB[0] - objA[0])**2 + (objB[1] - objA[1])**2 + (objB[2] - objA[2])**2 )
                
        return distancia
                

    for i in range(len(verts)):

        vertAtual = verts[i]
            
        distanciaVert = DistanciaObjs(ponto, vertAtual)

        listaDist.append([distanciaVert, i])
                
                

    listaFin = sorted(listaDist)
    print("MAIS PRÓXIMO!", listaFin[0])
    


    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    bpy.ops.object.mode_set(mode = 'EDIT') 
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set(mode = 'OBJECT')
    obj.data.vertices[listaFin[0][1]].select = True
    bpy.ops.object.mode_set(mode = 'EDIT')
    
    bpy.ops.mesh.select_linked()
    
    bpy.ops.mesh.select_all(action='INVERT')

    bpy.ops.mesh.delete(type='VERT')

    bpy.ops.object.mode_set(mode = 'OBJECT')


class SegmentaLinked(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.segmenta_linked"
    bl_label = "SegmentaLinked"
    
    def execute(self, context):
        SegmentaLinkedDef(self, context)
        return {'FINISHED'}

# WEIGHTS

def Weight1Def(self, context):
    bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
    bpy.data.brushes["Draw"].vertex_tool = 'DRAW'
    bpy.ops.brush.curve_preset(shape='MAX')
    bpy.context.scene.tool_settings.unified_paint_settings.weight = 1

class Weight1(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.weight_1"
    bl_label = "Change Weight to 1"

    def execute(self, context):
        Weight1Def(self, context)
        return {'FINISHED'}

def Weight0Def(self, context):
    bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
    bpy.data.brushes["Draw"].vertex_tool = 'DRAW'
    bpy.ops.brush.curve_preset(shape='MAX')
    bpy.context.scene.tool_settings.unified_paint_settings.weight = 0

class Weight0(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.weight_0"
    bl_label = "Change Weight to 0"

    def execute(self, context):
        Weight0Def(self, context)
        return {'FINISHED'}

# Segmentação por pintura - Apaga Azul

def MantemPintadoDef(self, context):
    bpy.ops.object.mode_set(mode = 'OBJECT')

    bpy.context.object.name = "ObjSplint"

    # Seleciona área interesse

    # Which group to find?
    groupName = 'Group'

    # Use the active object
    obj = bpy.context.view_layer.objects.active

    # Make sure you're in edit mode
    bpy.ops.object.mode_set(mode='EDIT')

    # Deselect all verts
    bpy.ops.mesh.select_all(action='DESELECT')

    # Make sure the active group is the one we want
    bpy.ops.object.vertex_group_set_active(group=groupName)

    # Select the verts
    bpy.ops.object.vertex_group_select()


    bpy.ops.object.vertex_group_assign()
    bpy.ops.mesh.select_all(action='INVERT')

    bpy.ops.mesh.delete(type='VERT')
    bpy.ops.object.mode_set(mode = 'OBJECT')

class MantemPintado(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.mantem_pintado"
    bl_label = "MantemPintado"
    
    def execute(self, context):
        MantemPintadoDef(self, context)
        return {'FINISHED'}

# Segmentação por pintura - Apaga Vermelho

def ApagaPintadoDef(self, context):
    bpy.ops.object.mode_set(mode = 'OBJECT')

    bpy.context.object.name = "ObjSplint"

    # Seleciona área interesse

    # Which group to find?
    groupName = 'Group'

    # Use the active object
    obj = bpy.context.view_layer.objects.active

    # Make sure you're in edit mode
    bpy.ops.object.mode_set(mode='EDIT')

    # Deselect all verts
    bpy.ops.mesh.select_all(action='DESELECT')

    # Make sure the active group is the one we want
    bpy.ops.object.vertex_group_set_active(group=groupName)

    # Select the verts
    bpy.ops.object.vertex_group_select()


    bpy.ops.object.vertex_group_assign()
#    bpy.ops.mesh.select_all(action='INVERT')

    bpy.ops.mesh.delete(type='VERT')
    bpy.ops.object.mode_set(mode = 'OBJECT')

class ApagaPintado(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.apaga_pintado"
    bl_label = "ApagaPintado"
    
    def execute(self, context):
        ApagaPintadoDef(self, context)
        return {'FINISHED'}

# SEGMENTA DESENHO

def SegmentaDesenhoDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    #bpy.ops.gpencil.convert(type='POLY')
    #bpy.ops.gpencil.convert(type='POLY', use_normalize_weights=True, radius_multiplier=1.0, use_link_strokes=False, timing_mode='FULL', frame_range=100, start_frame=1, use_realtime=False, end_frame=250, gap_duration=0.0, gap_randomness=0.0, seed=0, use_timing_data=False)

    # Desenha

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

    bpy.ops.object.convert(target='MESH')


#    bpy.ops.gpencil.layer_remove()
#    bpy.ops.object.editmode_toggle()
#    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.select_all(action='DESELECT')
    linha.select_set(True) 
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
#    bpy.ops.object.editmode_toggle()
    mesh=bmesh.from_edit_mesh(bpy.context.object.data)
#    for v in mesh.verts:
    for v in mesh.verts and mesh.faces:
        #print(v)
        v.select = True
#        v.select = True
    bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.active # Atualiza viewport
   
#    bpy.ops.mesh.flip_normals() # Inverter para funcionar o Knife fora a fora
    bpy.ops.mesh.select_all(action = 'DESELECT')

    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.knife_project(cut_through=True) # CUIDADO! Seleciona apenas a parte de trás
#    bpy.context.scene.objects.active = bpy.context.scene.objects.active
    bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.active
    bpy.ops.mesh.select_all(action='INVERT')
    bpy.ops.mesh.separate(type='SELECTED')
#    bpy.ops.mesh.delete(type='FACE')
    bpy.ops.mesh.select_all(action = 'SELECT')
#    bpy.ops.mesh.flip_normals()
    bpy.ops.object.editmode_toggle()

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['GP_Scene'].select_set(True)
    bpy.ops.object.delete()
    bpy.data.objects['Note'].select_set(True)
#    bpy.context.object.name = "Cut_Line"

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['Note'].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects['Note']
    bpy.context.object.name = "Cutline_to_Delete"

    bpy.ops.wm.tool_set_by_id(name="builtin.select_box")


#    bpy.ops.object.delete()
    

class SegmentaDesenho(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.segmenta_desenho"
    bl_label = "Segmenta Desenho"
    
    def execute(self, context):
        SegmentaDesenhoDef(self, context)
        return {'FINISHED'}

def DesenhaBooleanaDentroDef(self, context):

    context = bpy.context
    objOrigi = context.active_object
    scn = context.scene

    #bpy.ops.gpencil.convert(type='POLY')
    #bpy.ops.gpencil.convert(type='POLY', use_normalize_weights=True, radius_multiplier=1.0, use_link_strokes=False, timing_mode='FULL', frame_range=100, start_frame=1, use_realtime=False, end_frame=250, gap_duration=0.0, gap_randomness=0.0, seed=0, use_timing_data=False)

    # Centraliza no selecionado
#    bpy.ops.view3d.snap_cursor_to_selected()

    # Desenha

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

    bpy.ops.object.convert(target='MESH')
    bpy.context.object.name = "BoolCorte"

    # EXTRUSÃO

#    bpy.ops.view3d.snap_cursor_to_selected() # NAO USAR SENAÔ MUDA O CENTER!!!

    bpy.ops.object.mode_set(mode = 'EDIT')

    bpy.ops.mesh.select_mode(type="VERT")

    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.edge_face_add()

    bpy.ops.mesh.select_all(action='SELECT')

    bpy.ops.mesh.extrude_faces_move(MESH_OT_extrude_faces_indiv={"mirror":False}, TRANSFORM_OT_shrink_fatten={"value":300, "use_even_offset":False, "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":False, "use_accurate":False})

    bpy.ops.mesh.select_all(action='DESELECT')

    bpy.ops.mesh.select_non_manifold()

    bpy.ops.mesh.edge_face_add()
#    bpy.ops.mesh.fill()
    
    bpy.ops.mesh.extrude_faces_move(MESH_OT_extrude_faces_indiv={"mirror":False}, TRANSFORM_OT_shrink_fatten={"value":300, "use_even_offset":False, "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":False, "use_accurate":False})    


    bpy.ops.mesh.select_all(action='SELECT')

    bpy.ops.mesh.flip_normals()

    bpy.ops.object.mode_set(mode = 'OBJECT')

    objBool = context.active_object

    objOrigi.select_set(True)
    objBool.select_set(True)
    bpy.context.view_layer.objects.active = objBool

    bpy.ops.object.booleana_osteo_geral()

    bpy.ops.wm.tool_set_by_id(name="builtin.select_box")  

    '''
#    bpy.ops.gpencil.layer_remove()
#    bpy.ops.object.editmode_toggle()
#    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.select_all(action='DESELECT')
    linha.select_set(True) 
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
#    bpy.ops.object.editmode_toggle()
    mesh=bmesh.from_edit_mesh(bpy.context.object.data)
#    for v in mesh.verts:
    for v in mesh.verts and mesh.faces:
        #print(v)
        v.select = True
#        v.select = True
    bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.active # Atualiza viewport
   
#    bpy.ops.mesh.flip_normals() # Inverter para funcionar o Knife fora a fora
    bpy.ops.mesh.select_all(action = 'DESELECT')

    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.knife_project(cut_through=True) # CUIDADO! Seleciona apenas a parte de trás
#    bpy.context.scene.objects.active = bpy.context.scene.objects.active
    bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.active
    bpy.ops.mesh.select_all(action='INVERT')
    bpy.ops.mesh.separate(type='SELECTED')
#    bpy.ops.mesh.delete(type='FACE')
    bpy.ops.mesh.select_all(action = 'SELECT')
#    bpy.ops.mesh.flip_normals()
    bpy.ops.object.editmode_toggle()

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['GP_Scene'].select_set(True)
    bpy.ops.object.delete()
    bpy.data.objects['Note'].select_set(True)
    bpy.context.object.name = "Cut_Line"

#    bpy.ops.object.delete()
    '''

class DesenhaBooleanaDentro(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.desenha_booleana_dentro"
    bl_label = "Segmenta Desenho"
    
    def execute(self, context):
        DesenhaBooleanaDentroDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(DesenhaBooleanaDentro)


def DesenhaBooleanaForaDef(self, context):

    context = bpy.context
    objOrigi = context.active_object
    scn = context.scene

    #bpy.ops.gpencil.convert(type='POLY')
    #bpy.ops.gpencil.convert(type='POLY', use_normalize_weights=True, radius_multiplier=1.0, use_link_strokes=False, timing_mode='FULL', frame_range=100, start_frame=1, use_realtime=False, end_frame=250, gap_duration=0.0, gap_randomness=0.0, seed=0, use_timing_data=False)

    # Centraliza no selecionado
#    bpy.ops.view3d.snap_cursor_to_selected()

    # Desenha

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

    bpy.ops.object.convert(target='MESH')
    bpy.context.object.name = "BoolCorte"

    # EXTRUSÃO

#    bpy.ops.view3d.snap_cursor_to_selected() # NAO USAR SENAÔ MUDA O CENTER!!!

    bpy.ops.object.mode_set(mode = 'EDIT')

    bpy.ops.mesh.select_mode(type="VERT")

    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.edge_face_add()

    bpy.ops.mesh.select_all(action='SELECT')

    bpy.ops.mesh.extrude_faces_move(MESH_OT_extrude_faces_indiv={"mirror":False}, TRANSFORM_OT_shrink_fatten={"value":300, "use_even_offset":False, "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":False, "use_accurate":False})

    bpy.ops.mesh.select_all(action='DESELECT')

    bpy.ops.mesh.select_non_manifold()

    bpy.ops.mesh.edge_face_add()
#    bpy.ops.mesh.fill()
    
    bpy.ops.mesh.extrude_faces_move(MESH_OT_extrude_faces_indiv={"mirror":False}, TRANSFORM_OT_shrink_fatten={"value":300, "use_even_offset":False, "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":False, "use_accurate":False})    


    bpy.ops.mesh.select_all(action='SELECT')

    bpy.ops.mesh.flip_normals()

    bpy.ops.object.mode_set(mode = 'OBJECT')

    objBool = context.active_object

    objOrigi.select_set(True)
    objBool.select_set(True)
    bpy.context.view_layer.objects.active = objBool

    bpy.ops.object.booleana_osteo_inter()

    bpy.ops.wm.tool_set_by_id(name="builtin.select_box")  

    '''
#    bpy.ops.gpencil.layer_remove()
#    bpy.ops.object.editmode_toggle()
#    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.object.select_all(action='DESELECT')
    linha.select_set(True) 
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
#    bpy.ops.object.editmode_toggle()
    mesh=bmesh.from_edit_mesh(bpy.context.object.data)
#    for v in mesh.verts:
    for v in mesh.verts and mesh.faces:
        #print(v)
        v.select = True
#        v.select = True
    bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.active # Atualiza viewport
   
#    bpy.ops.mesh.flip_normals() # Inverter para funcionar o Knife fora a fora
    bpy.ops.mesh.select_all(action = 'DESELECT')

    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.knife_project(cut_through=True) # CUIDADO! Seleciona apenas a parte de trás
#    bpy.context.scene.objects.active = bpy.context.scene.objects.active
    bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.active
    bpy.ops.mesh.select_all(action='INVERT')
    bpy.ops.mesh.separate(type='SELECTED')
#    bpy.ops.mesh.delete(type='FACE')
    bpy.ops.mesh.select_all(action = 'SELECT')
#    bpy.ops.mesh.flip_normals()
    bpy.ops.object.editmode_toggle()

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['GP_Scene'].select_set(True)
    bpy.ops.object.delete()
    bpy.data.objects['Note'].select_set(True)
    bpy.context.object.name = "Cut_Line"

#    bpy.ops.object.delete()
    '''

class DesenhaBooleanaFora(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.desenha_booleana_fora"
    bl_label = "Segmenta Desenho Fora"
    
    def execute(self, context):
        DesenhaBooleanaForaDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(DesenhaBooleanaFora)

# Segmenta mandíbula

import bpy
import platform

def ImportaSeparaMandibulaDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene


    if platform.system() == "Linux":

        dirScript = bpy.utils.user_resource('SCRIPTS')

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Collection\\"
        object    = "Separa_Mandibula"

    if platform.system() == "Darwin":

        dirScript = bpy.utils.user_resource('SCRIPTS')
        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Collection\\"
        object    = "Separa_Mandibula"
        
    if platform.system() == "Windows":

        dirScript = 'C:/OrtogOnBlender/Blender/2.78/scripts/'

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Collection\\"
        object    = "Separa_Mandibula"    


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

#ImportaSeparaMandibulaDef()


class ImportaSeparaMandibula(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.importa_separa_mandibula"
    bl_label = "Importa Separa Mandíbula"
    
    def execute(self, context):
        ImportaSeparaMandibulaDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(ImportaSeparaMandibula)

def MovePara(objOrigem, objMove):

    ObjetoOrigem = bpy.data.objects[objOrigem]
    ObjetoMove = bpy.data.objects[objMove]

#    bpy.ops.object.select_all(action='DESELECT')
#    ObjetoMove.select_set(True)
#    context.view_layer.objects.active = ObjetoMove
    ObjetoMove.location[0] = ObjetoOrigem.location[0]
    ObjetoMove.location[1] = ObjetoOrigem.location[1]
    ObjetoMove.location[2] = ObjetoOrigem.location[2]

def AjustaMandibula():   
    MovePara("Condylar Process left", "EMP_Proc_Cond_esq")
    MovePara("Condylar Process right", "EMP_Proc_Cond_dir")

    MovePara("Coronoid Process left", "EMP_Proc_Cor_esq")
    MovePara("Coronoid Process right", "EMP_Proc_Cor_dir")

    MovePara("Mid Go-Ramus Fracure left", "EMP_Ang_Mand_esq")
    MovePara("Mid Go-Ramus Fracure right", "EMP_Ang_Mand_dir")

    MovePara("Go left", "EMP_Gon_esq")
    MovePara("Go right", "EMP_Gon_dir")

    MovePara("Mid Mandibula Angle left", "EMP_Meio_Mand_esq")
    MovePara("Mid Mandibula Angle right", "EMP_Meio_Mand_dir")

    MovePara("Gn point", "EMP_Protuberancia_down")
    MovePara("B point", "EMP_Protuberancia")
    MovePara("Mid Upper Incisors", "EMP_Protuberancia_up")

def BooleanSeparaMandibula():
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.select_all(action='DESELECT')

    MandibulaBase = bpy.data.objects['MandibulaBase']

    MandibulaBase.select_set(True) 
    bpy.context.view_layer.objects.active = MandibulaBase

    obj = context.active_object
    bpy.ops.object.collection_link(collection='Collection')



    bpy.ops.object.select_all(action='DESELECT')

    Cranio = bpy.data.objects['Bones']
    MandibulaBase = bpy.data.objects['MandibulaBase']

    Cranio.select_set(True) 
    MandibulaBase.select_set(True)

    bpy.context.view_layer.objects.active = MandibulaBase

    bpy.ops.object.booleana_osteo_inter()

    bpy.ops.object.select_all(action='DESELECT')


    ListaObjetos = ['EMP_Proc_Cor_dir', 'EMP_Proc_Cond_dir', 'EMP_Proc_Cor_esq', 'EMP_Proc_Cond_esq', 'EMP_Gon_dir', 'EMP_Ang_Mand_dir', 'EMP_Gon_esq', 'EMP_Ang_Mand_esq', 'EMP_Meio_Mand_esq', 'EMP_Meio_Mand_dir', 'EMP_Protuberancia_down', 'EMP_Protuberancia', 'EMP_Protuberancia_up', 'ArmatureMandibula', 'Condylar Process right', 'Coronoid Process right', 'Condylar Process left', 'Coronoid Process left', 'Mid Go-Ramus Fracure right', 'Go right', 'Mid Go-Ramus Fracure left', 'Go left', 'Mid Mandibula Angle right', 'Mid Mandibula Angle left', 'Gn point', 'B point', 'Mid Upper Incisors']


    for i in ListaObjetos:   
 
        bpy.data.objects[i].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[i]
        bpy.ops.object.delete(use_global=False)



# Traz para Collection

    bpy.ops.object.select_all(action='DESELECT')
    Cranio.select_set(True)



    bpy.context.view_layer.objects.active = Cranio

    bpy.ops.object.collection_link(collection='Collection')
    Cranio.hide_viewport=False

    try:
        bpy.context.object.active_material.diffuse_color = (0.8, 0.684753, 0.470028, 0.5)
    except:
        activeObject = bpy.context.active_object #Set active object to variable
        mat = bpy.data.materials.new(name="MaterialSkull") #set new material to variable
        activeObject.data.materials.append(mat) #add the material to the object
        bpy.context.object.active_material.diffuse_color = (0.8, 0.684753, 0.470028, 0.5) #change color


    bpy.ops.object.select_all(action='DESELECT')


    try:
        objAct = bpy.data.objects["Result.001"]
        objAct.select_set(True)
        bpy.context.view_layer.objects.active = objAct
    except:
        objAct = bpy.data.objects["Result"]
        objAct.select_set(True)
        bpy.context.view_layer.objects.active = objAct




class SeparacaoMandibula(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.separacao_mandibula"
    bl_label = "Importa Separa Mandíbula"
    
    def execute(self, context):
        ImportaSeparaMandibulaDef(self, context)
        AjustaMandibula()
        BooleanSeparaMandibula()
#        bpy.ops.wm.tool_set_by_id(name="builtin.select_box")
        return {'FINISHED'}

bpy.utils.register_class(SeparacaoMandibula)



def SeparaMandibulaCranioDef():

    bpy.ops.object.duplicate()
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.transform.shrink_fatten(value=-0.35, use_even_offset=False, mirror=True, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.modifier_add(type='REMESH')
    bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
    bpy.context.object.modifiers["Remesh"].octree_depth = 8
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh")

    context = bpy.context
    Mandibula = context.active_object
    scn = context.scene

    bpy.ops.object.select_all(action='DESELECT')

    Cranio = bpy.data.objects['Bones']

    Cranio.select_set(True) 
    Mandibula.select_set(True)    

    bpy.context.view_layer.objects.active = Mandibula

    bpy.ops.object.booleana_osteo_geral()

class SeparaMandibulaCranio(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.separacao_mandibula_cranio"
    bl_label = "Importa Separa Mandíbula Crânio"
    
    def execute(self, context):
        SeparaMandibulaCranioDef()
        return {'FINISHED'}

bpy.utils.register_class(SeparaMandibulaCranio)


class PreparaImpressao3D(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.prepara_impressao_3d"
    bl_label = "Prepara Impressão 3D"
    
    def execute(self, context):
        bpy.ops.object.modifier_add(type='REMESH')
        bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
        bpy.context.object.modifiers["Remesh"].octree_depth = 8
        bpy.context.object.modifiers["Remesh"].scale = 0.99
        return {'FINISHED'}

bpy.utils.register_class(PreparaImpressao3D)

def FecharBuracosTodosDef():
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_non_manifold()
    bpy.ops.mesh.remove_doubles(threshold=0.2)
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.mode_set(mode='OBJECT')

class FecharBuracosTodos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.fecha_buraco_todos"
    bl_label = "Prepara Impressão 3D"
    
    def execute(self, context):
        FecharBuracosTodosDef()
        return {'FINISHED'}

bpy.utils.register_class(FecharBuracosTodos)

def SeparaObjetoDef():

    bpy.ops.mesh.select_mode(type="FACE")
    bpy.ops.mesh.select_all(action='INVERT')
    bpy.ops.mesh.separate(type='SELECTED')
    bpy.ops.object.mode_set(mode='OBJECT')
    objSel = bpy.context.view_layer.objects.active
    bpy.ops.object.select_all(action='DESELECT')
    objSel.select_set(True)
    bpy.context.view_layer.objects.active = objSel

class SeparaObjeto(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.separa_objeto"
    bl_label = "Separa Ojeto"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects

        if bpy.context.active_object.mode == 'EDIT':
            return True
        else:
            if bpy.context.active_object.mode == 'OBJECT':
                return False

    def execute(self, context):
        SeparaObjetoDef()
        return {'FINISHED'}

bpy.utils.register_class(SeparaObjeto)

