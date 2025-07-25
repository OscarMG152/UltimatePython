buscar = 3

for numero in range(5):
    print(numero)
    if numero == buscar:
        print('Encontré', buscar)
        break
else:
    print('No lo encontré')
