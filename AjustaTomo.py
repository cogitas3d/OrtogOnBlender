import bpy
import os
import os.path
import json
import re
import shutil
from datetime import datetime
import tempfile
import os
import platform
import subprocess
import pydicom as dicom

from .GeraModelosTomo import *

if platform.system() == "Darwin" or platform.system() == "Linux":
    import pyexifinfo as p

def AjustaTomoDef(self, context):


    scn = context.scene


    #Cria diretorios temporarios e copia o conteudo para um deles
    #os.chdir('DEL')
    
#    scene = context.scene
#    rd = scene.render

    if scn.my_tool.path == "":
        bpy.ops.object.dialog_operator_informe_dicom('INVOKE_DEFAULT')
        return {'FINISHED'}

    else:

        tmpdirCopy = tempfile.mkdtemp()

        tmpdirTomo = tempfile.mkdtemp()

        shutil.copytree(scn.my_tool.path, tmpdirCopy+'COPY')

        # Lista os arquivos e salva arquivo de texto

        # Testa se existe e remove
        if os.path.exists('ListaArquivos.txt'):
            os.remove('ListaArquivos.txt')


        #for dirname, dirnames, filenames in os.walk('.'):
        for dirname, dirnames, filenames in os.walk(tmpdirCopy+'COPY'):
            # print path to all subdirectories first.
        #    for subdirname in dirnames:
        #        print(os.path.join(dirname, subdirname))

            for filename in filenames:
                #print(os.path.join(dirname, filename))
                ArquivosListados = os.path.join(dirname, filename)+'\n'

                with open("ListaArquivos.txt", "a") as arq:
                    arq.write(ArquivosListados)
                    arq.close()


        # Conta linhas do arquivo

        def obter_n_linhas (nomeDoArquivo):
            arquivo = open(nomeDoArquivo, "r")
            n_linhas = sum(1 for linha in arquivo)
            arquivo.close()
            return n_linhas


        def InstanceNumber(Arquivo):


            try:        
                ds = dicom.dcmread(Arquivo, force=True) # Diretório e arquivo concatenados
                #ds = dicom.dcmread(Arquivo, force=True) # Diretório e arquivo concatenados


                instance_number = ds.data_element("InstanceNumber")
                instanceLimpa1 = str(instance_number).split('IS: ')
                instanceLimpa2 = str(instanceLimpa1[1]).strip('"')


            except:
                print("Não rolou leitura do DICOM!")
                instanceLimpa2 = "Error"

            return instanceLimpa2

        NumeroLinhas = obter_n_linhas ('ListaArquivos.txt')

        #-----------------------------------------------------------

        # Le arquivo e cria pastas

        #ContadorLinhas = 0

        with open('ListaArquivos.txt','r') as f:
                ListaArquivos=f.readlines()
                print("Criado Lista Arquivo1")

        DCMNum = 0

        for x in range(NumeroLinhas):
            ArquivoAtual = ListaArquivos[x].strip('\n') # mostra linha 1 sem o caractere de quebra de linha
        #	print(ArquivoAtual)
            DCMInstanceNumber = InstanceNumber(ArquivoAtual)
            os.chdir(tmpdirTomo)

            shutil.copy(ArquivoAtual, "Copy-"+DCMInstanceNumber.zfill(5)+"-"+str(DCMNum))
            print("Copiado de: ", ArquivoAtual, " Para: ", "Copy-"+DCMInstanceNumber+"-"+str(DCMNum))
    #        shutil.copy(ArquivoAtual, str(datetime.now()).replace(":","").replace(".","").replace(" ","").replace("-",""))
    #        print("Copiado de: ", ArquivoAtual, " Para: ", str(datetime.now()).replace(":","").replace(".","").replace(" ","").replace("-",""))
        #	os.chdir('..')
            DCMNum += 1

        # Lista os arquivos e salva arquivo de texto

        # Testa se existe e remove
        if os.path.exists('ListaArquivos.txt'):
            os.remove('ListaArquivos.txt')
            print("Apagado ListaArquivo")



        #for dirname, dirnames, filenames in os.walk('.'):
        for dirname, dirnames, filenames in os.walk(tmpdirTomo):
            # print path to all subdirectories first.
        #    for subdirname in dirnames:
        #        print(os.path.join(dirname, subdirname))

            for filename in filenames:
                #print(os.path.join(dirname, filename))
                ArquivosListados = os.path.join(dirname, filename)+'\n'

                with open('ListaArquivos.txt', "a") as arq:
                    print("Criado ListaArquivo 2")
                    arq.write(ArquivosListados)
                    arq.close()


        # Conta linhas do arquivo

        def obter_n_linhas (nomeDoArquivo):
            arquivo = open(nomeDoArquivo, "r")
            n_linhas = sum(1 for linha in arquivo)
            arquivo.close()
            return n_linhas


        NumeroLinhas = obter_n_linhas ('ListaArquivos.txt')


        # Le arquivo e cria pastas

        #ContadorLinhas = 0

        with open('ListaArquivos.txt','r') as f:
                ListaArquivos=f.readlines()

    # PYEXIFINFO

        if platform.system() == "Darwin" or platform.system() == "Linux":
            print("EH MAC E LIN")
            for x in range(NumeroLinhas):
                ArquivoAtual = ListaArquivos[x].strip('\n') # mostra linha 1 sem o caractere de quebra de linha
        #	print(ArquivoAtual)

                data = p.get_json(ArquivoAtual)

                data2 = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

                with open("deletar.txt", "a") as arq:
                    arq.write(data2)
                    arq.close()

                    palavra = "SeriesNumber"
                        
                    for line in open("deletar.txt"):
                        if palavra in line:
                            SeriesRaw = line
                            SeriesLimpa1 = SeriesRaw.strip('"DICOM:SeriesNumber": "')
                            SeriesLimpa2 = SeriesLimpa1.strip('",'+'\n')
                            SeriesLimpo = SeriesLimpa2.strip(" ")
                            print("SERIES", SeriesLimpo)

                            if SeriesLimpo != '':
                                if not os.path.exists(SeriesLimpo):
                                    os.mkdir(SeriesLimpo)
                            
                            if SeriesLimpo != '':                    
                                shutil.copy(ArquivoAtual, SeriesLimpo)
                                print("Copiado de: ", ArquivoAtual, " Para: ", SeriesLimpo)
                                os.remove(ArquivoAtual)


                    os.remove('deletar.txt')

    # PYTHON DICOM

        if platform.system() == "Windows":
            print("EH WIN")
            for x in range(NumeroLinhas):
                ArquivoAtual = ListaArquivos[x].strip('\n') # mostra linha 1 sem o caractere de quebra de linha
                print("AQUIVO ATUAL: "+ArquivoAtual)

                try:
                    ds = dicom.dcmread(ArquivoAtual)

                    series_number = ds.data_element("SeriesNumber")

                    SeriesLimpa1 = str(series_number).strip('(0020, 0011) Series Number IS:')
                    SeriesLimpo2 = SeriesLimpa1.strip('"')
                    SeriesLimpo = SeriesLimpo2.strip(" ")

                except:
                    print("Não rolou leitura do DICOM!")
                    SeriesLimpo = "Error"


                if not os.path.exists(SeriesLimpo):
                    os.mkdir(SeriesLimpo)
                    print("Diretorio "+SeriesLimpo+" criado")

                #os.chdir(tmpdirTomo)
                shutil.copy(ArquivoAtual, SeriesLimpo)
                print("Copiado de: ", ArquivoAtual, " Para: ", SeriesLimpo)
                os.remove(ArquivoAtual)


				    
            #os.remove('deletar.txt')
    #        os.remove('deletar.txt')
        shutil.rmtree(tmpdirCopy+'COPY')
        shutil.rmtree(tmpdirCopy)

        print("CT-SCAN ready!")

    #    abrir_tomo(tmpdirTomo+'_CT-SCAN')
        abrir_diretorio(tmpdirTomo)

        scn.my_tool.path = tmpdirTomo+"/"

