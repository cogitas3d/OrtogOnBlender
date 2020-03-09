import bpy
from os.path import expanduser
import os

# MENSAGENS

class PatientName(bpy.types.Operator):
    bl_idname = "object.dialog_operator_patient_name"
    bl_label = "Please, write the patient's name and surname to save!"


    def execute(self, context):
        message = ("Teste")
        self.report({'INFO'}, message)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

bpy.utils.register_class(PatientName)



# CRIA DIRETÓRIO E SALVA ARQUIVO INICIAL

def NomePacienteDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    NomePacienteDir = homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente

    if NomePaciente != "" and SobrenomePaciente != "":

        if not os.path.exists(homeDir+"/OrtogOnBlenderDir"):
            os.mkdir(homeDir+"/OrtogOnBlenderDir")
            print("Diretorio OrtogOnBlender criado")

        if not os.path.exists(NomePacienteDir):
            os.mkdir(NomePacienteDir)
            bpy.ops.wm.save_as_mainfile(filepath=homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Base-"+NomePaciente+"_"+SobrenomePaciente+".blend")
            print("Diretorio "+NomePaciente+"_"+SobrenomePaciente+" criado!")

    else:
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

class NomePaciente(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente"
    bl_label = "Gera Nome Dir Nome Paciente"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteDir = homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente

#        if found == False:
        if not os.path.exists(NomePacienteDir):
            return True
        else:
            if os.path.exists(NomePacienteDir):
                return False

    def execute(self, context):
        NomePacienteDef(self, context)
        return {'FINISHED'}

# SALVA ARQUIVO TOMOGRAFIA

def NomePacienteVoxelDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Voxel-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacienteVoxel(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_voxel"
    bl_label = "Gera Nome Dir Nome Paciente Voxel"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Voxel-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        bpy.ops.file.pack_all()
        NomePacienteVoxelDef(self, context)
        return {'FINISHED'}


bpy.utils.register_class(NomePacienteVoxel)

# SALVA ARQUIVO TOMOGRAFIA

def NomePacienteTomoDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/CT_Scan-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacienteTomo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_tomo"
    bl_label = "Gera Nome Dir Nome Paciente Tomo"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/CT_Scan-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteTomoDef(self, context)
        return {'FINISHED'}

# SALVA ARQUIVO TOMOGRAFIA AUTO

def NomePacienteTomoAutoDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/CT_Scan_Auto-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacienteTomoAuto(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_tomo_auto"
    bl_label = "Gera Nome Dir Nome Paciente Tomo AUto"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/CT_Scan_Auto-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteTomoAutoDef(self, context)
        return {'FINISHED'}

# SALVA ARQUIVO MOLDES

def NomePacienteArcDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Arch-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo com os arcos criado!")

class NomePacienteArc(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_arc"
    bl_label = "Gera Nome Dir Nome Paciente Tomo"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Arch-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteArcDef(self, context)
        return {'FINISHED'}

# REFERENCIAS

def NomePacienteRefDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Ref-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo com os arcos criado!")

class NomePacienteRef(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_ref"
    bl_label = "Gera Nome Dir Nome Paciente Ref"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Ref-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteRefDef(self, context)
        return {'FINISHED'}

# SEGMENTAÇÃO

def NomePacienteSegDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Seg-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo com os arcos criado!")

class NomePacienteSeg(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_seg"
    bl_label = "Gera Nome Dir Nome Paciente Seg"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Seg-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteSegDef(self, context)
        return {'FINISHED'}

# FOTOGRAMETRIA

def NomePacienteFotogramDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Photogram-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo com os arcos criado!")

class NomePacienteFotogram(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_fotogram"
    bl_label = "Gera Nome Dir Nome Paciente Fotogram"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Photogram-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteFotogramDef(self, context)
        return {'FINISHED'}

# ALINHAMENTO

def NomePacienteAlinhaFaceDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Align_Face-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo com os arcos criado!")

class NomePacienteAlinhaFace(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_alinha_face"
    bl_label = "Gera Nome Dir Nome Paciente Alinha Face"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Align_Face-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteAlinhaFaceDef(self, context)
        return {'FINISHED'}

# ALINHAMENTO FOTO TOMO

def NomePacienteAlinhaFotoTomoDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Align_Photogram_CT-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo com os arcos criado!")

class NomePacienteAlinhaFotoTomo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_alinha_foto_tomo"
    bl_label = "Gera Nome Dir Nome Paciente Alinha Fotogram Tomo"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Align_Photogram_CT-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteAlinhaFotoTomoDef(self, context)
        return {'FINISHED'}

# PONTOS CABEÇA

def NomePacientePointsHeadDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Points_Head-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacientePointsHead(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_points_head"
    bl_label = "Gera Nome Dir Nome Paciente Voxel"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Points_Head-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacientePointsHeadDef(self, context)
        return {'FINISHED'}


bpy.utils.register_class(NomePacientePointsHead)

# PONTOS MAXILA

def NomePacientePointsMaxillaDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Points_Maxilla-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacientePointsMaxilla(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_points_maxilla"
    bl_label = "Gera Nome Dir Nome Paciente Maxilla"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Points_Maxilla-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacientePointsMaxillaDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(NomePacientePointsMaxilla)

# PONTOS MANDÍBULA

def NomePacientePointsMandibleDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Points_Mandible-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacientePointsMandible(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_points_mandible"
    bl_label = "Gera Nome Dir Nome Paciente Mandible"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Points_Mandible-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacientePointsMandibleDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(NomePacientePointsMandible)

# PONTOS DENTES

def NomePacientePointsTeethDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Points_Teeth-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacientePointsTeeth(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_points_teeth"
    bl_label = "Gera Nome Dir Nome Paciente Teeth"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Points_Teeth-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacientePointsTeethDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(NomePacientePointsTeeth)

# PONTOS TECIDO MOLE

def NomePacientePointsSoftDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Points_Soft-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacientePointsSoft(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_points_soft"
    bl_label = "Gera Nome Dir Nome Paciente Soft"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Points_Soft-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacientePointsSoftDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(NomePacientePointsSoft)

# PONTOS OSTEOTOMIA

def NomePacienteOsteotomyDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Osteotomy-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacienteOsteotomy(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_osteotomy"
    bl_label = "Gera Nome Dir Nome Paciente Osteotomy"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Osteotomy-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteOsteotomyDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(NomePacienteOsteotomy)

# DINÂMICA

def NomePacienteDynamicDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Dynamic-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacienteDynamic(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_dynamic"
    bl_label = "Gera Nome Dir Nome Paciente Dynamic"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Dynamic-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteDynamicDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(NomePacienteDynamic)

# CINEMÁTICA

def NomePacienteKinematicDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Kinematic-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacienteKinematic(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_kinematic"
    bl_label = "Gera Nome Dir Nome Paciente Kinematic"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Kinematic-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteKinematicDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(NomePacienteKinematic)


# GUIA E SPLINT

def NomePacienteGuideDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Guide-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacienteGuide(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_guide"
    bl_label = "Gera Nome Dir Nome Paciente Guide"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Guide-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteGuideDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(NomePacienteGuide)


def NomePacienteMarkersDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Markers-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacienteMarkers(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_markers"
    bl_label = "Gera Nome Dir Nome Paciente Markers"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Markers-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteMarkersDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(NomePacienteMarkers)


def NomePacienteMusclesDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Muscles-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacienteMuscles(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_muscles"
    bl_label = "Gera Nome Dir Nome Paciente Muscles"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Muscles-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteMusclesDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(NomePacienteMuscles)



def NomePacienteSculptDef(self, context):


    context = bpy.context
    obj = context.object
    scn = context.scene


#    scene = context.scene
#    rd = scene.render

    homeDir = expanduser("~")

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    if NomePaciente == "" and SobrenomePaciente == "":
        bpy.ops.object.dialog_operator_patient_name('INVOKE_DEFAULT')

    else:
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Sculpt-"+NomePaciente+"_"+SobrenomePaciente+".blend")

        if not os.path.exists(NomePacienteFile):
            bpy.ops.wm.save_as_mainfile(filepath=NomePacienteFile)
            print("Arquivo da tomografia criado!")


class NomePacienteSculpt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_dir_nome_paciente_sculpt"
    bl_label = "Gera Nome Dir Nome Paciente Sculpt"

    @classmethod
    def poll(cls, context):

#        found = 'Orbital right' in bpy.data.objects
        context = bpy.context
        obj = context.object
        scn = context.scene


    #    scene = context.scene
    #    rd = scene.render

        homeDir = expanduser("~")

        NomePaciente = bpy.context.scene.nome_paciente
        SobrenomePaciente = bpy.context.scene.sobrenome_paciente

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Sculpt-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteSculptDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(NomePacienteSculpt)


bpy.utils.register_class(NomePaciente)
bpy.utils.register_class(NomePacienteTomo)
bpy.utils.register_class(NomePacienteTomoAuto)
bpy.utils.register_class(NomePacienteArc)
bpy.utils.register_class(NomePacienteRef)
bpy.utils.register_class(NomePacienteSeg)
bpy.utils.register_class(NomePacienteFotogram)
bpy.utils.register_class(NomePacienteAlinhaFace)
bpy.utils.register_class(NomePacienteAlinhaFotoTomo)
