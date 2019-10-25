import bpy
import bmesh
from math import sqrt

def TestaPontoCollDef():

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    #Teste se há algum objeto ponto na cena aqui!
    ListaPontos = ['Orbital right', 'Orbital left', 'N point', 'Po right', 'Po left', 'Pt right', 'Pt left', 'Ba point', 'S point', 'U1 Tip', 'U1 Labial Gengival Border', 'U1 Lingual Gengival Border', 'M U6', 'D U6', 'U6 Occlusal', 'PNS point', 'A point', 'ANS point', 'U1 Root', 'L1 Tip', 'L1 Root', 'L1 Labial Gengival Border', 'L1 Lingual Gengival Border', 'B point', 'M L6', 'L6 Occlusal', 'D L6', 'Mid Ramus right', 'Mid Ramus left', 'R right', 'R left', 'Go right', 'Go left', 'Ar right', 'Ar left', 'Sigmoid right', 'Sigmoid left', 'Co right', 'Co left', 'Pg point', 'Gn point', 'Me point', 'ST Glabella', 'ST Nasion', 'Bridge of Nose', 'Tip of Nose', 'Cheekbone right', 'Cheekbone left', 'Columella', 'Subnasale', 'Subpupil right', 'Subpupil left', 'ST A point', 'Upper Lip', 'Stomion Superius', 'Stomion Inferius', 'Lower Lip', 'ST B point', 'ST Pogonion', 'ST Gnathion', 'ST Menton', 'Throat point', 'CB right', 'CB left', 'OR right', 'OR left', 'SP right', 'SP left', 'AB right', 'AB left', 'Tooth 8', 'Tooth 9', 'Tooth 6', 'Tooth 11', 'Tooth 3', 'Tooth 14', 'Tooth 24', 'Tooth 25', 'Tooth 22', 'Tooth 27', 'Tooth 19', 'Tooth 30', 'Condylar Process right', 'Condylar Process left', 'Coronoid Process left', 'Coronoid Process right', 'Mid Go-Ramus Fracure left', 'Mid Go-Ramus Fracure right', 'Mid Upper Incisors', 'Mid Mandibula Angle left', 'Mid Mandibula Angle right', 'Radix', 'Anterior Nostril left', 'Posterior Nostril left', 'Anterior Nostril right', 'Posterior Nostril right', 'Rhinion', 'Alar Groove right', 'Alar Groove left', 'Supratip', 'Infratip Lobule', 'Columella right', 'Columella left', 'Alar Rim right', 'Alar Rim left', 'Medial Canthus left', 'Medial Canthus right', 'Trichion', 'Submental', 'Supraglabella', 'Glabella']


    ObjetosColletion = bpy.data.collections['Collection'].objects

    for i in ObjetosColletion:
        if i.name in ListaPontos:
#            print("HÁ O NOME!", i.name)
            objColletion = bpy.data.objects[i.name]
            bpy.data.collections['Collection'].objects.unlink(objColletion)



def CriaPontoDef(nome, colecao):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    '''
    #Teste se há algum objeto ponto na cena aqui!
    ListaPontos = ['Orbital right', 'Orbital left', 'N', 'Po right', 'Po left', 'Pt rigt', 'Pt left', 'Ba', 'S', 'U1 Tip', 'U1 Labial Gengival Border', 'U1 Lingual Gengival Border', 'M U6', 'D U6', 'U6 Occlusal', 'PNS', 'A', 'ANS', 'U1 Root', 'L1 Tip', 'L1 Labial', 'Gengival Border', 'L1 Lingual Gengival Border', 'B', 'M L6', 'L6 Occlusal', 'D L6', 'Mid Ramus right', 'Mid Ramus left', 'R right', 'R left', 'Go right', 'Go left', 'Ar right', 'Ar left', 'Sigmoid right', 'Sigmoid left', 'Co right', 'Co left', 'Pg', 'Gn', 'Me', 'ST Glabela', 'ST Nasion', 'Bridge of Nose', 'Tip of Nose', 'Subnasale', 'ST A point', 'Upper Lip', 'Stomion Superius', 'Stomion Inferius', 'Lower Lip', 'ST B point', 'ST Pogonion', 'ST Gnathion', 'ST Menton', 'Throat point', 'CB right', 'CB left', 'OR right', 'OR left', 'SP right', 'SP left', 'AB right', 'AB left', 'Condylar Process right', 'Condylar Process left', 'Coronoid Process left', 'Coronoid Process right', 'Mid Go-Ramus Fracure left', 'Mid Go-Ramus Fracure right', 'Mid Upper Incisors']


    ObjetosColletion = bpy.data.collections['Collection'].objects

    for i in ObjetosColletion:
        if i.name in ListaPontos:
            print("HÁ O NOME!", i.name)
#            objColletion = bpy.data.objects[i.name]
#            bpy.data.collections['Collection'].objects.unlink(objColletion)

    '''


