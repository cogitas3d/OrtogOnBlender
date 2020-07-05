import bpy
import os
import pydicom as dicom
import subprocess
import tempfile
import platform
from os.path import expanduser
import platform


# EXTRAI DADOS DA TOMOGRAFIA
def ExtraiDadosTomo():

    global  EspacoSlices, DimensaoLateralX, DimensaoLateralY, RowsPixels, ColumnsPixels, TmpDirPNG, DiretorioDCM

    context = bpy.context
#    obj = context.active_object
    scn = context.scene

    DiretorioDCM = scn.my_tool.path #"/home/linux3dcs/prj/Estudos/Tomografia/TOMOGRAFIA_2_MENOR/ScalarVolume_10/"

    ListaArquivos =  sorted(os.listdir(DiretorioDCM))

    TmpDirPNG = tempfile.mkdtemp()

    if platform.system() == "Linux" or platform.system() == "Darwin":
        ds = dicom.dcmread(DiretorioDCM+ListaArquivos[0], force = True) # Diretório e arquivo concatenados


    if platform.system() == "Windows":
        ds = dicom.dcmread(DiretorioDCM+"\\"+ListaArquivos[0], force = True) # Diretório e arquivo concatenados


    # Distância da altura dos slices

    slice_thickness = ds.data_element("SliceThickness")
    sliceLimpa1 = str(slice_thickness).split('DS: ')
    sliceLimpa2 = sliceLimpa1[1].strip('"')
#    sliceLimpa1 = str(slice_thickness).strip('(0018, 0050) Slice Thickness DS:')
#    sliceLimpa2 = sliceLimpa1.strip('"')
    EspacoSlices = float(sliceLimpa2)


    bpy.types.Scene.SliceThickness = bpy.props.StringProperty \
      (
        name = "SliceThickness",
        description = "Slice Thickness",
        default = str(EspacoSlices)
      )


    # Dimensões laterais

    pixel_spacing = ds.data_element("PixelSpacing")
    pixelLimpa1 = str(pixel_spacing).split('DS: ')
#    pixelLimpa1 = str(pixel_spacing).strip('(0028, 0030) Pixel Spacing DS:')
    pixelLimpa2 = pixelLimpa1[1].strip('[')
    pixelLimpa3 = pixelLimpa2.strip(']')

    DimensoesLaterais = pixelLimpa3.split(",")


    DimensaoLateralX = float(DimensoesLaterais[0].strip("'"))

    bpy.types.Scene.PixelSpacingX = bpy.props.StringProperty \
      (
        name = "PixelSpacingX",
        description = "Pixel SpacingX",
        default = str(DimensaoLateralX)
      )

    DimensaoLateralY = float(DimensoesLaterais[1].strip("'").strip(" '"))

    bpy.types.Scene.PixelSpacingY = bpy.props.StringProperty \
      (
        name = "PixelSpacingY",
        description = "Pixel SpacingY",
        default = str(DimensaoLateralY)
      )


    # Pixels

    rows = ds.data_element("Rows")
    rowsLimpa1 = str(rows).split('US: ')
    RowsPixels = float(rowsLimpa1[1])

    bpy.types.Scene.IMGDimX = bpy.props.StringProperty \
      (
        name = "IMGDimX",
        description = "IMGDimX",
        default = str(RowsPixels)
      )


    columns = ds.data_element("Columns")
    columnsLimpa1 = str(rows).split('US: ')
    ColumnsPixels = float(rowsLimpa1[1])

    bpy.types.Scene.IMGDimY = bpy.props.StringProperty \
      (
        name = "IMGDimY",
        description = "IMGDimY",
        default = str(ColumnsPixels)
      )

# Conversão de DICOM para PNG

def ConverteDCMparaPNG():

    if platform.system() == "Linux":
        subprocess.call('cd '+DiretorioDCM+' && for i in *; do convert -verbose -auto-level $i "${i%.dcm}".png; done && mv *.png '+TmpDirPNG, shell=True)
        print("DICOMs convertidos em PNG")
