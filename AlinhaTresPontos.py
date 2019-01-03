import bpy
import math
import fnmatch


def ConfiguraNomes(self, context):

    global EMP1, EMP2, EMP3, FACE

#    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    FACE = bpy.context.scene.objects.active

    EMP1 = bpy.data.objects['PT_Alinha.001'] # Olho direito
    EMP2 = bpy.data.objects['PT_Alinha.002'] # Olho esquerdo
    EMP3 = bpy.data.objects['PT_Alinha'] # Ponto inferior
    
def CriaPTOrigem(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='SPHERE', location=((EMP1.location[0]+EMP2.location[0])/2, (EMP1.location[1]+EMP2.location[1])/2, (EMP1.location[2]+EMP2.location[2])/2))
    
    global EMP4 #, FACE

    
    bpy.context.object.name = "PT_Origem"
    bpy.context.object.empty_draw_size = .3

    EMP4 = bpy.data.objects['PT_Origem']
#    FACE = bpy.data.objects['Cube']
#    FACE = obj
    
    # Torna os outros empties filhos do PTOrigem
    bpy.ops.object.select_all(action='DESELECT')
    EMP1.select = True
    EMP2.select = True
    EMP3.select = True
    EMP4.select = True
    FACE.select = True     
    bpy.context.scene.objects.active = EMP4
    bpy.ops.object.parent_set()
#    bpy.ops.object.select_all(action='DESELECT')
#    EMP4.select = True
#    bpy.context.scene.objects.active = EMP4

    # Posiciona na origem
    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0
    
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')


def AlinhaFrente(self, context):

    global CB, A, AB, Cosc
    
    CB = math.sqrt( (EMP4.location[0] - EMP1.location[0])**2 + (EMP4.location[2] - EMP1.location[2])**2 )


    # Vista frontal
    # Define o valor de A, o ponto que está junto ao eixo
    
    if EMP1.location[0] > 0 and EMP1.location[2] < 0:
    
        A = [CB, 0]
        
    if EMP1.location[0] > 0 and EMP1.location[2] > 0:

        A = [CB, 0]
        
    if EMP1.location[0] < 0 and EMP1.location[2] > 0:

        A = [-(CB), 0]
        
    if EMP1.location[0] < 0 and EMP1.location[2] < 0:

        A = [0, -CB]
        

#    BC = CB/2
    AB = math.sqrt( (EMP1.location[0] - A[0])**2 + (EMP1.location[2] - A[1])**2 )
#    Meio
    Cosc = abs(((AB/2)/CB)*2)


    # Parenteia para rotacionar
            
    bpy.ops.object.select_all(action='DESELECT')
    EMP1.select = True
    EMP2.select = True
    EMP3.select = True
    EMP4.select = True
    FACE.select = True     
    bpy.context.scene.objects.active = EMP4
    bpy.ops.object.parent_set()    

    # Rotaciona frente (X, Z)

   

    if EMP1.location[0] > 0 and EMP1.location[2] < 0:
    
        bpy.ops.transform.rotate(value=-(Cosc), axis=(0, 1, 0))
        bpy.ops.transform.rotate(value=3.14159, axis=(0, 1, 0))


        
    if EMP1.location[0] > 0 and EMP1.location[2] > 0:

        bpy.ops.transform.rotate(value=Cosc, axis=(0, 1, 0))
        bpy.ops.transform.rotate(value=3.14159, axis=(0, 1, 0))

        

    if EMP1.location[0] < 0 and EMP1.location[2] > 0:

        bpy.ops.transform.rotate(value=-(Cosc), axis=(0, 1, 0))
        

    if EMP1.location[0] < 0 and EMP1.location[2] < 0:

        bpy.ops.transform.rotate(value=-(Cosc), axis=(0, 1, 0))
        bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0))


    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
    

