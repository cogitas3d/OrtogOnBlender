import bpy
import os


def ImportaSeqTomoDef(self, context):

    layout = self.layout
    scn = context.scene
    obj = context.object 
	
    IMGDir = str(bpy.types.Scene.IMGPathSeq[1]['default'])

    ListaArquivos = sorted(os.listdir(IMGDir))

    listaIMG=[]

    for Arquivo in ListaArquivos:
        listaIMG.append( {"name":Arquivo, "name":Arquivo} )

    print(listaIMG)

    bpy.ops.image.open(directory=IMGDir, files=listaIMG, relative_path=True, show_multiview=False)
    bpy.data.images[str(ListaArquivos[0])].source = 'SEQUENCE'


#    bpy.data.screens["Default"]..use_auto_refresh = True 
 
class ImportaSeqTomo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.importa_img_tomo"
    bl_label = "Teste"
    
    def execute(self, context):
        ImportaSeqTomoDef(self, context)
        return {'FINISHED'}
       

