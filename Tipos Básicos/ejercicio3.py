pago = float(input("Ingrese el monto del pago del producto: "))
costo = float(input("Ingrese el costo del producto: "))

cambio = pago - costo

print(f"Tu cambio es de {cambio: .2f}")
