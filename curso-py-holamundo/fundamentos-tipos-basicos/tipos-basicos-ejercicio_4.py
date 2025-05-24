# Ejercicio 4: Formateador de Nombres

nombre = input("¿Cual es tu nombre? ").strip().capitalize()
segundo_nombre = input("¿Cual es tu segundo nombre? ").strip().capitalize()
primer_apellido = input("¿Cual es tu primer apellido? ").strip().capitalize()
segundo_apellido = input("¿Cual es tu segundo apellido? ").strip().capitalize()

NOMBRE_COMPLETO = f"{nombre} {segundo_nombre} {primer_apellido} {segundo_apellido}".replace(
    "  ", " ").strip()
print(NOMBRE_COMPLETO)
