@echo off

echo Creating executable...
pyinstaller --onefile final.py

echo Adding executable to startup...
set exe_file=final.exe
set startup_folder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set path=%startup_folder%\final.lnk
set target=%CD%\%exe_file%
set wDir=%CD%
set icon=%target%

echo Set WScript Shell = CreateObject("WScript.Shell") > add_to_startup.vbs
echo Set shortcut = WScriptShell.CreateShortcut(path) >> add_to_startup.vbs
echo shortcut.Targetpath = target >> add_to_startup.vbs
echo shortcut.WorkingDirectory = wDir >> add_to_startup.vbs
echo shortcut.IconLocation = icon >> add_to_startup.vbs
echo shortcut.save >> add_to_startup.vbs

cscript //nologo add_to_startup.vbs

del add_to_startup.vbs

set source_folder=C:\source_folder
set target_folder=C:\target_folder
set file_name=example.txt

move "%source_folder%\%file_name%" "%target_folder%\%file_name%"

echo File moved successfully.
echo Executable added to startup successfully.
