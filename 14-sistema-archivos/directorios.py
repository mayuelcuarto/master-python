import os
import shutil

# Crear carpeta
if not os.path.isdir("./14-sistema-archivos/mi_carpeta"):
    os.mkdir("./14-sistema-archivos/mi_carpeta")
else:
    print("Ya existe el directorio")

# Eliminar carpeta
#os.rmdir("./14-sistema-archivos/mi_carpeta")

"""
ruta_original = "./14-sistema-archivos/mi_carpeta"
ruta_nueva = "./14-sistema-archivos/mi_carpeta_copiada"
shutil.copytree(ruta_original,ruta_nueva)
"""

# Eliminar carpeta
# os.rmdir("./14-sistema-archivos/mi_carpeta_copiada")

print("Contenido de mi carpeta:")
contenido = os.listdir("./14-sistema-archivos/mi_carpeta")

for fichero in contenido:
    print("Fichero: " + fichero)