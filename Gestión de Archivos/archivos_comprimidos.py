from pathlib import Path
from zipfile import ZipFile

# Escribir

with ZipFile("Gestión de Archivos/comprimidos.zip", "w", allowZip64=True) as zip:
    for path in Path().rglob("*.*"):
        print(path)
        if str(path) != "Gestión de Archivos/comprimidos.zip":
            zip.write(path)

# Leer

# with ZipFile("Gestión de Archivos/comprimidos.zip") as zip:
#     # print(zip.namelist())
#     info = zip.getinfo("Gestión de Archivos/archivos_comprimidos.py")
#     print(
#         info.file_size,
#         info.compress_size
#     )
#     zip.extractall("Gestión de Archivos/descomprimidos")
