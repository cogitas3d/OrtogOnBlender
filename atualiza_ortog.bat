cd C:\OrtogOnBlender\Blender\2.78\scripts\addons && ^
rd /s /q OrtogOnBlender-master && ^
C:\OrtogOnBlender\Python27\python.exe -c "import urllib; urllib.urlretrieve ('https://github.com/cogitas3d/OrtogOnBlender/archive/master.zip', 'master.zip')" && ^
C:\OrtogOnBlender\7-Zip\7z x  master.zip && ^
del master.zip