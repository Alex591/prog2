
import subprocess
def installer(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def run_batch_file(file_path):
    Popen(file_path,creationflags=subprocess.CREATE_NEW_CONSOLE)


# Example
if __name__ == '__main__':
    import sys
    import os
    from subprocess import Popen


   # telepités
    installer('pyqt5')
    installer('pyqt5-tools')
    installer("pyqt5designer")
    installer('pyside2')



    ##create desktop shortcut

    miaz=sys.executable
    print(miaz)
    hossz=len(miaz)-10
    miaz=miaz[:hossz]
    miaz=miaz+'Lib\site-packages\QtDesigner\designer.exe'
    print(miaz)
    script=open("script.bat","w")
    print("@echo off",file=script)
    print('set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"',file=script)
    print('echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%',file=script)
    print('echo sLinkFile = "%USERPROFILE%\Desktop\QT Designer.lnk" >> %SCRIPT%',file=script)
    print('echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%',file=script)
    print(f'echo oLink.TargetPath = "{miaz}" >> %SCRIPT%',file=script)
    print('echo oLink.Save >> %SCRIPT%',file=script)
    print('cscript /nologo %SCRIPT%',file=script)
    print('del %SCRIPT%',file=script)
    print('DEL "%~f0"',file=script)
    script.close()
    scriptdir=os.getcwd()+"\script.bat"
    run_batch_file('script.bat')













