celcius = input("Ingrese temperatura en Celcius: ")

celcius = int(celcius)

farenheit = (celcius * (9 / 5) + 32)
kelvin = celcius + 273.15

print(f"La temperatura en Celsius es de {celcius}°C")
print(f"La temperatura en Farenheit es de {farenheit}°F")
print(f"La temperatura en Kelvin es de {kelvin}°K")
