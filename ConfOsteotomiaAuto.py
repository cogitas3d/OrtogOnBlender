import bpy
import platform
import bmesh

# IMPORTA ARMATURE

def ImportaArmatureDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    if platform.system() == "Linux" or platform.system() == "Darwin":
        dirScript = bpy.utils.user_resource('SCRIPTS')
        
        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Object\\"
        object    = "Armature_Head"
        
    if platform.system() == "Windows":
        dirScript = 'C:/OrtogOnBlender/Blender/2.78/scripts/' 

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Object\\"
        object    = "Armature_Head"

    filepath  = blendfile + section + object
    directory = blendfile + section
    filename  = object

    bpy.ops.wm.append(
        filepath=filepath, 
        filename=filename,
        directory=directory)
        
 #   bpy.ops.wm.append(filename=filename, directory=directory)

    # APAGA OBJETOS EXCEDENTES

    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['Mandibula']
    b = bpy.data.objects['SETA_Corpo_M']
    c = bpy.data.objects['SETA_Maxila']
    d = bpy.data.objects['SETA_Mento']


    a.select_set(True)
    b.select_set(True)
    c.select_set(True)
    d.select_set(True)


    bpy.ops.object.delete(use_global=False)

class ImportaArmature(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.importa_armature"
    bl_label = "Importa estrutura de bones"
    
    def execute(self, context):
        ImportaArmatureDef(self, context)
        return {'FINISHED'}

# CONFIGURA CABEÇA

def ConfiguraCabecaDef(self, context):

    context = bpy.context
    obj = context.active_object
 #   scn = context.scene


 
    ob=bpy.data.objects["Armature_Head"]
        
    bpy.ops.object.mode_set(mode='EDIT')
    mesh=bmesh.from_edit_mesh(bpy.context.object.data)
    for v in mesh.verts:
        v.select_set(True)

    vg = obj.vertex_groups.new(name="ca")
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.vertex_group_assign()
    bpy.ops.object.mode_set(mode='OBJECT')
        
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialCabeca") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0.8, 0.75, 0.2, 1) #change color
    bpy.context.object.name = "ca"

    armatureHead = bpy.data.objects['Armature_Head']
    bpy.ops.object.select_all(action='DESELECT')
    armatureHead.hide_viewport=False
    armatureHead.select_set(True)
    bpy.context.view_layer.objects.active = armatureHead
    bpy.ops.object.posemode_toggle()
#    bpy.data.objects['ca'].select = True
#    bpy.data.objects['Armature_Head'].select = True
#    bpy.ops.object.parent_set(type='ARMATURE_NAME')

    bpy.ops.pose.select_all(action='DESELECT')
    o=bpy.context.object
    b=o.data.bones['ca']
    b.select=True
    o.data.bones.active=b
     
    bpy.ops.pose.constraint_add(type='CHILD_OF')
    bpy.context.object.pose.bones["ca"].constraints["Child Of"].target = bpy.data.objects["ca"]

    pbone = bpy.context.active_object.pose.bones["ca"] # Bone
    context_copy = bpy.context.copy()
    context_copy["constraint"] = pbone.constraints["Child Of"]
    bpy.ops.constraint.childof_set_inverse(context_copy, constraint="Child Of", owner='BONE')

    bpy.ops.object.posemode_toggle()
    armatureHead.hide_viewport=True  


class ConfiguraCabeca(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_cabeca"
    bl_label = "Configura Cabeça"
    
    def execute(self, context):
        ConfiguraCabecaDef(self, context)
        return {'FINISHED'}

# CONFIGURA MAXILA
def ConfiguraMaxilaDef(self, context):

    context = bpy.context
    obj = context.active_object
 #   scn = context.scene


    ob=bpy.data.objects["Armature_Head"]

    bpy.ops.object.mode_set(mode='EDIT')
    mesh=bmesh.from_edit_mesh(bpy.context.object.data)
    for v in mesh.verts:
        v.select = True

    vg = obj.vertex_groups.new(name="Maxila.GUIA")
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.vertex_group_assign()
    bpy.ops.object.mode_set(mode='OBJECT')
    
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialMaxila") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0.8, 0.3, 0.2, 1) #change color
    bpy.context.object.name = "ma"

    armatureHead = bpy.data.objects['Armature_Head']
    bpy.ops.object.select_all(action='DESELECT')
    armatureHead.hide_viewport=False
    armatureHead.select_set(True)
    bpy.context.view_layer.objects.active = armatureHead
    bpy.ops.object.posemode_toggle()
#    bpy.data.objects['ma'].select = True
#    bpy.data.objects['Armature_Head'].select = True
#    bpy.ops.object.parent_set(type='ARMATURE_NAME')

    bpy.ops.pose.select_all(action='DESELECT')
    o=bpy.context.object
    b=o.data.bones['Maxila.GUIA']
    b.select=True
    o.data.bones.active=b
 
    bpy.ops.pose.constraint_add(type='CHILD_OF')
    bpy.context.object.pose.bones["Maxila.GUIA"].constraints["Child Of"].target = bpy.data.objects["ma"]

    pbone = bpy.context.active_object.pose.bones["Maxila.GUIA"] # Bone
    context_copy = bpy.context.copy()
    context_copy["constraint"] = pbone.constraints["Child Of"]
    bpy.ops.constraint.childof_set_inverse(context_copy, constraint="Child Of", owner='BONE')

    bpy.ops.object.posemode_toggle()
    armatureHead.hide_viewport=True

class ConfiguraMaxila(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_maxila"
    bl_label = "Configura Maxila"
    
    def execute(self, context):
        ConfiguraMaxilaDef(self, context)
        return {'FINISHED'}

# CONFIGURA RAMO DIREITO
def ConfiguraRamoDirDef(self, context):
    
    context = bpy.context
    obj = context.active_object
 #   scn = context.scene

 
    ob=bpy.data.objects["Armature_Head"]

    bpy.ops.object.mode_set(mode='EDIT')
    mesh=bmesh.from_edit_mesh(bpy.context.object.data)
    for v in mesh.verts:
        v.select = True

    vg = obj.vertex_groups.new(name="rd")
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.vertex_group_assign()
    bpy.ops.object.mode_set(mode='OBJECT')

    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialRamoDir") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0.4, 0.3, 0.8, 1) #change color
    bpy.context.object.name = "rd"

    armatureHead = bpy.data.objects['Armature_Head']
    bpy.ops.object.select_all(action='DESELECT')
    armatureHead.hide_viewport=False
    armatureHead.select_set(True)
    bpy.context.view_layer.objects.active = armatureHead
    bpy.ops.object.posemode_toggle()
#    bpy.data.objects['rd'].select = True
#    bpy.data.objects['Armature_Head'].select = True
#    bpy.ops.object.parent_set(type='ARMATURE_NAME')

    bpy.ops.pose.select_all(action='DESELECT')
    o=bpy.context.object
    b=o.data.bones['rd']
    b.select=True
    o.data.bones.active=b
 
    bpy.ops.pose.constraint_add(type='CHILD_OF')
    bpy.context.object.pose.bones["rd"].constraints["Child Of"].target = bpy.data.objects["rd"]

    pbone = bpy.context.active_object.pose.bones["rd"] # Bone
    context_copy = bpy.context.copy()
    context_copy["constraint"] = pbone.constraints["Child Of"]
    bpy.ops.constraint.childof_set_inverse(context_copy, constraint="Child Of", owner='BONE')

    bpy.ops.object.posemode_toggle()
    armatureHead.hide_viewport=True

class ConfiguraRamoDir(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_ramo_dir"
    bl_label = "Configura Ramo Direito"
    
    def execute(self, context):
        ConfiguraRamoDirDef(self, context)
        return {'FINISHED'}

# CONFIGURA RAMO ESQUERDO
def ConfiguraRamoEsqDef(self, context):

    context = bpy.context
    obj = context.active_object
 #   scn = context.scene

 
    ob=bpy.data.objects["Armature_Head"]

    bpy.ops.object.mode_set(mode='EDIT')
    mesh=bmesh.from_edit_mesh(bpy.context.object.data)
    for v in mesh.verts:
        v.select = True

    vg = obj.vertex_groups.new(name="re")
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.vertex_group_assign()
    bpy.ops.object.mode_set(mode='OBJECT')
    
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialRamoEsq") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0.4, 0.3, 0.8, 1) #change color
    bpy.context.object.name = "re"

    armatureHead = bpy.data.objects['Armature_Head']
    bpy.ops.object.select_all(action='DESELECT')
    armatureHead.hide_viewport=False
    armatureHead.select_set(True)
    bpy.context.view_layer.objects.active = armatureHead
    bpy.ops.object.posemode_toggle()
#    bpy.data.objects['re'].select = True
#    bpy.data.objects['Armature_Head'].select = True
#    bpy.ops.object.parent_set(type='ARMATURE_NAME')

    bpy.ops.pose.select_all(action='DESELECT')
    o=bpy.context.object
    b=o.data.bones['re']
    b.select=True
    o.data.bones.active=b
 
    bpy.ops.pose.constraint_add(type='CHILD_OF')
    bpy.context.object.pose.bones["re"].constraints["Child Of"].target = bpy.data.objects["re"]

    pbone = bpy.context.active_object.pose.bones["re"] # Bone
    context_copy = bpy.context.copy()
    context_copy["constraint"] = pbone.constraints["Child Of"]
    bpy.ops.constraint.childof_set_inverse(context_copy, constraint="Child Of", owner='BONE')

    bpy.ops.object.posemode_toggle()
    armatureHead.hide_viewport=True

class ConfiguraRamoEsq(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_ramo_esq"
    bl_label = "Configura Ramo Esquerdo"
    
    def execute(self, context):
        ConfiguraRamoEsqDef(self, context)
        return {'FINISHED'}

# CONFIGURA RAMO DA MANDÍBULA
def ConfiguraCorpoMandDef(self, context):
    
    context = bpy.context
    obj = context.active_object
 #   scn = context.scene


    ob=bpy.data.objects["Armature_Head"]

    bpy.ops.object.mode_set(mode='EDIT')
    mesh=bmesh.from_edit_mesh(bpy.context.object.data)
    for v in mesh.verts:
        v.select = True

    vg = obj.vertex_groups.new(name="Corpo_Mandibular.GUIA")
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.vertex_group_assign()
    bpy.ops.object.mode_set(mode='OBJECT')

    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialCorpoMand") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0.35, 0.8, 0.4, 1) #change color
    bpy.context.object.name = "cm"

    armatureHead = bpy.data.objects['Armature_Head']
    bpy.ops.object.select_all(action='DESELECT')
    armatureHead.hide_viewport=False
    armatureHead.select_set(True)
    bpy.context.view_layer.objects.active = armatureHead
    bpy.ops.object.posemode_toggle()

#    bpy.data.objects['cm'].select = True
#    bpy.data.objects['Armature_Head'].select = True
#    bpy.ops.object.parent_set(type='ARMATURE_NAME')

    bpy.ops.pose.select_all(action='DESELECT')
    o=bpy.context.object
    b=o.data.bones['Corpo_Mandibular.GUIA']
    b.select=True
    o.data.bones.active=b
 
    bpy.ops.pose.constraint_add(type='CHILD_OF')
    bpy.context.object.pose.bones["Corpo_Mandibular.GUIA"].constraints["Child Of"].target = bpy.data.objects["cm"]

    pbone = bpy.context.active_object.pose.bones["Corpo_Mandibular.GUIA"] # Bone
    context_copy = bpy.context.copy()
    context_copy["constraint"] = pbone.constraints["Child Of"]
    bpy.ops.constraint.childof_set_inverse(context_copy, constraint="Child Of", owner='BONE')


    bpy.ops.object.posemode_toggle()
    armatureHead.hide_viewport=True

class ConfiguraCorpoMand(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_corpo_mand"
    bl_label = "Configura Mento"
    
    def execute(self, context):
        ConfiguraCorpoMandDef(self, context)
        return {'FINISHED'}

# CONFIGURA MENTO
def ConfiguraMentoDef(self, context):

    context = bpy.context
    obj = context.active_object
 #   scn = context.scene

    ob=bpy.data.objects["Armature_Head"]


    ob=bpy.data.objects["cm"]

    bpy.ops.object.mode_set(mode='EDIT')
    mesh=bmesh.from_edit_mesh(bpy.context.object.data)


    for v in mesh.verts:
        v.select = True

    vg = obj.vertex_groups.new(name="me")
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.vertex_group_assign()
    bpy.ops.object.mode_set(mode='OBJECT')
    
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialMento") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0.8, 0.35, 0.2, 1) #change color
    bpy.context.object.name = "me"

    armatureHead = bpy.data.objects['Armature_Head']
    bpy.ops.object.select_all(action='DESELECT')
    armatureHead.hide_viewport=False
    armatureHead.select_set(True)
    bpy.context.view_layer.objects.active = armatureHead
    bpy.ops.object.posemode_toggle()

 #   bpy.data.objects['me'].select = True
 #   bpy.data.objects['Armature_Head'].select = True
 #   bpy.ops.object.parent_set(type='ARMATURE_NAME')

    bpy.ops.pose.select_all(action='DESELECT')
    o=bpy.context.object
    b=o.data.bones['me']
    b.select=True
    o.data.bones.active=b
 
    bpy.ops.pose.constraint_add(type='CHILD_OF')
    bpy.context.object.pose.bones["me"].constraints["Child Of"].target = bpy.data.objects["me"]

    pbone = bpy.context.active_object.pose.bones["me"] # Bone
    context_copy = bpy.context.copy()
    context_copy["constraint"] = pbone.constraints["Child Of"]
    bpy.ops.constraint.childof_set_inverse(context_copy, constraint="Child Of", owner='BONE')

    bpy.ops.object.posemode_toggle()
    armatureHead.hide_viewport=True

    a = bpy.data.objects['cm']
    b = bpy.data.objects['me']

    bpy.ops.object.select_all(action='DESELECT')
    a.select_set(True)
    b.select_set(True) 
    bpy.context.view_layer.objects.active = a
    bpy.ops.object.parent_set()

class ConfiguraMento(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.configura_mento"
    bl_label = "Configura Mento"
    
    def execute(self, context):
        ConfiguraMentoDef(self, context)
        return {'FINISHED'}

# CONFIGURA OSTEO

def ConfOsteotomiaAutoDef(self, context):
    objetos_selecionados = [ o for o in bpy.context.selected_objects ]
#    objetos_selecionados = [ o for o in bpy.context.scene.objects if o.select ]

    Obj_Hor = []
    for i in objetos_selecionados:
        Obj_Hor.append(i.location[0])

    # Ramos da mandíbula    
    MaxHor = max(Obj_Hor)
    IndexMax = [i for i, j in enumerate(Obj_Hor) if j == MaxHor]
    re = objetos_selecionados[int(IndexMax[0])]
    print(re)

    MinHor = min(Obj_Hor)
    IndexMin = [i for i, j in enumerate(Obj_Hor) if j == MinHor]
    rd = objetos_selecionados[int(IndexMin[0])]
    print(rd)

    print("Len antes: ",len(objetos_selecionados))
    objetos_selecionados.remove(re)
    objetos_selecionados.remove(rd)
    print("Len depois: ",len(objetos_selecionados))

    # Cabeça e mento
    Obj_Ver = []
    for i in objetos_selecionados:
        Obj_Ver.append(i.location[2])

    MaxVer = max(Obj_Ver)
    IndexMax = [i for i, j in enumerate(Obj_Ver) if j == MaxVer]
    ca = objetos_selecionados[int(IndexMax[0])]
    print(ca)

    MinVer = min(Obj_Ver)
    IndexMin = [i for i, j in enumerate(Obj_Ver) if j == MinVer]
    me = objetos_selecionados[int(IndexMin[0])]
    print(me)

    print("Len antes: ",len(objetos_selecionados))
    objetos_selecionados.remove(ca)
    objetos_selecionados.remove(me)
    print("Len depois: ",len(objetos_selecionados))


    # Maxila e corpo da mandíbula
    Obj_Ver = []
    for i in objetos_selecionados:
        Obj_Ver.append(i.location[2])
        
    MaxVer = max(Obj_Ver)
    IndexMax = [i for i, j in enumerate(Obj_Ver) if j == MaxVer]
    ma = objetos_selecionados[int(IndexMax[0])]
    print(ma)

    MinVer = min(Obj_Ver)
    IndexMin = [i for i, j in enumerate(Obj_Ver) if j == MinVer]
    cm = objetos_selecionados[int(IndexMin[0])]
    print(cm)

    # Configura osteotomias
    bpy.ops.object.importa_armature()

    ca.select_set(True)
    bpy.context.view_layer.objects.active = ca
    bpy.ops.object.configura_cabeca()
    bpy.ops.object.select_all(action='DESELECT')

    ma.select_set(True)
    bpy.context.view_layer.objects.active = ma
    bpy.ops.object.configura_maxila()
    bpy.ops.object.select_all(action='DESELECT')

    rd.select_set(True)
    bpy.context.view_layer.objects.active = rd
    bpy.ops.object.configura_ramo_dir()
    bpy.ops.object.select_all(action='DESELECT')

    re.select_set(True)
    bpy.context.view_layer.objects.active = re
    bpy.ops.object.configura_ramo_esq()
    bpy.ops.object.select_all(action='DESELECT')

    cm.select_set(True)
    bpy.context.view_layer.objects.active = cm
    bpy.ops.object.configura_corpo_mand()
    bpy.ops.object.select_all(action='DESELECT')

    me.select_set(True)
    bpy.context.view_layer.objects.active = me
    bpy.ops.object.configura_mento()
    bpy.ops.object.select_all(action='DESELECT')

class ConfOsteotomiaAuto(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.conf_osteo_auto"
    bl_label = "Configura osteotomias automaticamente"
    
    def execute(self, context):
       ConfOsteotomiaAutoDef(self, context)
       return {'FINISHED'} 
