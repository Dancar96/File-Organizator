import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organizar_carpetas(ruta_para_organizar, ruta_destino):
    tipos_archivos = {}

    archivos = os.listdir(ruta_para_organizar)

    for archivo in archivos:
        ruta_completa = os.path.join(ruta_para_organizar, archivo)

        if os.path.isdir(ruta_completa):
            continue

        _, extension = os.path.splitext(archivo)
        extension = extension.lower()

        if extension not in tipos_archivos:
            tipos_archivos[extension] = os.path.join(ruta_destino, extension[1:])

            if not os.path.exists(tipos_archivos[extension]):
                os.makedirs(tipos_archivos[extension])

        shutil.move(ruta_completa, os.path.join(tipos_archivos[extension], archivo))

    messagebox.showinfo("Éxito", "Archivos organizados correctamente.")

def seleccionar_carpeta():
    ruta_para_organizar = filedialog.askdirectory()
    entry_archivos.delete(0, tk.END)
    entry_archivos.insert(0, ruta_para_organizar)

def seleccionar_carpeta_destino():
    ruta_destino = filedialog.askdirectory()
    entry_destino.delete(0, tk.END)
    entry_destino.insert(0, ruta_destino)

def organizar_archivos():
    ruta_para_organizar = entry_archivos.get()
    ruta_destino = entry_destino.get()

    organizar_carpetas(ruta_para_organizar, ruta_destino)

ventana = tk.Tk()
ventana.title("Organizador de Archivos")

tk.Label(ventana, text="Carpeta que quieres organizar:").grid(row=0, column=0, padx=10, pady=5)
entry_archivos = tk.Entry(ventana, width=40)
entry_archivos.grid(row=0, column=1, padx=10, pady=5)
tk.Button(ventana, text="Seleccionar Carpeta", command=seleccionar_carpeta).grid(row=0, column=2, padx=10, pady=5)

tk.Label(ventana, text="Carpeta de Destino:").grid(row=1, column=0, padx=10, pady=5)
entry_destino = tk.Entry(ventana, width=40)
entry_destino.grid(row=1, column=1, padx=10, pady=5)
tk.Button(ventana, text="Seleccionar Carpeta", command=seleccionar_carpeta_destino).grid(row=1, column=2, padx=10, pady=5)

tk.Button(ventana, text="Organizar Archivos", command=organizar_archivos).grid(row=2, column=1, pady=10)

ventana.mainloop()