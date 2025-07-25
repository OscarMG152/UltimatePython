def get_product(**datos):
    print(datos["id"], datos["name"])


get_product(id="id",
            name="iPhone",
            desc="Esto es un iPhone")
