# 01‑funciones.py

def hola(nombre, apellido="Feliz"):
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")

# Llamadas a la función
hola("Nicolas", "Schurmann")  # apellido explícito
hola("Chanchito")             # usa el apellido por defecto "Feliz"


hola(apellido="Chanchito", nombre="Wolfgman")