import bpy
import subprocess
import platform
from os.path import expanduser

def AtualizaScriptDef(self, context):

	if platform.system() == "Windows":
#		subprocess.call('cd C:\OrtogOnBlender\Blender\2.78\scripts\addons\OrtogOnBlender-master && atualiza_ortog.bat', shell=True)

		arquivo = open('atualiza_ortog.bat', 'w+')
		arquivo.writelines("""cd C:/OrtogOnBlender/Blender/2.78/scripts/addons && ^
rd /s /q OrtogOnBlender-master && ^
C:/OrtogOnBlender/Python27/python.exe -c "import urllib; urllib.urlretrieve ('https://github.com/cogitas3d/OrtogOnBlender/archive/master.zip', 'master.zip')" && ^
C:/OrtogOnBlender/7-Zip/7z x  master.zip && ^
del master.zip""")

		arquivo.close()

		subprocess.call('atualiza_ortog.bat', shell=True)

	if platform.system() == "Linux":

        home = expanduser("~")
        arquivo = open(home+'Programs/OrtogOnBlender/atualiza_ortog.sh', 'w+')
        arquivo.writelines("""cd $HOME/Downloads && rm -Rfv OrtogOnBlender-master* && \
if [ -f "master.zip" ]; then echo "tem arquivo" && rm master.zi*; fi && \
wget https://github.com/cogitas3d/OrtogOnBlender/archive/master.zip && \
rm -Rfv $HOME/.config/blender/2.78/scripts/addons/OrtogOnBlender-master && \
unzip master.zip && \
cp -Rv OrtogOnBlender-master $HOME/.config/blender/2.78/scripts/addons/""")

		arquivo.close()

		subprocess.call('chmod +x Programs/OrtogOnBlender/atualiza_ortog.sh && Programs/OrtogOnBlender/atualiza_ortog.sh', shell=True)
        

	if platform.system() == "Darwin":

		arquivo = open('atualiza_ortog.sh', 'w+')
		arquivo.writelines("""cd $HOME/Downloads && rm -Rfv OrtogOnBlender-master* && \
if [ -f "master.zip" ]; then echo "tem arquivo" && rm master.zi*; fi && \
wget https://github.com/cogitas3d/OrtogOnBlender/archive/master.zip && \
rm -Rfv $HOME/Library/Application\ Support/Blender/2.78/scripts/addons/OrtogOnBlender-master && \
unzip master.zip && \
mv OrtogOnBlender-master $HOME/Library/Application\ Support/Blender/2.78/scripts/addons/""")

		arquivo.close()

		subprocess.call('chmod +x atualiza_ortog.sh && ./atualiza_ortog.sh', shell=True)
