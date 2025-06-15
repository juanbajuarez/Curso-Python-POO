# Autor: Juan Bautista Juárez
# Fecha: Junio de 2025
# Descripción: A triangle number n is an integer such that n
# objects can be arranged into an equilateral triangle.
# For example, 6 is a triangle number because you can arrange
# 6 objects into an equilateral triangle:
#   1
#  2 3
# 4 5 6

import math
def is_triangle_number(number: int) -> bool:
    """
    Función que dice si un número es triangular o no.
    :param number: numero entero
    :return: Bool que describe si el número es triangular o no.
    """
    if number==0 or number==1:
        return True
    else:
        x = 8 * number + 1
        raiz = math.isqrt(x)
        if raiz*raiz==x:
            return True
        else:
            return False

#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(is_triangle_number(3))
    print(is_triangle_number(5))
    print(is_triangle_number(8))
    print(is_triangle_number(10))
    print(is_triangle_number(20))
    print(is_triangle_number(1))
    print(is_triangle_number(0))
    print(is_triangle_number(779376))