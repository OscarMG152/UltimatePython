class Caminador:
    def caminar(self):
        print("Caminando.")


class Volador:
    def volar(self):
        print("Volando.")


class Nadador:
    def nadar(self):
        print("Nadando.")


class Pato(Caminador, Volador, Nadador):
    def programar(self):
        print("Programando.")
