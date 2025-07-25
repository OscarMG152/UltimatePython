class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print("Guau")

    @classmethod
    def factory(cls):
        return cls("Luna", 5)
