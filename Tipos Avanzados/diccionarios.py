punto = {"x": 25, "y": 50}
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)

if "lala" in punto:
    print("Encontre lala", punto["lala"])

print(punto.get("x"))
print(punto.get("lala"))
print(punto.get("lala"), 97)

del punto["x"]
del punto["y"]

punto["x"] = 25

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "User1"},
    {"id": 2, "nombre": "User2"},
    {"id": 3, "nombre": "User3"},
    {"id": 4, "nombre": "User4"},
]

for usuario in usuarios:
    print(usuario["nombre"])
