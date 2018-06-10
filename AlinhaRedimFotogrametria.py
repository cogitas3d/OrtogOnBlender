import bpy
from math import sqrt

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

    rosto = bpy.data.objects['Rosto_OK']
    rosto.select = True
    bpy.context.scene.objects.active = rosto

    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
