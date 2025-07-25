class CajaRegistradora:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({'Nombre': nombre, 'Precio': precio})

    def obtener_total(self):
        return sum(producto['Precio'] for producto in self.productos)

    def dar_cambio(self, pago):
        total = self.obtener_total()
        if pago < total:
            raise ValueError("Pago insuficiente.")
        return pago - total


caja = CajaRegistradora()
caja.agregar_producto('Manzana', 0.5)
caja.agregar_producto('Pan', 1.0)
print('Total:', caja.obtener_total())
print('Cambio:', caja.dar_cambio(2))
try:
    print('Cambio:', caja.dar_cambio(1))
except ValueError as e:
    print("ValueError:", e)
