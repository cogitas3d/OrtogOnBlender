import bpy
import fnmatch

def ColisaoArcosDef():

    context = bpy.context
    scn = context.scene

    bpy.context.scene.frame_end = 110

    if len(bpy.context.selected_objects) != 2:
	    print("Selecione dois objetos!")
	    # Substituir por mensagem de erro!
    else:
        print("Tudo certo")

        # Inverte gravidade.
        bpy.context.scene.gravity[2] = -9.81


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

        if bpy.context.selected_objects[0].location[2] > bpy.context.selected_objects[1].location[2]: # if bpy.context.selected_objects[0].location[2] > bpy.context.selected_objects[1].location[2]:

            ArcadaSup = bpy.context.selected_objects[0]
            ArcadaInf = bpy.context.selected_objects[1]
            print("Obj[0] mais alnto")

        if bpy.context.selected_objects[0].location[2] < bpy.context.selected_objects[1].location[2]:  # if bpy.context.selected_objects[0].location[2] < bpy.context.selected_objects[1].location[2]:

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
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        if len(bpy.context.selected_objects) == 2:
            return True
        else:
            if len(bpy.context.selected_objects) != 2:
                return False

    def execute(self, context):
        ColisaoArcosDef()
        return {'FINISHED'}

bpy.utils.register_class(ColisaoArcos)

# GARAVIDADE INVERSA

def ColisaoArcosInversoDef():

    context = bpy.context
    scn = context.scene

    bpy.context.scene.frame_end = 110

    if len(bpy.context.selected_objects) != 2:
	    print("Selecione dois objetos!")
	    # Substituir por mensagem de erro!
    else:
        print("Tudo certo")

        # Inverte gravidade.
        bpy.context.scene.gravity[2] = 9.81

        ObjOriginais = bpy.context.selected_objects


        for i in ObjOriginais:
            bpy.ops.object.select_all(action='DESELECT')
            i.select_set(True)
            bpy.context.view_layer.objects.active = i
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')



        for i in ObjOriginais:
            i.select_set(True)


        if ObjOriginais[0].location[2] == ObjOriginais[1].location[2]:
            print("Os objetos estão na mesma altura!")

        if ObjOriginais[0].location[2] > ObjOriginais[1].location[2]: # if bpy.context.selected_objects[0].location[2] > bpy.context.selected_objects[1].location[2]:

            ArcadaSup = ObjOriginais[0]
            ArcadaInf = ObjOriginais[1]
            print("Obj[1] mais baixo")
            print("LocSUP",ArcadaSup.name,ArcadaSup.location[2])
            print("LocINF",ArcadaInf.name,ArcadaInf.location[2])


        if ObjOriginais[0].location[2] < ObjOriginais[1].location[2]:  # if bpy.context.selected_objects[0].location[2] < bpy.context.selected_objects[1].location[2]:

            ArcadaSup = ObjOriginais[1]
            ArcadaInf = ObjOriginais[0]
            print("Obj[0] mais baixo")
            print("LocSUP",ArcadaSup.name,ArcadaSup.location[2])
            print("LocINF",ArcadaInf.name,ArcadaInf.location[2])
            print(ArcadaInf.name)

        #Arco Superior

        bpy.ops.object.select_all(action='DESELECT')
        ArcadaSup.select_set(True)
        bpy.context.view_layer.objects.active = ArcadaSup

        try:
            bpy.ops.object.modifier_remove(modifier="ArchInfTouch")
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
        scn.tool_settings.vertex_group_weight=1
        bpy.ops.object.vertex_group_assign()
        bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.enabled = False
        bpy.context.object.rigid_body.collision_shape = 'MESH'
        bpy.context.object.rigid_body.collision_margin = 0

        # Arcada inferior

        bpy.ops.object.select_all(action='DESELECT')
        ArcadaInf.select_set(True)
        bpy.context.view_layer.objects.active = ArcadaInf

        try:
            bpy.ops.object.modifier_remove(modifier="ArchInfTouch")
            bpy.ops.object.vertex_group_remove(all=False, all_unlocked=False)
            bpy.ops.rigidbody.object_remove()
            ArcadaInf.animation_data_clear()
            print("APAGADOS o grupo e o modificador.")
        except:
            print("Não foi criado grupo.")

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action='SELECT')
        vg = ArcadaInf.vertex_groups.new(name="ArchInf")
        scn.tool_settings.vertex_group_weight=0
        bpy.ops.object.vertex_group_assign()
        bpy.ops.object.mode_set(mode='OBJECT')

        # Vertex proximity
        bpy.ops.object.modifier_add(type='VERTEX_WEIGHT_PROXIMITY')
        bpy.context.object.modifiers["VertexWeightProximity"].vertex_group = "ArchInf"
        bpy.context.object.modifiers["VertexWeightProximity"].target = ArcadaSup
        bpy.context.object.modifiers["VertexWeightProximity"].proximity_mode = 'GEOMETRY'
        bpy.context.object.modifiers["VertexWeightProximity"].min_dist =0
        bpy.context.object.modifiers["VertexWeightProximity"].max_dist = .5 #3
        bpy.context.object.modifiers["VertexWeightProximity"].falloff_type = 'LINEAR'
        bpy.context.object.modifiers["VertexWeightProximity"].name = "ArchInfTouch"
        bpy.context.object.modifiers["ArchInfTouch"].show_expanded = False

        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.collision_shape = 'MESH'
        bpy.context.object.rigid_body.collision_margin = 0

        bpy.ops.screen.animation_play()

