class OverheatingError(Exception):
    "Esta clase es para representar un error de temperatura alta."

    def __init__(self, mensaje):
        self.mensaje = mensaje


def temperatura_cpu(temp):
    if temp >= 100:
        raise OverheatingError(
            'Error: La temperatura de la CPU ha alcanzado el límite crítico de 100°C.')
    elif temp >= 90:
        print(f"Advertencia: La temperatura de la CPU ({temp}°C) es muy alta.")
    elif temp >= 75:
        print(f"Advertencia: La temperatura de la CPU ({temp}°C) es elevada.")
    else:
        print('La temperatura de la CPU se encuentra normal.')


try:
    temperatura_actual = 60
    temperatura_cpu(temperatura_actual)
except OverheatingError as e:
    print(e)