#        subprocess.call('cd '+DiretorioDCM+' && for i in *; do mogrify -verbose -format png $i; done && mv *.png '+TmpDirPNG, shell=True)
#        print("DICOMs convertidos em PNG")

    if platform.system() == "Darwin":
        subprocess.call('cd '+DiretorioDCM+' && for i in *; do magick $i -auto-level -verbose "${i%.dcm}".png; done && mv *.png '+TmpDirPNG, shell=True)
        print("DICOMs convertidos em PNG")

    if platform.system() == "Windows":
        subprocess.call('cd '+DiretorioDCM+' & for %f in (*) do C:\OrtogOnBlender\ImageMagick\magick %f -auto-level -verbose %f.png & move *.png '+TmpDirPNG, shell=True)
        print("DICOMs convertidos em PNG")
#        subprocess.call('cd '+DiretorioDCM+' & for %f in (*) do C:\OrtogOnBlender\ImageMagick\mogrify -verbose -format png %f & move *.png '+TmpDirPNG, shell=True)
#        print("DICOMs convertidos em PNG")




# Material

class Material:

    def set_cycles(self):
        scn = bpy.context.scene
        if not scn.render.engine == 'CYCLES':
            scn.render.engine = 'CYCLES'

    def make_material(self, name):
        self.mat = bpy.data.materials.new(name)
        self.mat.use_nodes = True
        self.nodes = self.mat.node_tree.nodes

    def link(self, from_node, from_slot_name, to_node, to_slot_name):
        input = to_node.inputs[to_slot_name]
        output = from_node.outputs[from_slot_name]
        self.mat.node_tree.links.new(input, output)

    def makeNode(self, type, name):
        self.node = self.nodes.new(type)
        self.node.name = name
        self.xpos += 200
        self.node.location = self.xpos, self.ypos
        return self.node

    def dump_node(self, node):
        print (node.name)
        print ("Inputs:")
        for n in node.inputs: print ("	", n)
        print ("Outputs:")
        for n in node.outputs: print ("	", n)

    def new_row():
        self.xpos = 0
        self.ypos += 200

    def __init__(self):
        self.xpos = 0
        self.ypos = 0

# Importação dos slices

def ImportaFatiasDef():

    context = bpy.context
#    obj = context.active_object
    scn = context.scene

    ExtraiDadosTomo()
    ConverteDCMparaPNG()

    #Diretorio = "/home/linux3dcs/prj/Estudos/Tomografia/TOMOGRAFIA_2_MENOR/imagens/"


    ListaArquivos = sorted(os.listdir(TmpDirPNG))
