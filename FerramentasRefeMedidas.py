import bpy

def MedidasVerDentesDef(self, context):

	context = bpy.context
	obj = context.active_object

	bpy.ops.mesh.add_linhabase(location=(0,0,0), rotation=(0, 1.5708, 0))
	bpy.context.object.show_x_ray = True
	bpy.context.object.lock_location[0] = True
	bpy.context.object.name = "LinhaMedida"


	bpy.ops.object.select_all(action='DESELECT')

	# CRIA CÓPIAS DOS EMPTIES

	bpy.data.objects['EMP11'].select = True
	bpy.data.objects['EMP21'].select = True
	bpy.data.objects['EMP13'].select = True
	bpy.data.objects['EMP23'].select = True
	bpy.data.objects['EMP16'].select = True
	bpy.data.objects['EMP26'].select = True

	bpy.ops.object.duplicate()

	# TRAVA OS EMPTIES NA LINHA DE REFERÊNCIA

	bpy.ops.object.select_all(action='DESELECT')
	objAct = bpy.data.objects['EMP11.001']
	objAct.select = True
	bpy.context.scene.objects.active = objAct
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["LinhaMedida"]
	bpy.context.object.constraints["Copy Location"].use_x = False
	bpy.context.object.constraints["Copy Location"].use_y = False


	bpy.ops.object.select_all(action='DESELECT')
	objAct = bpy.data.objects['EMP21.001']
	objAct.select = True
	bpy.context.scene.objects.active = objAct
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["LinhaMedida"]
	bpy.context.object.constraints["Copy Location"].use_x = False
	bpy.context.object.constraints["Copy Location"].use_y = False

	bpy.ops.object.select_all(action='DESELECT')
	objAct = bpy.data.objects['EMP13.001']
	objAct.select = True
	bpy.context.scene.objects.active = objAct
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["LinhaMedida"]
	bpy.context.object.constraints["Copy Location"].use_x = False
	bpy.context.object.constraints["Copy Location"].use_y = False

	bpy.ops.object.select_all(action='DESELECT')
	objAct = bpy.data.objects['EMP23.001']
	objAct.select = True
	bpy.context.scene.objects.active = objAct
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["LinhaMedida"]
	bpy.context.object.constraints["Copy Location"].use_x = False
	bpy.context.object.constraints["Copy Location"].use_y = False

	bpy.ops.object.select_all(action='DESELECT')
	objAct = bpy.data.objects['EMP16.001']
	objAct.select = True
	bpy.context.scene.objects.active = objAct
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["LinhaMedida"]
	bpy.context.object.constraints["Copy Location"].use_x = False
	bpy.context.object.constraints["Copy Location"].use_y = False

	bpy.ops.object.select_all(action='DESELECT')
	objAct = bpy.data.objects['EMP26.001']
	objAct.select = True
	bpy.context.scene.objects.active = objAct
	bpy.ops.object.constraint_add(type='COPY_LOCATION')
	bpy.context.object.constraints["Copy Location"].target = bpy.data.objects["LinhaMedida"]
	bpy.context.object.constraints["Copy Location"].use_x = False
	bpy.context.object.constraints["Copy Location"].use_y = False


	# CRIA MEDIDAS

	bpy.ops.measureit.runopenglbutton()

	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['EMP11']
	b = bpy.data.objects['EMP11.001']
	a.select = True
	b.select = True
	bpy.context.scene.objects.active = a
	bpy.ops.measureit.addlinkbutton()

	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['EMP21']
	b = bpy.data.objects['EMP21.001']
	a.select = True
	b.select = True
	bpy.context.scene.objects.active = a
	bpy.ops.measureit.addlinkbutton()

	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['EMP13']
	b = bpy.data.objects['EMP13.001']
	a.select = True
	b.select = True
	bpy.context.scene.objects.active = a
	bpy.ops.measureit.addlinkbutton()

	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['EMP23']
	b = bpy.data.objects['EMP23.001']
	a.select = True
	b.select = True
	bpy.context.scene.objects.active = a
	bpy.ops.measureit.addlinkbutton()

	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['EMP16']
	b = bpy.data.objects['EMP16.001']
	a.select = True
	b.select = True
	bpy.context.scene.objects.active = a
	bpy.ops.measureit.addlinkbutton()

	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['EMP26']
	b = bpy.data.objects['EMP26.001']
	a.select = True
	b.select = True
	bpy.context.scene.objects.active = a
	bpy.ops.measureit.addlinkbutton()

# SELECIONA LINHA MEDIDA


	bpy.ops.object.select_all(action='DESELECT')
	a = bpy.data.objects['LinhaMedida']
	a.select = True
	bpy.context.scene.objects.active = a
