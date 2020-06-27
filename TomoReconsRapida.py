import bpy
import os
import pydicom as dicom
from collections import Counter
import tempfile
import shutil
import subprocess
import platform

def GeraModelo3DTomo(ossos, mole, dentes):

    context = bpy.context
    obj = context.object
    scn = context.scene

    #if ReducaoTomo == "REDUZIR": # NÃO USAR!!!
    #    bpy.ops.object.reduz_dimensao_dicom() # NÃO USAR!!!

    bpy.ops.object.corrige_dicom()
    bpy.ops.object.corrige_tomo_raw()

    bpy.context.scene.interesse_ossos = ossos
    bpy.context.scene.interesse_mole = mole
    bpy.context.scene.interesse_dentes = dentes

    print("TENTATIVA 1")
    try:
        bpy.ops.object.gera_modelo_tomo_manual()
    except:
        print("\nERROO!")
        print("TENTATIVA 2")
        scn.my_tool.path = tmpdirTomo
        bpy.ops.object.gera_modelo_tomo_manual()


def CorrigeTomoRawDef():

    context = bpy.context
    obj = context.object
    scn = context.scene

    os.chdir(scn.my_tool.path)

    if platform.system() == "Linux" or platform.system() == "Darwin":
        subprocess.call('for i in *; do gdcmconv -w -i $i -o '+tmpdirTomo2+'/$i; done', shell=True)
        print("Tomografia corrigida!!!")

    if platform.system() == "Linux" or platform.system() == "Darwin":
        subprocess.call('for %f in (*) do C:\OrtogOnBlender\GDCM\gdcmconv -w -i %f -o '+tmpdirTomo2+'/%f', shell=True)
        print("Tomografia corrigida!!!")

    scn.my_tool.path = tmpdirTomo2