#    ListaArquivos = sorted(os.listdir(TmpDirPNG))


    DistanciaZ = 0

    EscalaX = DimensaoLateralX * RowsPixels
    EscalaY = DimensaoLateralY * ColumnsPixels

    #Renderização
    bpy.context.scene.eevee.use_gtao = True
    bpy.context.scene.eevee.gtao_distance = 8
    bpy.context.scene.eevee.use_gtao_bent_normals = False
    # bpy.context.scene.eevee.use_bloom = True # NÃO FICA BOM!
    bpy.context.scene.eevee.use_sss = False #Senão não fica bom!
    bpy.context.scene.eevee.use_ssr = True
    bpy.context.scene.eevee.use_ssr_refraction = True
    bpy.context.scene.eevee.ssr_thickness = 3
    bpy.context.scene.render.hair_type = 'STRIP'
    bpy.context.scene.eevee.shadow_method = 'ESM'
    bpy.context.scene.eevee.shadow_cube_size = '512'
    bpy.context.scene.eevee.shadow_cascade_size = '512'
    bpy.context.scene.eevee.use_soft_shadows = True
    bpy.context.scene.eevee.light_threshold = 0.013
    bpy.context.scene.view_settings.exposure = 0.2

    bpy.context.scene.render.engine = 'BLENDER_EEVEE'

    bpy.context.space_data.shading.type = 'MATERIAL' # Descobri sozinho!
    bpy.context.space_data.shading.use_scene_world = True # Tem que ser aqui  - muda fundo

    # Background
    BackNodeTree = bpy.data.materials.data.worlds['World'].node_tree
    BackNodeTree.nodes['Background'].inputs['Color'].default_value = (1,1,1,1)


    # Importa node group

    if platform.system() == "Linux":

        dirScript = bpy.utils.user_resource('SCRIPTS')

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
#        section   = "\\Collection\\"
#        object    = "SPLINT"
        section   = "\\NodeTree\\"
        object    = "GroupVoxelShader"

    if platform.system() == "Darwin":

        dirScript = bpy.utils.user_resource('SCRIPTS')

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\NodeTree\\"
        object    = "GroupVoxelShader"

    if platform.system() == "Windows":

        dirScript = 'C:/OrtogOnBlender/Blender280/2.80/scripts/'

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\NodeTree\\"
        object    = "GroupVoxelShader"

    filepath  = blendfile + section + object
    directory = blendfile + section
    filename  = object

    bpy.ops.wm.append(
        filepath=filepath,
        filename=filename,
        directory=directory)


    # Importa fatias
    for Arquivo in ListaArquivos:

        bpy.ops.import_image.to_plane(files=[{"name":Arquivo, "name":Arquivo}], directory=TmpDirPNG)

        bpy.ops.transform.translate(value=(0, 0, DistanciaZ), constraint_axis=(False, False, True), mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)

        bpy.ops.transform.resize(value=(EscalaX, EscalaY, 0), constraint_axis=(False, False, False), mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

        #bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {'area': area, 'region': region, 'edit_object': bpy.context.edit_object}
                        bpy.ops.view3d.view_all(override)

        print(Arquivo)

        DistanciaZ += EspacoSlices

    # ATRIBUI MATERIAL

        m = Material()
        m.set_cycles()
        # from chapter 1 of [DRM protected book, could not copy author/title]
        m.make_material("mat_"+Arquivo)

        image_path = TmpDirPNG+"/"+Arquivo

        ImageTexture = m.makeNode('ShaderNodeTexImage', 'Image Texture')
        ImageTexture.image = bpy.data.images.load(image_path)

        bpy.data.materials["mat_"+Arquivo].node_tree.nodes['Image Texture'].color_space = "NONE" # Sozinho! Coloca como Non-Color Data


        materialOutput = m.nodes['Material Output']

        m.link(ImageTexture, 'Color', materialOutput, 'Surface')

        # Faze ro link com o GROUP

        node_tree = bpy.data.materials["mat_"+Arquivo].node_tree
        # And a node group that you have in the file:
        node_group_name = "GroupVoxelShader"


        nodes = node_tree.nodes
        links = node_tree.links

        # Let's at least check if some image node and output node exists
        # you might need a way to determine which ones to use if there are multiple
        image_node = output_node = None
        node_group_exists = False
        for node in nodes:
            if node.type == 'TEX_IMAGE':
                image_node = node
            elif node.type == 'OUTPUT_MATERIAL':
                output_node = node
            elif node.type == 'GROUP': # in case the script was used already
                if node.node_tree.name == node_group_name:
                    node_group_exists = True
                    print('exists')
                    group_node = node

        if output_node and image_node:
            if node_group_name in bpy.data.node_groups and not node_group_exists:
                group_node=nodes.new("ShaderNodeGroup")
                # Creating the group is not enough, we need to specify data(node tree) for it
                group_node.node_tree = bpy.data.node_groups[node_group_name]
                group_node.location = (0,0) #This is default anyway,  but in case you wish to move it

            links.new(image_node.outputs[0], group_node.inputs[0])
            links.new(group_node.outputs[0], output_node.inputs[0])



        # Código original
        '''
        ImageTexture = m.makeNode('ShaderNodeTexImage', 'Image Texture')
        ImageTexture.image = bpy.data.images.load(image_path)


        diffuseBSDF = m.nodes['Principled BSDF']
        diffuseBSDF.inputs["Base Color"].default_value = [0.3, 0.2, 0.4, 0.5]
        materialOutput = m.nodes['Material Output']
        transparentBSDF = m.makeNode('ShaderNodeBsdfTransparent', 'Transparent BSDF')
        invertColor = m.makeNode('ShaderNodeInvert', 'Invert')
        mixShader = m.makeNode('ShaderNodeMixShader', 'Mix Shader')
        m.dump_node(mixShader)
        mixShader.inputs['Fac'].default_value = 0.3
        m.link(transparentBSDF, 'BSDF', mixShader, 1)
        m.link(diffuseBSDF, 'BSDF', mixShader, 2)
        m.link(mixShader, 'Shader', materialOutput, 'Surface')

        m.link(ImageTexture, 'Color', diffuseBSDF, 'Base Color')
        m.link(ImageTexture, 'Color', transparentBSDF, 'Color')
        m.link(ImageTexture, 'Color', mixShader, 'Fac')

        m.link(ImageTexture, 'Color', invertColor, 'Color')
        m.link(invertColor, 'Color', transparentBSDF, 'Color')
        '''

        bpy.ops.object.material_slot_remove()
        bpy.ops.object.material_slot_add()

        bpy.data.objects[bpy.context.view_layer.objects.active.name].active_material = bpy.data.materials["mat_"+Arquivo]


        #bpy.context.object.active_material.blend_method = 'BLEND' # Descobri sozinho!
        #bpy.context.object.active_material.blend_method = 'CLIP'
        bpy.context.object.active_material.blend_method = 'HASHED' # Para a textura

        if platform.system() == "Windows":
            bpy.context.object.active_material.transparent_shadow_method = 'HASHED'

        if platform.system() == "Linux" or platform.system() == "Darwin":
            bpy.context.object.active_material.shadow_method = 'HASHED'



        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        # ENVIA COLLECTION

        ListaColl = []

        for i in bpy.data.collections:
            ListaColl.append(i.name)

        if "CT_Scan Voxel" not in ListaColl:

            obj = context.active_object
            myCol = bpy.data.collections.new("CT_Scan Voxel")
            bpy.context.scene.collection.children.link(myCol)
            obj.instance_collection = myCol
            bpy.ops.object.collection_link(collection='CT_Scan Voxel')
            bpy.data.collections['Collection'].objects.unlink(obj)

        else:
            obj = context.active_object
            bpy.ops.object.collection_link(collection='CT_Scan Voxel')
            bpy.data.collections['Collection'].objects.unlink(obj)


    # Agrupa e ajusta posição

    bpy.ops.object.select_all(action='DESELECT')

    for Arquivo in ListaArquivos:
        bpy.data.objects[str(Arquivo).strip('.png')].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[str(Arquivo).strip('.png')]

    bpy.ops.object.join()

    bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    # Adiciona Array
    bpy.ops.object.modifier_add(type='ARRAY')
    bpy.context.object.modifiers["Array"].use_constant_offset = True
    bpy.context.object.modifiers["Array"].use_relative_offset = False
    bpy.context.object.modifiers["Array"].constant_offset_displace[2] = 0.1
    bpy.context.object.modifiers["Array"].count = 4
    bpy.context.object.modifiers["Array"].show_viewport = False

    # Renderizador
    bpy.context.scene.eevee.use_sss = False

    bpy.context.scene.eevee.gtao_distance = 30
    bpy.context.scene.eevee.gtao_factor = 2
    bpy.context.scene.eevee.use_gtao_bounce = True

#    bpy.data.node_groups["Shader Nodetree"].nodes["Background"].inputs[0].default_value = (0.983241, 0.914842, 1, 1)

    #bpy.data.screens["Default"].shading.use_scene_world = True


    # Centraliza
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for region in area.regions:
                if region.type == 'WINDOW':
                    override = {'area': area, 'region': region, 'edit_object': bpy.context.edit_object}
                    bpy.ops.view3d.view_all(override)

#    bpy.context.space_data.shading.type = 'MATERIAL' # Descobri sozinho!



#    bpy.ops.file.autopack_toggle()

    bpy.context.scene.frame_end = int(len(ListaArquivos))+1


    bpy.types.Scene.IMGPathSeq = bpy.props.StringProperty \
      (
        name = "IMGPathSeq",
        description = "IMGPathSeq",
        default = str(TmpDirPNG)
      )

    bpy.ops.file.pack_all()



class ImportaFatias(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.importa_fatias_dcm"
    bl_label = "Importa fatias de tomografia DICOM"

    def execute(self, context):
       bpy.ops.object.corrige_dicom()
       ImportaFatiasDef()
       return {'FINISHED'}

bpy.utils.register_class(ImportaFatias)

# IMPORTA IMAGENS

def ImportaSeqTomoDef(self, context):

    layout = self.layout
    scn = context.scene
    obj = context.object

    IMGDir = str(bpy.types.Scene.IMGPathSeq[1]['default'])

    ListaArquivos = sorted(os.listdir(IMGDir))

    listaIMG=[]

    for Arquivo in ListaArquivos:
        listaIMG.append( {"name":Arquivo, "name":Arquivo} )

    print(listaIMG)

    bpy.ops.image.open(directory=IMGDir, files=listaIMG, relative_path=True, show_multiview=False)
    bpy.data.images[str(ListaArquivos[0])].source = 'SEQUENCE'

    space = context.space_data
    space.image_user.use_auto_refresh = True


#    bpy.data.screens["Default"]..use_auto_refresh = True

class ImportaSeqTomo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.importa_img_tomo"
    bl_label = "Import CT-Scan Images"

    def execute(self, context):
        ImportaSeqTomoDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(ImportaSeqTomo)

def ExportaSeqTomoDef(self, context):

    layout = self.layout
    scn = context.scene
    obj = context.object

    IMGDir = str(bpy.types.Scene.IMGPathSeq[1]['default'])

    SliceThickness = str(bpy.types.Scene.SliceThickness[1]['default'])

    PixelSpacingX = str(bpy.types.Scene.PixelSpacingX[1]['default'])

    PixelSpacingY = str(bpy.types.Scene.PixelSpacingY[1]['default'])

    DimPixelX = str(bpy.types.Scene.IMGDimX[1]['default'])

    DimPixelY = str(bpy.types.Scene.IMGDimY[1]['default'])

    DirDcmExp = tempfile.mkdtemp()

    if platform.system() == "Linux":

        subprocess.call('cd '+IMGDir+' && mkdir GREY && for i in *.png; do convert $i -type Grayscale -depth 8 GREY/$i; done', shell=True)
        print("PNGs GERADOS!!!")

        subprocess.call('python ~/Programs/OrtogOnBlender/Img2Dcm/img2dcm.py -i '+IMGDir+'/GREY/ -o '+DirDcmExp+' -s '+PixelSpacingX+' '+PixelSpacingY+' '+SliceThickness+' -t png', shell=True)
        print("DICOM BASE GERADO!!!")

#        ListaArquivos = sorted(os.listdir(DirDcmExp))
       # ListaArquivos = sorted(os.listdir(IMGDir+'/GREY/'))

#        subprocess.call('cd '+DirDcmExp, shell=True)

#        for fatia in range(len(ListaArquivos)):
#            ds = dicom.dcmread(ListaArquivos[fatia])
#            ds.ImagePositionPatient[2] = int(fatia)*float(SliceThickness)
#            print("Fatia", ListaArquivos[fatia], "Slice", int(fatia)*float(SliceThickness))
#            ds.save_as(ListaArquivos[fatia])
#        print("LOOP FINALIZADO")

        scn.my_tool.path = DirDcmExp+"/"


    if platform.system() == "Darwin":


# Converte slices em PNGs e depois o PNGs em JPGs monocromaticos
        subprocess.call('cd '+IMGDir+' && mkdir GREY && for i in *.png; do convert $i -type Grayscale -depth 8 -quality 100 GREY/${i%.png}.jpg; done', shell=True)
        print("JPEGs GERADOS!!!")


        subprocess.call('cd '+IMGDir+'/GREY/ && for i in *.jpg; do img2dcm $i ${i%.jpg}.dcm; done && rm *.jpg', shell=True)

# Ajusta os DICOMs nos campos que dao erro
        ListaArquivos = sorted(os.listdir(IMGDir+"/GREY/"))

        os.chdir(IMGDir+"/GREY/")

        for fatia in range(len(ListaArquivos)):
            ds = dicom.dcmread(str(ListaArquivos[fatia]), force=True)
            ds.SeriesNumber = "1"
            ds.AccessionNumber = "1"
            ds.Modality = "CT"
            ds.ImagePositionPatient = "0\\0\\"+str((fatia)*float(SliceThickness)) # Valor do SliceThickness
            ds.PatientID = "OrtogOnBlender"
            ds.InstanceNumber = str(int(fatia)-1)
            ds.SliceThickness = SliceThickness
            ds.PixelSpacing = PixelSpacingX+"\\"+PixelSpacingY
            ds.StudyID = "TESTEID"
            ds.PatientName = "Teste"
            ds.Rows = int(float(DimPixelX))
            ds.Columns = int(float(DimPixelY))
            ds.save_as(str(ListaArquivos[fatia]))

            scn.my_tool.path = IMGDir+"/GREY/"


    if platform.system() == "Windows":


        DirGrayDcm = tempfile.mkdtemp()

        os.chdir(IMGDir)

# Converte slices em PNGs e depois o PNGs em JPGs monocromaticos
#        subprocess.call('for %f in (*); do C:\OrtogOnBlender\ImageMagick\magick %f -type Grayscale -depth 8 -quality 100 %f.jpg; done && mkdir GREY && move *.jpg GREY', shell=True)

        subprocess.call('C:\OrtogOnBlender\ImageMagick\mogrify -type Grayscale -format jpg *.png && mkdir GREY && move *.jpg GREY', shell=True)

        print("JPEGs GERADOS!!!")
        scn.my_tool.path = IMGDir

#        subprocess.call('cd '+IMGDir+'/GREY & mkdir DCM', shell=True)

#        subprocess.call('cd '+IMGDir+'/GREY & for %f in *.jpg do C:\OrtogOnBlender\dcmtk\img2dcm %f %f.dcm', shell=True)

        ListaArquivos = sorted(os.listdir(IMGDir+"/GREY/"))

        os.chdir(IMGDir+"/GREY/")

        for arquivo in ListaArquivos:
            subprocess.call('C:\OrtogOnBlender\dcmtk\img2dcm '+arquivo+' '+DirGrayDcm+'\\'+arquivo+'.dcm', shell=True)
            print("Arquivo "+arquivo+" gerado!")

#            scn.my_tool.path = DirGrayDcm

# Ajusta os DICOMs nos campos que dao erro
        ListaArquivos = sorted(os.listdir(DirGrayDcm))

        os.chdir(DirGrayDcm)

        for fatia in range(len(ListaArquivos)):
            ds = dicom.dcmread(str(ListaArquivos[fatia]), force=True)
            ds.SeriesNumber = "1"
            ds.AccessionNumber = "1"
            ds.Modality = "CT"
            ds.ImagePositionPatient = "0\\0\\"+str((fatia)*float(SliceThickness)) # Valor do SliceThickness
            ds.PatientID = "OrtogOnBlender"
            ds.InstanceNumber = str(int(fatia)-1)
            ds.SliceThickness = SliceThickness
            ds.PixelSpacing = PixelSpacingX+"\\"+PixelSpacingY
            ds.StudyID = "TESTEID"
            ds.PatientName = "Teste"
            ds.Rows = int(float(DimPixelX))
            ds.Columns = int(float(DimPixelY))
            ds.save_as(str(ListaArquivos[fatia]))
            print("Ajustados parâmetros de "+str(fatia))

            scn.my_tool.path = DirGrayDcm

# Ajusta com o dicomtodicom e corrige os pontos que dao erro na importacao

        bpy.ops.object.corrige_dicom()

        ListaArquivos = sorted(os.listdir(DirGrayDcm+"/FIXED/"))

        os.chdir(DirGrayDcm+"/FIXED/")

        for fatia in range(len(ListaArquivos)):
            ds = dicom.dcmread(str(ListaArquivos[fatia]), force=True)
            ds.SeriesNumber = "1"
            ds.AccessionNumber = "1"
            ds.Modality = "CT"
            ds.ImagePositionPatient = "0\\0\\"+str((fatia)*float(SliceThickness)) # Valor do SliceThickness
            ds.PatientID = "OrtogOnBlender"
            ds.InstanceNumber = str(int(fatia)-1)
            ds.SliceThickness = SliceThickness
            ds.PixelSpacing = PixelSpacingX+"\\"+PixelSpacingY
            ds.StudyID = "TESTEID"
            ds.PatientName = "Teste"
            ds.Rows = int(float(DimPixelX))
            ds.Columns = int(float(DimPixelY))
            ds.save_as(str(ListaArquivos[fatia]))
            print("Ajustados FIXED de "+str(fatia))


            scn.my_tool.path = DirGrayDcm+"/FIXED/"


class ExportaSeqTomo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.exporta_img_tomo"
    bl_label = "Teste"

    def execute(self, context):
        ExportaSeqTomoDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(ExportaSeqTomo)


# Abre o SLicer para ver o Threshold

def AbreSlicerDef(self, context):

    context = bpy.context
    scn = context.scene

    if scn.my_tool.path == "":
            bpy.ops.object.dialog_operator_informe_dicom('INVOKE_DEFAULT')
            return {'FINISHED'}

    else:

        homeall = expanduser("~")

        os.chdir(scn.my_tool.path)
        DirAtual = os.getcwd()
        ArqAtual = os.listdir(os.getcwd())[0]
        print("Atual:", os.getcwd())
        print (os.listdir(os.getcwd())[0])


        # ABRE SLICER

        if platform.system() == "Linux":
            subprocess.call(homeall+'/Programs/OrtogOnBlender/Slicer481/./Slicer '+str(DirAtual+"/"+ArqAtual+" &"), shell=True)

        if platform.system() == "Windows":
            subprocess.call('START /B C:/OrtogOnBlender/Slicer410/Slicer.exe '+str(DirAtual+"/"+ArqAtual), shell=True)

        if platform.system() == "Darwin":
            subprocess.call(homeall+'/Programs/OrtogOnBlender/Slicer/Slicer.app/Contents/MacOS/Slicer '+str(DirAtual+"/"+ArqAtual+" &"), shell=True)

class AbreSlicer(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.abre_slicer"
    bl_label = "Open Slicer"

    def execute(self, context):
        AbreSlicerDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(AbreSlicer)


def AbreSlicerMHADef(self, context):

    context = bpy.context
    scn = context.scene

    homeall = expanduser("~")

    if platform.system() == "Linux":
        subprocess.call(homeall+'/Programs/OrtogOnBlender/Slicer481/./Slicer '+scn.my_tool.filepathmha+" &", shell=True)

    if platform.system() == "Windows":
        subprocess.call('START /B C:/OrtogOnBlender/Slicer410/Slicer.exe '+scn.my_tool.filepathmha, shell=True)

    if platform.system() == "Darwin":
        subprocess.call(homeall+'/Programs/OrtogOnBlender/Slicer/Slicer.app/Contents/MacOS/Slicer '+scn.my_tool.filepathmha+" &", shell=True)

class AbreSlicerMHA(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.abre_slicer_mha"
    bl_label = "Open Slicer MHA"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        AbreSlicerMHADef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(AbreSlicerMHA)


def VoxelShaderDefaultDef():

    try:
        bpy.data.materials.data.node_groups['GroupVoxelShader'].nodes['ColorRamp.004'].color_ramp.elements[0].position = 0.164

        bpy.data.materials.data.node_groups['GroupVoxelShader'].nodes['ColorRamp.004'].color_ramp.elements[1].position = 1

        # Cor pele
        bpy.data.materials.data.node_groups['GroupVoxelShader'].nodes['ColorRamp.003'].color_ramp.elements[1].position = 0.364313

    except:
        print("Problema com o material do voxel na cena, pode não conter!")


class VoxelShaderDefault(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.voxelshader_default"
    bl_label = "Voxel Shader Default"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        VoxelShaderDefaultDef()
        return {'FINISHED'}

bpy.utils.register_class(VoxelShaderDefault)



def VoxelShaderOssoDef():

    try:
        bpy.data.materials.data.node_groups['GroupVoxelShader'].nodes['ColorRamp.004'].color_ramp.elements[0].position = 0.11

        bpy.data.materials.data.node_groups['GroupVoxelShader'].nodes['ColorRamp.004'].color_ramp.elements[1].position = 0.20

        # Cor pele
        bpy.data.materials.data.node_groups['GroupVoxelShader'].nodes['ColorRamp.003'].color_ramp.elements[1].position = 0.364313

    except:
        print("Problema com o material do voxel na cena, pode não conter!")


class VoxelShaderOsso(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.voxelshader_osso"
    bl_label = "Voxel Shader Bone"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        VoxelShaderOssoDef()
        return {'FINISHED'}

bpy.utils.register_class(VoxelShaderOsso)


def VoxelShaderPeleDef():

    try:
        bpy.data.materials.data.node_groups['GroupVoxelShader'].nodes['ColorRamp.004'].color_ramp.elements[0].position = 0.0

        bpy.data.materials.data.node_groups['GroupVoxelShader'].nodes['ColorRamp.004'].color_ramp.elements[1].position = 0.20

        # Cor pele
        bpy.data.materials.data.node_groups['GroupVoxelShader'].nodes['ColorRamp.003'].color_ramp.elements[1].position = 0.071017

    except:
        print("Problema com o material do voxel na cena, pode não conter!")


class VoxelShaderPele(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.voxelshader_pele"
    bl_label = "Voxel Shader Skin"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        VoxelShaderPeleDef()
        return {'FINISHED'}

bpy.utils.register_class(VoxelShaderPele)
