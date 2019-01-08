import bpy
import os
import pydicom as dicom
import subprocess
import tempfile
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

    ds = dicom.dcmread(DiretorioDCM+ListaArquivos[0]) # Diretório e arquivo concatenados


    # Distância da altura dos slices

    slice_thickness = ds.data_element("SliceThickness")
    sliceLimpa1 = str(slice_thickness).split('DS: ')
    sliceLimpa2 = sliceLimpa1[1].strip('"')
#    sliceLimpa1 = str(slice_thickness).strip('(0018, 0050) Slice Thickness DS:')
#    sliceLimpa2 = sliceLimpa1.strip('"')
    EspacoSlices = float(sliceLimpa2)

    # Dimensões laterais

    pixel_spacing = ds.data_element("PixelSpacing")
    pixelLimpa1 = str(pixel_spacing).split('DS: ')
#    pixelLimpa1 = str(pixel_spacing).strip('(0028, 0030) Pixel Spacing DS:')
    pixelLimpa2 = pixelLimpa1[1].strip('[')
    pixelLimpa3 = pixelLimpa2.strip(']')

    DimensoesLaterais = pixelLimpa3.split(",")

    DimensaoLateralX = float(DimensoesLaterais[0].strip("'"))
    DimensaoLateralY = float(DimensoesLaterais[1].strip("'").strip(" '"))

    # Pixels

    rows = ds.data_element("Rows")
    rowsLimpa1 = str(rows).split('US: ')
    RowsPixels = float(rowsLimpa1[1])

    columns = ds.data_element("Columns")
    columnsLimpa1 = str(rows).split('US: ')
    ColumnsPixels = float(rowsLimpa1[1])

# Conversão de DICOM para PNG

def ConverteDCMparaPNG():

    if platform.system() == "Linux":
        subprocess.call('cd '+DiretorioDCM+' && for i in *; do mogrify -verbose -format png $i; done && mv *.png '+TmpDirPNG, shell=True)
        print("DICOMs convertidos em PNG")
        
    if platform.system() == "Darwin":
        subprocess.call('cd '+DiretorioDCM+' && for i in *; do magick $i -auto-level -verbose $i "${i%.dcm}".png; done && mv *.png '+TmpDirPNG, shell=True)
        print("DICOMs convertidos em PNG")

    if platform.system() == "Windows":
        subprocess.call('cd '+DiretorioDCM+' & for %f in (*) do C:\OrtogOnBlender\ImageMagick\mogrify -verbose -format png %f & move *.png '+TmpDirPNG, shell=True)
        print("DICOMs convertidos em PNG")


		
		
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

    ExtraiDadosTomo()
    ConverteDCMparaPNG()

    #Diretorio = "/home/linux3dcs/prj/Estudos/Tomografia/TOMOGRAFIA_2_MENOR/imagens/"

    
    ListaArquivos = sorted(os.listdir(TmpDirPNG))
#    ListaArquivos = sorted(os.listdir(TmpDirPNG))

    DistanciaZ = 0

    EscalaX = DimensaoLateralX * RowsPixels
    EscalaY = DimensaoLateralY * ColumnsPixels

     
    for Arquivo in ListaArquivos:
        bpy.ops.import_image.to_plane(files=[{"name":Arquivo, "name":Arquivo}], directory=TmpDirPNG)

        bpy.ops.transform.translate(value=(0, 0, DistanciaZ), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)

        bpy.ops.transform.resize(value=(EscalaX, EscalaY, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

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

        diffuseBSDF = m.nodes['Diffuse BSDF']
        diffuseBSDF.inputs["Color"].default_value = [0.3, 0.2, 0.4, 0.5]
        materialOutput = m.nodes['Material Output']
        transparentBSDF = m.makeNode('ShaderNodeBsdfTransparent', 'Transparent BSDF')
        #transparentBSDF.inputs["Color"].default_value = [0.4, 0.3, 0.5, 0.5]
        mixShader = m.makeNode('ShaderNodeMixShader', 'Mix Shader')
        m.dump_node(mixShader)
        mixShader.inputs['Fac'].default_value = 0.3
        m.link(transparentBSDF, 'BSDF', mixShader, 1)
        m.link(diffuseBSDF, 'BSDF', mixShader, 2)
        m.link(mixShader, 'Shader', materialOutput, 'Surface')

        m.link(ImageTexture, 'Color', diffuseBSDF, 'Color')
        m.link(ImageTexture, 'Color', transparentBSDF, 'Color')
        m.link(ImageTexture, 'Color', mixShader, 'Fac')

        bpy.ops.object.material_slot_remove()
        bpy.ops.object.material_slot_add()

        bpy.data.objects[bpy.context.scene.objects.active.name].active_material = bpy.data.materials["mat_"+Arquivo]

        bpy.context.object.active_material.game_settings.alpha_blend = 'ALPHA'

    bpy.ops.view3d.view_all(center=False)
    bpy.context.space_data.viewport_shade = 'MATERIAL'
    bpy.ops.file.autopack_toggle()


class ImportaFatias(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.importa_fatias_dcm"
    bl_label = "Importa fatias de tomografia DICOM"
    
    def execute(self, context):
       ImportaFatiasDef()
       return {'FINISHED'}  
