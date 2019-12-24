import bpy
import math
import fnmatch

# MENSAGENS

class MessageSelecioneObj(bpy.types.Operator):
    bl_idname = "object.dialog_operator_selecione"
    bl_label = "Please, select an object before!"

    def execute(self, context):
        message = ("Please, select an object before!")
        self.report({'INFO'}, message)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

bpy.utils.register_class(MessageSelecioneObj)

class MessageColoqueValor(bpy.types.Operator):
    bl_idname = "object.dialog_operator_coloque_valor"
    bl_label = "Please, inform a value on Real Size!"

    def execute(self, context):
        message = ("Please, inform a value on Real Size!")
        self.report({'INFO'}, message)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

bpy.utils.register_class(MessageColoqueValor)

# COMANDOS

def CriaBaseOrigem():

    bpy.ops.object.empty_add(type='PLAIN_AXES', view_align=False, location=(-1, 0, 1))
    bpy.context.object.name = "EMP1a"

    bpy.ops.object.empty_add(type='PLAIN_AXES', view_align=False, location=(1, 0, 1))
    bpy.context.object.name = "EMP2a"

    bpy.ops.object.empty_add(type='PLAIN_AXES', view_align=False, location=(0, 0, -1))
    bpy.context.object.name = "EMP3a"

    bpy.ops.object.select_all(action='DESELECT')


def Redimensiona(self, context):

    global EMP1EMP2, medidareal2

    context = bpy.context
    FACE = context.active_object

    EMP1 = bpy.data.objects['EMP1b'] # Olho direito
    EMP2 = bpy.data.objects['EMP2b'] # Olho esquerdo
    EMP3 = bpy.data.objects['EMP3b'] # Ponto inferior
    bpy.ops.object.empty_add(type='SPHERE', location=((EMP1.location[0]+EMP2.location[0])/2, (EMP1.location[1]+EMP2.location[1])/2, (EMP1.location[2]+EMP2.location[2])/2))
    bpy.context.object.name = "PT_Origem"
    EMP4 = bpy.data.objects['PT_Origem']

    l = []
    EMP1EMP2 = [EMP1, EMP2]

    for item in EMP1EMP2:
       l.append(item.location)

    medidaAtual2 = math.sqrt( (l[0][0] - l[1][0])**2 + (l[0][1] - l[1][1])**2 + (l[0][2] - l[1][2])**2)
    print(medidaAtual2)

    medidaReal2 = float(bpy.context.scene.medida_real2)

# Redimensiona

    fatorEscala2 = medidaReal2 / medidaAtual2

    bpy.ops.object.select_all(action='DESELECT')
    EMP1.select_set(True)
    EMP2.select_set(True)
    EMP3.select_set(True)
    EMP4.select_set(True)
    FACE.select_set(True)
    bpy.context.view_layer.objects.active = EMP4
    bpy.ops.object.parent_set()

    EMP4.scale = ( fatorEscala2, fatorEscala2, fatorEscala2 )


#    bpy.ops.object.select_all(action='DESELECT')
#    FACE.select = True
#    bpy.context.scene.objects.active = FACE
#    FACE.scale = ( fatorEscala2, fatorEscala2, fatorEscala2 )

    print("Medida Atual:", medidaAtual2)
    print("Medida Real: ", medidaReal2)
    print("Fator de Escala: ", fatorEscala2)

    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    bpy.ops.object.select_all(action='DESELECT')
#    EMP1.select_set(True)
#    EMP2.select_set(True)
#    EMP3.select_set(True)
    EMP4.select_set(True)
    bpy.context.view_layer.objects.active = EMP1
    bpy.ops.object.delete(use_global=False)


    FACE.select_set(True)
    bpy.context.view_layer.objects.active = FACE

    bpy.ops.object.transform_apply() # É necessário colocar os ()

    bpy.ops.view3d.view_axis(type='FRONT')
#    bpy.ops.view3d.viewnumpad(type='FRONT')
    bpy.ops.view3d.view_selected()

    #bpy.ops.view3d.view_all(center=True)

    # Centraliza zoom
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for region in area.regions:
                if region.type == 'WINDOW':
                    override = {'area': area, 'region': region, 'edit_object': bpy.context.edit_object}
                    bpy.ops.view3d.view_all(override)


class AlinhaForcaBtn(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.alinha_forca"
    bl_label = "Cálculo de Alinhamento da Mandíbula"

    def execute(self, context):

        context = bpy.context
        obj = context.active_object
        scn = context.scene

        if bpy.context.scene.medida_real2 == "None":
            bpy.ops.object.dialog_operator_coloque_valor('INVOKE_DEFAULT')
        else:

            CriaBaseOrigem()
            print("OBJETOS CRIADOS!!!")
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
            Redimensiona(self, context)
            bpy.ops.object.alinha_tres_pontos()

            bpy.context.object.location[0] = 0
            bpy.context.object.location[1] = 0
            bpy.context.object.location[2] = 0

            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

            # Centraliza zoom
            for area in bpy.context.screen.areas:
                if area.type == 'VIEW_3D':
                    for region in area.regions:
                        if region.type == 'WINDOW':
                            override = {'area': area, 'region': region, 'edit_object': bpy.context.edit_object}
                            bpy.ops.view3d.view_all(override)


#            ApagaPontosAlinhaDef()
#            ApagaPontosOrigemDef()

#        bpy.ops.object.transform_apply

        return {'FINISHED'}

bpy.utils.register_class(AlinhaForcaBtn)

# Alinhamento por ICP
def ForceICPDef(self, context):

    # TESTA SE TEM MAIS DO QUE 200 K???
    context = bpy.context

    if len(context.selected_objects) == 2:

        ativo_antigo = context.view_layer.objects.active.name
#        print("Objeto ativo:", ativo_antigo)

        for i in bpy.context.selected_objects:

            if i.name != ativo_antigo:
                context.view_layer.objects.active = i
#                print("Deu certo?", i.name)

        bpy.ops.object.align_icp()
        bpy.ops.object.align_icp()
        bpy.ops.object.align_icp()
        bpy.ops.object.align_icp()
        bpy.ops.object.align_icp()
        bpy.ops.object.align_icp()
        bpy.ops.object.align_icp()
        bpy.ops.object.align_icp()

class ForceICP(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.force_icp"
    bl_label = "Force_ICP"


    @classmethod
    def poll(cls, context):
        condition_1 = len(context.selected_objects) == 2
        conidion_2 = context.object.type == 'MESH'
        return condition_1 and condition_1


    def execute(self, context):
        ForceICPDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(ForceICP)
