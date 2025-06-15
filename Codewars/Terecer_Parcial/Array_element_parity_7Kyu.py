# Autor: Juan Bautista Juárez
# Fecha: Junio de 2025
# Descripción: In this Kata, you will be given an array of
# integers whose elements have both a negative and a positive
# value, except for one integer that is either only negative or
# only positive. Your task will be to find that integer.
# Examples:
# [1, -1, 2, -2, 3] => 3
# 3 has no matching negative appearance

def solve(arr)->int:
    """
    Función que encuentra el numero que no tiene su opuesto positivo o negativo.
    :param arr:Cadena de enteros positivos y negativos
    :return: Número que no tiene su número opuesto positivo o negativo.
    """
    num=None
    for a in arr:
        if not a * -1 in arr:
            num = a
            break
    return num


#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(solve([-3, 1, 2, 3, -1, -4, -2]))
    print(solve([1, -1, 2, -2, 3, 3]))
    print(solve([-9, -105, -9, -9, -9, -9, 105]))
    print(solve([-110, 110, -38, -38, -62, 62, -38, -38, -38]))