import bpy

def ColisaoArcosDef():

    context = bpy.context
    scn = context.scene

    if len(bpy.context.selected_objects) != 2:
	    print("Selecione dois objetos!")
	    # Substituir por mensagem de erro!
    else:
        print("Tudo certo")

        ObjOriginais = bpy.context.selected_objects

        for i in bpy.context.selected_objects:
            bpy.ops.object.select_all(action='DESELECT')
            i.select_set(True)
            bpy.context.view_layer.objects.active = i
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')



        for i in ObjOriginais:
            i.select_set(True)


        if bpy.context.selected_objects[0].location[2] == bpy.context.selected_objects[1].location[2]:
            print("Os objetos estão na mesma altura!")

        if bpy.context.selected_objects[0].location[2] > bpy.context.selected_objects[1].location[2]:

            ArcadaSup = bpy.context.selected_objects[0]
            ArcadaInf = bpy.context.selected_objects[1]
            print("Obj[0] mais alto")

        if bpy.context.selected_objects[0].location[2] < bpy.context.selected_objects[1].location[2]:

            ArcadaSup = bpy.context.selected_objects[1]
            ArcadaInf = bpy.context.selected_objects[0]
            print("Obj[1] mais alto")

        # Seleciona arcada inferior e cria vertex group

        bpy.ops.object.select_all(action='DESELECT')
        ArcadaInf.select_set(True)
        bpy.context.view_layer.objects.active = ArcadaInf



        try:
            bpy.ops.object.modifier_remove(modifier="ArchSupTouch")
            bpy.ops.object.vertex_group_remove(all=False, all_unlocked=False)
            bpy.ops.rigidbody.object_remove()
            ArcadaSup.animation_data_clear()
            print("APAGADOS o grupo e o modificador.")
        except:
            print("Não foi criado grupo.")

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action='SELECT')
        vg = ArcadaInf.vertex_groups.new(name="ArchInf")
        scn.tool_settings.vertex_group_weight=1
        bpy.ops.object.vertex_group_assign()
        bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.enabled = False
        bpy.context.object.rigid_body.collision_shape = 'MESH'
        bpy.context.object.rigid_body.collision_margin = 0

        #Arco Superior

        bpy.ops.object.select_all(action='DESELECT')
        ArcadaSup.select_set(True)
        bpy.context.view_layer.objects.active = ArcadaSup

        try:
            bpy.ops.object.modifier_remove(modifier="ArchSupTouch")
            bpy.ops.object.vertex_group_remove(all=False, all_unlocked=False)
            bpy.ops.rigidbody.object_remove()
            ArcadaSup.animation_data_clear()
            print("APAGADOS o grupo e o modificador.")
        except:
            print("Não foi criado grupo e modificador.")

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action='SELECT')
        vg = ArcadaSup.vertex_groups.new(name="ArchSup")
        scn.tool_settings.vertex_group_weight=0
        bpy.ops.object.vertex_group_assign()
        bpy.ops.object.mode_set(mode='OBJECT')

        # Vertex proximity
        bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
        bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "ArchSup"
        bpy.context.object.modifiers["VertexWeightProximity"].target = ArcadaInf
        bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
        bpy.context.object.modifiers["VertexWeightProximity"].min_dist =0
        bpy.context.object.modifiers["VertexWeightProximity"].max_dist = .5 #3
        bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'LINEAR'
        bpy.context.object.modifiers["VertexWeightProximity"].name = "ArchSupTouch"
        bpy.context.object.modifiers["ArchSupTouch"].show_expanded = False

        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.collision_shape = 'MESH'
        bpy.context.object.rigid_body.collision_margin = 0

#        override = {'scene': bpy.context.scene,
#                'point_cache': bpy.context.scene.rigidbody_world.point_cache}
#        bpy.ops.ptcache.bake(override, bake=True)
#        bpy.context.scene.update()
#        bpy.ops.rigidbody.bake_to_keyframes(frame_start=1, frame_end=110)

#        bpy.ops.object.mode_set(mode='WEIGHT_PAINT')

        bpy.ops.screen.animation_play()

class ColisaoArcos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.colisao_arcos"
    bl_label = "Archs Collision"

    @classmethod
    def poll(cls, context):

        found = 'Tooth 8' in bpy.data.objects

        if len(bpy.context.selected_objects) == 2:
            return True
        else:
            if len(bpy.context.selected_objects) != 2:
                return False
    
    def execute(self, context):
        ColisaoArcosDef()
        return {'FINISHED'}

bpy.utils.register_class(ColisaoArcos)
