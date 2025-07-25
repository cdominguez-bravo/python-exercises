def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado    # ← dentro del for, se ejecuta en la primera pasada

print("chanchito")
l = largo("Hola Mundo")
print(l)  # imprime 1