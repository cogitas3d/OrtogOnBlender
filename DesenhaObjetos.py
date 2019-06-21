import bpy
import fnmatch
import bmesh
import time

from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )

from mathutils import Matrix, Vector
from bpy_extras.object_utils import AddObjectHelper, object_data_add

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
    bpy.ops.object.collection_link(collection='Collection')

    # Seleciona linha e converte em mesh

    bpy.ops.gpencil.convert_old_files()
    bpy.ops.gpencil.paintmode_toggle()
    bpy.ops.gpencil.paintmode_toggle()
    bpy.ops.gpencil.convert(type='POLY', use_timing_data=True)
    
    bpy.ops.object.select_all(action='DESELECT')
    linha = bpy.data.objects['Note']
    linha.select_set(True)
    # linha = bpy.context.view_layer.objects.active
    bpy.context.view_layer.objects.active = bpy.data.objects['Note']



    bpy.ops.object.convert(target='MESH')

# Subdivide pois nessa versão a linha está simplificada
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.subdivide(quadcorner='INNERVERT')
    bpy.ops.mesh.subdivide()
    bpy.ops.mesh.remove_doubles() # Para juntar as partes separadas
    bpy.ops.mesh.remove_doubles(threshold=2)
    bpy.ops.mesh.subdivide()
    bpy.ops.object.editmode_toggle()

# Modificadores para ficar sobre a superfície
    bpy.ops.object.modifier_add(type='SHRINKWRAP')
#    bpy.context.object.modifiers["Shrinkwrap"].use_keep_above_surface = True
    bpy.context.object.modifiers["Shrinkwrap"].wrap_mode = 'ABOVE_SURFACE'
    bpy.context.object.modifiers["Shrinkwrap"].target = Osso
    bpy.context.object.modifiers["Shrinkwrap"].offset = 1.5
 
    bpy.ops.object.modifier_add(type='SMOOTH')
    bpy.context.object.modifiers["Smooth"].factor = 1
    bpy.context.object.modifiers["Smooth"].iterations = 1


    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.mode_set(mode='EDIT')    
    bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.remove_doubles(threshold=2)


    bpy.ops.mesh.select_all(action='SELECT')

    bpy.ops.mesh.edge_face_add()
#    bpy.ops.mesh.fill()

    bpy.ops.mesh.extrude_faces_move(MESH_OT_extrude_faces_indiv={"mirror":False}, TRANSFORM_OT_shrink_fatten={"value":.5, "use_even_offset":False, "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":False, "use_accurate":False})

    bpy.ops.mesh.select_all(action='DESELECT')

    bpy.ops.mesh.select_non_manifold()

    bpy.ops.mesh.edge_face_add()

    bpy.ops.object.editmode_toggle()
    
 
    bpy.context.object.name = "Corte"    
    Linha = bpy.data.objects['Corte']

    bpy.ops.object.select_all(action='DESELECT')
    Linha.select_set(True)
    Osso.select_set(True)
    bpy.context.view_layer.objects.active = Osso

# Se não duplicar não funciona!
#    bpy.ops.object.duplicate()
    

    bpy.ops.object.booleana_osteo()

    #Joga osso para copier
    Osso.select_set(True)
    bpy.context.view_layer.objects.active = Osso
    bpy.ops.object.hide_view_set(unselected=False)
#    bpy.ops.object.collection_link(collection='Copied_Objects')
#    bpy.data.collections['Collection'].objects.unlink(Osso)



    bpy.ops.object.select_all(action='DESELECT')
 
# Apaga os objetos anteriores   
#    bpy.ops.object.select_all(action='DESELECT')
#    Linha.select_set(True)
#    Osso.select_set(True)
#    bpy.ops.object.delete(use_global=False)



