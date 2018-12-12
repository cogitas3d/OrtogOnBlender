import bpy
import subprocess
import platform

def AtualizaScriptDef(self, context):

	if platform.system() == "Windows":
		subprocess.call('cd C:\OrtogOnBlender\Blender\2.78\scripts\addons\OrtogOnBlender-master && atualiza_ortog.bat', shell=True)
