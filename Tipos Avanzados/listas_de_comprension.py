usuarios = [['User1', 4], ['User2', 1], ['User3', 5]]

# nombres = [usuario[0] for usuario in usuarios] <-- Transformado
# nombres = [usuario for usuario in usuarios if usuario[1] > 2] <-- Filtrado

# Transformado y filtrado
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)
