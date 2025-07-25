numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort()
# numeros.sort(reverse=True)

# numeros2 = sorted(numeros)
numeros2 = sorted(numeros, reverse=True)

print(numeros)
print(numeros2)

usuarios = [['User1', 4], ['User2', 1], ['User3', 5]]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena)
print(usuarios)

usuarios.sort(key=ordena, reverse=True)
print(usuarios)
