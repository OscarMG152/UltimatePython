pila = []

pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

ultimoElemento = pila.pop()
print(ultimoElemento)
print(pila)
pila.pop()
pila.pop()

if not pila:
    print("Pila vacía")
