saludo = "Hola global"         # (1) Variable global, de tipo str

def saludar():
    global saludo              # (2) Indica que usamos la 'saludo' global
    saludo = "Hola Mundo"      # (3) Modifica la variable global

def saludaChanchito():
    saludo = 24                # (4) Aquí se crea una variable local 'saludo', no toca la global
    print(saludo)              # imprime 24

# ---- flujo principal ----

resultado1 = saludo + 3       # (5) ¡Error! estás intentando sumar str + int  
print(resultado1)
saludar()                      # (6) Ahora la variable global 'saludo' vale "Hola Mundo"
resultado2 = saludo + 3       # (7) ¡Mismo error: str + int!
print(saludo)                 # (8) Esto sí funcionaría y mostraría "Hola Mundo"