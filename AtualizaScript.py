import bpy
import subprocess
import platform
from os.path import expanduser

def AtualizaScriptDef(self, context):

	if platform.system() == "Windows":
#		subprocess.call('cd C:\OrtogOnBlender\Blender\2.78\scripts\addons\OrtogOnBlender-master && atualiza_ortog.bat', shell=True)

		arquivo = open('atualiza_ortog.bat', 'w+')
		arquivo.writelines("""cd C:/OrtogOnBlender/Blender280/2.80/scripts/addons && ^
rd /s /q OrtogOnBlender-master && ^
C:/OrtogOnBlender/Python27/python.exe -c "import urllib; urllib.urlretrieve ('http://www.ciceromoraes.com.br/downloads/OrtogOnBlender/addon/280/OrtogOnBlender-master.zip', 'OrtogOnBlender-master.zip')" && ^
C:/OrtogOnBlender/7-Zip/7z x  OrtogOnBlender-master.zip && ^
del OrtogOnBlender-master.zip""")

		arquivo.close()

		subprocess.call('atualiza_ortog.bat', shell=True)

	if platform.system() == "Linux":

		home = expanduser("~")
		arquivo = open(home+'/Programs/OrtogOnBlender/Blender280/atualiza_ortog.sh', 'w+')
		arquivo.writelines("""cd $HOME/Downloads && rm -Rfv OrtogOnBlender-master* && \
if [ -f "OrtogOnBlender-master.zip" ]; then echo "tem arquivo" && rm OrtogOnBlender-master.zi*; fi && \
wget http://www.ciceromoraes.com.br/downloads/OrtogOnBlender/addon/280/OrtogOnBlender-master.zip && \
rm -Rfv $HOME/.config/blender/2.80/scripts/addons/OrtogOnBlender-master && \
unzip OrtogOnBlender-master.zip && \
cp -Rv OrtogOnBlender-master $HOME/.config/blender/2.80/scripts/addons/""")

		arquivo.close()

		subprocess.call('chmod +x '+home+'/Programs/OrtogOnBlender/Blender280/atualiza_ortog.sh && '+home+'/Programs/OrtogOnBlender/Blender280/atualiza_ortog.sh', shell=True)
        

	if platform.system() == "Darwin":

		arquivo = open('atualiza_ortog.sh', 'w+')
		arquivo.writelines("""cd $HOME/Downloads && rm -Rfv OrtogOnBlender-master* && \
if [ -f "OrtogOnBlender-master.zip" ]; then echo "tem arquivo" && rm OrtogOnBlender-master.zi*; fi && \
wget http://www.ciceromoraes.com.br/downloads/OrtogOnBlender/addon/280/OrtogOnBlender-master.zip && \
rm -Rfv $HOME/Library/Application\ Support/Blender/2.80/scripts/addons/OrtogOnBlender-master && \
unzip OrtogOnBlender-master.zip && \
mv OrtogOnBlender-master $HOME/Library/Application\ Support/Blender/2.80/scripts/addons/""")

		arquivo.close()

		subprocess.call('chmod +x atualiza_ortog.sh && ./atualiza_ortog.sh', shell=True)

class AtualizaScript(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.atualiza_script"
    bl_label = "Atualiza Script"

    def execute(self, context):
        AtualizaScriptDef(self, context)
        bpy.ops.wm.quit_blender()
        return {'FINISHED'}
