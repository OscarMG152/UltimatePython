def cuenta(total, porcentaje_descuento):
    descuento = total * (porcentaje_descuento / 100)
    pago = total - descuento
    return pago


resultado = cuenta(1000, 20)
print(f"El total a pagar es de {resultado}")
