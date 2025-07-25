def calcular_mediana(datos):
    lista_ordenada = sorted(datos)
    n = len(lista_ordenada)
    mitad = n // 2
    if n % 2 == 0:
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        return lista_ordenada[mitad]


def calcular_moda(datos):
    frecuencia = {}
    for numero in datos:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1
    return max(frecuencia, key=frecuencia.get)


datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
mediana = calcular_mediana(datos)
moda = calcular_moda(datos)

print(f"Mediana: {mediana}, Moda: {moda}")
