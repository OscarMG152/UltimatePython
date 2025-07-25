compras = {
    'Cliente1': 200,
    'Cliente2': 100,
    'Cliente3': 180,
}


def aplicar_promocion(compras):
    promocion_clientes = []

    for cliente, monto in compras.items():
        if monto >= 150:
            promocion_clientes.append(cliente)
    return promocion_clientes


clientes_promocion = aplicar_promocion(compras)
print(clientes_promocion)