#    bpy.ops.object.empty_add(type='PLAIN_AXES')
#    bpy.context.object.name = "EMP1a"
#    bpy.context.object.empty_draw_size = 3
#    bpy.context.object.empty_display_size = 3

    bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
    bpy.context.object.name = nome
    bpy.context.object.show_name = True


    # MATERIAL

    ListaMateriais = []
    MateriaisCena = bpy.data.materials

    for i in MateriaisCena:
        ListaMateriais.append(i.name)

    if 'MatAnatPoints' in ListaMateriais:
        activeObject = bpy.context.active_object #Set active object to variable
        mat = bpy.data.materials["MatAnatPoints"] #set new material to variable
        activeObject.data.materials.append(mat) #add the material to the object
        bpy.context.object.active_material.diffuse_color = (0.45, 0.0, 0.9, 1)
    else:
        activeObject = bpy.context.active_object #Set active object to variable
        mat = bpy.data.materials.new(name="MatAnatPoints") #set new material to variable
        activeObject.data.materials.append(mat) #add the material to the object
        bpy.context.object.active_material.diffuse_color = (0.45, 0.0, 0.9, 1)


    # COLEÇÃO
    # Copia para a coleção determinada

    ListaColecoes = []
    ColocoesCena =  bpy.data.collections

    for i in ColocoesCena:
        ListaColecoes.append(i.name)

    if colecao in ListaColecoes:
        bpy.ops.object.collection_link(collection=colecao)
#        bpy.data.collections['Collection'].objects.unlink(obj)
    else:
        myCol = bpy.data.collections.new(colecao)
        bpy.context.scene.collection.children.link(myCol)
        bpy.ops.object.collection_link(collection=colecao)
#        bpy.data.collections['Collection'].objects.unlink(obj)


# CABEÇA

class Orbital_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.orbital_right_pt"
    bl_label = "Orbital right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Orbital right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Orbital right', 'Anatomical Points - Head')
        TestaPontoCollDef()
        return {'FINISHED'}

class Orbital_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.orbital_left_pt"
    bl_label = "Orbital left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Orbital left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Orbital left', 'Anatomical Points - Head')
        TestaPontoCollDef()
        return {'FINISHED'}

class N_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.n_pt"
    bl_label = "N point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'N point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('N point', 'Anatomical Points - Head')
        TestaPontoCollDef()
        return {'FINISHED'}

class Po_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.po_right"
    bl_label = "Po right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Po right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Po right', 'Anatomical Points - Head')
        TestaPontoCollDef()
        return {'FINISHED'}

class Po_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.po_left"
    bl_label = "Po left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Po left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Po left', 'Anatomical Points - Head')
        TestaPontoCollDef()
        return {'FINISHED'}

class Pt_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pt_right"
    bl_label = "Pt right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Pt right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Pt right', 'Anatomical Points - Head')
        TestaPontoCollDef()
        return {'FINISHED'}

class Pt_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pt_left"
    bl_label = "Pt left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Pt left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Pt left', 'Anatomical Points - Head')
        TestaPontoCollDef()
        return {'FINISHED'}

class Ba_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.ba_pt"
    bl_label = "Ba point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Ba point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Ba point', 'Anatomical Points - Head')
        TestaPontoCollDef()
        return {'FINISHED'}

