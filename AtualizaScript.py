import bpy
import subprocess
import platform

def AtualizaScriptDef(self, context):

	if platform.system() == "Windows":
		subprocess.call('cd C:\OrtogOnBlender && atualiza_ortog.bat', shell=True)