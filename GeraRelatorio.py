import bpy
import csv
import tempfile
import subprocess
import openpyxl
import platform
from string import ascii_uppercase
from openpyxl import Workbook
from openpyxl.styles import Font, Fill
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment

from .CalculaPontos import *
from .AjustaTomo import *
from .Cefalometria import *


def DeslocamentoINIFIN(obj, obj1, obj2):
    objini = bpy.data.objects[obj1]
    objfin = bpy.data.objects[obj2]
    

#    if bpy.data.objects.get(obj) is not None:
    Xdes = str(round(objfin.location[0] - objini.location[0], 2))
    Ydes = str(round(objfin.location[1] - objini.location[1], 2))
    Zdes = str(round(objfin.location[2] - objini.location[2], 2))


    a = [obj, str(Xdes), str(Ydes), str(Zdes)]

    return a


def CapturaCefaloINI():    
    print("Nada")


#    global SNA_INI, SNB_INI, ANB_INI, Y_Cresc_INI, Y_Cresc_INI, SNPlO_INI, FMA_INI, FMIA_INI, IMPA_INI, NS_INI

#    bpy.ops.object.cefalo_calc_tudo()

#    SNA_INI = bpy.types.Scene.angulo_SNA[1]['default']
#    SNB_INI = bpy.types.Scene.angulo_SNB[1]['default']
#    ANB_INI = bpy.types.Scene.angulo_ANB[1]['default']
#    Y_Cresc_INI = bpy.types.Scene.angulo_Y_Cresc[1]['default']
#    SNPlO_INI = bpy.types.Scene.angulo_SNPlO[1]['default'] 
#    FMA_INI = bpy.types.Scene.angulo_FMA[1]['default']
#    FMIA_INI = bpy.types.Scene.angulo_FMIA[1]['default']
#    IMPA_INI = bpy.types.Scene.angulo_IMPA[1]['default']
#    NS_INI = bpy.types.Scene.angulo_NS[1]['default']

def CapturaCefaloFIN():    
    print("Nada")
#    global SNA_FIN, SNB_FIN, ANB_FIN, Y_Cresc_FIN, Y_Cresc_FIN, SNPlO_FIN, FMA_FIN, FMIA_FIN, IMPA_FIN, NS_FIN

#    bpy.ops.object.cefalo_calc_tudo()

#    SNA_FIN = bpy.types.Scene.angulo_SNA[1]['default']
#    SNB_FIN = bpy.types.Scene.angulo_SNB[1]['default']
#    ANB_FIN = bpy.types.Scene.angulo_ANB[1]['default']
#    Y_Cresc_FIN = bpy.types.Scene.angulo_Y_Cresc[1]['default']
#    SNPlO_FIN = bpy.types.Scene.angulo_SNPlO[1]['default']
#    FMA_FIN = bpy.types.Scene.angulo_FMA[1]['default']
#    FMIA_FIN = bpy.types.Scene.angulo_FMIA[1]['default']
#    IMPA_FIN = bpy.types.Scene.angulo_IMPA[1]['default']
#    NS_FIN = bpy.types.Scene.angulo_NS[1]['default']

def GeraRelatorioDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    # CAPTURA FRAME INICIAL

    frame1 = bpy.data.scenes["Scene"].frame_start

    obj_pre(frame1)
    CapturaCefaloINI()


    # CAPTURA FRAME INICIAL

    frame2 = bpy.data.scenes["Scene"].frame_end

    obj_pos(frame2)
    CapturaCefaloFIN()


    # Gera CSV
    tmpdir = tempfile.mkdtemp()

    with open(tmpdir+'/Report_OrtogOnBlender.csv', mode='w') as centroid_file:
        report_writer = csv.writer(centroid_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        report_writer.writerow(['ORTOGONBLENDER'])
        report_writer.writerow([''])

        report_writer.writerow(['MAXILLA'])
        report_writer.writerow(['ID', 'LocX', 'LocY', 'LocZ'])


        

        report_writer.writerow(DeslocamentoINIFIN('Teeth 8 (11)','EMP11.INI', 'EMP11.FIN'))

        '''
        report_writer.writerow(DeslocamentoINIFIN('Teeth 9 (21) : ', 'EMP21.INI', 'EMP21.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Teeth 6 (13) : ', 'EMP13.INI', 'EMP13.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Teeth 11 (23) :', 'EMP16.INI', 'EMP16.FIN'))   
        report_writer.writerow(DeslocamentoINIFIN('Teeth 3 (16) : ', 'EMP26.INI', 'EMP26.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Palatine :     ', 'EMPPalatine.INI', 'EMPPalatine.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('A Point :      ', 'EMPApoint.INI', 'EMPApoint.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Nasal Spine :  ', 'EMPNasalSpine.INI', 'EMPNasalSpine.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Pterygoid (L) :', 'EMPPterygoidL.INI', 'EMPPterygoidL.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Pterygoid (R) :', 'EMPPterygoidR.INI', 'EMPPterygoidR.FIN'))
        report_writer.writerow([''])
        report_writer.writerow(['MANDIBLE BODY'])
        report_writer.writerow(['ID', 'LocX', 'LocY', 'LocZ'])
        report_writer.writerow(DeslocamentoINIFIN('Teeth 24 (31) :', 'EMP31.INI', 'EMP31.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Teeth 25 (41) :', 'EMP41.INI', 'EMP41.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Teeth 22 (33) :', 'EMP33.INI', 'EMP33.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Teeth 27 (43) :', 'EMP43.INI', 'EMP43.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Teeth 19 (36) :', 'EMP36.INI', 'EMP36.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Teeth 30 (46) :', 'EMP46.INI', 'EMP46.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('B Point or Up: ', 'EMPBpoint.INI', 'EMPBpoint.FIN'))
        report_writer.writerow([''])
        report_writer.writerow(['CHIN'])
        report_writer.writerow(['ID', 'LocX', 'LocY', 'LocZ'])
        report_writer.writerow(DeslocamentoINIFIN('Pogonion:      ', 'EMPPogonion.INI', 'EMPPogonion.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Menton:        ', 'EMPMenton.INI', 'EMPMenton.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Menton (L):    ', 'EMPMentonL.INI', 'EMPMentonL.FIN'))
        report_writer.writerow(DeslocamentoINIFIN('Menton (R) :   ', 'EMPMentonR.INI', 'EMPMentonR.FIN'))
        report_writer.writerow([''])
        report_writer.writerow([''])
        report_writer.writerow(['CEFALOMETRY'])
        report_writer.writerow(['ID', 'PRE', 'POST', 'RANGE'])
        report_writer.writerow(['SNA', str(SNA_INI), str(SNA_FIN), '80º - 84º'])
        report_writer.writerow(['SNB', str(SNB_INI), str(SNB_FIN), '78º - 82º'])
        report_writer.writerow(['ANB', str(ANB_INI), str(ANB_FIN), '0º - 4º'])
        report_writer.writerow(['Y_Cresc', str(Y_Cresc_INI), str(Y_Cresc_FIN), '65º - 69º'])
        report_writer.writerow(['SNPlO', str(SNPlO_INI), str(SNPlO_FIN), '12º - 16º'])
        report_writer.writerow(['FMA', str(FMA_INI), str(FMA_FIN), '23º - 27º'])
        report_writer.writerow(['FMIA', str(FMIA_INI), str(FMIA_FIN), '66º - 70º'])
        report_writer.writerow(['IMPA', str(IMPA_INI), str(IMPA_FIN), '85º - 89º'])
        report_writer.writerow(['1NS', str(NS_INI), str(NS_FIN), '101º - 105º'])
	    '''

#        subprocess.Popen("libreoffice "+tmpdir+"/Report_OrtogOnBlender.csv", shell=True)

    # Converte em XLSX
    wb = Workbook()
    ws = wb.active
    with open(tmpdir+'/Report_OrtogOnBlender.csv', 'r') as f:
        for row in csv.reader(f):
            ws.append(row)
    wb.save(tmpdir+'/Report_OrtogOnBlender.xlsx')

# AJUSTA OS TAMANHOS DAS CÉLULAS (AUTOFIT)

    newFile = tmpdir+'/Report_OrtogOnBlender.xlsx'

    wb = openpyxl.load_workbook(filename = newFile)        
    worksheet = wb.active

    for col in worksheet.columns:
         max_length = 0
         column = col[0].column # Get the column name
         for cell in col:
             try: # Necessary to avoid error on empty cells
                 if len(str(cell.value)) > max_length:
                     max_length = len(cell.value)
             except:
                 pass
         adjusted_width = (max_length + 2) * 1.2
         worksheet.column_dimensions[column].width = adjusted_width

#    wb.save(newFile)

    # STYLE

    listaFontes1 = ['A1','A3','A16','A26','A34']

    for i in listaFontes1:
        c = worksheet[i]
#        c.font = Font(bold=True, name='Arial')
        c.font = Font(bold=True, name="Calibri")


    ListaCor1 = ['A3','B3','C3','D3','A16','B16','C16','D16','A26','B26','C26','D26','A34','B34','C34','D34']

    for i in ListaCor1:
        d = worksheet[i]
        d.fill = PatternFill("solid", fgColor="b1e2e2")

    ListaCor2 = ['A4','B4','C4','D4','A17','B17','C17','D17','A27','B27','C27','D27','A35','B35','C35','D35']

    for i in ListaCor2:
        d = worksheet[i]
        d.fill = PatternFill("solid", fgColor="fff9ae")

    wb.save(newFile)


    if platform.system() == "Linux":
        subprocess.Popen("libreoffice "+tmpdir+"/Report_OrtogOnBlender.xlsx", shell=True)

    if platform.system() == "Windows":
        abrir_diretorio(tmpdir)
        subprocess.Popen('cd "C:/Program Files/LibreOffice/program/" & dir & soffice.bin '+tmpdir+"/Report_OrtogOnBlender.xlsx", shell=True)
        
    if platform.system() == "Darwin":
        abrir_diretorio(tmpdir)
        subprocess.Popen('/Applications/LibreOffice.app/Contents/MacOS/soffice '+tmpdir+"/Report_OrtogOnBlender.xlsx", shell=True)    
    

		# APAGANDO

    apagaObjeto('EMP11.INI')
    apagaObjeto('EMP11.FIN')
    apagaObjeto('EMP21.INI')
    apagaObjeto('EMP21.FIN')
    apagaObjeto('EMP13.INI')
    apagaObjeto('EMP13.FIN')
    apagaObjeto('EMP23.INI')
    apagaObjeto('EMP23.FIN')
    apagaObjeto('EMP16.INI')
    apagaObjeto('EMP16.FIN')
    apagaObjeto('EMP26.INI')
    apagaObjeto('EMP26.FIN')
    apagaObjeto('EMPPalatine.INI')
    apagaObjeto('EMPPalatine.FIN')
    apagaObjeto('EMPApoint.INI')
    apagaObjeto('EMPApoint.FIN')
    apagaObjeto('EMPNasalSpine.INI')
    apagaObjeto('EMPNasalSpine.FIN')
    apagaObjeto('EMPPterygoidL.INI')
    apagaObjeto('EMPPterygoidR.FIN')
    apagaObjeto('EMP31.INI')
    apagaObjeto('EMP31.FIN')
    apagaObjeto('EMP41.INI')
    apagaObjeto('EMP41.FIN')
    apagaObjeto('EMP33.INI')
    apagaObjeto('EMP33.FIN')
    apagaObjeto('EMP43.INI')
    apagaObjeto('EMP43.FIN')
    apagaObjeto('EMP36.INI')
    apagaObjeto('EMP36.FIN')
    apagaObjeto('EMP46.INI')
    apagaObjeto('EMP46.FIN')
    apagaObjeto('EMPBpoint.INI')
    apagaObjeto('EMPBpoint.FIN')
    apagaObjeto('EMPPogonion.INI')
    apagaObjeto('EMPPogonion.FIN')
    apagaObjeto('EMPMenton.INI')
    apagaObjeto('EMPMenton.FIN')
    apagaObjeto('EMPMentonL.INI')
    apagaObjeto('EMPMentonL.FIN')
    apagaObjeto('EMPMentonR.INI')
    apagaObjeto('EMPMentonR.FIN')

class GeraRelatorio(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_relatorio"
    bl_label = "Gera deslocamento de todos"

    def execute(self, context):
        GeraRelatorioDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(GeraRelatorio)
