tareas = [
    {"id": 1, "descripcion": "Lavar los platos"},
    {"id": 2, "descripcion": "Sacar la basura"},
    {"id": 3, "descripcion": "Limpiar el baño"},
    {"id": 4, "descripcion": "Hacer la cama"},
    {"id": 5, "descripcion": "Cocinar la cena"},
    {"id": 6, "descripcion": "Pasear al perro"},
    {"id": 7, "descripcion": "Hacer la compra"},
    {"id": 8, "descripcion": "Planchar la ropa"},
    {"id": 9, "descripcion": "Regar las plantas"},
    {"id": 10, "descripcion": "Lavar el coche"},
]


def buscar_tarea_por_id(tareas, id):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    return None


def buscar_tareas_por_texto(tareas, texto):
    tareas_encontradas = []
    for tarea in tareas:
        if texto.lower() in tarea["descripcion"].lower():
            tareas_encontradas.append(tarea)
    return tareas_encontradas


print(f"Tarea encontrada por ID = {buscar_tarea_por_id(tareas, 1)}")
print(
    f"Tarea encontrada por texto = {buscar_tareas_por_texto(tareas, "co")}")
