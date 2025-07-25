def division(n=0):
    if n == 0:
        raise ZeroDivisionError(
            f"No es posible dividir entre {n}.", f"Intente con un número distinto.")
    return 5/n


try:
    division()
except ZeroDivisionError as e:
    print(e)
