compras = {
    'Cliente1': 200,
    'Cliente2': 100,
    'Cliente3': 180,
}


def aplicar_promocion(compras):
    clientes_con_promocion = [cliente for cliente,
                              monto in compras.items() if monto >= 150]
    cuentas_cliente_con_promocion = {
        cliente: monto for cliente, monto in compras.items() if monto > 150}

    for cliente, monto in cuentas_cliente_con_promocion.items():
        cuentas_cliente_con_promocion[cliente] = round(monto * 0.9, 2)

    return [clientes_con_promocion, cuentas_cliente_con_promocion]


clientes_promocion = aplicar_promocion(compras)
print(clientes_promocion)
