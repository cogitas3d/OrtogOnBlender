import bpy
from .Cefalometria import *
from .GeraRelatorio import *
from .PontosAnatomicos import *
from .FerrMedidas import *
from .FerrImgTomo import * # Importa tratamento de materiais
from math import sqrt
import csv
import bmesh
from mathutils import Matrix, Vector
from time import gmtime, strftime

# PONTOS ANATOMICOS

class  Pronasale_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pronasale_digi_pt"
    bl_label = " Pronasale digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Pronasale digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Pronasale digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Pronasale_digi_pt)

class  Exocanthus_Alar_Base_right_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.exocanthus_alar_base_right_digi_pt"
    bl_label = "Exocanthus-Alar Base right digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Exocanthus-Alar Base right digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Exocanthus-Alar Base right digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Exocanthus_Alar_Base_right_digi_pt)

class  Exocanthus_Alar_Base_left_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.exocanthus_alar_base_left_digi_pt"
    bl_label = "Exocanthus-Alar Base left digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Exocanthus-Alar Base left digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Exocanthus-Alar Base left digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Exocanthus_Alar_Base_left_digi_pt)

class  Cheek_right_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cheek_right_digi_pt"
    bl_label = "Cheek right digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Cheek right digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Cheek right digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Cheek_right_digi_pt)

class  Cheek_left_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cheek_left_digi_pt"
    bl_label = "Cheek left digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Cheek left digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Cheek left digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Cheek_left_digi_pt)

class  Alar_Base_right_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.alar_base_right_digi_pt"
    bl_label = "Alar Base right digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Alar Base right digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Alar Base right digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Alar_Base_right_digi_pt)

class  Alar_Base_left_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.alar_base_left_digi_pt"
    bl_label = "Alar Base left digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Alar Base left digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Alar Base left digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Alar_Base_left_digi_pt)

class  Subnasale_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.subnasale_digi_pt"
    bl_label = "Subnasale digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Subnasale digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Subnasale digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class( Subnasale_digi_pt)

class  Cheilion_Alar_Base_right_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cheilion_alar_base_right_digi_pt"
    bl_label = "Cheilion-Alar Base right digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Cheilion-Alar Base right digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Cheilion-Alar Base right digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Cheilion_Alar_Base_right_digi_pt)

class  Cheilion_Alar_Base_left_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cheilion_alar_base_left_digi_pt"
    bl_label = "Cheilion-Alar Base left digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Cheilion-Alar Base left digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Cheilion-Alar Base left digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Cheilion_Alar_Base_left_digi_pt)

class  Cupids_Bow_right_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cupids_bow_right_digi_pt"
    bl_label = "Cupid's Bow right digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Cupid\'s Bow right digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Cupid\'s Bow right digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Cupids_Bow_right_digi_pt)

class  Cupids_Bow_left_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cupids_bow_left_digi_pt"
    bl_label = "Cupid's Bow left digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Cupid\'s Bow left digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Cupid\'s Bow left digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Cupids_Bow_left_digi_pt)

class  Cheilion_right_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cheilion_right_digi_pt"
    bl_label = "Cheilion right digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Cheilion right digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Cheilion right digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Cheilion_right_digi_pt)

class  Cheilion_left_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cheilion_left_digi_pt"
    bl_label = "Cheilion left digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Cheilion left digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Cheilion left digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Cheilion_left_digi_pt)

class Lower_Lip_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.lower_lip_digi_pt"
    bl_label = "Lower Lip digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Lower Lip digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Lower Lip digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Lower_Lip_digi_pt)

class B_point_soft_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.b_point_soft_digi_pt"
    bl_label = "B point soft digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'B point soft digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('B point soft digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(B_point_soft_digi_pt)

class Pogonion_soft_digi_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pogonion_soft_digi_pt"
    bl_label = "Pogonion soft digi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Pogonion soft digi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Pogonion soft digi', 'Anatomical Points - Digital')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Pogonion_soft_digi_pt)

# Real

class  Pronasale_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.pronasale_real_pt"
   bl_label = " Pronasale real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Pronasale real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Pronasale real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Pronasale_real_pt)

class  Exocanthus_Alar_Base_right_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.exocanthus_alar_base_right_real_pt"
   bl_label = "Exocanthus-Alar Base right real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Exocanthus-Alar Base right real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Exocanthus-Alar Base right real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Exocanthus_Alar_Base_right_real_pt)

class  Exocanthus_Alar_Base_left_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.exocanthus_alar_base_left_real_pt"
   bl_label = "Exocanthus-Alar Base left real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Exocanthus-Alar Base left real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Exocanthus-Alar Base left real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Exocanthus_Alar_Base_left_real_pt)

