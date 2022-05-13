
import subprocess

command =  "copy \"font\\game.ttf\" \"%WINDIR%\\Fonts\""
check = subprocess.run(command, check=True)
print("The exit code was: %d" % check.returncode)
command = "reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\Fonts\" /v \"FontName (TrueType)\" /t REG_SZ /d FontName.ttf /f"
check1 = subprocess.run(command, check=True)
print("The exit code was: %d" % check.returncode)
#copy "font\\game.ttf" "%WINDIR%\\Fonts"
#reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\Fonts" /v "FontName (TrueType)" /t REG_SZ /d FontName.ttf /f