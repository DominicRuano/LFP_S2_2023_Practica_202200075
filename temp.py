import os

def cambiar_extension(nombre_archivo, nueva_extension):
    nombre, _ = os.path.splitext(nombre_archivo)
    nuevo_nombre = nombre + nueva_extension
    os.rename(nombre_archivo, nuevo_nombre)

# Llamamos a la función para cambiar la extensión del archivo
nombre_archivo_original = "movimiento.txt"
nueva_extension = ".mov"

cambiar_extension(nombre_archivo_original, nueva_extension)
