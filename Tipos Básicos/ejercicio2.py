local = float(input("Ingrese la cantidad de dinero en moneda local: "))

usd = local * 0.050
eur = local * 0.047
gbp = local * 0.039
jpy = local * 7.71

print(f"La cantidad de {local} en moneda local es: {usd: .2f} en USD.")
print(f"La cantidad de {local} en moneda local es: {eur: .2f} en EUR.")
print(f"La cantidad de {local} en moneda local es: {gbp: .2f} en GBP.")
print(f"La cantidad de {local} en moenda local es: {jpy: .2f} en JPY.")
