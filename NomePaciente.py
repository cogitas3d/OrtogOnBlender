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
            bpy.ops.wm.save_as_mainfile(filepath=homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/01_Base-"+NomePaciente+"_"+SobrenomePaciente+".blend")
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
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/02_CT_Scan-"+NomePaciente+"_"+SobrenomePaciente+".blend")

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

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/02_CT_Scan-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteTomoDef(self, context)
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
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/04_Arch-"+NomePaciente+"_"+SobrenomePaciente+".blend")

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

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/04_Arch-"+NomePaciente+"_"+SobrenomePaciente+".blend")

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
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/03_Ref-"+NomePaciente+"_"+SobrenomePaciente+".blend")

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

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/03_Ref-"+NomePaciente+"_"+SobrenomePaciente+".blend")

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
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/05_Seg-"+NomePaciente+"_"+SobrenomePaciente+".blend")

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

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/05_Seg-"+NomePaciente+"_"+SobrenomePaciente+".blend")

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
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/06_Photogram-"+NomePaciente+"_"+SobrenomePaciente+".blend")

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

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/06_Photogram-"+NomePaciente+"_"+SobrenomePaciente+".blend")

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
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/07_Align_Face-"+NomePaciente+"_"+SobrenomePaciente+".blend")

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

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/07_Align_Face-"+NomePaciente+"_"+SobrenomePaciente+".blend")

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
        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/08_Align_Photogram_CT-"+NomePaciente+"_"+SobrenomePaciente+".blend")

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

        NomePacienteFile = str(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/08_Align_Photogram_CT-"+NomePaciente+"_"+SobrenomePaciente+".blend")

#        if found == False:
        if not os.path.exists(NomePacienteFile):
            return True
        else:
            if os.path.exists(NomePacienteFile):
                return False


    def execute(self, context):
        NomePacienteAlinhaFotoTomoDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(NomePaciente)
bpy.utils.register_class(NomePacienteTomo)
bpy.utils.register_class(NomePacienteArc)
bpy.utils.register_class(NomePacienteRef)
bpy.utils.register_class(NomePacienteSeg)
bpy.utils.register_class(NomePacienteFotogram)
bpy.utils.register_class(NomePacienteAlinhaFace)
bpy.utils.register_class(NomePacienteAlinhaFotoTomo)
