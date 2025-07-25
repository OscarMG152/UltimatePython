from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "Base de datos",
    "api": "Esta es la api",
    "graphql": "Esto es graphql"
}


def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene función init.")


list(map(load, paths))
