import bpy
import tempfile
import platform
import os

from .AjustaTomo import *

def SegmentacaoImagemFaceDef():

    context = bpy.context
#    obj = context.object
    scn = context.scene

    TmpDirSegFace = tempfile.mkdtemp()
    SegFaceScript = TmpDirSegFace+'/SegmentaFace.py'

    with open(SegFaceScript, "a") as ScriptF:
        ScriptF.write("from imutils import face_utils\n")
        ScriptF.write("import imutils\n")
        ScriptF.write("import numpy as np\n")
        ScriptF.write("import collections\n")
        ScriptF.write("import dlib\n")
        ScriptF.write("import cv2\n")
        ScriptF.write("from os.path import expanduser\n")
        ScriptF.write("import platform\n")
        ScriptF.write("import os\n")
        ScriptF.write("from os import listdir\n")
        ScriptF.write("from os.path import isfile, join\n")
        ScriptF.write("\n")
        ScriptF.write("def face_remap(shape):\n")
        ScriptF.write("    remapped_image = cv2.convexHull(shape)\n")
        ScriptF.write("    return remapped_image\n")
        ScriptF.write("\n")
        ScriptF.write("def GeraImagemComMascara(imgOriginal, imgFinal):\n")
        ScriptF.write("\n")
        ScriptF.write("    image = cv2.imread(imgOriginal)\n")
        Arquivo = os.listdir(scn.my_tool.path_photo)[0]
        Imagem = bpy.data.images.load(scn.my_tool.path_photo+Arquivo)
        Largura = str(Imagem.size[1])
        print("A largura é:", Largura)
        ScriptF.write("    image = imutils.resize(image, width="+Largura+")\n")
        ScriptF.write("    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n")
        ScriptF.write("\n")
        ScriptF.write("    out_face = np.zeros_like(image)\n")
        ScriptF.write("\n")
        ScriptF.write("    detector = dlib.get_frontal_face_detector()\n")
        if platform.system() == "Linux":
            ScriptF.write("    predictor = dlib.shape_predictor('/home/linux3dcs/Programs/OrtogOnBlender/SegmentaImagens/shape_predictor_81_face_landmarks.dat')\n")
        if platform.system() == "Windows":
            ScriptF.write("    predictor = dlib.shape_predictor('C:\OrtogOnBlender\SegmentaImagens\shape_predictor_81_face_landmarks.dat')\n")
        ScriptF.write("\n")
        ScriptF.write("    rects = detector(gray, 1)\n")
        ScriptF.write("\n")
        ScriptF.write("\n")
        ScriptF.write("    for (i, rect) in enumerate(rects):\n")
        ScriptF.write("\n")
        ScriptF.write("       shape = predictor(gray, rect)\n")
        ScriptF.write("       shape = face_utils.shape_to_np(shape)\n")
        ScriptF.write("\n")
        ScriptF.write("       remapped_shape = np.zeros_like(shape)\n")
        ScriptF.write("       feature_mask = np.zeros((image.shape[0], image.shape[1]))\n")
        ScriptF.write("\n")
        ScriptF.write("       remapped_shape = face_remap(shape)\n")
        ScriptF.write("       cv2.fillConvexPoly(feature_mask, remapped_shape[0:27], 1)\n")
        ScriptF.write("       feature_mask = feature_mask.astype(np.bool)\n")
        ScriptF.write("       out_face[feature_mask] = image[feature_mask]\n")
        ScriptF.write("       cv2.imshow('mask_inv', out_face)\n")
        ScriptF.write("       cv2.imwrite(imgFinal, out_face)\n")
        ScriptF.write("\n")
        ScriptF.write("def AdicionaModeloDistanciaFocal(diretorioFinalFotos):\n")
        ScriptF.write("\n")
        ScriptF.write("    homeall = expanduser('~')\n")
        ScriptF.write("\n")
        ScriptF.write("    if platform.system() == 'Linux':\n")
        ScriptF.write("        os.system('cd '+diretorioFinalFotos+' && exiftool -overwrite_original -Model=\"Z00AD\" -FocalLength=\"3.8 mm\" *')\n")
        # '+homeall+'/Programs/OrtogOnBlender/openMVG/ExifTool.sh
        # exiftool -overwrite_original -Model="Z00AD" -FocalLength="3.8 mm" *
        ScriptF.write("\n")
        ScriptF.write("    if platform.system() == 'Darwin':\n")
        ScriptF.write("        os.system('cd '+diretorioFinalFotos+' && /OrtogOnBlender/openMVGMACelcap/ExifTool.sh')\n")
        ScriptF.write("\n")
        ScriptF.write("    if platform.system() == 'Windows':\n")
        ScriptF.write("        print(mypath)\n")
        ScriptF.write("        subprocess.call(['C:\OrtogOnBlender\ExitTool\exiftool.exe', '-overwrite_original', '-Model=\"Z00AD\"', '-FocalLength=4', diretorioFinalFotos+'*'])\n")
        ScriptF.write("\n")
        ScriptF.write("dirOrigi = '/home/linux3dcs/prj/Estudos/DLIB/ROSTO/'\n")
        ScriptF.write("os.mkdir('"+TmpDirSegFace+"/SegmentedPhotos')\n")
        ScriptF.write("dirFinal = '"+TmpDirSegFace+"/SegmentedPhotos/'\n")
        ScriptF.write("\n")
        ScriptF.write("mypath = '"+scn.my_tool.path_photo+"'\n")
        ScriptF.write("\n")
        ScriptF.write("onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]\n")
        ScriptF.write("\n")
        ScriptF.write("for i in onlyfiles:\n")
        ScriptF.write("    GeraImagemComMascara(mypath+i, dirFinal+i)\n")
        ScriptF.write("    print('Image '+i+' Finished!')\n")
        ScriptF.write("AdicionaModeloDistanciaFocal(dirFinal)\n")
        ScriptF.close()

    if platform.system() == "Linux":
        os.system('python3 '+TmpDirSegFace+'/SegmentaFace.py')
        scn.my_tool.path_photo = TmpDirSegFace+"/SegmentedPhotos/"
        abrir_diretorio(TmpDirSegFace+"/SegmentedPhotos/")

    if platform.system() == "Windows":
        os.system('C:\OrtogOnBlender\Python36\python3 '+TmpDirSegFace+'/SegmentaFace.py')
        scn.my_tool.path_photo = TmpDirSegFace+"/SegmentedPhotos/"
        abrir_diretorio(TmpDirSegFace+"/SegmentedPhotos/")        
        
class SegmentacaoImagemFace(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.segmenta_imagem_face"
    bl_label = "Imagem Segmentation"

    def execute(self, context):
        SegmentacaoImagemFaceDef()
        return {'FINISHED'}

bpy.utils.register_class(SegmentacaoImagemFace)
