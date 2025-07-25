import random


def tirar_dados(veces):
    frecuencias = {i: 0 for i in range(1, 7)}
    if veces <= 0:
        return "Error: El número de lanzamientos debe ser mayor a 0."
    for _ in range(veces):
        resultado = random.randint(1, 6)
        frecuencias[resultado] += 1
    for cara, frecuencia in frecuencias.items():
        porcentaje = (frecuencia / veces) * 100
        print(
            f"Porcentaje de veces que salió la cara {cara}: {porcentaje:.2f}%")


tirar_dados(100)