class S_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.s_pt"
    bl_label = "S point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'S point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('S point', 'Anatomical Points - Head')
        TestaPontoCollDef()
        return {'FINISHED'}

# MAXILA

class U1_Tip_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.u1_tip_pt"
    bl_label = "U1 Tip"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'U1 Tip' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('U1 Tip', 'Anatomical Points - Maxilla')
        TestaPontoCollDef()
        return {'FINISHED'}

class U1_LabGenBor_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.u1_labgenbor_pt"
    bl_label = "U1 Labial Gengival Border"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'U1 Labial Gengival Border' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('U1 Labial Gengival Border', 'Anatomical Points - Maxilla')
        TestaPontoCollDef()
        return {'FINISHED'}

class U1_LinGenBor_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.u1_lingenbor_pt"
    bl_label = "U1 Lingual Gengival Border"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'U1 Lingual Gengival Border' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('U1 Lingual Gengival Border', 'Anatomical Points - Maxilla')
        TestaPontoCollDef()
        return {'FINISHED'}

class M_U6_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.m_u6_pt"
    bl_label = "M U6"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'M U6' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('M U6', 'Anatomical Points - Maxilla')
        TestaPontoCollDef()
        return {'FINISHED'}

class D_U6_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.d_u6_pt"
    bl_label = "D U6"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'D U6' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('D U6', 'Anatomical Points - Maxilla')
        TestaPontoCollDef()
        return {'FINISHED'}

class U6_Occlusal_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.u6_occlusal_pt"
    bl_label = "U6 Occlusal"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'U6 Occlusal' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('U6 Occlusal', 'Anatomical Points - Maxilla')
        TestaPontoCollDef()
        return {'FINISHED'}

class PNS_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pns_pt"
    bl_label = "PNS point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'PNS point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('PNS point', 'Anatomical Points - Maxilla')
        TestaPontoCollDef()
        return {'FINISHED'}

class A_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.a_pt"
    bl_label = "A point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'A point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('A point', 'Anatomical Points - Maxilla')
        TestaPontoCollDef()
        return {'FINISHED'}

class ANS_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.ans_pt"
    bl_label = "ANS point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'ANS point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('ANS point', 'Anatomical Points - Maxilla')
        TestaPontoCollDef()
        return {'FINISHED'}

class U1_Root_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.u1_root_pt"
    bl_label = "U1 Root"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'U1 Root' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('U1 Root', 'Anatomical Points - Maxilla')
        TestaPontoCollDef()
        return {'FINISHED'}

# MANDÍBULA