class AjustaTomo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.ajusta_tomo"
    bl_label = "Ajusta Tomo"


    def execute(self, context):
        AjustaTomoDef(self, context)
        return {'FINISHED'}

# ---------------------------------------
	
def abrir_diretorio(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])
	
def AbreTMPDef(self, context):
    
    scn = context.scene
        
    tmpdir = tempfile.gettempdir()
    abrir_diretorio(tmpdir)

def CorrigeDicomDef(self, context):

    scn = context.scene

    if scn.my_tool.path == "":
        bpy.ops.object.dialog_operator_informe_dicom('INVOKE_DEFAULT')
        return {'FINISHED'}

    else:

    #    scene = context.scene
    #    rd = scene.render
        
        os.chdir(scn.my_tool.path)
        os.makedirs("FIXED")
        if platform.system() == "Linux":
            os.system("dicomtodicom -o FIXED *")
    #        os.system("for i in *; do gdcmconv -X $i FIXED/$i; done")
    #        print("TOMO AJUSTADA PELO GDCM")

        if platform.system() == "Darwin":
            os.system("/OrtogOnBlender/vtk-dicom/./dicomtodicom --verbose -o FIXED *")
        print("DICOM FIXED")
	    
        if platform.system() == "Windows":
            os.system("C:\OrtogOnBlender\dicomtools\dicomtodicom --verbose -o FIXED *")
        print("DICOM FIXED")
	    
        scn.my_tool.path = os.getcwd()+"/FIXED/"

class CorrigeDicom(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.corrige_dicom"
    bl_label = "Corrige DICOM"

    def execute(self, context):
        CorrigeDicomDef(self, context)
        return {'FINISHED'}
