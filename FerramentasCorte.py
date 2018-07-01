import bpy

# ERROS

def ERROselCorteDef(self, context):
    self.layout.label("Select correctly the TWO objects!")

def ERROTermSelCorte():
     CRED = '\033[91m'
     CEND = '\033[0m'
     print(CRED + "Select correctly the TWO objects!" + CEND)


def ERROselTipoDef(self, context):
    self.layout.label("Select only MESH or CURVE objects!")

def ERROTermSelTipo():
     CRED = '\033[91m'
     CEND = '\033[0m'
     print(CRED + "Select only MESH or CURVE objects!" + CEND)

# CÍRCULO DE CORTE

def CriaCirculoCorteDef(self, context):
    context = bpy.context
    obj = context.active_object

    bpy.ops.mesh.primitive_circle_add(vertices=100, radius=200, view_align=False, enter_editmode=False, location=(0, 0, 0))

    bpy.context.object.rotation_euler[1] = 1.5708

    bpy.context.object.show_x_ray = True

# CORTA FACE

def CortaFaceDef(self, context):
    
    context = bpy.context
    obj = context.active_object

    sel=bpy.context.selected_objects

    
    if len(sel) != 2:
        ERROTermSelCorte()     
        bpy.context.window_manager.popup_menu(ERROselCorteDef, title="Attention!", icon='INFO')

    if len(sel) == 2:  
        obj0 = sel[0].data
        obj1 = sel[1].data 
        ObjDel = sel[0]    

        if type(obj0) != bpy.types.Mesh and type(obj0) != bpy.types.Curve:
            ERROTermSelTipo()     
            bpy.context.window_manager.popup_menu(ERROselTipoDef, title="Attention!", icon='INFO')

        if type(obj1) != bpy.types.Mesh and type(obj1) != bpy.types.Curve:
            ERROTermSelTipo()     
            bpy.context.window_manager.popup_menu(ERROselTipoDef, title="Attention!", icon='INFO')

        else:
            bpy.context.object.name = "FaceMalha"
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.knife_project(cut_through=True)
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            bpy.ops.mesh.separate(type='SELECTED')
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects['FaceMalha.001'].select = False
            bpy.data.objects['FaceMalha'].select = True
            bpy.ops.object.delete()
            ObjDel.select = True
#            bpy.data.objects['Circle'].select = True
            bpy.ops.object.delete()
        
 

# CÍRCULO DE CORTE DA ARCADA

def CriaCirculoCorteArcDef(self, context):
    context = bpy.context
    obj = context.active_object

    bpy.ops.mesh.primitive_circle_add(vertices=100, radius=45, view_align=False, enter_editmode=False, location=(0,-70,-70))

    bpy.context.object.rotation_euler[1] = 1.5708

    bpy.ops.transform.resize(value=(1, 1, 0.33))

    bpy.ops.transform.rotate(value=0.279253, axis=(1, 0, 0))


    bpy.context.object.name = "Círculo Corte Arcada"

    bpy.context.object.show_x_ray = True

# CORTA ARCADA - SOBRA DENTRO

def  CortaArcadaDef(self, context):
    
    context = bpy.context
    obj = context.active_object

    sel=bpy.context.selected_objects

    if len(sel) != 2:
        ERROTermSelCorte()     
        bpy.context.window_manager.popup_menu(ERROselCorteDef, title="Attention!", icon='INFO')

    if len(sel) == 2:  
        obj0 = sel[0].data
        obj1 = sel[1].data 
        ObjDel = sel[0]    

        if type(obj0) != bpy.types.Mesh and type(obj0) != bpy.types.Curve:
            ERROTermSelTipo()     
            bpy.context.window_manager.popup_menu(ERROselTipoDef, title="Attention!", icon='INFO')

        if type(obj1) != bpy.types.Mesh and type(obj1) != bpy.types.Curve:
            ERROTermSelTipo()     
            bpy.context.window_manager.popup_menu(ERROselTipoDef, title="Attention!", icon='INFO')

        
        else:
            bpy.context.object.name = "ArcadaCut"
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.knife_project(cut_through=True)
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            bpy.ops.mesh.separate(type='SELECTED')
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects['ArcadaCut.001'].select = False
            bpy.data.objects['ArcadaCut'].select = True
            bpy.ops.object.delete()
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects['ArcadaCut.001'].select = True
            bpy.context.scene.objects.active = bpy.data.objects['ArcadaCut.001']
            bpy.context.object.name = "ArcadaPronta"

# CORTA OSSOS - SOBRA FORA

def  CortaOssosDef(self, context):
    
    context = bpy.context
    obj = context.active_object

    sel=bpy.context.selected_objects

    if len(sel) != 2:
        ERROTermSelCorte()     
        bpy.context.window_manager.popup_menu(ERROselCorteDef, title="Attention!", icon='INFO')

    if len(sel) == 2:  
        obj0 = sel[0].data
        obj1 = sel[1].data 
        ObjDel = sel[0]    

        if type(obj0) != bpy.types.Mesh and type(obj0) != bpy.types.Curve:
            ERROTermSelTipo()     
            bpy.context.window_manager.popup_menu(ERROselTipoDef, title="Attention!", icon='INFO')

        if type(obj1) != bpy.types.Mesh and type(obj1) != bpy.types.Curve:
            ERROTermSelTipo()     
            bpy.context.window_manager.popup_menu(ERROselTipoDef, title="Attention!", icon='INFO')

        
        else:
            bpy.context.object.name = "OssoCut"
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.knife_project(cut_through=True)
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            bpy.ops.mesh.select_all(action='INVERT')
            bpy.ops.mesh.separate(type='SELECTED')
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects['OssoCut.001'].select = False
            bpy.data.objects['OssoCut'].select = True
            bpy.ops.object.delete()
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects['OssoCut.001'].select = True
            bpy.context.scene.objects.active = bpy.data.objects['OssoCut.001']
            bpy.context.object.name = "OssoPronto"

# FECHA BURACOS

def FechaBuracosDef(self, context):
    
    context = bpy.context
    obj = context.active_object

    bpy.ops.object.modifier_add(type='REMESH') 
#    bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
    bpy.context.object.modifiers["Remesh"].use_remove_disconnected = False
    bpy.context.object.modifiers["Remesh"].scale = 0.99
    bpy.context.object.modifiers["Remesh"].octree_depth = 9

    bpy.ops.object.modifier_add(type='DECIMATE')
    bpy.context.object.modifiers["Decimate"].ratio = 0.1
