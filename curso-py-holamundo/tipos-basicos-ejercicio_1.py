# Ejercicio 1: Conversor de Temperatura

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"La temperatura ingresada es {celsius} grados C.")
print(f"En Fahrenheit, esto es {fahrenheit} grados F.")
print(f"En Kelvin, esto es {kelvin} K.")
