class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


class Coche(Vehiculo):
    def descripcion(self):
        return f"Coche: - {super().descripcion()}"


class Moto(Vehiculo):
    def descripcion(self):
        return f"Moto: - {super().descripcion()}"


class Bicicleta(Vehiculo):
    def descripcion(self):
        return f"Bicicleta: - {super().descripcion()}"


coche = Coche("Nissan", "Versa")
moto = Moto("Yamaha", "MT-07")
bicicleta = Bicicleta("Giant", "Escape 3")

print(coche.descripcion)
print(moto.descripcion)
print(bicicleta.descripcion)
