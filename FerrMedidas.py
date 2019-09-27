import bpy
import math
from math import sqrt


def CalculaAngulo(Obj1, Obj2, Obj3):

        # Calcula

        d1_2 = DistanciaObjetos(Obj1, Obj2)
        d2_3 = DistanciaObjetos(Obj2, Obj3)
        d1_3 = DistanciaObjetos(Obj1, Obj3)


        Grau = (d2_3**2 + d1_2**2 - d1_3**2) / (2 * d2_3 * d1_2)

        Angulo = float(round(math.degrees(math.acos(Grau)),2))

        print("Grau (rad):", Grau)

        print("Ângulo:", Angulo)

        return str(Angulo)+"º"


def DistanciaObjetos(obj1, obj2):

    objA = bpy.data.objects[obj1].location
    objB = bpy.data.objects[obj2].location

    distancia = sqrt( (objB[0] - objA[0])**2 + (objB[1] - objA[1])**2 + (objB[2] - objA[2])**2 )

    print("Distancia", obj1 , "<-->", obj2 , "=" , distancia )

    return distancia



def MedidasVerDentesDef(self, context):

	context = bpy.context
	obj = context.active_object

	bpy.context.scene.measureit_default_color = (1, 1, 1, 1)
	bpy.context.scene.measureit_font_size = 16

	bpy.ops.mesh.add_linhabase(location=(0,0,0), rotation=(0, 1.5708, 0))
#	bpy.context.object.show_x_ray = True
	bpy.context.object.lock_location[0] = True
	bpy.context.object.lock_location[1] = True
	bpy.context.object.name = "LinhaMedida"


	bpy.ops.object.select_all(action='DESELECT')

	# CRIA CÓPIAS DOS EMPTIES

	bpy.data.objects['Tooth 8'].select_set(True)
	bpy.data.objects['Tooth 9'].select_set(True)
	bpy.data.objects['Tooth 6'].select_set(True)
	bpy.data.objects['Tooth 11'].select_set(True)
	bpy.data.objects['Tooth 3'].select_set(True)
	bpy.data.objects['Tooth 14'].select_set(True)

	bpy.ops.object.duplicate()

	# TRAVA OS EMPTIES NA LINHA DE REFERÊNCIA

	bpy.ops.object.select_all(action='DESELECT')
	objAct = bpy.data.objects['Tooth 8.001']
	objAct.select_set(True)
	context.view_layer.objects.active = objAct
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["LinhaMedida"]
	bpy.context.object.constraints["Copy Location"].use_x = False
	bpy.context.object.constraints["Copy Location"].use_y = False

	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location.001"].target = bpy.data.objects["Tooth 8"]
	bpy.context.object.constraints["Copy Location.001"].use_z = False


	bpy.ops.object.select_all(action='DESELECT')
	objAct = bpy.data.objects['Tooth 9.001']
	objAct.select_set(True)
	context.view_layer.objects.active = objAct
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["LinhaMedida"]
	bpy.context.object.constraints["Copy Location"].use_x = False
	bpy.context.object.constraints["Copy Location"].use_y = False

	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location.001"].target = bpy.data.objects["Tooth 9"]
	bpy.context.object.constraints["Copy Location.001"].use_z = False

	bpy.ops.object.select_all(action='DESELECT')
	objAct = bpy.data.objects['Tooth 6.001']
	objAct.select_set(True)
	context.view_layer.objects.active = objAct
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["LinhaMedida"]
	bpy.context.object.constraints["Copy Location"].use_x = False
	bpy.context.object.constraints["Copy Location"].use_y = False

	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location.001"].target = bpy.data.objects["Tooth 6"]
	bpy.context.object.constraints["Copy Location.001"].use_z = False

	bpy.ops.object.select_all(action='DESELECT')
	objAct = bpy.data.objects['Tooth 11.001']
	objAct.select_set(True)
	context.view_layer.objects.active = objAct
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["LinhaMedida"]
	bpy.context.object.constraints["Copy Location"].use_x = False
	bpy.context.object.constraints["Copy Location"].use_y = False

	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location.001"].target = bpy.data.objects["Tooth 11"]
	bpy.context.object.constraints["Copy Location.001"].use_z = False

	bpy.ops.object.select_all(action='DESELECT')
	objAct = bpy.data.objects['Tooth 3.001']
	objAct.select_set(True)
	context.view_layer.objects.active = objAct
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["LinhaMedida"]
	bpy.context.object.constraints["Copy Location"].use_x = False
	bpy.context.object.constraints["Copy Location"].use_y = False

	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location.001"].target = bpy.data.objects["Tooth 3"]
	bpy.context.object.constraints["Copy Location.001"].use_z = False

	bpy.ops.object.select_all(action='DESELECT')
	objAct = bpy.data.objects['Tooth 14.001']
	objAct.select_set(True)
	context.view_layer.objects.active = objAct
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["LinhaMedida"]
	bpy.context.object.constraints["Copy Location"].use_x = False
	bpy.context.object.constraints["Copy Location"].use_y = False

	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location.001"].target = bpy.data.objects["Tooth 14"]
	bpy.context.object.constraints["Copy Location.001"].use_z = False


	# CRIA MEDIDAS

	bpy.ops.measureit.runopengl()

	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['Tooth 8']
	b = bpy.data.objects['Tooth 8.001']
	a.select_set(True)
	b.select_set(True)
	context.view_layer.objects.active = a
	bpy.ops.measureit.addlink()

	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['Tooth 9']
	b = bpy.data.objects['Tooth 9.001']
	a.select_set(True)
	b.select_set(True)
	context.view_layer.objects.active = a
	bpy.ops.measureit.addlink()

	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['Tooth 6']
	b = bpy.data.objects['Tooth 6.001']
	a.select_set(True)
	b.select_set(True)
	context.view_layer.objects.active = a
	bpy.ops.measureit.addlink()

	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['Tooth 11']
	b = bpy.data.objects['Tooth 11.001']
	a.select_set(True)
	b.select_set(True)
	context.view_layer.objects.active = a
	bpy.ops.measureit.addlink()

	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['Tooth 3']
	b = bpy.data.objects['Tooth 3.001']
	a.select_set(True)
	b.select_set(True)
	context.view_layer.objects.active = a
	bpy.ops.measureit.addlink()

	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['Tooth 14']
	b = bpy.data.objects['Tooth 14.001']
	a.select_set(True)
	b.select_set(True)
	context.view_layer.objects.active = a
	bpy.ops.measureit.addlink()

