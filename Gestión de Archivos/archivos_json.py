import json
from pathlib import Path

# Escribir

# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"},
# ]

# data = json.dumps(productos)
# Path("Gestión de Archivos/productos.json").write_text(data)

# Leer

data = Path("Gestión de Archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
# print(productos)

# Modificar

productos[0]["name"] = "Chanchito feliz"
Path("Gestión de Archivos/productos.json").write_text(json.dumps(productos))