class CorrigeTomoRaw(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.corrige_tomo_raw"
    bl_label = "CT-Scan fix raw"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
            CorrigeTomoRawDef()
            return {'FINISHED'}

bpy.utils.register_class(CorrigeTomoRaw)


def TomoRecRapidaDef():

    context = bpy.context
    obj = context.object
    scn = context.scene


    DirTomoOriginal = scn.my_tool.path

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

            #print("SERIESSSSSS", ds.SeriesNumber)
            if ds.SeriesNumber == "":
                try:
                    ds.SeriesNumber = "198291829182"
                    ds.save_as(str(ArquivoAtual))
                    print("SALVOOOO")
                except:
                    print("PROBLEMA NA INSERÇÃO!")
            #ListaInstanceCreationTime.append(ds.InstanceCreationTime)
            try:
                ListaSeriesNumber.append(ds.SeriesNumber)
            except:
                print("Problem com o SeriesNumer")
                print("Series:", ArquivoAtual)

            try:
                ListaConvolutionKernel.append(ds.ConvolutionKernel)
            except:
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
        if i == '':
            i = "2312457886300"
        listaSeries.append([SeriesValores[i], int(i)])

    print("ORDEM ORIGINAL")
    print(listaSeries)

    # Calcula o número de arquivos por diretório
    print("SORT")
    listaFinal = sorted(listaSeries, reverse=True)
    print(sorted(listaSeries, reverse=True))

    print("Diretório com mais arquivos:", listaFinal[0][1])

    DiretorioFinal = listaFinal[0][1]


    # Copia os arquivos para diretório temporário

    global tmpdirTomo
    global tmpdirTomo2
    tmpdirTomo = tempfile.mkdtemp()
    tmpdirTomo2 = tempfile.mkdtemp()

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

    #global ReducaoTomo

    try:
        ConvKernel = ds.ConvolutionKernel

        print("ConvolutionKernel:", ConvKernel)
    except:
        ConvKernel = ""
        print("Erro no ConvKernel!")

    try:
        Manufacturer = ds.Manufacturer

        print("Manufacturer", Manufacturer)
    except:
        Manufacturer = ""
        print("Erro no Manufacturer!")

    '''
    try:
        DimPixelsX = ds.Rows
        DimPixelsY = ds.Columns

        if DimPixelsX > 512 or DimPixelsY > 512:
            ReducaoTomo = "REDUZIR"
        else:
            ReducaoTomo = "NAO REDUZIR"

    except:
        ReducaoTomo = "Problema"
        print("Problema ao verificar as dimensões")
    '''

    # Reconstrói tomografia HELICOIDAL


    if not ConvKernel == "" and not Manufacturer == "NewTom":

        try:
            print("Há ConvKernel!")

            if ConvKernel == "FC03" or ConvKernel =="FC04" or ConvKernel == "STANDARD" or ConvKernel == "H30s" or ConvKernel == "SOFT" or ConvKernel == "UB" or ConvKernel == "SA" or ConvKernel == "FC23" or ConvKernel == "FC08" or ConvKernel == ['Hr40f', '3'] or ConvKernel == "FC21" or ConvKernel =="A" or ConvKernel =="FC02" or ConvKernel =="B" or ConvKernel =="H23s" or ConvKernel =="H20s" or ConvKernel == "H31s" or ConvKernel == "H32s" or ConvKernel == ['J30s', '3'] or ConvKernel == "H40s" or ConvKernel == "H31s" or ConvKernel == "B41s" or ConvKernel == "B70s" or ConvKernel == "H22s" or ConvKernel == ['J30f', '2'] or ConvKernel == "H20f" or ConvKernel == "FC68" or ConvKernel == "FC07" or ConvKernel == "B30s" or ConvKernel == "B41s" or ConvKernel == ['I31f', '3'] or ConvKernel == ['Br40f', '3'] or ConvKernel == "D10f" or ConvKernel == "B45s" or ConvKernel == "B26f" or ConvKernel == "B30f":

                GeraModelo3DTomo("200", "-300", "1430")


            if ConvKernel == "BONE" or ConvKernel =="BONEPLUS" or ConvKernel =="FC30" or ConvKernel =="H70s" or ConvKernel =="D" or ConvKernel =="EA" or ConvKernel == ['Hr60f', '3'] or ConvKernel =="FC81" or ConvKernel =="YC" or ConvKernel =="YD" or ConvKernel =="H70h" or ConvKernel =="H60s" or ConvKernel == "H60f" or ConvKernel == "FC35" or ConvKernel == "B80s" or ConvKernel == "H90s" or ConvKernel == ['I70f', '3'] or ConvKernel == "B70f":

                GeraModelo3DTomo("400", "-300", "995")

        except:

            # Usa o diretório FIXED em caso de erro com o gdcmconv

            print("Problema na reconstrução... tentando outro meio:")

            DirTemporario = tempfile.gettempdir()

            if os.path.isfile(DirTemporario+"/tmpdirFIXED.txt"):
                arquivo = open(DirTemporario+"/tmpdirFIXED.txt", 'r')
                DiretorioFIXED = arquivo.read()
                arquivo.close()

                scn.my_tool.path = DiretorioFIXED

                bpy.ops.object.gera_modelo_tomo_manual()

            if not os.path.isfile(DirTemporario+"/tmpdirFIXED.txt"):
                print("Infelizmente não foi possível reconstruir, tente exportar no Slicer!")


    # Reconstrói tomografia CONE BEAM

    # Excepcionalmente!
    if not ConvKernel == "" and Manufacturer == "NewTom":
            GeraModelo3DTomo("606", "-466", "1032")

    # Normal
    if ConvKernel == "" and not Manufacturer == "":
        print("Tentando pelo modelo...")

        if Manufacturer == "Imaging Sciences International":
            GeraModelo3DTomo("358", "-629", "995")

        if Manufacturer == "Xoran Technologies ®":
            GeraModelo3DTomo("331", "-679", "1052")

        if Manufacturer == "Planmeca":
            GeraModelo3DTomo("330", "-548", "756")

        if Manufacturer == "J.Morita.Mfg.Corp.":
            GeraModelo3DTomo("487", "-315", "787")

        if Manufacturer == "Carestream Health":
            GeraModelo3DTomo("388", "-598", "1013")

        if Manufacturer == "NewTom":
            GeraModelo3DTomo("606", "-466", "1032")

        if Manufacturer == "MyRay":
            GeraModelo3DTomo("850", "-360", "1735")

        if Manufacturer == "NIM":
            GeraModelo3DTomo("1300", "-1", "1260")

        if Manufacturer == "PreXion":
            GeraModelo3DTomo("312", "-687", "1505")

        if Manufacturer == "Sirona":
            GeraModelo3DTomo("590", "-170", "780")

        if Manufacturer == "Dabi Atlante":
            GeraModelo3DTomo("575", "-375", "1080")

        if Manufacturer == "INSTRUMENTARIUM DENTAL":
            GeraModelo3DTomo("430", "-480", "995")


class TomoRecRapida(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_modelotomo_rec_rapida"
    bl_label = "CT-Scan fast auto reconstruction"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
            TomoRecRapidaDef()
            return {'FINISHED'}

bpy.utils.register_class(TomoRecRapida)
