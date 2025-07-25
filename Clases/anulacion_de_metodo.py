class Ave:
    def __init__(self):
        self.volador = "Volador"

    def vuela(self):
        print("Vuela Ave")


class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = "Nadador"

    def nada(self):
        print("Vuela Pato")


pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)
