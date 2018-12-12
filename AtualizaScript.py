import bpy
import subprocess
import platform

def AtualizaScriptDef(self, context):

	if platform.system() == "Windows":
#		subprocess.call('cd C:\OrtogOnBlender\Blender\2.78\scripts\addons\OrtogOnBlender-master && atualiza_ortog.bat', shell=True)

		arquivo = open('atualiza_ortog.bat', 'w+')
		arquivo.writelines("""cd C:/OrtogOnBlender/Blender/2.78/scripts/addons && ^
rd /s /q OrtogOnBlender-master && ^
C:/OrtogOnBlender/Python27/python.exe -c "import urllib; urllib.urlretrieve ('https://github.com/cogitas3d/OrtogOnBlender/archive/master.zip', 'master.zip')" && ^
C:/OrtogOnBlender/7-Zip/7z x  master.zip && ^
del master.zip""")
#faca o que quiser
		arquivo.close()

		subprocess.call('atualiza_ortog.bat', shell=True)