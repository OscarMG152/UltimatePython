class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau")

    @classmethod
    def factory(cls):
        return cls("Luna", 5)


Perro.habla()
perro = Perro.factory()
print(perro.nombre, perro.edad)