def AlinhaCima(self, context):

    CB2 = math.sqrt( (EMP4.location[0] - EMP1.location[0])**2 + (EMP4.location[1] - EMP1.location[1])**2 )

    global D, DB, Cosd
    
    # Define o valor de D, o ponto que está junto ao eixo
    
    if EMP1.location[0] > 0 and EMP1.location[1] > 0:
    
        D = [CB2, 0]
        
    if EMP1.location[0] > 0 and EMP1.location[1] < 0:

        D = [CB2, 0]
        
    if EMP1.location[0] < 0 and EMP1.location[1] < 0:

        D = [-(CB2), 0]
        
    if EMP1.location[0] < 0 and EMP1.location[1] > 0:

        D = [-CB2, 0]

    #BC = CB/2
    DB = math.sqrt( (EMP1.location[0] - D[0])**2 + (EMP1.location[1] - D[1])**2 )

    Cosd = abs(((DB/2)/CB2)*2)
    print("DB")
    print(DB)
    print("Cosd")
    print(Cosd)

    # Parenteia para rotacionar
            
    bpy.ops.object.select_all(action='DESELECT')
    EMP1.select = True
    EMP2.select = True
    EMP3.select = True
    EMP4.select = True
    FACE.select = True     
    bpy.context.scene.objects.active = EMP4
    bpy.ops.object.parent_set()    

    # Rotaciona por cima (X, Y)
    
    if EMP1.location[0] > 0 and EMP1.location[1] > 0:
    
        bpy.ops.transform.rotate(value=-(Cosd), axis=(-0,-0,-1))
        bpy.ops.transform.rotate(value=-3.14159, axis=(-0,-0,-1))
        print("1")

        
    if EMP1.location[0] > 0 and EMP1.location[1] < 0:

        bpy.ops.transform.rotate(value=Cosd, axis=(-0,-0,-1))
        bpy.ops.transform.rotate(value=3.14159, axis=(-0,-0,-1))
        print("2")
        

    if EMP1.location[0] < 0 and EMP1.location[1] < 0:

        bpy.ops.transform.rotate(value=-(Cosd), axis=(-0,-0,-1))
        print("3")
        

    if EMP1.location[0] < 0 and EMP1.location[1] > 0:

        bpy.ops.transform.rotate(value=-(Cosd), axis=(-0,-0,-1))
#        bpy.ops.transform.rotate(value=0.349066, axis=(-0,-0,-1))
        print("4")

    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')


def AlinhaLado(self, context):

    global CE, EF, G, Cose
    
    CE = math.sqrt( (EMP4.location[1] - EMP3.location[1])**2 + (EMP4.location[2] - EMP3.location[2])**2 )
    print("CE")
    print(CE)

    # Vista frontal
    # Define o valor de G, o ponto que está junto ao eixo
    
    if EMP3.location[1] > 0 and EMP3.location[2] < 0:
    
        G = [0, -(CE)]
        print("1G")
        
    if EMP3.location[1] > 0 and EMP3.location[2] > 0:

        G = [CE, 0]
        print("2G")
        
    if EMP3.location[1] < 0 and EMP3.location[2] > 0:

        G = [-(CE), 0]
        print("3G")
        
    if EMP3.location[1] < 0 and EMP3.location[2] < 0:

        G = [0, -(CE)]
        print("4G")
        

#    BC = CB/2
    EF = math.sqrt( (EMP3.location[1] - G[0])**2 + (EMP3.location[2] - G[1])**2 )
#    Meio

#    Cose = ((EF/2)/CE)*2
    CatetoAdj = abs(math.sqrt(-((EF/2)**2)+(CE**2)))
    
    Cose = abs(((EF/2)/CE)*2)

    print("EF")
    print(EF)
    print("Cose")
    print(Cose)
    print("CatetoAdj")
    print(CatetoAdj)

    # Parenteia para rotacionar
            
    bpy.ops.object.select_all(action='DESELECT')
    EMP1.select = True
    EMP2.select = True
    EMP3.select = True
    EMP4.select = True
    FACE.select = True     
    bpy.context.scene.objects.active = EMP4
    bpy.ops.object.parent_set()    

    # Rotaciona lado (Y, Z)
    
#'''
    if EMP3.location[1] > 0 and EMP3.location[2] < 0:
    
        bpy.ops.transform.rotate(value=Cose, axis=(-1, 0, 0))

        
    if EMP3.location[1] > 0 and EMP3.location[2] > 0:

        bpy.ops.transform.rotate(value=Cose, axis=(-1, 0, 0))
        bpy.ops.transform.rotate(value=1.5708, axis=(-1, 0, 0))

    

    if EMP3.location[1] < 0 and EMP3.location[2] > 0:

        bpy.ops.transform.rotate(value=-(Cose), axis=(-1, 0, 0))
        bpy.ops.transform.rotate(value=-1.5708, axis=(-1, 0, 0))        


    if EMP3.location[1] < 0 and EMP3.location[2] < 0:

        bpy.ops.transform.rotate(value=-(Cose), axis=(-1, 0, 0))



    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')    
#'''

# Distância intercantal

def Redimensiona(self, context):

    global EMP1EMP2, medidareal2


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
    EMP1.select = True
    EMP2.select = True
    EMP3.select = True
    EMP4.select = True
    FACE.select = True     
    bpy.context.scene.objects.active = EMP4
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
    EMP1.select = True
    EMP2.select = True
    EMP3.select = True
    EMP4.select = True 
    bpy.context.scene.objects.active = EMP1
    bpy.ops.object.delete(use_global=False)


    FACE.select = True     
    bpy.context.scene.objects.active = EMP4

    bpy.ops.view3d.viewnumpad(type='FRONT')
    bpy.ops.view3d.view_selected()
    
  