class DesenhaLinhaCorte(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.desenha_linha_corte"
    bl_label = "Desenha Linha Corte"

    # ------------------------------
    # Poll
    # ------------------------------
    @classmethod
    def poll(cls, context):
        o = context.object
        if o is None:
            return False
        else:
            if o.type == "MESH":
                if bpy.context.mode == 'OBJECT':
                    return True
                else:
                    return False
            else:
                return False
    
    def execute(self, context):
        DesenhaLinhaCorteDef(self, context)
        return {'FINISHED'}

def DesenhaLinhaVertexDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    Osso = bpy.context.active_object
# Renomeia para não dar erro
    OssoNome = Osso.name
    Osso.name = OssoNome+time.strftime("%Y%m%d%H%M%S")
    bpy.ops.object.collection_link(collection='Collection')
    print("NOMEDADO")


    # Seleciona linha e converte em mesh

    bpy.ops.gpencil.convert_old_files()
    bpy.ops.gpencil.paintmode_toggle()
    bpy.ops.gpencil.paintmode_toggle()
    bpy.ops.gpencil.convert(type='POLY', use_timing_data=True)
    
    bpy.ops.object.select_all(action='DESELECT')
    linha = bpy.data.objects['Note']
    linha.select_set(True)
    # linha = bpy.context.view_layer.objects.active
    bpy.context.view_layer.objects.active = bpy.data.objects['Note']



    bpy.ops.object.convert(target='MESH')

# Subdivide pois nessa versão a linha está simplificada
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.subdivide(quadcorner='INNERVERT')
    bpy.ops.mesh.subdivide()
    bpy.ops.mesh.remove_doubles() # Para juntar as partes separadas
    bpy.ops.mesh.remove_doubles(threshold=2)
    bpy.ops.mesh.subdivide()
    bpy.ops.object.editmode_toggle()

# Modificadores para ficar sobre a superfície
    bpy.ops.object.modifier_add(type='SHRINKWRAP')
#    bpy.context.object.modifiers["Shrinkwrap"].use_keep_above_surface = True
    bpy.context.object.modifiers["Shrinkwrap"].wrap_mode = 'ABOVE_SURFACE'
    bpy.context.object.modifiers["Shrinkwrap"].target = Osso
    bpy.context.object.modifiers["Shrinkwrap"].offset = 1.5
 
    bpy.ops.object.modifier_add(type='SMOOTH')
    bpy.context.object.modifiers["Smooth"].factor = 1
    bpy.context.object.modifiers["Smooth"].iterations = 1


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
    
    # ------------------------------
    # Poll
    # ------------------------------
    @classmethod
    def poll(cls, context):
        o = context.object
        if o is None:
            return False
        else:
            if o.type == "MESH":
                if bpy.context.mode == 'OBJECT':
                    return True
                else:
                    return False
            else:
                return False

    def execute(self, context):
        DesenhaLinhaVertexDef(self, context)
        return {'FINISHED'}

def DesenhaLinhaVertexFinDef(self, context):

    context = bpy.context
    scn = context.scene

    Linha = context.active_object

    bpy.ops.object.mode_set(mode='EDIT')

# É NECESSÁRIO SELECIONAR OS EDGES!!! NÃO OS VÉRTICES!
#    mesh = bmesh.from_edit_mesh(Linha.data)
#    for e in mesh.edges:
#        e.select = True
    # trigger viewport update
#    bpy.context.scene.objects.active = bpy.context.scene.objects.active

    bpy.ops.mesh.select_all(action='SELECT')

    bpy.ops.mesh.edge_face_add()
#    bpy.ops.mesh.fill()

    bpy.ops.mesh.extrude_faces_move(MESH_OT_extrude_faces_indiv={"mirror":False}, TRANSFORM_OT_shrink_fatten={"value":.5, "use_even_offset":False, "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":False, "use_accurate":False})

    bpy.ops.mesh.select_all(action='DESELECT')

    bpy.ops.mesh.select_non_manifold()

    bpy.ops.mesh.edge_face_add()

    '''
    bpy.ops.mesh.extrude_region()

    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(1.81608e-08, .6, .6), "orient_type":'NORMAL', "orient_matrix":((0.238327, 0.958761, 0.154848), (0.00483444, -0.160612, 0.987006), (0.971173, -0.234481, -0.0429132)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
    '''
    bpy.ops.object.editmode_toggle()
 

    Osso = bpy.data.objects[str(Linha.name.strip("Linha_"))]
    print("OSSSOOO", Osso)


    bpy.context.object.name = "Corte" 

#    OssoNome = Osso.name
#    Osso.name = OssoNome+time.strftime("%Y%m%d%H%M%S")
#    print("NOMEDADO")

    bpy.ops.object.select_all(action='DESELECT')
    Linha.select_set(True)
    Osso.select_set(True)
    bpy.context.view_layer.objects.active = Osso

# Se não duplicar não funciona!
#    bpy.ops.object.duplicate()

    
    bpy.ops.object.booleana_osteo()
 
# Apaga os objetos anteriores   
    bpy.ops.object.select_all(action='DESELECT')
    Linha.select_set(True)
    Osso.select_set(True)
    bpy.ops.object.delete(use_global=False)
    

class DesenhaLinhaVertexFin(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.desenha_linha_vertex_fin"
    bl_label = "Desenha Linha Corte"
    
    def execute(self, context):
        DesenhaLinhaVertexFinDef(self, context)
        return {'FINISHED'}

def LinhaCorteDef(self, context):

    context = bpy.context
    scn = context.scene

#   bpy.context.scene.tool_settings.gpencil_stroke_placement_view3d = 'SURFACE'
#    bpy.ops.gpencil.convert(type='POLY', timing_mode='LINEAR', use_timing_data=False)
#    bpy.ops.gpencil.draw('INVOKE_DEFAULT', mode="DRAW_POLY")
    #bpy.ops.gpencil.annotate(mode="DRAW_POLY")
    bpy.ops.wm.tool_set_by_id(name="builtin.annotate_polygon") # Capturar direto dos botões da interface
    bpy.context.scene.tool_settings.annotation_stroke_placement_view3d = 'SURFACE'



class LinhaCorte(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.linha_corte"
    bl_label = "Desenha Linha Corte"

    # ------------------------------
    # Poll
    # ------------------------------
    @classmethod
    def poll(cls, context):
        o = context.object
        if o is None:
            return False
        else:
            if o.type == "MESH":
                if bpy.context.mode == 'OBJECT':
                    return True
                else:
                    return False
            else:
                return False

    def execute(self, context):
        LinhaCorteDef(self, context)
        return {'FINISHED'}

# Modal

class ModalTimerOperator(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "wm.modal_cria_pontos"
    bl_label = "Create points line"

    _timer = None

    def modal(self, context, event):

        context = bpy.context
        obj = context.active_object

        bpy.ops.wm.tool_set_by_id(name="builtin.cursor")    

        if event.type in {'RIGHTMOUSE', 'ESC'}:
            self.cancel(context)
            return {'CANCELLED'}

#        bpy.ops.object.select_pattern(pattern="Cub*") # Seleciona objetos com esse padrão
     

        if event.type == 'LEFTMOUSE' and event.value == 'RELEASE':


            if context.area.type == 'VIEW_3D':
                region = context.region
                r3d = context.space_data.region_3d

#                bpy.ops.object.empty_add(type='PLAIN_AXES', radius=1, location=(0,0,0))

                bpy.ops.mesh.primitive_uv_sphere_add(radius=0.7, location=(0,0,0)) #Atrasa também
                bpy.ops.transform.translate(value=(bpy.context.scene.cursor.location))
                bpy.context.object.name = "PT_Linha"

                ListaMateriais = []
                MateriaisCena = bpy.data.materials

                for i in MateriaisCena:
                    ListaMateriais.append(i.name)

                if 'MatModalPoints' in ListaMateriais:
                    activeObject = bpy.context.active_object #Set active object to variable
                    mat = bpy.data.materials["MatModalPoints"] #set new material to variable
                    activeObject.data.materials.append(mat) #add the material to the object
                    bpy.context.object.active_material.diffuse_color = (0.2, 0.9, 0.2, 1)
                else:
                    activeObject = bpy.context.active_object #Set active object to variable
                    mat = bpy.data.materials.new(name="MatModalPoints") #set new material to variable
                    activeObject.data.materials.append(mat) #add the material to the object
                    bpy.context.object.active_material.diffuse_color = (0.2, 0.9, 0.2, 1)

                bpy.ops.object.select_all(action='DESELECT')

              
                obj.select_set(True)
                bpy.context.view_layer.objects.active = obj


        return {'PASS_THROUGH'}

    def execute(self, context):
        if context.area.type != 'VIEW_3D':
            print("Must use in a 3d region")
            return {'CANCELLED'}

        wm = context.window_manager
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager

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

bpy.utils.register_class(ModalTimerOperator)

def CriaLinhaPontosDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene


    Pontos = [obj for obj in bpy.context.scene.objects if fnmatch.fnmatchcase(obj.name, "PT_Linh*")]

    vertices = []

    for i in Pontos:
        VetorAtual = i.location
        VetX = i.location[0]
        VetY = i.location[1]
        VetZ = i.location[2]
        vertices.append((VetX, VetY, VetZ))

    edges = []

    for i in range(len(vertices)):
        edges.append([i,i+1])

    del(edges[-1]) # Apaga o último elemento da cena

    faces = []


    mesh = bpy.data.meshes.new(name="LineSolid")
    mesh.from_pydata(vertices, edges, faces)
    object_data_add(context, mesh, operator=self)

    bpy.context.object.location = 0,0,0

    bpy.ops.object.convert(target='CURVE')

    bpy.context.object.data.fill_mode = 'FULL'
    bpy.context.object.data.bevel_depth = 0.915
    bpy.context.object.data.bevel_resolution = 7


class CriaLinhaPontos(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_linha_pontos"
    bl_label = "Create Points Line"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        CriaLinhaPontosDef(self, context)

        return {'FINISHED'}

bpy.utils.register_class(CriaLinhaPontos)

def CriaBezierDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene


    Pontos = [obj for obj in bpy.context.scene.objects if fnmatch.fnmatchcase(obj.name, "PT_Linh*")]

    coords = []

    for i in Pontos:
        VetorAtual = i.location
        VetX = i.location[0]
        VetY = i.location[1]
        VetZ = i.location[2]
        coords.append((VetX, VetY, VetZ))

#    edges = []

#    for i in range(len(vertices)):
#        edges.append([i,i+1])

#    del(edges[-1]) # Apaga o último elemento da cena


    # create the Curve Datablock
    curveData = bpy.data.curves.new('myCurve', type='CURVE')
    curveData.dimensions = '3D'
    curveData.resolution_u = 6

    # map coords to spline
    polyline = curveData.splines.new('BEZIER')
    polyline.bezier_points.add(len(coords)-1)
#    for i, coord in enumerate(coords):
#        x,y,z = coord
#        polyline.points[i].co = (x, y, z, 1)

    from bpy_extras.io_utils import unpack_list
    polyline.bezier_points.foreach_set("co", unpack_list(coords))

    # Apaga pontos
    bpy.ops.object.select_all(action='DESELECT')

    for i in Pontos:
        i.select_set(True)

    bpy.ops.object.delete(use_global=False)

    

    # Cria Linha
    curveOB = bpy.data.objects.new('myCurve', curveData)

    # attach to scene and validate context
    scn = bpy.context.scene
#   scn.objects.link(curveOB)
    scn.collection.objects.link(curveOB)
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = curveOB
    curveOB.select_set(True)

    bpy.ops.object.editmode_toggle()
    bpy.ops.curve.select_all(action='SELECT')
    bpy.ops.curve.handle_type_set(type='AUTOMATIC')
    bpy.ops.object.editmode_toggle()

    bpy.context.object.data.bevel_depth = 5.5

    bpy.ops.object.modifier_add(type='REMESH')
    bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
    bpy.context.object.modifiers["Remesh"].octree_depth = 6
    bpy.context.object.modifiers["Remesh"].scale = 0.99


#    bpy.context.object.location = 0,0,0

class CriaBezier(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_curva_bezier"
    bl_label = "Create Points Line 2"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        CriaBezierDef(self, context)

        return {'FINISHED'}

bpy.utils.register_class(CriaBezier)

def CriaBezierUnidoDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene


    Pontos = [obj for obj in bpy.context.scene.objects if fnmatch.fnmatchcase(obj.name, "PT_Linh*")]

    coords = []

    for i in Pontos:
        VetorAtual = i.location
        VetX = i.location[0]
        VetY = i.location[1]
        VetZ = i.location[2]
        coords.append((VetX, VetY, VetZ))

#    edges = []

#    for i in range(len(vertices)):
#        edges.append([i,i+1])

#    del(edges[-1]) # Apaga o último elemento da cena


    # create the Curve Datablock
    curveData = bpy.data.curves.new('myCurve', type='CURVE')
    curveData.dimensions = '3D'
#    curveData.resolution_u = 6
    curveData.resolution_u = 36


    # map coords to spline
    polyline = curveData.splines.new('BEZIER')
    polyline.bezier_points.add(len(coords)-1)
#    for i, coord in enumerate(coords):
#        x,y,z = coord
#        polyline.points[i].co = (x, y, z, 1)

    from bpy_extras.io_utils import unpack_list
    polyline.bezier_points.foreach_set("co", unpack_list(coords))

    # Apaga pontos
    bpy.ops.object.select_all(action='DESELECT')

    for i in Pontos:
        i.select_set(True)

    bpy.ops.object.delete(use_global=False)

    

    # Cria Linha
    curveOB = bpy.data.objects.new('myCurve', curveData)

    # attach to scene and validate context
    scn = bpy.context.scene
#   scn.objects.link(curveOB)
    scn.collection.objects.link(curveOB)
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = curveOB
    curveOB.select_set(True)

    bpy.ops.object.editmode_toggle()
    bpy.ops.curve.select_all(action='SELECT')
    bpy.ops.curve.handle_type_set(type='AUTOMATIC')

    bpy.ops.curve.make_segment()

    bpy.ops.object.editmode_toggle()

    bpy.ops.object.modifier_add(type='SHRINKWRAP')
    bpy.context.object.modifiers["Shrinkwrap"].target = obj
    bpy.context.object.modifiers["Shrinkwrap"].offset = 0.01
    bpy.context.object.modifiers["Shrinkwrap"].wrap_mode = 'ABOVE_SURFACE'

    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj




class CriaBezierUnido(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_curva_bezier_unido"
    bl_label = "Create Points Line 2"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        CriaBezierUnidoDef(self, context)

        return {'FINISHED'}

bpy.utils.register_class(CriaBezierUnido)

def BezierCortaDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.editmode_toggle()

    objInicial = obj.name


    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['myCurve'].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects['myCurve']

    bpy.context.object.modifiers["Shrinkwrap"].offset = 0

    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')

    context = bpy.context
    obj = context.active_object
    bm = bmesh.from_edit_mesh(obj.data)
    vertices = bm.verts
    edges = bm.verts

    VertIndexOrigi = []

    for i in edges:
        print(i.index)
        VertIndexOrigi.append(i.index)

    print("VertIndexOrigi:", VertIndexOrigi)

    # Extruda para dentro   
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})

    bpy.ops.transform.resize(value=(0.9, 0.9, 0.9), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.select_all(action='DESELECT')

    for i in VertIndexOrigi:
    #    print(vertices)

        # É necessário fazer isso senão não seleciona e dá erro!
        if hasattr(bm.edges, "ensure_lookup_table"): 
            bm.edges.ensure_lookup_table()
            
        bm.edges[i].select_set(True)

    # Extruda para fora    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})

    bpy.ops.transform.resize(value=(1.1, 1.1, 1.1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.select_all(action='DESELECT')

    for i in VertIndexOrigi:
    #    print(vertices)

        # É necessário fazer isso senão não seleciona e dá erro!
        if hasattr(bm.edges, "ensure_lookup_table"): 
            bm.edges.ensure_lookup_table()
            
        bm.edges[i].select_set(True)

    # Apaga vértices do meio e une as outras 
    bpy.ops.mesh.delete(type='VERT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.bridge_edge_loops()

    bpy.ops.object.editmode_toggle()

    bpy.data.objects[objInicial].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects[objInicial]

    
    bpy.ops.object.join()

    obj = context.active_object

    bpy.ops.object.editmode_toggle()


    bm2 = bmesh.from_edit_mesh(obj.data)
    vertices2 = bm2.verts
    edges2 = bm2.edges

    VertIndexOrigi2 = []

    for i in vertices2:
        if i.select == True:
            print(i.index)
            VertIndexOrigi2.append(i.index)


    bpy.ops.mesh.select_all(action='SELECT')

    bpy.ops.mesh.intersect()
    bpy.ops.mesh.intersect(mode='SELECT')

    bpy.ops.mesh.select_all(action='DESELECT')

    
    for i in VertIndexOrigi2:
    #    print(vertices)

        # É necessário fazer isso senão não seleciona e dá erro!
        if hasattr(bm2.verts, "ensure_lookup_table"): 
            bm2.verts.ensure_lookup_table()
            
        bm2.verts[i].select_set(True)

    bpy.ops.mesh.delete(type='VERT')

    bpy.ops.object.editmode_toggle()

    bpy.ops.mesh.separate(type='LOOSE')

    bpy.ops.wm.tool_set_by_id(name="builtin.select_box")

    

class BezierCorta(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "object.bezier_corta"
    bl_label = "Create Points Line 2"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        BezierCortaDef(self, context)

        return {'FINISHED'}

bpy.utils.register_class(BezierCorta)

def BezierCortaDuplaDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.editmode_toggle()

    objInicial = obj.name


    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['myCurve'].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects['myCurve']

    bpy.ops.object.convert(target='MESH')

    # Revoncerte em linha
    bpy.ops.object.convert(target='CURVE')
    bpy.context.object.data.bevel_depth = 0.5

    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')


    # Cria vertex group

    objeto = bpy.data.objects['myCurve']
    vg = objeto.vertex_groups.new(name="Apagar")
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.vertex_group_assign()



    bpy.ops.object.editmode_toggle()

    bpy.ops.object.join()
  
    bpy.ops.object.editmode_toggle()

    context = bpy.context
    obj = context.active_object

   
    bpy.data.objects[objInicial].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects[objInicial]

    
    bpy.ops.object.join()

    # Corta
    bpy.ops.object.editmode_toggle()


    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.intersect(mode='SELECT')
    bpy.ops.mesh.select_all(action='DESELECT')

# --------

    groupName = 'Apagar'


    obj = bpy.context.view_layer.objects.active
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.vertex_group_set_active(group=groupName)
    bpy.ops.object.vertex_group_select()

    bpy.ops.mesh.delete(type='VERT')
 
    bpy.ops.object.editmode_toggle()

    bpy.ops.mesh.separate(type='LOOSE')

    bpy.ops.wm.tool_set_by_id(name="builtin.select_box")



class BezierCortaDupla(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "object.bezier_corta_dupla"
    bl_label = "Create Points Line 2"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        BezierCortaDuplaDef(self, context)

        return {'FINISHED'}

bpy.utils.register_class(BezierCortaDupla)
