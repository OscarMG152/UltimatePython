usuarios = [['User1', 4], ['User2', 1], ['User3', 5]]

# map
nombres = list(map(lambda usuario: usuario[0], usuarios))

# filter
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))

print(nombres)
print(menosUsuarios)
