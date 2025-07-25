def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

# Llamadas de ejemplo
suma(2, 5, 7)        # Imprime 14
suma(2, 5)           # Imprime 7
suma(2, 8, 7, 45, 32)  # Imprime 94