# Autor: Juan Bautista Juárez
# Fecha: Junio de 2025
# Descripción:Triangular numbers are so called because of the
# equilateral triangular shape that they occupy when laid out
# as dots. i.e.
# 1st (1)   2nd (3)    3rd (6)
#  *          **        ***
#             *         **
#                       *

def triangular(n)->int:
    """
    Función que calcula el número de caracteres (*) que formaran
    el triángulo equilátero
    :param n: Base del triángulo equilátero.
    :return: Numero de caracteres que contendrá.
    """
    if n <= 0:
        return 0
    else:
        return n * (n + 1) // 2

if __name__ == '__main__':
   print(triangular(0))
   print(triangular(2))
   print(triangular(3))
   print(triangular(4))
   print(triangular(9))
   print(triangular(-10))