class L1_Tip_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.l1_tip_pt"
    bl_label = "L1 Tip"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'L1 Tip' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('L1 Tip', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class L1_Root_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.l1_root_pt"
    bl_label = "L1 Root"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'L1 Root' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('L1 Root', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class L1_LabGenBor_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.l1_labgenbor_pt"
    bl_label = "L1 Labial Gengival Border"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'L1 Labial Gengival Border' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('L1 Labial Gengival Border', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class L1_LinGenBor_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.l1_lingenbor_pt"
    bl_label = "L1 Lingual Gengival Border"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'L1 Lingual Gengival Border' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('L1 Lingual Gengival Border', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class B_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.b_pt"
    bl_label = "B point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'B point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('B point', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class M_L6_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.m_l6_pt"
    bl_label = "M L6"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'M L6' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('M L6', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class L6_Occlusal_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.l6_occlusal_pt"
    bl_label = "L6 Occlusal"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'L6 Occlusal' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('L6 Occlusal', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class D_L6_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.d_l6_pt"
    bl_label = "D L6"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'D L6' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('D L6', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class MidRamusRight_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.mid_ramus_right_pt"
    bl_label = "Mid Ramus right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Mid Ramus right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Mid Ramus right', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class MidRamusLeft_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.mid_ramus_left_pt"
    bl_label = "Mid Ramus left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Mid Ramus left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Mid Ramus left', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class R_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.r_right_pt"
    bl_label = "R right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'R right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('R right', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class R_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.r_left_pt"
    bl_label = "R left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'R left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('R left', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class Go_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.go_right_pt"
    bl_label = "Go right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Go right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Go right', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class Go_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.go_left_pt"
    bl_label = "Go left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Go left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Go left', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class Ar_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.ar_right_pt"
    bl_label = "Ar right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Ar right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Ar right', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class Ar_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.ar_left_pt"
    bl_label = "Ar left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Ar left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Ar left', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class Sigmoid_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.sigmoid_right_pt"
    bl_label = "Sigmoid right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Sigmoid right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Sigmoid right', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class Sigmoid_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.sigmoid_left_pt"
    bl_label = "Sigmoid left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Sigmoid left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Sigmoid left', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class Co_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.co_right_pt"
    bl_label = "Co right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Co right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Co right', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class Co_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.co_left_pt"
    bl_label = "Co left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Co left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Co left', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class Pg_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pg_pt"
    bl_label = "Pg point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Pg point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Pg point', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class Gn_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gn_pt"
    bl_label = "Gn point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Gn point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Gn point', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

class Me_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.me_pt"
    bl_label = "Me point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Me point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Me point', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}


class Condylar_Process_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.condylar_process_left_pt"
    bl_label = "Condylar Process left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Condylar Process left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Condylar Process left', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Condylar_Process_left_pt)


class Condylar_Process_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.condylar_process_right_pt"
    bl_label = "Condylar Process right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Condylar Process right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Condylar Process right', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Condylar_Process_right_pt)


class Coronoid_Process_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.coronoid_process_left_pt"
    bl_label = "Coronoid Process left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Coronoid Process left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Coronoid Process left', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Coronoid_Process_left_pt)


class Coronoid_Process_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.coronoid_process_right_pt"
    bl_label = "Coronoid Process right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Coronoid Process right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Coronoid Process right', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Coronoid_Process_right_pt)


class Go_Ramus_Fracure_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.go_ramus_fracure_left_pt"
    bl_label = "Mid Go-Ramus Fracure left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Mid Go-Ramus Fracure left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Mid Go-Ramus Fracure left', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Go_Ramus_Fracure_left_pt)


class Go_Ramus_Fracure_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.go_ramus_fracure_right_pt"
    bl_label = "Mid Go-Ramus Fracure right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Mid Go-Ramus Fracure right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Mid Go-Ramus Fracure right', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Go_Ramus_Fracure_right_pt)


class Mid_Mandibula_Angle_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.mid_mandibula_angle_left_pt"
    bl_label = "Mid Mandibula Angle left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Mid Mandibula Angle left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Mid Mandibula Angle left', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Mid_Mandibula_Angle_left_pt)

class Mid_Mandibula_Angle_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.mid_mandibula_angle_right_pt"
    bl_label = "Mid Mandibula Angle right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Mid Mandibula Angle right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Mid Mandibula Angle right', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Mid_Mandibula_Angle_right_pt)


class Mid_Upper_Incisors_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.mid_upper_incisors_pt"
    bl_label = "Mid Upper Incisors"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Mid Upper Incisors' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Mid Upper Incisors', 'Anatomical Points - Mandible')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Mid_Upper_Incisors_pt)


# DENTES

class Tooth_8_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tooth_8_pt"
    bl_label = "Tooth 8"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Tooth 8' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Tooth 8', 'Anatomical Points - Teeth')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Tooth_8_pt)

class Tooth_9_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tooth_9_pt"
    bl_label = "Tooth 9"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Tooth 9' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Tooth 9', 'Anatomical Points - Teeth')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Tooth_9_pt)

class Tooth_6_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tooth_6_pt"
    bl_label = "Tooth 6"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Tooth 6' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Tooth 6', 'Anatomical Points - Teeth')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Tooth_6_pt)

class Tooth_11_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tooth_11_pt"
    bl_label = "Tooth 11"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Tooth 11' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Tooth 11', 'Anatomical Points - Teeth')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Tooth_11_pt)

class Tooth_3_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tooth_3_pt"
    bl_label = "Tooth 3"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Tooth 3' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Tooth 3', 'Anatomical Points - Teeth')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Tooth_3_pt)

