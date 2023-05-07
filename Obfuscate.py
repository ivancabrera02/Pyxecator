import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def ofuscar_y_convertir():
    # Seleccionar el archivo a ofuscar y convertir
    file_path = select_file()
    
    # Ofuscar el archivo seleccionado con pyarmor
    ofuscado_path = os.path.splitext(file_path)[0] + '_ofuscado.py'
    pyarmor_command = f'pyarmor-7 obfuscate {file_path} --output={ofuscado_path}'
    subprocess.run(pyarmor_command, shell=True, check=True)
    
    # Convertir el archivo ofuscado en un archivo ejecutable con pyinstaller
    pyinstaller_command = f'pyinstaller C:/Users/ivan/Desktop/Carpeta/EscanerPuertos.py' #Sustituir ruta
    subprocess.run(pyinstaller_command)
    
    # Mostrar un mensaje de confirmación
    print(f"El archivo {file_path} ha sido ofuscado y convertido en un archivo ejecutable.")

ofuscar_y_convertir()