class Animal:
    def comer(self):
        print("Comiendo.")

# Herencia


class Perro(Animal):
    def pasear(self):
        print("Paseando.")

# class Chanchito(Animal):
#     def programar(self):
#         print("Programando.")

# Herencia multi-nivel


class Chanchito(Perro):
    def programar(self):
        print("Programando.")
