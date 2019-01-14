import bpy
import os
import subprocess
import tempfile
import platform
import pydicom as dicom

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

    space = context.space_data
    space.image_user.use_auto_refresh = True


#    bpy.data.screens["Default"]..use_auto_refresh = True 
 
class ImportaSeqTomo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.importa_img_tomo"
    bl_label = "Teste"
    
    def execute(self, context):
        ImportaSeqTomoDef(self, context)
        return {'FINISHED'}


def ExportaSeqTomoDef(self, context):

    layout = self.layout
    scn = context.scene
    obj = context.object

    IMGDir = str(bpy.types.Scene.IMGPathSeq[1]['default'])

    SliceThickness = str(bpy.types.Scene.SliceThickness[1]['default'])

    PixelSpacingX = str(bpy.types.Scene.PixelSpacingX[1]['default'])

    PixelSpacingY = str(bpy.types.Scene.PixelSpacingY[1]['default'])

    DimPixelX = str(bpy.types.Scene.IMGDimX[1]['default'])

    DimPixelY = str(bpy.types.Scene.IMGDimY[1]['default'])

    DirDcmExp = tempfile.mkdtemp()

    if platform.system() == "Linux":    

        subprocess.call('cd '+IMGDir+' && mkdir GREY && for i in *.png; do convert $i -type Grayscale -depth 8 GREY/$i; done', shell=True)
        print("PNGs GERADOS!!!")

        subprocess.call('python ~/Programs/OrtogOnBlender/Img2Dcm/img2dcm.py -i '+IMGDir+'/GREY/ -o '+DirDcmExp+' -s '+PixelSpacingX+' '+PixelSpacingY+' '+SliceThickness+' -t png', shell=True)
        print("DICOM BASE GERADO!!!")

#        ListaArquivos = sorted(os.listdir(DirDcmExp))
       # ListaArquivos = sorted(os.listdir(IMGDir+'/GREY/'))

#        subprocess.call('cd '+DirDcmExp, shell=True)

#        for fatia in range(len(ListaArquivos)):
#            ds = dicom.dcmread(ListaArquivos[fatia])
#            ds.ImagePositionPatient[2] = int(fatia)*float(SliceThickness)
#            print("Fatia", ListaArquivos[fatia], "Slice", int(fatia)*float(SliceThickness))
#            ds.save_as(ListaArquivos[fatia])
#        print("LOOP FINALIZADO")

        scn.my_tool.path = DirDcmExp+"/"


    if platform.system() == "Darwin":


# Converte slices em PNGs e depois o PNGs em JPGs monocromaticos
        subprocess.call('cd '+IMGDir+' && mkdir GREY && for i in *.png; do convert $i -type Grayscale -depth 8 -quality 100 GREY/${i%.png}.jpg; done', shell=True)
        print("JPEGs GERADOS!!!")

        
        subprocess.call('cd '+IMGDir+'/GREY/ && for i in *.jpg; do img2dcm $i ${i%.jpg}.dcm; done && rm *.jpg', shell=True)

# Ajusta os DICOMs nos campos que dao erro
        ListaArquivos = sorted(os.listdir(IMGDir+"/GREY/"))

        os.chdir(IMGDir+"/GREY/")

        for fatia in range(len(ListaArquivos)):
            ds = dicom.dcmread(str(ListaArquivos[fatia]), force=True)
            ds.SeriesNumber = "1"
            ds.AccessionNumber = "1"
            ds.Modality = "CT"
            ds.ImagePositionPatient = "0\\0\\"+str((fatia)*float(SliceThickness)) # Valor do SliceThickness
            ds.PatientID = "OrtogOnBlender"
            ds.InstanceNumber = str(int(fatia)-1)
            ds.SliceThickness = SliceThickness
            ds.PixelSpacing = PixelSpacingX+"\\"+PixelSpacingY
            ds.StudyID = "TESTEID"
            ds.PatientName = "Teste"
            ds.Rows = int(float(DimPixelX))
            ds.Columns = int(float(DimPixelY))
            ds.save_as(str(ListaArquivos[fatia]))
            
            scn.my_tool.path = IMGDir+"/GREY/"

# Ajusta com o dicomtodicom e corrige os pontos que dao erro na importacao
        
        bpy.ops.object.corrige_dicom()

        ListaArquivos = sorted(os.listdir(IMGDir+"/GREY/FIXED/"))

        os.chdir(IMGDir+"/GREY/FIXED/")

        for fatia in range(len(ListaArquivos)):
            ds = dicom.dcmread(str(ListaArquivos[fatia]), force=True)
            ds.SeriesNumber = "1"
            ds.AccessionNumber = "1"
            ds.Modality = "CT"
            ds.ImagePositionPatient = "0\\0\\"+str((fatia)*float(SliceThickness)) # Valor do SliceThickness
            ds.PatientID = "OrtogOnBlender"
            ds.InstanceNumber = str(int(fatia)-1)
            ds.SliceThickness = SliceThickness
            ds.PixelSpacing = PixelSpacingX+"\\"+PixelSpacingY
            ds.StudyID = "TESTEID"
            ds.PatientName = "Teste"
            ds.Rows = int(float(DimPixelX))
            ds.Columns = int(float(DimPixelY))
            ds.save_as(str(ListaArquivos[fatia]))
        
        
        scn.my_tool.path = IMGDir+"/GREY/FIXED/"
        #scn.my_tool.path = DirDcmExp+"/"
  

class ExportaSeqTomo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.exporta_img_tomo"
    bl_label = "Teste"
    
    def execute(self, context):
        ExportaSeqTomoDef(self, context)
        return {'FINISHED'}
