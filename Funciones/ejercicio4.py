def promedio(*numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)


print(promedio(1, 2, 3, 4, 5))
print(promedio())
