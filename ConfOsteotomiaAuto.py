import bpy

def ConfOsteotomiaAutoDef(self, context):
    objetos_selecionados = [ o for o in bpy.context.scene.objects if o.select ]

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

    ca.select = True
    bpy.context.scene.objects.active = ca
    bpy.ops.object.configura_cabeca()
    bpy.ops.object.select_all(action='DESELECT')

    ma.select = True
    bpy.context.scene.objects.active = ma
    bpy.ops.object.configura_maxila()
    bpy.ops.object.select_all(action='DESELECT')

    rd.select = True
    bpy.context.scene.objects.active = rd
    bpy.ops.object.configura_ramo_dir()
    bpy.ops.object.select_all(action='DESELECT')

    re.select = True
    bpy.context.scene.objects.active = re
    bpy.ops.object.configura_ramo_esq()
    bpy.ops.object.select_all(action='DESELECT')

    cm.select = True
    bpy.context.scene.objects.active = cm
    bpy.ops.object.configura_corpo_mand()
    bpy.ops.object.select_all(action='DESELECT')

    me.select = True
    bpy.context.scene.objects.active = me
    bpy.ops.object.configura_mento()
    bpy.ops.object.select_all(action='DESELECT')

class ConfOsteotomiaAuto(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.conf_osteo_auto"
    bl_label = "Configura osteotomias automaticamente"
    
    def execute(self, context):
       ConfOsteotomiaAutoDef(self, context)
       return {'FINISHED'} 
