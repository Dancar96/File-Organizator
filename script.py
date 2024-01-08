import os
import shutil

def organizar_descargas():
    # Solicitar la ruta de la carpeta de descargas
    ruta_descargas = input("Ingrese la ruta de la carpeta de descargas: ")

    # Verificar que la ruta de descargas sea válida
    if not os.path.exists(ruta_descargas):
        print("La ruta de descargas no es válida.")
        return

    # Solicitar la ruta del directorio de destino
    ruta_destino = input("Ingrese la ruta del directorio de destino: ")

    # Verificar que la ruta de destino sea válida
    if not os.path.exists(ruta_destino):
        print("La ruta de destino no es válida.")
        return

    tipos_archivos = {}

    # Obtener la lista de archivos en la carpeta de descargas
    archivos = os.listdir(ruta_descargas)

    for archivo in archivos:
        ruta_completa = os.path.join(ruta_descargas, archivo)

        # Ignorar directorios
        if os.path.isdir(ruta_completa):
            continue

        # Obtener la extensión del archivo
        _, extension = os.path.splitext(archivo)
        extension = extension.lower()

        # Crear una carpeta para la extensión en la ruta de destino si no existe
        if extension not in tipos_archivos:
            tipos_archivos[extension] = os.path.join(ruta_destino, extension[1:])

            if not os.path.exists(tipos_archivos[extension]):
                os.makedirs(tipos_archivos[extension])

        # Mover el archivo a la carpeta correspondiente
        shutil.move(ruta_completa, os.path.join(tipos_archivos[extension], archivo))

    print("Archivos organizados correctamente.")

# Llama a la función para organizar los archivos
organizar_descargas()