class Tooth_14_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tooth_14_pt"
    bl_label = "Tooth 14"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Tooth 14' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Tooth 14', 'Anatomical Points - Teeth')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Tooth_14_pt)

class Tooth_24_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tooth_24_pt"
    bl_label = "Tooth 24"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Tooth 24' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Tooth 24', 'Anatomical Points - Teeth')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Tooth_24_pt)

class Tooth_25_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tooth_25_pt"
    bl_label = "Tooth 25"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Tooth 25' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Tooth 25', 'Anatomical Points - Teeth')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Tooth_25_pt)

class Tooth_22_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tooth_22_pt"
    bl_label = "Tooth 22"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Tooth 22' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Tooth 22', 'Anatomical Points - Teeth')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Tooth_22_pt)

class Tooth_27_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tooth_27_pt"
    bl_label = "Tooth 27"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Tooth 27' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Tooth 27', 'Anatomical Points - Teeth')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Tooth_27_pt)

class Tooth_19_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tooth_19_pt"
    bl_label = "Tooth 19"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Tooth 19' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Tooth 19', 'Anatomical Points - Teeth')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Tooth_19_pt)

class Tooth_30_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tooth_30_pt"
    bl_label = "Tooth 30"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Tooth 30' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Tooth 30', 'Anatomical Points - Teeth')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Tooth_30_pt)


# TECIDO MOLE

class ST_Glabella_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.st_glabella_pt"
    bl_label = "ST Glabella"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'ST Glabella' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('ST Glabella', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(ST_Glabella_pt)


class ST_Nasion_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.st_nasion_pt"
    bl_label = "ST Nasion"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'ST Nasion' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('ST Nasion', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(ST_Nasion_pt)

class Bridge_Nose_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.bridge_nose_pt"
    bl_label = "Bridge of Nose"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Bridge of Nose' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Bridge of Nose', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Bridge_Nose_pt)

class Tip_Nose_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.tip_nose_pt"
    bl_label = "Tip of Nose"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Tip of Nose' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Tip of Nose', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Tip_Nose_pt)

class Columella_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.columella_pt"
    bl_label = "Columalla"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Columella' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Columella', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Columella_pt)

class Subnasale_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.subnasale_pt"
    bl_label = "Subnasale"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Subnasale' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Subnasale', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Subnasale_pt)

class ST_A_point_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.st_a_point_pt"
    bl_label = "ST A point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'ST A point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('ST A point', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(ST_A_point_pt)

class Upper_Lip_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.upper_lip_pt"
    bl_label = "Upper Lip"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Upper Lip' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Upper Lip', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Upper_Lip_pt)

class Stomion_Superius_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.stomion_superius_pt"
    bl_label = "Stomion Superius"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Stomion Superius' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Stomion Superius', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Stomion_Superius_pt)

class Stomion_Inferius_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.stomion_inferius_pt"
    bl_label = "Stomion Inferius"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Stomion Inferius' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Stomion Inferius', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Stomion_Inferius_pt)

class Lower_Lip_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.lower_lip_pt"
    bl_label = "Lower Lip"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Lower Lip' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Lower Lip', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Lower_Lip_pt)

class ST_B_point_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.st_b_point_pt"
    bl_label = "ST B point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'ST B point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('ST B point', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(ST_B_point_pt)


