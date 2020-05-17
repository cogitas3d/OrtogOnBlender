import bpy
import os
import os.path
import json
import re
import shutil
# from datetime import datetime
import tempfile
import os
import platform
import subprocess
import pydicom as dicom
import csv
import fnmatch
from os.path import expanduser

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
        try:
            shutil.rmtree(tmpdirCopy+'COPY')
            shutil.rmtree(tmpdirCopy)
        except:
            print("Erro de permissão ao apagar os diretório do TMP!")

        print("CT-SCAN ready!")

# Lista diretórios e arquivos
        try:
            tmpdirCSV = tempfile.mkdtemp()

            diretorio = tmpdirTomo+"/"

            lista_compara = []

            lista = [ name for name in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, name)) ]

            #print(lista)
            try:
                for i in lista:
                #    print("\n")
                #    print("Directory:", i)
                #    print(os.listdir(diretorio+i)[0])
                #    print("Number of files:", len(os.listdir(diretorio+i)))
                    ArquivoAtual = os.listdir(diretorio+i)[0]
                #    print(diretorio+i+"/"+ArquivoAtual)
                    ds = dicom.dcmread(diretorio+i+"/"+ArquivoAtual, force=True)

                    if ds.data_element("SeriesDescription"):
                        SeriesDescription = ds.data_element("SeriesDescription")
                        SeriesDescriptionLimpa1 = str(SeriesDescription).split('LO: ')
                        SeriesDescriptionLimpa2 = str(SeriesDescriptionLimpa1[1]).strip('"')
                    #    print(SeriesDescriptionLimpa2)
                    #    print("Directory:", i, "|| Number of files:", len(os.listdir(diretorio+i)), "||", SeriesDescriptionLimpa2, "\n")
                        lista_compara.append([len(os.listdir(diretorio+i)), i, SeriesDescriptionLimpa2])
                        lista_compara.sort(reverse = True)
                        #print("LISTA COMPARA!!!")
                        #print(lista_compara)
                    if not ds.data_element("SeriesDescription"):
                        SeriesDescriptionLimpa2 = ("Erro O!")
                    #    print(SeriesDescriptionLimpa2)
                    #    print("Directory:", i, "|| Number of files:", len(os.listdir(diretorio+i)), "||", SeriesDescriptionLimpa2, "\n")
                        lista_compara.append([len(os.listdir(diretorio+i)), i, SeriesDescriptionLimpa2])
                        lista_compara.sort(reverse = True)
            except:
                print("Erro no SeriesDescription")
                try:
                    SeriesDescriptionLimpa2 = ("Erro 1!")
                #    print(SeriesDescriptionLimpa2)
                #    print("Directory:", i, "|| Number of files:", len(os.listdir(diretorio+i)), "||", SeriesDescriptionLimpa2, "\n")
                    lista_compara.append([len(os.listdir(diretorio+i)), i, SeriesDescriptionLimpa2])
                    lista_compara.sort(reverse = True)
                except:
                    print("Problema ao inserir o SeriesDescription!")


            lista_diretorios_mole = []
            print("LISTA COMPARA MOLE", lista_compara)

            try:

                print("lista compara:",lista_compara)
                for i in lista_compara:
                    print("Comecou a comparar!")
                    print("i Atual:", i)
                    if fnmatch.fnmatchcase(str(i[2]), "*PM*") or fnmatch.fnmatchcase(str(i[2]), "*P/M*") or fnmatch.fnmatchcase(str(i[2]), "*Soft*") or fnmatch.fnmatchcase(str(i[2]), "*Sft Tissue*") or fnmatch.fnmatchcase(str(i[2]), "*STD*") or fnmatch.fnmatchcase(str(i[2]), "*PARTES MOLES*") or fnmatch.fnmatchcase(str(i[2]), "*Head*") or fnmatch.fnmatchcase(str(i[2]), "*SEM CONTRASTE*") or fnmatch.fnmatchcase(str(i[2]), "*FACE*") or fnmatch.fnmatchcase(str(i[2]), "*Recon 3*") or fnmatch.fnmatchcase(str(i[2]), "*ARQUIVO*") or fnmatch.fnmatchcase(str(i[2]), "*RECON*") or fnmatch.fnmatchcase(str(i[2]), "*Cranio*") or fnmatch.fnmatchcase(str(i[2]), "*VOLUME STD*")  or fnmatch.fnmatchcase(str(i[2]), "*VOL*") or fnmatch.fnmatchcase(str(i[2]), "*Imagens Processadas*"):
                            print("Encontrou!")
                            lista_diretorios_mole.append(i[1])
                    else:
                        print("Não encontrou!")

                    global diretorio_final_reconstruir_mole

                    try:
                        print("Diretorio final:", lista_diretorios_mole[0] )
                        print("Comparou!")

                        diretorio_final_reconstruir_mole = lista_diretorios_mole[0]

                    except:
                        print("Diretorio final:", lista_diretorios_mole ) # Não sei pq!!! Se coloco index dá erro!
                        print("Comparou!")

                        diretorio_final_reconstruir_mole = lista_diretorios_mole

            except:
                print("Problema para encontrar diretório com tecido mole na tomo!")



            with open(tmpdirCSV+'/C-Scan_DATA.csv', mode='w') as centroid_file:
                report_writer = csv.writer(centroid_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                report_writer.writerow(['DIRECTORY', 'NUMBER OF FILES', 'DESCRIPTION'])


                if lista_compara == []:
                    report_writer.writerow(["No data", "No data", "No data"])

                if lista_compara != []:
                    for linha in lista_compara:
                        report_writer.writerow([linha[1],linha[0],linha[2]])
                        print("Directory:", linha[1], "|| Number of files", linha[0], "|| Description:", linha[2])


            try:
                if platform.system() == "Linux":
                #    abrir_diretorio(tmpdir)
                    subprocess.Popen("libreoffice "+tmpdirCSV+"/C-Scan_DATA.csv", shell=True)

                if platform.system() == "Windows":
                #    abrir_diretorio(tmpdir)
                    subprocess.Popen('cd "C:/Program Files/LibreOffice/program/" & dir & soffice.bin '+tmpdirCSV+"/C-Scan_DATA.csv", shell=True)

                if platform.system() == "Darwin":
                #    abrir_diretorio(tmpdir)
                    subprocess.Popen('/Applications/LibreOffice.app/Contents/MacOS/soffice '+tmpdirCSV+"/C-Scan_DATA.csv", shell=True)
            except:
                print("Não há programa atribuído ao CSV!")
        except:
            print("Algum problema aconteceu com a leitura dos dados do tomógrafo.")


            try:

                with open(tmpdirCSV+'/C-Scan_DATA.csv', mode='w') as centroid_file:
                    report_writer = csv.writer(centroid_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    report_writer.writerow(['DIRECTORY', 'NUMBER OF FILES', 'DESCRIPTION'])

                    if lista_compara == []:
                        report_writer.writerow(["No data", "No data", "No data"])

                    if lista_compara != []:
                        for linha in lista_compara:
                            report_writer.writerow([linha[1],linha[0],linha[2]])
                            print("Directory:", linha[1], "|| Number of files", linha[0], "|| Description:", linha[2])

                try:
                    if platform.system() == "Linux":
                    #    abrir_diretorio(tmpdir)
                        subprocess.Popen("libreoffice "+tmpdirCSV+"/C-Scan_DATA.csv", shell=True)

                    if platform.system() == "Windows":
                    #    abrir_diretorio(tmpdir)
                        subprocess.Popen('cd "C:/Program Files/LibreOffice/program/" & dir & soffice.bin '+tmpdirCSV+"/C-Scan_DATA.csv", shell=True)

                    if platform.system() == "Darwin":
                    #    abrir_diretorio(tmpdir)
                        subprocess.Popen('/Applications/LibreOffice.app/Contents/MacOS/soffice '+tmpdirCSV+"/C-Scan_DATA.csv", shell=True)
                except:
                    print("Não há programa atribuído ao CSV!")
            except:
                print("Problemas com o CSV!")

# Atualiza path

#        abrir_diretorio(tmpdirTomo)

        scn.my_tool.path = tmpdirTomo+"/"


        try:
            with open(tmpdirTomo+'/AUTOEXPDIR.txt', "a") as arq:
                if diretorio_final_reconstruir_mole:
                    arq.write(tmpdirTomo+"/"+diretorio_final_reconstruir_mole)
                if not diretorio_final_reconstruir_mole:
                    arq.write(tmpdirTomo+"/")
                arq.close()

        except:
            print("Algum problema com a variável global do tecido mole!")


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

    homeall = expanduser("~")

    if scn.my_tool.path == "":
        bpy.ops.object.dialog_operator_informe_dicom('INVOKE_DEFAULT')
        return {'FINISHED'}

    else:

    #    scene = context.scene
    #    rd = scene.render

        tmpdirFIXED = tempfile.mkdtemp()

        # Cria arquivo com o nome do diretorio FIXED para ser acessado

        DirTemporario = tempfile.gettempdir()

        if os.path.isfile(DirTemporario+"/tmpdirFIXED.txt"):
            print("Apagando tmpdirFIXED.txt!")
            os.remove(DirTemporario+"/tmpdirFIXED.txt")

        if not os.path.isfile(DirTemporario+"/tmpdirFIXED.txt"):
            with open(DirTemporario+"/tmpdirFIXED.txt", 'w') as arquivo:
                arquivo.write(str(tmpdirFIXED))


        print("DIRETÓRIO CORREÇÂO:", tmpdirFIXED)

        os.chdir(scn.my_tool.path)
        dirDICOM = scn.my_tool.path
        #os.makedirs("FIXED")
        if platform.system() == "Linux":
            os.system("dicomtodicom -o "+tmpdirFIXED+" *")
    #        os.system("for i in *; do gdcmconv -X $i FIXED/$i; done")
    #        print("TOMO AJUSTADA PELO GDCM")

        if platform.system() == "Darwin":
            os.system(homeall+"/Programs/OrtogOnBlender/vtk-dicom/./dicomtodicom --verbose -o "+tmpdirFIXED+" *")
        print("DICOM FIXED")


        if platform.system() == "Windows":


            os.chdir(scn.my_tool.path)
            os.system("C:\\OrtogOnBlender\\dicomtools\\dicomtodicom --verbose -o "+tmpdirFIXED+" *")

            print("C:\\OrtogOnBlender\\dicomtools\\dicomtodicom --verbose -o "+tmpdirFIXED+" *")

            a = os.path.isfile(tmpdirFIXED+"\\"+"IM-0001-0001.dcm")
            print("teste", a)
            print("Diretorio FIXED: ", tmpdirFIXED+"\\"+"IM-0001-0001.dcm")

            #print("DICOM FIXED")
            if os.path.isfile(tmpdirFIXED+"\\"+"IM-0001-0001.dcm"):
                print("EXISTE O ARQUIVO EM FIXED!")
                scn.my_tool.path = tmpdirFIXED

                return tmpdirFIXED

            if not os.path.isfile(tmpdirFIXED+"\\"+"IM-0001-0001.dcm"):
                tmpdirFIXED2 = tempfile.mkdtemp()
                print("TENTA WSL FIXED!!!")
                tmpdirFIXEDAtual = str(tmpdirFIXED2).replace("\\", "/").replace('\\', "/").replace("C:", "/mnt/c")
                #dirDICOMAtual = str(dirDICOM).replace("\\", "/").replace('\\', "/").replace("C:", "/mnt/c")

                os.chdir(dirDICOM)
                #print("wsl \"dicomtodicom\" -o \""+tmpdirFIXEDAtual+"\" \""+dirDICOMAtual+"\"")
                #print("wsl \"dicomtodicom\" -o \""+tmpdirFIXEDAtual+"\" *")

                #subprocess.call("wsl \"dicomtodicom\" -o \""+tmpdirFIXEDAtual+"\" \""+dirDICOMAtual+"\"", shell=True)
                subprocess.call("wsl \"dicomtodicom\" -o \""+tmpdirFIXEDAtual+"\" *", shell=True)

                scn.my_tool.path = tmpdirFIXED2


class CorrigeDicom(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.corrige_dicom"
    bl_label = "Corrige DICOM"

    def execute(self, context):
        CorrigeDicomDef(self, context)
        return {'FINISHED'}
