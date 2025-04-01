# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: You forgot to count the number of toast you put
# into there, you don't know if you  put exactly six pieces of
# toast into the toasters. Define a function that counts how
# many more (or less) pieces of toast you need in the toasters.
# Even though you need more or less, the number will still be
# positive, not negative.

def six_toast(num)->int:
    """
    Función que calcula cuantas tostadas le faltan por tostar.
    :param num: numero de tostadas.
    :return: numero de tostadas que le faltan.
    """
    return abs(num-6)
#Código a nivel de módulo.
if __name__ == '__main__':
    # Mi código para hacer pruebas.
    print(six_toast(15))
    print(six_toast(6))
    print(six_toast(3))