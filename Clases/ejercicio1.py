class CajaRegistradora:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({'nombre': nombre, 'precio': precio})

    def obtener_total(self):
        return sum(producto['precio'] for producto in self.productos)

    def listar_productos(self):
        return self.productos

    def dar_cambio(self, pago):
        total = self.obtener_total()
        if pago < total:
            print("Pago insuficiente")
        self.productos = []
        return pago - total


caja = CajaRegistradora()

caja.agregar_producto('Manzana', 0.5)
print('Total:', caja.obtener_total())
caja.agregar_producto('Pan', 1.0)

print('Total:', caja.obtener_total())
print('Cambio:', caja.dar_cambio(2.0))
print('Total:', caja.obtener_total())
print(caja.listar_productos())
