# Autor: Juan Bautista Juárez
# Fecha: 27 de Marzo de 2025
# Descripción: You will be given an array a and a value x.
# All you need to do is check whether the provided array contains the value.
# a can contain numbers or strings. x can be either.
# Return true if the array contains the value, false if not.


def check(seq, elem)->bool:
    """
    Función que busca un número en una cadena.
    :param seq: Una secuencia de números.
    :param elem: Elemento a buscar en la secuencia de números
    :return: Valor bool que indica si existe o no el elemento en la secuencia.
    """
    if elem in seq:
        return True
    else:
        return False

#Código a nivel de módulo.
if __name__ == '__main__':

    # Mi código para hacer pruebas.
    print(check([66, 101], 66))
    print(check([78, 117, 110, 99, 104, 117, 107, 115], 8))
    print(check([101, 45, 75, 105, 99, 107], 107))
    print(check([66, 101], 66))
    print(check([66, 101], 66))
    print(check([66, 101], 66))
    print(check([66, 101], 66))
    print(check([66, 101], 66))
    print(check([66, 101], 66))
    print(check([66, 101], 66))
