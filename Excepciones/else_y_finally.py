try:
    n1 = int(input("Ingresa primer número: "))
except Exception as e:
    print("Error.")
else:
    print("Solo si no hay errores.")
finally:
    print("Siempre se ejecuta.")
