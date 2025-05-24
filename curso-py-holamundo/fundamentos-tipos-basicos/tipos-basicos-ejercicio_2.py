# Ejercicio 2: Conversor de Divisas

moneda_local = float(input("Introduce la cantidad de tu moneda local: "))
cantidad_usd = moneda_local * 0.050
cantidad_eur = moneda_local * 0.047
cantidad_gbp = moneda_local * 0.039
cantidad_jpy = moneda_local * 7.71

print(f"{moneda_local} en tu moneda local es {cantidad_usd:.2f} en USD")
print(f"{moneda_local} en tu moneda local es {cantidad_eur:.2f} en EUR")
print(f"{moneda_local} en tu moneda local es {cantidad_gbp:.2f} en GBP")
print(f"{moneda_local} en tu moneda local es {cantidad_jpy:.2f} en JPY")
