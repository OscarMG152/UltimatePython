from pathlib import Path

# Path(r"C:\ Archivos de Programa\Minecraft") <- Ruta absoluta en Windows
# Path("usr/bin") <- Ruta absoluta en MacOS y Linux
# Path()
# Path.home()
# Path("one/__init__.py") <- Ruta relativa

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("chanchito.py")
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("feliz")
print(p)
