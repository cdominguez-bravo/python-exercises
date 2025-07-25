def get_product(**datos):
    """
    Imprime el id y nombre de un producto recibido como argumentos keyword.
    """
    print(datos["id"], datos["name"])

# Ejemplos de llamadas:
get_product(id="23", name="iPhone", desc="Esto es un iPhone")