class ColisaoArcosInverso(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.colisao_arcos_inverso"
    bl_label = "Inverted Archs Collision"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        if len(bpy.context.selected_objects) == 2:
            return True
        else:
            if len(bpy.context.selected_objects) != 2:
                return False

    def execute(self, context):
        ColisaoArcosInversoDef()
        return {'FINISHED'}

bpy.utils.register_class(ColisaoArcosInverso)

def AplicaAnimCorDef():

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.screen.animation_cancel()


    override = {'scene': bpy.context.scene,
	            'point_cache': bpy.context.scene.rigidbody_world.point_cache}
    bpy.ops.ptcache.bake(override, bake=True)
    bpy.context.scene.update()
    bpy.ops.rigidbody.bake_to_keyframes(frame_start=1, frame_end=110)

    bpy.context.scene.frame_current = 110

    bpy.ops.object.mode_set(mode='WEIGHT_PAINT')

    bpy.ops.screen.animation_play()

class AplicaAnimCor(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.aplica_anima_cor"
    bl_label = "Apply Color and Animation"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        if len(bpy.context.selected_objects) == 1:
            return True
        else:
            if len(bpy.context.selected_objects) != 1:
                return False

    def execute(self, context):
        AplicaAnimCorDef()
        return {'FINISHED'}

bpy.utils.register_class(AplicaAnimCor)

def TravaArcoDef():

    context = bpy.context
    obj = context.active_object
    scn = context.scene

#    bpy.ops.screen.animation_cancel()
    bpy.ops.object.mode_set(mode='OBJECT')
#    bpy.context.scene.frame_current = 110
    obj.animation_data_clear()

    '''
    try:
        bpy.ops.object.vertex_group_remove(all=False, all_unlocked=False)
        bpy.ops.rigidbody.object_remove()
        ArcadaSup.animation_data_clear()
        print("APAGADOS o grupo e o modificador.")
    except:
        print("Não foi criado grupo e modificador.")
    '''


class TravaArco(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.trava_arco"
    bl_label = "Arch Stop"
    bl_options = {'REGISTER', 'UNDO'}


    # Programação diferente para funcionar!!!

    @classmethod
    def poll(cls, context):

        scene = context.scene
        tool_settings = context.tool_settings
        screen = context.screen

        if not screen.is_animation_playing:
            return True
        if screen.is_animation_playing:
            return False

    def execute(self, context):
        bpy.ops.screen.animation_cancel()
        TravaArcoDef()
        return {'FINISHED'}

bpy.utils.register_class(TravaArco)


def PreparaMaxilaMandibulaDef():

    context = bpy.context
    #obj = context.active_object
    scn = context.scene

    Maxila = bpy.data.objects['ma']
    Mandibula = bpy.data.objects['cm']

    bpy.ops.object.select_all(action='DESELECT')
    Maxila.select_set(True)
    Mandibula.select_set(True)
    bpy.context.view_layer.objects.active = Maxila

    bpy.ops.object.duplicate()

    Maxila.hide_viewport=True
    Mandibula.hide_viewport=True

#    Apagar_Ziga = [obj for obj in bpy.context.scene.objects if fnmatch.fnmatchcase(obj.name, "*Ziga")]
        #for Ziga in Apagar_Ziga:


    for objeto in context.selected_objects:
        if fnmatch.fnmatchcase(objeto.name, "ma*"):
            objeto.name = "MaxillaCopyZiga"
            MaxilaCopia = objeto
            objeto.animation_data_clear()
            print("Maxila OK", objeto)

        if fnmatch.fnmatchcase(objeto.name, "cm*"):
            objeto.name = "MandibleCopyZiga"
            MandibulaCopia = objeto
            objeto.animation_data_clear()
            print("Mandibula OK", objeto)

    #Apagar_Bracket_ref = [obj for obj in bpy.context.scene.objects if fnmatch.fnmatchcase(obj.name, "Bracket_re*")]

class PreparaMaxilaMandibula(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.prepara_maxila_mandibula"
    bl_label = "Prepares Maxilla & Mandible"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        if bpy.data.objects['MaxillaCopyZiga'] and bpy.data.objects['MandibleCopyZiga']:
            return False
        else:
            return True

    def execute(self, context):
        PreparaMaxilaMandibulaDef()
        return {'FINISHED'}

bpy.utils.register_class(PreparaMaxilaMandibula)


def FinalizaColisaoMaxMandDef():

    context = bpy.context
    scn = context.scene

    bpy.context.scene.frame_end = 100
    bpy.context.scene.frame_current = 100

#    bpy.ops.screen.animation_cancel(restore_frame=True)

#    bpy.ops.screen.animation_cancel()

    bpy.ops.object.trava_arco()


    bpy.data.objects['ma'].hide_viewport=False
    bpy.data.objects['cm'].hide_viewport=False
    bpy.data.objects['cm'].location = bpy.data.objects['MandibleCopyZiga'].location
    bpy.data.objects['cm'].rotation_euler = bpy.data.objects['MandibleCopyZiga'].rotation_euler

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['cm'].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects['cm']
    bpy.ops.anim.ortog_loc_rot()

#    bpy.context.scene.frame_end = 100
#    FrameEnd = bpy.data.scenes["Scene"].frame_end
#    bpy.context.scene.frame_set(FrameEnd)
#    bpy.context.scene.frame_current = 100

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['MaxillaCopyZiga'].select_set(True)
    bpy.data.objects['MandibleCopyZiga'].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects['MandibleCopyZiga']
    bpy.ops.object.delete(use_global=False)

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['cm'].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects['cm']


class FinalizaColisaoMaxMand(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.finaliza_colisao_max_mand"
    bl_label = "Apply Maxilla & Mandible Collision"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        FinalizaColisaoMaxMandDef()
        return {'FINISHED'}

bpy.utils.register_class(FinalizaColisaoMaxMand)