class  Cheek_right_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.cheek_right_real_pt"
   bl_label = "Cheek right real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Cheek right real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Cheek right real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Cheek_right_real_pt)

class  Cheek_left_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.cheek_left_real_pt"
   bl_label = "Cheek left real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Cheek left real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Cheek left real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Cheek_left_real_pt)

class  Alar_Base_right_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.alar_base_right_real_pt"
   bl_label = "Alar Base right real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Alar Base right real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Alar Base right real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Alar_Base_right_real_pt)

class  Alar_Base_left_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.alar_base_left_real_pt"
   bl_label = "Alar Base left real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Alar Base left real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Alar Base left real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Alar_Base_left_real_pt)

class  Subnasale_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.subnasale_real_pt"
   bl_label = "Subnasale real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Subnasale real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Subnasale real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class( Subnasale_real_pt)

class  Cheilion_Alar_Base_right_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.cheilion_alar_base_right_real_pt"
   bl_label = "Cheilion-Alar Base right real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Cheilion-Alar Base right real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Cheilion-Alar Base right real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Cheilion_Alar_Base_right_real_pt)

class  Cheilion_Alar_Base_left_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.cheilion_alar_base_left_real_pt"
   bl_label = "Cheilion-Alar Base left real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Cheilion-Alar Base left real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Cheilion-Alar Base left real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Cheilion_Alar_Base_left_real_pt)

class  Cupids_Bow_right_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.cupids_bow_right_real_pt"
   bl_label = "Cupid's Bow right real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Cupid\'s Bow right real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Cupid\'s Bow right real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Cupids_Bow_right_real_pt)

class  Cupids_Bow_left_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.cupids_bow_left_real_pt"
   bl_label = "Cupid's Bow left real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Cupid\'s Bow left real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Cupid\'s Bow left real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Cupids_Bow_left_real_pt)

class  Cheilion_right_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.cheilion_right_real_pt"
   bl_label = "Cheilion right real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Cheilion right real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Cheilion right real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Cheilion_right_real_pt)

class  Cheilion_left_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.cheilion_left_real_pt"
   bl_label = "Cheilion left real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Cheilion left real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Cheilion left real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Cheilion_left_real_pt)

class Lower_Lip_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.lower_lip_real_pt"
   bl_label = "Lower Lip real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Lower Lip real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Lower Lip real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Lower_Lip_real_pt)

class B_point_soft_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.b_point_soft_real_pt"
   bl_label = "B point soft real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'B point soft real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('B point soft real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(B_point_soft_real_pt)

