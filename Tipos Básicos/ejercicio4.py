p_nombre = input("Ingrese su primer nombre: ").strip().capitalize()
s_nombre = input("Ingrese su segundo nombre (opcional): ").strip().capitalize()
p_apellido = input("Ingrese su primer apellido: ").strip().capitalize()
s_apellido = input(
    "Ingrese su segundo apellido (opcional): ").strip().capitalize()

nombre_completo = f"{p_nombre} {s_nombre} {p_apellido} {s_apellido}".replace(
    "  ", " ")

print(nombre_completo)
