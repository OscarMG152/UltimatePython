mascotas = ['Luna', 'Pandi', 'Coffee', 'Trini', 'Coffee', 'Luna']


mascotas.insert(1, "Mascota 1")
mascotas.append("Mascota 2")

print(mascotas)

mascotas.remove("Coffee")
mascotas.pop()
mascotas.pop(1)

print(mascotas)

del mascotas[0]

print(mascotas)

mascotas.clear()

print(mascotas)
