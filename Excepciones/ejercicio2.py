class WithdrawalError(Exception):
    "Esta clase es para representar un error de retiro de efectivo."

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo


class CuentaBancaria:
    def __init__(self, mensaje, codigo, saldo=0):
        self.mensaje = mensaje
        self.codigo = codigo
        self.saldo = saldo

    def deposito(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito realizado con éxito. Nuevo saldo: ${self.saldo}.")
        else:
            print("La cantidad de depósito debe ser positiva.")

    def retiro(self, cantidad):
        if cantidad <= 0:
            raise WithdrawalError(
                "La cantidad de retiro debe ser positiva.", 401)
        elif cantidad > self.saldo:
            raise WithdrawalError(
                "Fondos insuficientes para realizar el retiro.", 400)
        else:
            self.saldo -= cantidad
            print(f"Retiro realizado con éxito. Nuevo saldo: ${self.saldo}.")

    def mostrar_saldo(self):
        print(f"Saldo actual: ${self.saldo}.")


try:
    cuenta = CuentaBancaria("123456789", "Juan", 1000)
    cuenta.mostrar_saldo()
    cuenta.retiro(700)
    cuenta.deposito(500)
    cuenta.retiro(2000)
except WithdrawalError as e:
    print(e)

try:
    cuenta.retiro(-100)
except WithdrawalError as e:
    print(e)
