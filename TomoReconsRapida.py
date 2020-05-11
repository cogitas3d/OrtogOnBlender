import bpy
import os
import pydicom as dicom
from collections import Counter
import tempfile
import shutil


def TomoRecRapidaDef():

    context = bpy.context
    obj = context.object
    scn = context.scene

    # Listar todos os arquivos

    ListaArquivosAbs = []


    #DiretorioDCM = '/home/linux3dcs/del/TOMOGRAFIAS_ESTUDOS/DAVI/000'

    for dirname, dirnames, filenames in os.walk(scn.my_tool.path):

        for filename in filenames:
            print(os.path.join(dirname, filename))
            ListaArquivosAbs.append(os.path.join(dirname, filename))

    #print(ListaArquivosAbs)

    ListaConvolutionKernel = []
    ListaSeriesNumber = []
    ListaArquivosDICOM = []
    #ListaInstanceCreationTime = []

    NaoEhDICOM = []

    # Pesquisa os arquivos
    for ArquivoAtual in ListaArquivosAbs:
        try:
            ds = dicom.dcmread(ArquivoAtual, force=True)

            ListaArquivosDICOM.append(ArquivoAtual)

            #ListaInstanceCreationTime.append(ds.InstanceCreationTime)
            try:
                ListaSeriesNumber.append(ds.SeriesNumber)
            except:
                print("Problem com o SeriesNumer")
                print("Series:", ArquivoAtual)

            try:
                ListaConvolutionKernel.append(ds.ConvolutionKernel)
            except:
                print("Problema com o ConvolutionKernel")
                print("ConvKernel:", ArquivoAtual)

        except:
           NaoEhDICOM.append(ArquivoAtual)
    #       print(ArquivoAtual, "Não é!")


    print("FINISHED!")

    #for i in NaoEhDICOM:
    #    print(i, "Não é DICOM!")

    #print(DiretorioDCM)
    #print(Counter(ListaInstanceCreationTime))
    print(Counter(ListaSeriesNumber))
    try:
        print(Counter(ListaConvolutionKernel))
    except:
        print("Problema ao imprimir o ConvKernel")

    SeriesValores = Counter(ListaSeriesNumber)

    print("SERIES")

    print(SeriesValores)

    listaSeries = []

    for i in SeriesValores:
        listaSeries.append([SeriesValores[i], i])

    print(listaSeries)

    # Calcula o número de arquivos por diretório
    print("SORT")
    listaFinal = sorted(listaSeries, reverse=True)
    print(sorted(listaSeries, reverse=True))

    print("Diretório com mais arquivos:", listaFinal[0][1])

    DiretorioFinal = listaFinal[0][1]


    # Copia os arquivos para diretório temporário

    tmpdirTomo = tempfile.mkdtemp()


    DCMNum = 0

    for ArquivoAtual in ListaArquivosDICOM:

        ds = dicom.dcmread(ArquivoAtual, force=True)


        try:
            if ds.SeriesNumber == DiretorioFinal:
                #print(ds.SeriesNumber )

                os.chdir(tmpdirTomo)

                shutil.copy(ArquivoAtual, "Copy-"+str(DCMNum))
                #print("Copiado de: ", ArquivoAtual, " Para: ", "Copy-"+str(DCMNum))
                DCMNum += 1
        except:
            print("Erro de leitura do SeriesNumber no:", ArquivoAtual)

    scn.my_tool.path = tmpdirTomo


    print("Arquivos DICOM copiados!")

    # Captura o 0018,1210 do primeiro arquivo

    ArquivoTopo = os.listdir(os.getcwd())[0]
    print("Arquivo topo:", ArquivoTopo)


    ds = dicom.dcmread(ArquivoTopo, force=True)

    try:
        ConvKernel = ds.ConvolutionKernel

        print("ConvolutionKernel:", ConvKernel)
    except:
        print("Erro no ConvKernel!")


    # Reconstrói tomografia

    if ConvKernel == "FC03" or ConvKernel == "STANDARD" or ConvKernel == "H30s" or ConvKernel == "SOFT" or ConvKernel == "UB" or ConvKernel == "SA" or ConvKernel == "FC23" or ConvKernel == "FC08" or ConvKernel == ['Hr40f', '3'] or ConvKernel == "FC21":

        bpy.context.scene.interesse_ossos = "200"
        bpy.context.scene.interesse_mole = "-300"
        bpy.context.scene.interesse_dentes = "1430"

        bpy.ops.object.gera_modelos_tomo()

    if ConvKernel == "BONE" or ConvKernel =="FC30" or ConvKernel =="H70s" or ConvKernel =="D" or ConvKernel =="EA" or ConvKernel == ['Hr60f', '3']:

        bpy.context.scene.interesse_ossos = "400"
        bpy.context.scene.interesse_mole = "-300"
        bpy.context.scene.interesse_dentes = "995"

        bpy.ops.object.gera_modelos_tomo()



class TomoRecRapida(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_modelotomo_rec_rapida"
    bl_label = "CT-Scan fast auto reconstruction"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
            TomoRecRapidaDef()
            return {'FINISHED'}

bpy.utils.register_class(TomoRecRapida)