class Pogonion_soft_real_pt(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.pogonion_soft_real_pt"
   bl_label = "Pogonion soft real"
   bl_options = {'REGISTER', 'UNDO'}

   @classmethod
   def poll(cls, context):

       found = 'Pogonion soft real' in bpy.data.objects

       if found == False:
           return True
       else:
           if found == True:
               return False

   def execute(self, context):
       CriaPontoDef('Pogonion soft real', 'Anatomical Points - Real')
       TestaPontoCollDef()
       return {'FINISHED'}

bpy.utils.register_class(Pogonion_soft_real_pt)

def GeraPlanilha():

    tmpdir = tempfile.mkdtemp()

    ListaApagar = []

    with open(tmpdir+'/Report_CompareOnBlender.csv', mode='w') as centroid_file:
        report_writer = csv.writer(centroid_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        report_writer.writerow(['CompareOnBlender'])
        report_writer.writerow([''])
        report_writer.writerow(['Point Number', 'Point Name', 'Distance'])
        report_writer.writerow([''])
        report_writer.writerow(['1', 'Pronasale (Pn)', CalculaDistanciaObjetos("Pronasale digi", "Pronasale real")])
        report_writer.writerow(['2', 'Rigth Exocanthus-Alar Base (Rt.Exo-Al)', CalculaDistanciaObjetos("Exocanthus-Alar Base right digi", "Exocanthus-Alar Base right real")])
        report_writer.writerow(['3', 'Rigth Cheek (Rt.Ck)', CalculaDistanciaObjetos("Cheek right digi", "Cheek right real")])
        report_writer.writerow(['4', 'Rigth Alar Base (Rt.Al)', CalculaDistanciaObjetos("Alar Base right digi", "Alar Base right real")])
        report_writer.writerow(['5', 'Subnasale (Sn)', CalculaDistanciaObjetos("Subnasale digi", "Subnasale real")])
        report_writer.writerow(['6', 'Left Alar Base (Lt.Al)', CalculaDistanciaObjetos("Alar Base left digi", "Alar Base left real")])
        report_writer.writerow(['7', 'Left Cheek (Ir.Ck)', CalculaDistanciaObjetos("Cheek left digi", "Cheek left real")])
        report_writer.writerow(['8', 'Left Exocanthus-Alar Base (Lt.Exo-Al)', CalculaDistanciaObjetos("Exocanthus-Alar Base left digi", "Exocanthus-Alar Base left real")])
        report_writer.writerow(['9', 'Rigth Cheilion-Alar Base (Rt.Ch-Al)', CalculaDistanciaObjetos("Cheilion-Alar Base right digi", "Cheilion-Alar Base right real")])
        report_writer.writerow(['10', 'Rigth Cupid\'s Bow (Rt.Cu)', CalculaDistanciaObjetos("Cupid's Bow right digi", "Cupid's Bow right real")])
        report_writer.writerow(['11', 'Left Cupid\'s Bow (Lt.Cu)', CalculaDistanciaObjetos("Cupid's Bow left digi", "Cupid's Bow left real")])
        report_writer.writerow(['12', 'Left Cheilion-Alar Base (Lt.Ch-Al)', CalculaDistanciaObjetos("Cheilion-Alar Base left digi", "Cheilion-Alar Base left real")])
        report_writer.writerow(['13', 'Rigth Cheilion (Rt.Ch)', CalculaDistanciaObjetos("Cheilion right digi", "Cheilion right real")])
        report_writer.writerow(['14', 'Left Cheilion (Lt.Ch)', CalculaDistanciaObjetos("Cheilion left digi", "Cheilion left real")])
        report_writer.writerow(['15', 'Lower Lip (LL)', CalculaDistanciaObjetos("Lower Lip digi", "Lower Lip real")])
        report_writer.writerow(['16', 'Soft  Tissue B Point (B\')', CalculaDistanciaObjetos("B point soft digi", "B point soft real")])
        report_writer.writerow(['17', 'Soft Tissue Pogonion (Pog\')', CalculaDistanciaObjetos("Pogonion soft digi", "Pogonion soft real")])

        Media = (CalculaDistanciaObjetos("Pronasale digi", "Pronasale real") + CalculaDistanciaObjetos("Exocanthus-Alar Base right digi", "Exocanthus-Alar Base right real") + CalculaDistanciaObjetos("Cheek right digi", "Cheek right real") + CalculaDistanciaObjetos("Alar Base right digi", "Alar Base right real") + CalculaDistanciaObjetos("Subnasale digi", "Subnasale real") + CalculaDistanciaObjetos("Alar Base left digi", "Alar Base left real") + CalculaDistanciaObjetos("Cheek left digi", "Cheek left real") + CalculaDistanciaObjetos("Exocanthus-Alar Base left digi", "Exocanthus-Alar Base left real") + CalculaDistanciaObjetos("Cheilion-Alar Base right digi", "Cheilion-Alar Base right real") + CalculaDistanciaObjetos("Cupid's Bow right digi", "Cupid's Bow right real") + CalculaDistanciaObjetos("Cupid's Bow left digi", "Cupid's Bow left real") + CalculaDistanciaObjetos("Cheilion-Alar Base left digi", "Cheilion-Alar Base left real") + CalculaDistanciaObjetos("Cheilion right digi", "Cheilion right real") + CalculaDistanciaObjetos("Cheilion left digi", "Cheilion left real") + CalculaDistanciaObjetos("Lower Lip digi", "Lower Lip real") + CalculaDistanciaObjetos("B point soft digi", "B point soft real") + CalculaDistanciaObjetos("Pogonion soft digi", "Pogonion soft real"))/17

        report_writer.writerow([''])

        report_writer.writerow(['', 'AVERAGE', round(Media, 2)])

        if platform.system() == "Linux":
            abrir_diretorio(tmpdir)
            subprocess.Popen("libreoffice "+tmpdir+"/Report_CompareOnBlender.csv", shell=True)

        if platform.system() == "Windows":
            abrir_diretorio(tmpdir)
            subprocess.Popen('cd "C:/Program Files/LibreOffice/program/" & dir & soffice.bin '+tmpdir+"/Report_CompareOnBlender.csv", shell=True)

        if platform.system() == "Darwin":
            abrir_diretorio(tmpdir)
            subprocess.Popen('/Applications/LibreOffice.app/Contents/MacOS/soffice '+tmpdir+"/Report_CompareOnBlender.csv", shell=True)

class CalculaDistanciasCompare(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "object.calcula_distancias_compare"
   bl_label = "Calc Distances on Compare"
   bl_options = {'REGISTER', 'UNDO'}

   def execute(self, context):
       GeraPlanilha()
       #CalculaDistanciaObjetos("Cheek left real","Cheek left digi")
       return {'FINISHED'}

bpy.utils.register_class(CalculaDistanciasCompare)
