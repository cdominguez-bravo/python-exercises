def no_space(texto):
    """
    Quita todos los espacios de la cadena.
    """
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    """
    Devuelve la cadena dada en sentido inverso.
    """
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    """
    Devuelve True si 'texto' (ignorando espacios y mayúsculas/minúsculas)
    es igual a su reverso.
    """
    # 1) Quitamos espacios
    limpio = no_space(texto)
    # 2) Invertimos
    al_reves = reverse(limpio)
    # 3) Comparamos en minúsculas
    return limpio.lower() == al_reves.lower()


# --- Pruebas ---
print(es_palindromo("Amo la paloma"))   # True
print(es_palindromo("Hola Mundo"))      # False