def AlinhaForca(self, context):

#    print(abs(float("{:.2f}".format(float(EMP1.location[2])))))
#    print(abs(float("{:.2f}".format(float(EMP2.location[2])))))   
#    bpy.ops.object.alinha_frente()
#    print(abs(float("{:.2f}".format(float(EMP1.location[2])))))
#    print(abs(float("{:.2f}".format(float(EMP2.location[2])))))

    while abs(float("{:.2f}".format(float(EMP1.location[2])))) != 0.0 and abs(float("{:.2f}".format(float(EMP2.location[2])))) != 0.0:
        AlinhaFrente(self, context)
        print(abs(float("{:.2f}".format(float(EMP1.location[2])))))
        print(abs(float("{:.2f}".format(float(EMP2.location[2])))))
        
    while abs(float("{:.2f}".format(float(EMP1.location[1])))) != 0.0 and abs(float("{:.2f}".format(float(EMP2.location[1])))) != 0.0:
        AlinhaCima(self, context)
        print(abs(float("{:.2f}".format(float(EMP1.location[1])))))
        print(abs(float("{:.2f}".format(float(EMP2.location[1])))))
        
    while abs(float("{:.2f}".format(float(EMP3.location[1])))) != 0.0 and print(abs(float("{:.2f}".format(float(EMP4.location[1]))))) != 0.0:
        AlinhaLado(self, context)
        print(abs(float("{:.2f}".format(float(EMP3.location[1])))))
        print(abs(float("{:.2f}".format(float(EMP4.location[1])))))

class AlinhaForcaBtn(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.alinha_forca"
    bl_label = "Cálculo de Alinhamento da Mandíbula"
    
    def execute(self, context):
        ConfiguraNomes(self, context)
        CriaPTOrigem(self, context)
        AlinhaForca(self, context)
        
        Redimensiona(self, context)
        
        ApagaPontosAlinhaDef()
        ApagaPontosOrigemDef()
        
        return {'FINISHED'}


def ApagaPontosAlinhaDef():
    
    bpy.ops.object.select_all(action='DESELECT')    
    Pontos = [obj for obj in bpy.context.scene.objects if fnmatch.fnmatchcase(obj.name, "PT_Ali*")]
    
    for i in Pontos:
        i.select=True
    
    bpy.ops.object.delete(use_global=False)
    
def ApagaPontosOrigemDef():
    
    bpy.ops.object.select_all(action='DESELECT')    
    Pontos = [obj for obj in bpy.context.scene.objects if fnmatch.fnmatchcase(obj.name, "PT_Ori*")]
    
    for i in Pontos:
        i.select=True
    
    bpy.ops.object.delete(use_global=False)
    

class CriaTresPontosBtn(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_tres_pontos"
    bl_label = "Cálculo de Alinhamento da Mandíbula"
    
    def execute(self, context):
        ApagaPontosAlinhaDef()
        print("Tudo apagado")
        bpy.ops.wm.modal_timer_operator()       
        return {'FINISHED'}
    



class ModalTimerOperator(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "wm.modal_timer_operator"
    bl_label = "Click on 3 points"

    _timer = None

    def modal(self, context, event):
    

        if event.type in {'RIGHTMOUSE', 'ESC'}:
            self.cancel(context)
            return {'CANCELLED'}

#        bpy.ops.object.select_pattern(pattern="Cub*") # Seleciona objetos com esse padrão
	        
      

        if event.type == 'LEFTMOUSE' and event.value == 'RELEASE':


            if context.area.type == 'VIEW_3D':
                region = context.region
                r3d = context.space_data.region_3d

#                bpy.ops.object.empty_add(type='PLAIN_AXES', radius=1, location=(0,0,0))

                bpy.ops.mesh.primitive_uv_sphere_add(size=.1, location=(0,0,0)) #Atrasa também
                bpy.ops.transform.translate(value=(bpy.context.scene.cursor_location))
                bpy.context.object.name = "PT_Alinha"


        return {'PASS_THROUGH'}

    def execute(self, context):
        if context.area.type != 'VIEW_3D':
            print("Must use in a 3d region")
            return {'CANCELLED'}

        wm = context.window_manager
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager

    def end_ui(self, context):            
        context.area.header_text_set()
        context.window.cursor_modal_restore()
        
    def cleanup(self, context, cleantype=''):
        '''
        remove temporary object
        '''
        if cleantype == 'commit':
            pass

        elif cleantype == 'cancel':
            pass