# SELECIONA LINHA MEDIDA


	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['LinhaMedida']
	a.select_set(True)
	context.view_layer.objects.active = a

def CriaMedidaHor(Obj1, Obj2):

	bpy.context.scene.measureit_default_color = (1, 1, 0, 1)
	bpy.context.scene.measureit_font_size = 16

	bpy.ops.object.empty_add(type='PLAIN_AXES')
#	bpy.context.space_data.context = 'CONSTRAINT'
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["LinhaMedidaHor"]
	bpy.context.object.constraints["Copy Location"].use_y = False
	bpy.context.object.constraints["Copy Location"].use_z = False
	bpy.context.object.constraints["Copy Location"].use_z = True
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location.001"].target = bpy.data.objects[Obj1]
	bpy.context.object.constraints["Copy Location.001"].use_x = False
	bpy.context.object.constraints["Copy Location.001"].use_z = False
	bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
	bpy.context.object.name = Obj2

	bpy.ops.object.select_all(action='DESELECT')

	bpy.data.objects[Obj1].select_set(True)
	bpy.data.objects[Obj2].select_set(True)
#	context.view_layer.objects.active = bpy.data.objects['Tooth 9.001']

	bpy.ops.measureit.addlink()

	bpy.ops.object.select_all(action='DESELECT')


def MedidasHorDentesDef(self, context):

	context = bpy.context
	obj = context.active_object

	bpy.ops.mesh.add_linhabase(location=(0,0,0), rotation=( 1.5708, 0 , 0))


#	bpy.context.object.show_x_ray = True
	bpy.context.object.lock_location[0] = True
	bpy.context.object.lock_location[1] = True
	bpy.context.object.name = "LinhaMedidaHor"

	bpy.ops.object.select_all(action='DESELECT')

	bpy.data.objects['LinhaMedida'].select_set(True)
	bpy.data.objects['LinhaMedidaHor'].select_set(True)
	context.view_layer.objects.active = bpy.data.objects['LinhaMedida']
	bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)



	bpy.ops.object.select_all(action='DESELECT')


	CriaMedidaHor("Tooth 9.001", "EMPHor_9")
	CriaMedidaHor("Tooth 8.001", "EMPHor_8")
	CriaMedidaHor("Tooth 6.001", "EMPHor_6")
	CriaMedidaHor("Tooth 11.001", "EMPHor_11")
	CriaMedidaHor("Tooth 3.001", "EMPHor_3")
	CriaMedidaHor("Tooth 14.001", "EMPHor_14")



class MedidasVerHorDentes(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.medverhor_dentes"
    bl_label = "Medidas Verticais"

    def execute(self, context):

        MedidasVerDentesDef(self, context)
        MedidasHorDentesDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(MedidasVerHorDentes)


def ApagaPontosCopiadosDef():

    ListaPontos = ["Tooth 9.001","Tooth 8.001","Tooth 6.001","Tooth 11.001","Tooth 3.001","Tooth 14.001"]

    for ob in ListaPontos:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[ob].select_set(True)
        bpy.ops.object.delete(use_global=False)

class ApagaPontosCopiados(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.apaga_pontos_objetos"
    bl_label = "Apaga Pontos Copiados"

    def execute(self, context):

        ApagaPontosCopiadosDef()
        return {'FINISHED'}

bpy.utils.register_class(ApagaPontosCopiados)
