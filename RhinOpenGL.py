import bpy
import gpu
import bgl
from gpu_extras.batch import batch_for_shader

def LinhasCentraisCria():

    CantusRightX = bpy.data.objects['Medial Canthus right'].location[0]
    CantusRightY = bpy.data.objects['Medial Canthus right'].location[1]

    CantusLeftX = bpy.data.objects['Medial Canthus left'].location[0]
    CantusLeftY = bpy.data.objects['Medial Canthus left'].location[1]

    TrichionY = bpy.data.objects['Trichion'].location[1]
    TrichionZ = bpy.data.objects['Trichion'].location[2]

    STGlabellaY = bpy.data.objects['ST Glabella'].location[1]
    STGlabellaZ = bpy.data.objects['ST Glabella'].location[2]


    SubnasaleY = bpy.data.objects['Subnasale'].location[1]
    SubnasaleZ = bpy.data.objects['Subnasale'].location[2]

    STMentonY = bpy.data.objects['ST Menton'].location[1]
    STMentonZ = bpy.data.objects['ST Menton'].location[2]

    DistanciaCantus = abs(CantusLeftX - CantusRightX)

    print("DISTANCIA CANTUS!!!", DistanciaCantus)

    try:

        LatCantusRightX = bpy.data.objects['Lateral Canthus right'].location[0]
        LatCantusRightY = bpy.data.objects['Lateral Canthus right'].location[1]

        LatCantusLeftX = bpy.data.objects['Lateral Canthus left'].location[0]
        LatCantusLeftY = bpy.data.objects['Lateral Canthus left'].location[1]

        coords = [(LatCantusRightX,LatCantusRightY,-1000), (LatCantusRightX,LatCantusRightY,1000),(CantusRightX,CantusRightY,-1000), (CantusRightX,CantusRightY,1000), (LatCantusLeftX,LatCantusLeftY,-1000), (LatCantusLeftX,LatCantusLeftY, 1000),(CantusLeftX,CantusLeftY,-1000), (CantusLeftX,CantusLeftY, 1000), (1000, TrichionY, TrichionZ), (-1000, TrichionY, TrichionZ), (1000, STGlabellaY, STGlabellaZ), (-1000, STGlabellaY, STGlabellaZ), (1000, SubnasaleY, SubnasaleZ), (-1000, SubnasaleY, SubnasaleZ), (1000, STMentonY, STMentonZ), (-1000, STMentonY, STMentonZ) ] #, (CantusRightX-DistanciaCantus,CantusRightY,-1000), (CantusRightX-DistanciaCantus,CantusRightY, 1000), (CantusLeftX+DistanciaCantus,CantusLeftY,-1000), (CantusLeftX+DistanciaCantus,CantusLeftY, 1000)]

        shader = gpu.shader.from_builtin('3D_UNIFORM_COLOR')

        batch = batch_for_shader(shader, 'LINES', {"pos": coords})

    except:
        coords = [(CantusRightX,CantusRightY,-1000), (CantusRightX,CantusRightY,1000),(CantusLeftX,CantusLeftY,-1000), (CantusLeftX,CantusLeftY, 1000), (1000, TrichionY, TrichionZ), (-1000, TrichionY, TrichionZ), (1000, STGlabellaY, STGlabellaZ), (-1000, STGlabellaY, STGlabellaZ), (1000, SubnasaleY, SubnasaleZ), (-1000, SubnasaleY, SubnasaleZ), (1000, STMentonY, STMentonZ), (-1000, STMentonY, STMentonZ) ] #, (CantusRightX-DistanciaCantus,CantusRightY,-1000), (CantusRightX-DistanciaCantus,CantusRightY, 1000), (CantusLeftX+DistanciaCantus,CantusLeftY,-1000), (CantusLeftX+DistanciaCantus,CantusLeftY, 1000)]

        shader = gpu.shader.from_builtin('3D_UNIFORM_COLOR')

        batch = batch_for_shader(shader, 'LINES', {"pos": coords})

    def draw():
        shader.bind()
        bgl.glLineWidth(3) # 1 Grossura
    #    bgl.glDisable(bgl.GL_BLEND)
    #    bgl.glEnable(bgl.GL_DEPTH_TEST)
        bgl.glDisable(bgl.GL_DEPTH_TEST)
    #    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
        shader.uniform_float("color", (1, 1, 1, 1))
        batch.draw(shader)

    global my_draw_handler
    my_draw_handler = bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_VIEW')

    bpy.ops.view3d.view_all(center=False)


class RhinVisualizaGL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.rhin_visualiza_gl"
    bl_label = "Visualiza OpenGL"

    def execute(self, context):
        LinhasCentraisCria()
        return {'FINISHED'}

bpy.utils.register_class(RhinVisualizaGL)


def LinhasCentraisApaga():

    bpy.types.SpaceView3D.draw_handler_remove(my_draw_handler, 'WINDOW')
    bpy.ops.view3d.view_all(center=False)


class RhinRemoveGL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.rhin_remove_gl"
    bl_label = "Remove OpenGL"

    def execute(self, context):
        LinhasCentraisApaga()
        return {'FINISHED'}

bpy.utils.register_class(RhinRemoveGL)
