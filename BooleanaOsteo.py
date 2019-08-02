import bpy
import os
import tempfile
import subprocess
import platform

def BooleanaMandDef(self, context):

    context = bpy.context
    scn = context.scene

    tmpdir = tempfile.mkdtemp()

    #objetos_selecionados = [ o for o in bpy.context.scene.objects if o.select ]

    A = bpy.data.objects['Bones']
    B = context.active_object #objetos_selecionados[0]

# Infla o objeto    
    bpy.ops.object.mode_set(mode = 'EDIT') 
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action = 'SELECT')
    
    bpy.ops.transform.shrink_fatten(value=-1.61748, use_even_offset=False, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.object.mode_set(mode = 'OBJECT')
    
    bpy.ops.object.modifier_add(type='REMESH')
    bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
    bpy.context.object.modifiers["Remesh"].octree_depth = 7

    # Seleciona objeto A
    A.hide_viewport=False
    bpy.ops.object.select_all(action='DESELECT')
    A.select_set(True)
    bpy.context.view_layer.objects.active = A

    bpy.ops.object.modifier_add(type='TRIANGULATE')
    bpy.ops.export_mesh.off(filepath=tmpdir+"/A.off")
    bpy.ops.object.modifier_remove(modifier="Triangulate")

    
    obj2 = bpy.context.view_layer.objects.active

# ENVIA COLLECTION

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
    
# ----------------------

    # Cria objeto B
    bpy.ops.object.select_all(action='DESELECT')
    B.select_set(True)
    bpy.context.view_layer.objects.active = B

    bpy.ops.object.modifier_add(type='TRIANGULATE')
    bpy.ops.export_mesh.off(filepath=tmpdir+"/B.off")
    bpy.ops.object.modifier_remove(modifier="Triangulate")

    
    obj2 = bpy.context.view_layer.objects.active

# ENVIA COLLETION

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
    
# -------------------

    bpy.ops.object.select_all(action='DESELECT')

    # Booleana
    if platform.system() == "Linux":
        subprocess.call('~/Programs/OrtogOnBlender/Cork/./cork -diff '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Skull.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Skull.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        
        subprocess.call('~/Programs/OrtogOnBlender/Cork/./cork -isct '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Mandible.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Mandible.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    if platform.system() == "Windows":
        subprocess.call('C:\OrtogOnBlender\Cork\wincork.exe -diff '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Skull.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Skull.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        
        subprocess.call('C:\OrtogOnBlender\Cork\wincork.exe -isct '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Mandible.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Mandible.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    if platform.system() == "Darwin":
        subprocess.call('/OrtogOnBlender/Cork/./cork -diff '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Skull.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Skull.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        
        subprocess.call('/OrtogOnBlender/Cork/./cork -isct '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Mandible.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Mandible.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    
    Mandible = bpy.data.objects['Mandible']
    bpy.ops.object.select_all(action='DESELECT')
    Mandible.select_set(True)
    bpy.context.view_layer.objects.active = Mandible
    bpy.ops.object.move_to_collection(collection_index=1)
        
class BooleanaMand(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.booleana_mandib"
    bl_label = "Booleanas da mandíbula"
    
    def execute(self, context):
       BooleanaMandDef(self, context)
       return {'FINISHED'}

def BooleanaOsteoDef(self, context):

    context = bpy.context
#    obj = context.active_object
    scn = context.scene

    tmpdir = tempfile.mkdtemp()

#    objetos_selecionados = [ o for o in bpy.context.scene.objects if o.select_set ]

#    A = objetos_selecionados[1]
#    B = objetos_selecionados[0]

    B = bpy.data.objects['Corte']
    A = context.active_object #objetos_selecionados[0]

    # Cria objeto A
    bpy.ops.object.select_all(action='DESELECT')
    A.select_set(True)
    bpy.context.view_layer.objects.active = A



    bpy.ops.object.modifier_add(type='TRIANGULATE')
    bpy.ops.export_mesh.off(filepath=tmpdir+"/A.off")
    bpy.ops.object.modifier_remove(modifier="Triangulate")


    obj2 = bpy.context.view_layer.objects.active



# ENVIA COLLECTION

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

    # Cria objeto B
    bpy.ops.object.select_all(action='DESELECT')
    B.select_set(True)
    bpy.context.view_layer.objects.active = B

    bpy.ops.object.modifier_add(type='TRIANGULATE')
    bpy.ops.export_mesh.off(filepath=tmpdir+"/B.off")
    bpy.ops.object.modifier_remove(modifier="Triangulate")

    obj2 = bpy.context.view_layer.objects.active

# ENVIA COLLECTION

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

    bpy.ops.object.select_all(action='DESELECT')


    # Booleana
    if platform.system() == "Linux":
        subprocess.call('~/Programs/OrtogOnBlender/Cork/./cork -diff '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')


    if platform.system() == "Windows":
        subprocess.call('C:\OrtogOnBlender\Cork\wincork.exe -diff '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    if platform.system() == "Darwin":
        subprocess.call('/OrtogOnBlender/Cork/./cork -diff '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    

#    Result = context.active_object
#    Result = bpy.context.view_layer.objects.active

    objetos_selecionados = [ o for o in bpy.context.scene.objects if o.select_set ]
    
    try:
        bpy.data.collections['Collection'].objects.link(objetos_selecionados[0])
    except:
        print("O objeto já está na Collecion!")

#    obj = context.active_object


    bpy.ops.mesh.separate(type='LOOSE')

    objetos_selecionados = [ o for o in bpy.context.scene.objects if o.select_set ]

    for i in objetos_selecionados:
        bpy.ops.object.select_all(action='DESELECT')
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        bpy.ops.object.move_to_collection(collection_index=1)
        bpy.ops.object.transforms_to_deltas(mode='ALL')


class BooleanaOsteoClass(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.booleana_osteo"
    bl_label = "Importa fatias de tomografia DICOM"
    
    def execute(self, context):
        BooleanaOsteoDef(self, context)
#        bpy.ops.object.collection_link(collection='Collection')
        return {'FINISHED'}


def BooleanaOsteoGeralDef(self, context):

    context = bpy.context
#    obj = context.active_object
    scn = context.scene

    tmpdir = tempfile.mkdtemp()


    B = bpy.context.view_layer.objects.active
    print("Objeto B:", B)

    for i in bpy.context.selected_objects:
        if i.name != B.name:
            A = i
            print("Objeto A:", A.name)
#    B = bpy.context.selected_objects[1]

#    B = bpy.data.objects['Corte']
#    A = context.active_object #objetos_selecionados[0]

    # Remover vértices duplos
    bpy.ops.object.select_all(action='DESELECT')
    A.select_set(True)
    bpy.context.view_layer.objects.active = A

    if A.type == 'MESH':
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')
    else:
        print("Não é malha!")
    bpy.ops.object.select_all(action='DESELECT')
    B.select_set(True)
    bpy.context.view_layer.objects.active = B
    if B.type == 'MESH':
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')
    else:
        print("Não é malha!")


    # Cria objeto A
    bpy.ops.object.select_all(action='DESELECT')
    A.select_set(True)
    bpy.context.view_layer.objects.active = A



    bpy.ops.object.modifier_add(type='TRIANGULATE')
    bpy.ops.export_mesh.off(filepath=tmpdir+"/A.off")
    bpy.ops.object.modifier_remove(modifier="Triangulate")


    obj2 = bpy.context.view_layer.objects.active



# ENVIA COLLECTION

    ListaColl = []

    for i in bpy.data.collections:
        ListaColl.append(i.name)

    if "Copied_Objects" not in ListaColl:

        obj = context.active_object
        myCol = bpy.data.collections.new("Copied_Objects")
        bpy.context.scene.collection.children.link(myCol)
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj)


    else:
        obj = context.active_object
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj)

    bpy.data.collections['Copied_Objects'].hide_viewport=True

    # Cria objeto B
    bpy.ops.object.select_all(action='DESELECT')
    B.select_set(True)
    bpy.context.view_layer.objects.active = B

    bpy.ops.object.modifier_add(type='TRIANGULATE')
    bpy.ops.export_mesh.off(filepath=tmpdir+"/B.off")
    bpy.ops.object.modifier_remove(modifier="Triangulate")

    obj2 = bpy.context.view_layer.objects.active

# ENVIA COLLECTION

    ListaColl = []

    for i in bpy.data.collections:
        ListaColl.append(i.name)

    if "Copied_Objects" not in ListaColl:

        obj = context.active_object
        myCol = bpy.data.collections.new("Copied_Objects")
        bpy.context.scene.collection.children.link(myCol)
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj2)


    else:
        obj = context.active_object
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj2)

    bpy.data.collections['Copied_Objects'].hide_viewport=True

    bpy.ops.object.select_all(action='DESELECT')

    # OCulta objetos originais
    A.hide_viewport=True
    B.hide_viewport=True

    # Booleana
    if platform.system() == "Linux":
        subprocess.call('~/Programs/OrtogOnBlender/Cork/./cork -diff '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    if platform.system() == "Windows":
        subprocess.call('C:\OrtogOnBlender\Cork\wincork.exe -diff '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    if platform.system() == "Darwin":
        subprocess.call('/OrtogOnBlender/Cork/./cork -diff '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

#    Result = context.active_object
#    Result = bpy.context.view_layer.objects.active

#    objetos_selecionados = [ o for o in bpy.context.scene.objects if o.select_set ]
#    bpy.data.collections['Collection'].objects.link(objetos_selecionados[0])

#    bpy.data.collections['Collection'].objects.link(bpy.context.selected_objects[0])

    bpy.ops.mesh.separate(type='LOOSE')

    objetos_selecionados = [ o for o in bpy.context.selected_objects ]

    for i in objetos_selecionados:
        bpy.ops.object.select_all(action='DESELECT')
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        bpy.ops.object.collection_link(collection='Collection')
        bpy.ops.object.move_to_collection(collection_index=1)
        bpy.ops.object.transforms_to_deltas(mode='ALL')


class BooleanaOsteoGeral(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.booleana_osteo_geral"
    bl_label = "Importa fatias de tomografia DICOM"
    
    def execute(self, context):
        BooleanaOsteoGeralDef(self, context)
#        bpy.ops.object.collection_link(collection='Collection')
        return {'FINISHED'}

# Booleana Union

def BooleanaOsteoUnionDef(self, context):

    context = bpy.context
#    obj = context.active_object
    scn = context.scene

    tmpdir = tempfile.mkdtemp()


    B = bpy.context.view_layer.objects.active
    print("Objeto B:", B)

    for i in bpy.context.selected_objects:
        if i.name != B.name:
            A = i
            print("Objeto A:", A.name)
#    B = bpy.context.selected_objects[1]

#    B = bpy.data.objects['Corte']
#    A = context.active_object #objetos_selecionados[0]

    # Remover vértices duplos
    bpy.ops.object.select_all(action='DESELECT')
    A.select_set(True)
    bpy.context.view_layer.objects.active = A
    if A.type == 'MESH':
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')
    else:
        print("Não é malha!")
    bpy.ops.object.select_all(action='DESELECT')
    B.select_set(True)
    bpy.context.view_layer.objects.active = B
    if B.type == 'MESH':
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')
    else:
        print("Não é malha!")

    # Cria objeto A
    bpy.ops.object.select_all(action='DESELECT')
    A.select_set(True)
    bpy.context.view_layer.objects.active = A



    bpy.ops.object.modifier_add(type='TRIANGULATE')
    bpy.ops.export_mesh.off(filepath=tmpdir+"/A.off")
    bpy.ops.object.modifier_remove(modifier="Triangulate")


#    obj2 = bpy.context.view_layer.objects.active



# ENVIA COLLECTION

    ListaColl = []

    for i in bpy.data.collections:
        ListaColl.append(i.name)

    if "Copied_Objects" not in ListaColl:

        obj = context.active_object
        myCol = bpy.data.collections.new("Copied_Objects")
        bpy.context.scene.collection.children.link(myCol)
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj)


    else:
        obj = context.active_object
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj)

    bpy.data.collections['Copied_Objects'].hide_viewport=True


    # Cria objeto B
    bpy.ops.object.select_all(action='DESELECT')
    B.select_set(True)
    bpy.context.view_layer.objects.active = B

    bpy.ops.object.modifier_add(type='TRIANGULATE')
    bpy.ops.export_mesh.off(filepath=tmpdir+"/B.off")
    bpy.ops.object.modifier_remove(modifier="Triangulate")

    obj2 = bpy.context.view_layer.objects.active

# ENVIA COLLECTION

    ListaColl = []

    for i in bpy.data.collections:
        ListaColl.append(i.name)

    if "Copied_Objects" not in ListaColl:

        myCol = bpy.data.collections.new("Copied_Objects")
        bpy.context.scene.collection.children.link(myCol)
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj2)


    else:
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj2)



    bpy.data.collections['Copied_Objects'].hide_viewport=True

    bpy.ops.object.select_all(action='DESELECT')


    # OCulta objetos originais
#    A.hide_viewport=True
#    B.hide_viewport=True

    # Booleana
    if platform.system() == "Linux":
        subprocess.call('~/Programs/OrtogOnBlender/Cork/./cork -union '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    if platform.system() == "Windows":
        subprocess.call('C:\OrtogOnBlender\Cork\wincork.exe -union '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    if platform.system() == "Darwin":
        subprocess.call('/OrtogOnBlender/Cork/./cork -union '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')



#    Result = context.active_object
#    Result = bpy.context.view_layer.objects.active

#    objetos_selecionados = [ o for o in bpy.context.scene.objects if o.select_set ]
#    bpy.data.collections['Collection'].objects.link(objetos_selecionados[0])

#    bpy.data.collections['Collection'].objects.link(bpy.context.selected_objects[0])

    bpy.ops.mesh.separate(type='LOOSE')


    objetos_selecionados = [ o for o in bpy.context.selected_objects ]

    for i in objetos_selecionados:
        if i.visible_get() == True:
            bpy.ops.object.select_all(action='DESELECT')
            i.select_set(True)
            bpy.context.view_layer.objects.active = i
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            bpy.ops.object.collection_link(collection='Collection')
            bpy.ops.object.move_to_collection(collection_index=1)
            bpy.ops.object.transforms_to_deltas(mode='ALL')


class BooleanaOsteoUnion(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.booleana_osteo_union"
    bl_label = "Importa fatias de tomografia DICOM"
    
    def execute(self, context):
        BooleanaOsteoUnionDef(self, context)
#g        bpy.ops.object.collection_link(collection='Collection')
        return {'FINISHED'}

bpy.utils.register_class(BooleanaOsteoUnion)

# Booleana Intersect

def BooleanaOsteoInterDef(self, context):

    context = bpy.context
#    obj = context.active_object
    scn = context.scene

    tmpdir = tempfile.mkdtemp()


    B = bpy.context.view_layer.objects.active
    print("Objeto B:", B)

    for i in bpy.context.selected_objects:
        if i.name != B.name:
            A = i
            print("Objeto A:", A.name)
#    B = bpy.context.selected_objects[1]

#    B = bpy.data.objects['Corte']
#    A = context.active_object #objetos_selecionados[0]

    # Remover vértices duplos
    bpy.ops.object.select_all(action='DESELECT')
    A.select_set(True)
    bpy.context.view_layer.objects.active = A
    if A.type == 'MESH':
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')
    else:
        print("Não é malha!")
    bpy.ops.object.select_all(action='DESELECT')
    B.select_set(True)
    bpy.context.view_layer.objects.active = B
    if B.type == 'MESH':
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')
    else:
        print("Não é malha!")

    # Cria objeto A
    bpy.ops.object.select_all(action='DESELECT')
    A.select_set(True)
    bpy.context.view_layer.objects.active = A



    bpy.ops.object.modifier_add(type='TRIANGULATE')
    bpy.ops.export_mesh.off(filepath=tmpdir+"/A.off")
    bpy.ops.object.modifier_remove(modifier="Triangulate")


    obj2 = bpy.context.view_layer.objects.active



# ENVIA COLLECTION

    ListaColl = []

    for i in bpy.data.collections:
        ListaColl.append(i.name)

    if "Copied_Objects" not in ListaColl:

        obj = context.active_object
        myCol = bpy.data.collections.new("Copied_Objects")
        bpy.context.scene.collection.children.link(myCol)
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj)


    else:
        obj = context.active_object
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj)

    bpy.data.collections['Copied_Objects'].hide_viewport=True

    # Cria objeto B
    bpy.ops.object.select_all(action='DESELECT')
    B.select_set(True)
    bpy.context.view_layer.objects.active = B

    bpy.ops.object.modifier_add(type='TRIANGULATE')
    bpy.ops.export_mesh.off(filepath=tmpdir+"/B.off")
    bpy.ops.object.modifier_remove(modifier="Triangulate")

    obj2 = bpy.context.view_layer.objects.active

# ENVIA COLLECTION

    ListaColl = []

    for i in bpy.data.collections:
        ListaColl.append(i.name)

    if "Copied_Objects" not in ListaColl:

        myCol = bpy.data.collections.new("Copied_Objects")
        bpy.context.scene.collection.children.link(myCol)
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj2)


    else:
        bpy.ops.object.collection_link(collection='Copied_Objects')
        try:
            bpy.data.collections['Collection'].objects.unlink(obj2)
        except:
            print("Não está no Collection!")

    bpy.data.collections['Copied_Objects'].hide_viewport=True

    bpy.ops.object.select_all(action='DESELECT')

    # OCulta objetos originais
    A.hide_viewport=True
    B.hide_viewport=True

    # Booleana
    if platform.system() == "Linux":
        subprocess.call('~/Programs/OrtogOnBlender/Cork/./cork -isct '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    if platform.system() == "Windows":
        subprocess.call('C:\OrtogOnBlender\Cork\wincork.exe -isct '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    if platform.system() == "Darwin":
        subprocess.call('/OrtogOnBlender/Cork/./cork -isct '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')



#    Result = context.active_object
#    Result = bpy.context.view_layer.objects.active

#    objetos_selecionados = [ o for o in bpy.context.scene.objects if o.select_set ]
#    bpy.data.collections['Collection'].objects.link(objetos_selecionados[0])

#    bpy.data.collections['Collection'].objects.link(bpy.context.selected_objects[0])

    bpy.ops.mesh.separate(type='LOOSE')

    objetos_selecionados = [ o for o in bpy.context.selected_objects ]

    '''
    for i in objetos_selecionados:
        bpy.ops.object.collection_link(collection='Collection')
        bpy.ops.object.select_all(action='DESELECT')
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    '''

    for i in objetos_selecionados:
        if i.visible_get() == True:
            bpy.ops.object.select_all(action='DESELECT')
            i.select_set(True)
            bpy.context.view_layer.objects.active = i
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            bpy.ops.object.collection_link(collection='Collection')
            bpy.ops.object.move_to_collection(collection_index=1)
            bpy.ops.object.transforms_to_deltas(mode='ALL')


class BooleanaOsteoInter(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.booleana_osteo_inter"
    bl_label = "Importa fatias de tomografia DICOM"
    
    def execute(self, context):
        BooleanaOsteoInterDef(self, context)
#        bpy.ops.object.collection_link(collection='Collection')
        return {'FINISHED'}

bpy.utils.register_class(BooleanaOsteoInter)


def BooleanaUnionSimplesDef(self, context):

    context = bpy.context
#    obj = context.active_object
    scn = context.scene

    tmpdir = tempfile.mkdtemp()


    B = bpy.context.view_layer.objects.active
    print("Objeto B:", B)

    for i in bpy.context.selected_objects:
        if i.name != B.name:
            A = i
            print("Objeto A:", A.name)
#    B = bpy.context.selected_objects[1]

#    B = bpy.data.objects['Corte']
#    A = context.active_object #objetos_selecionados[0]

    # Remover vértices duplos
    bpy.ops.object.select_all(action='DESELECT')
    A.select_set(True)
    bpy.context.view_layer.objects.active = A
    if A.type == 'MESH':
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')
    else:
        print("Não é malha!")
    bpy.ops.object.select_all(action='DESELECT')
    B.select_set(True)
    bpy.context.view_layer.objects.active = B
    if B.type == 'MESH':
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')
    else:
        print("Não é malha!")
    bpy.ops.object.mode_set(mode='OBJECT')


    # Cria objeto A
    bpy.ops.object.select_all(action='DESELECT')
    A.select_set(True)
    bpy.context.view_layer.objects.active = A



    bpy.ops.object.modifier_add(type='TRIANGULATE')
    bpy.ops.export_mesh.off(filepath=tmpdir+"/A.off")
    bpy.ops.object.modifier_remove(modifier="Triangulate")


    obj2 = bpy.context.view_layer.objects.active



# ENVIA COLLECTION

    ListaColl = []

    for i in bpy.data.collections:
        ListaColl.append(i.name)

    if "Copied_Objects" not in ListaColl:

        obj = context.active_object
        myCol = bpy.data.collections.new("Copied_Objects")
        bpy.context.scene.collection.children.link(myCol)
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj)


    else:
        obj = context.active_object
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj)

    bpy.data.collections['Copied_Objects'].hide_viewport=True

    # Cria objeto B
    bpy.ops.object.select_all(action='DESELECT')
    B.select_set(True)
    bpy.context.view_layer.objects.active = B

    bpy.ops.object.modifier_add(type='TRIANGULATE')
    bpy.ops.export_mesh.off(filepath=tmpdir+"/B.off")
    bpy.ops.object.modifier_remove(modifier="Triangulate")

    obj2 = bpy.context.view_layer.objects.active

# ENVIA COLLECTION

    ListaColl = []

    for i in bpy.data.collections:
        ListaColl.append(i.name)

    if "Copied_Objects" not in ListaColl:

        myCol = bpy.data.collections.new("Copied_Objects")
        bpy.context.scene.collection.children.link(myCol)
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj2)


    else:
        bpy.ops.object.collection_link(collection='Copied_Objects')
        bpy.data.collections['Collection'].objects.unlink(obj2)

    bpy.data.collections['Copied_Objects'].hide_viewport=True

    bpy.ops.object.select_all(action='DESELECT')

    # OCulta objetos originais
    A.hide_viewport=True
    B.hide_viewport=True

    # Booleana
    if platform.system() == "Linux":
        subprocess.call('~/Programs/OrtogOnBlender/Cork/./cork -union '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    if platform.system() == "Windows":
        subprocess.call('C:\OrtogOnBlender\Cork\wincork.exe -union '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

    if platform.system() == "Darwin":
        subprocess.call('/OrtogOnBlender/Cork/./cork -union '+tmpdir+'/A.off '+tmpdir+'/B.off '+tmpdir+'/Result.off', shell=True)
        bpy.ops.import_mesh.off(filepath=tmpdir+"/Result.off")
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')


#    Result = context.active_object
#    Result = bpy.context.view_layer.objects.active

#    objetos_selecionados = [ o for o in bpy.context.scene.objects if o.select_set ]
#    bpy.data.collections['Collection'].objects.link(objetos_selecionados[0])

#    bpy.data.collections['Collection'].objects.link(bpy.context.selected_objects[0])

#    bpy.ops.mesh.separate(type='LOOSE')

    objetos_selecionados = [ o for o in bpy.context.selected_objects ]

    for i in objetos_selecionados:
        if i.visible_get() == True:
            bpy.ops.object.select_all(action='DESELECT')
            i.select_set(True)
            bpy.context.view_layer.objects.active = i
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            bpy.ops.object.collection_link(collection='Collection')
            bpy.ops.object.move_to_collection(collection_index=1)
            bpy.ops.object.transforms_to_deltas(mode='ALL')

        
class BooleanaUnionSimples(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.booleana_union_simples"
    bl_label = "Importa fatias de tomografia DICOM"
    
    def execute(self, context):
        BooleanaUnionSimplesDef(self, context)
#        bpy.ops.object.collection_link(collection='Collection')
        return {'FINISHED'}


bpy.utils.register_class(BooleanaUnionSimples)   
# -------------------

def UnionMultiplaDef(self, context):
    Objetos = [ o for o in bpy.context.selected_objects ]
    #Results = []

    Contador = int(len(Objetos))

    while Contador > 1:
        bpy.ops.object.select_all(action='DESELECT')
        Objetos[0].select_set(True)       
        Objetos[-1].select_set(True) 
        bpy.context.view_layer.objects.active = Objetos[0]
        bpy.ops.object.booleana_union_simples()
        Objetos.remove(Objetos[0])
        Objetos.remove(Objetos[-1])
        Objetos.append(bpy.context.active_object)
        Contador = int(len(Objetos))
        print("Contador", Contador)

class UnionMultipla(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.booleana_union_multipla"
    bl_label = "Ortog multiple union boolean"
    
    def execute(self, context):
        UnionMultiplaDef(self, context)
#        bpy.ops.object.collection_link(collection='Collection')
        return {'FINISHED'}


bpy.utils.register_class(UnionMultipla) 
