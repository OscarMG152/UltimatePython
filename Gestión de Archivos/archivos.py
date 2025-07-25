from pathlib import Path
from time import ctime

archivo = Path("Gestión de Archivos/archivo-prueba.txt")

# archivo.exists()
# archivo.rename()
# archivo.unlink()
# print(archivo.stat())

print("Acceso:", ctime(archivo.stat().st_atime))
print("Creación:", ctime(archivo.stat().st_ctime))
print("Modificación:", ctime(archivo.stat().st_mtime))
