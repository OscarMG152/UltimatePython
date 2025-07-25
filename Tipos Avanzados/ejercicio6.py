import random


def tirar_dados(veces):
    resultados = [0] * 6

    for _ in range(veces):
        resultado = random. randint(1, 6)
        resultados[resultado - 1] += 1

    if veces == 1:
        print(f"Salió cara: {resultado}")
    else:
        for i in range(6):
            porcentaje = (resultados[i] / veces) * 100
            print(f"Cara {i + 1}: {porcentaje:.2f}%")
