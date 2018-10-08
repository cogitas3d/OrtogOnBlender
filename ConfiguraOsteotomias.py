import bpy
import bmesh

# CONFIGURA MENTO
def ConfiguraMentoDef(self, context):

    context = bpy.context
    obj = context.active_object
 #   scn = context.scene


    try: 
        ob=bpy.data.objects["Armature_Head"]

        try: 
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
            bpy.context.object.active_material.diffuse_color = (0.8, 0.35, 0.2) #change color
            bpy.context.object.name = "me"

            armatureHead = bpy.data.objects['Armature_Head']
            bpy.ops.object.select_all(action='DESELECT')
            armatureHead.hide=False
            armatureHead.select=True
            bpy.context.scene.objects.active = armatureHead
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
            armatureHead.hide=True

            a = bpy.data.objects['cm']
            b = bpy.data.objects['me']

            bpy.ops.object.select_all(action='DESELECT')
            a.select = True
            b.select = True 
            bpy.context.scene.objects.active = a
            bpy.ops.object.parent_set()
        
        except KeyError:
            bpy.context.window_manager.popup_menu(ERROcmDef, title="Atenção!", icon='INFO')

 #   bpy.context.active_object.data.bones.active = pbone.bone


    except KeyError:
        bpy.context.window_manager.popup_menu(ERROarmatureDef, title="Atenção!", icon='INFO')

    except TypeError:
        bpy.context.window_manager.popup_menu(ERROtipoDef, title="Atenção!", icon='INFO')

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDef, title="Atenção!", icon='INFO')

# CONFIGURA RAMO DA MANDÍBULA
def ConfiguraCorpoMandDef(self, context):
    
    context = bpy.context
    obj = context.active_object
 #   scn = context.scene

    try: 
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
        bpy.context.object.active_material.diffuse_color = (0.35, 0.8, 0.4) #change color
        bpy.context.object.name = "cm"

        armatureHead = bpy.data.objects['Armature_Head']
        bpy.ops.object.select_all(action='DESELECT')
        armatureHead.hide=False
        armatureHead.select=True
        bpy.context.scene.objects.active = armatureHead
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
        armatureHead.hide=True

    except KeyError:
        bpy.context.window_manager.popup_menu(ERROarmatureDef, title="Atenção!", icon='INFO')

    except TypeError:
        bpy.context.window_manager.popup_menu(ERROtipoDef, title="Atenção!", icon='INFO')

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDef, title="Atenção!", icon='INFO') 

# CONFIGURA RAMO DIREITO
def ConfiguraRamoDirDef(self, context):
    
    context = bpy.context
    obj = context.active_object
 #   scn = context.scene

    try: 
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
        bpy.context.object.active_material.diffuse_color = (0.4, 0.3, 0.8) #change color
        bpy.context.object.name = "rd"

        armatureHead = bpy.data.objects['Armature_Head']
        bpy.ops.object.select_all(action='DESELECT')
        armatureHead.hide=False
        armatureHead.select=True
        bpy.context.scene.objects.active = armatureHead
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
        armatureHead.hide=True


    except KeyError:
        bpy.context.window_manager.popup_menu(ERROarmatureDef, title="Atenção!", icon='INFO')

    except TypeError:
        bpy.context.window_manager.popup_menu(ERROtipoDef, title="Atenção!", icon='INFO')

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDef, title="Atenção!", icon='INFO')  


# CONFIGURA RAMO ESQUERDO
def ConfiguraRamoEsqDef(self, context):

    context = bpy.context
    obj = context.active_object
 #   scn = context.scene

    try: 
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
        bpy.context.object.active_material.diffuse_color = (0.4, 0.3, 0.8) #change color
        bpy.context.object.name = "re"

        armatureHead = bpy.data.objects['Armature_Head']
        bpy.ops.object.select_all(action='DESELECT')
        armatureHead.hide=False
        armatureHead.select=True
        bpy.context.scene.objects.active = armatureHead
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
        armatureHead.hide=True

    except KeyError:
        bpy.context.window_manager.popup_menu(ERROarmatureDef, title="Atenção!", icon='INFO')

    except TypeError:
        bpy.context.window_manager.popup_menu(ERROtipoDef, title="Atenção!", icon='INFO')

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDef, title="Atenção!", icon='INFO') 

# CONFIGURA MAXILA
def ConfiguraMaxilaDef(self, context):

    context = bpy.context
    obj = context.active_object
 #   scn = context.scene

    try: 
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
        bpy.context.object.active_material.diffuse_color = (0.8, 0.3, 0.2) #change color
        bpy.context.object.name = "ma"

        armatureHead = bpy.data.objects['Armature_Head']
        bpy.ops.object.select_all(action='DESELECT')
        armatureHead.hide=False
        armatureHead.select=True
        bpy.context.scene.objects.active = armatureHead
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
        armatureHead.hide=True
        
    except KeyError:
        bpy.context.window_manager.popup_menu(ERROarmatureDef, title="Atenção!", icon='INFO')

    except TypeError:
        bpy.context.window_manager.popup_menu(ERROtipoDef, title="Atenção!", icon='INFO')

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDef, title="Atenção!", icon='INFO')  

# CONFIGURA CABEÇA
def ConfiguraCabecaDef(self, context):

    context = bpy.context
    obj = context.active_object
 #   scn = context.scene


    try: 
        ob=bpy.data.objects["Armature_Head"]
        
        bpy.ops.object.mode_set(mode='EDIT')
        mesh=bmesh.from_edit_mesh(bpy.context.object.data)
        for v in mesh.verts:
            v.select = True

        vg = obj.vertex_groups.new(name="ca")
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.vertex_group_assign()
        bpy.ops.object.mode_set(mode='OBJECT')
        
        activeObject = bpy.context.active_object #Set active object to variable
        mat = bpy.data.materials.new(name="MaterialCabeca") #set new material to variable
        activeObject.data.materials.append(mat) #add the material to the object
        bpy.context.object.active_material.diffuse_color = (0.8, 0.75, 0.2) #change color
        bpy.context.object.name = "ca"

        armatureHead = bpy.data.objects['Armature_Head']
        bpy.ops.object.select_all(action='DESELECT')
        armatureHead.hide=False
        armatureHead.select=True
        bpy.context.scene.objects.active = armatureHead
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
        armatureHead.hide=True        
        
    except KeyError:
        bpy.context.window_manager.popup_menu(ERROarmatureDef, title="Atenção!", icon='INFO')

    except TypeError:
        bpy.context.window_manager.popup_menu(ERROtipoDef, title="Atenção!", icon='INFO')

    except RuntimeError:
        bpy.context.window_manager.popup_menu(ERROruntimeDef, title="Atenção!", icon='INFO')