class ST_Pogonion_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.st_pogonion_pt"
    bl_label = "ST Pogonion"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'ST Pogonion' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('ST Pogonion', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(ST_Pogonion_pt)


class ST_Gnathion_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.st_gnathion_pt"
    bl_label = "ST Gnathion"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'ST Gnathion' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('ST Gnathion', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(ST_Gnathion_pt)


class ST_Menton_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.st_menton_pt"
    bl_label = "ST Menton"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'ST Menton' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('ST Menton', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(ST_Menton_pt)


class Throat_point_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.throat_point_pt"
    bl_label = "Throat point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Throat point' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Throat point', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Throat_point_pt)

class Subpupil_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.subpupil_right_pt"
    bl_label = "Subpupil right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Subpupil right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Subpupil right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Subpupil_right_pt)

class Subpupil_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.subpupil_left_pt"
    bl_label = "Subpupil left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Subpupil left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Subpupil left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Subpupil_left_pt)

class CB_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cb_right_pt"
    bl_label = "CB right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'CB right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('CB right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(CB_right_pt)


class CB_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cb_left_pt"
    bl_label = "CB left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'CB left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('CB left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(CB_left_pt)

class OR_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.or_right_pt"
    bl_label = "OR right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'OR right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('OR right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(OR_right_pt)


class OR_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.or_left_pt"
    bl_label = "OR left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'OR left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('OR left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(OR_left_pt)

class Cheekbone_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cheekbone_left_pt"
    bl_label = "Cheekbone left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Cheekbone left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Cheekbone left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Cheekbone_left_pt)

class Cheekbone_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cheekbone_right_pt"
    bl_label = "Cheekbone right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Cheekbone right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Cheekbone right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Cheekbone_right_pt)


class SP_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.sp_right_pt"
    bl_label = "SP right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'SP right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('SP right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(SP_right_pt)

class SP_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.sp_left_pt"
    bl_label = "SP left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'SP left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('SP left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(SP_left_pt)


class AB_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.ab_right_pt"
    bl_label = "AB right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'AB right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('AB right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(AB_right_pt)


class AB_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.ab_left_pt"
    bl_label = "AB left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'AB left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('AB left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(AB_left_pt)

# Parenteia pontos duro

def ParenteiaPonto(ponto):

    listaDist = []

    osteotomias = [bpy.data.objects["ca"], bpy.data.objects["ma"], bpy.data.objects["cm"], bpy.data.objects["me"], bpy.data.objects["rd"], bpy.data.objects["re"]]

#    for item in bpy.data.objects:
    for item in osteotomias:
#        if item.hide == False and item.type == 'MESH':

            obj = bpy.data.objects[item.name]
            # print("OBJETO ATUAL", obj)

            # Lista os vértices do objeto
            if obj.mode == 'EDIT':
                bm = bmesh.from_edit_mesh(obj.data)
                vertices = bm.verts

            else:
                vertices = obj.data.vertices

            # Todos os vértices por vetor
            verts = [obj.matrix_world @ vert.co for vert in vertices]

            # Captura vetor do objeto

            referencia = bpy.data.objects[ponto].location



            # Calcula distância pontos

            def DistanciaObjs(obj1, obj2):

                objA = bpy.data.objects[obj1].location
                objB = obj2

                distancia = sqrt( (objB[0] - objA[0])**2 + (objB[1] - objA[1])**2 + (objB[2] - objA[2])**2 )

                return distancia



            for i in range(len(verts)):

                vertAtual = verts[i]

                distanciaVert = DistanciaObjs(ponto, vertAtual)

                listaDist.append([distanciaVert, obj.name])




    listaFin = sorted(listaDist)
    print("MAIS PRÓXIMO!", listaFin[0])

    bpy.ops.object.select_all(action='DESELECT')
    ObjPai = bpy.data.objects[listaFin[0][1]]
    ObjFilho = bpy.data.objects[ponto]
    ObjPai.select_set(True)
    ObjFilho.select_set(True)
    bpy.context.view_layer.objects.active = ObjPai
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')

# Parenteia pontos mole

def ParenteiaPontoMole(ponto):

    listaDist = []

    obj = bpy.data.objects["SoftTissueDynamic"]
            # print("OBJETO ATUAL", obj)

            # Lista os vértices do objeto
    if obj.mode == 'EDIT':
        bm = bmesh.from_edit_mesh(obj.data)
        vertices = bm.verts

    else:
        vertices = obj.data.vertices

            # Todos os vértices por vetor
    verts = [obj.matrix_world @ vert.co for vert in vertices]

            # Captura vetor do objeto

    referencia = bpy.data.objects[ponto].location

            # Calcula distância pontos

    def DistanciaObjs(obj1, obj2):
        objA = bpy.data.objects[obj1].location
        objB = obj2

        distancia = sqrt( (objB[0] - objA[0])**2 + (objB[1] - objA[1])**2 + (objB[2] - objA[2])**2 )

        return distancia


    for i in range(len(verts)):

        vertAtual = verts[i]

        distanciaVert = DistanciaObjs(ponto, vertAtual)

        listaDist.append([distanciaVert, i])



    listaFin = sorted(listaDist)
    print("MAIS PRÓXIMO!", listaFin[0])



    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set(mode = 'OBJECT')

# Quebra aqui
    obj.data.vertices[listaFin[0][1]].select = True



    bpy.ops.object.mode_set(mode = 'EDIT')


    bpy.ops.object.mode_set(mode = 'OBJECT')

    bpy.ops.object.select_all(action='DESELECT')


    b = bpy.data.objects[ponto]

    b.select_set(True)
    bpy.context.view_layer.objects.active = b
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.select_all(action = 'DESELECT')


    obj.select_set(True)
    b.select_set(True)
    bpy.context.view_layer.objects.active = obj

    print(b.name)


    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.object.vertex_parent_set()
    bpy.ops.object.mode_set(mode = 'OBJECT')


class testaPontos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.testa_pontos"
    bl_label = "TestaPontos"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        testaPontosDef(self, context)
        return {'FINISHED'}

# Parenteia pontos

def ParenteiaEMPDef(self, context):


	# Lista com todos os pontos

	ListaPontos = ['Orbital right', 'Orbital left', 'N point', 'Po right', 'Po left', 'Pt right', 'Pt left', 'Ba point', 'S point', 'U1 Tip', 'U1 Labial Gengival Border', 'U1 Lingual Gengival Border', 'M U6', 'D U6', 'U6 Occlusal', 'PNS point', 'A point', 'ANS point', 'U1 Root', 'L1 Tip', 'L1 Root', 'L1 Labial Gengival Border', 'L1 Lingual Gengival Border', 'B point', 'M L6', 'L6 Occlusal', 'D L6', 'Mid Ramus right', 'Mid Ramus left', 'R right', 'R left', 'Go right', 'Go left', 'Ar right', 'Ar left', 'Sigmoid right', 'Sigmoid left', 'Co right', 'Co left', 'Pg point', 'Gn point', 'Me point', 'Tooth 8', 'Tooth 9', 'Tooth 6', 'Tooth 11', 'Tooth 3', 'Tooth 14', 'Tooth 24', 'Tooth 25', 'Tooth 22', 'Tooth 27', 'Tooth 19', 'Tooth 30']

	ListaPontosMole = [ 'ST Glabella', 'ST Nasion', 'Bridge of Nose', 'Tip of Nose', 'Cheekbone right', 'Cheekbone left', 'Columella', 'Subnasale', 'Subpupil right', 'Subpupil left' ,'ST A point', 'Upper Lip', 'Stomion Superius', 'Stomion Inferius', 'Lower Lip', 'ST B point', 'ST Pogonion', 'ST Gnathion', 'ST Menton', 'Throat point', 'CB right', 'CB left', 'OR right', 'OR left', 'SP right', 'SP left', 'AB right', 'AB left', 'Radix', 'Anterior Nostril left', 'Posterior Nostril left', 'Anterior Nostril right', 'Posterior Nostril right','Rhinion', 'Alar Groove right', 'Alar Groove left', 'Supratip', 'Infratip Lobule', 'Alar Rim right', 'Alar Rim left', 'Columella right', 'Columella left', 'Alar Rim right', 'Alar Rim left', 'Medial Canthus left', 'Medial Canthus right', 'Trichion', 'Submental', 'Supraglabella', 'Glabella']

	# Cria lista com pontos da cena

	ObjetosCena = bpy.data.objects

# Compara pontos duro
	for ob in ListaPontos:
		if ob in ObjetosCena:
			ParenteiaPonto(ob)
			print(ob,"Existe na lista (Duro)!")


# Compara pontos mole
	for ob in ListaPontosMole:
		if ob in ObjetosCena:
			ParenteiaPontoMole(ob)
			print(ob,"Existe na lista (Mole)!")

class ParenteiaEMP(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.parenteia_emp"
    bl_label = "ParenteiaEMP"

    def execute(self, context):
        ParenteiaEMPDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(ParenteiaEMP)
