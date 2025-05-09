# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: Write a function that takes an array of numbers and returns
# the sum of the numbers. The numbers can be negative or non-integer. If the array
# does not contain any numbers then you should return 0.

def sum_array(a)->int:
    """
    Función que suma todos los elementos de un vector.
    :param a: Vector de números
    :return: Entero correspondiente a la suma total.
    """
    suma=sum(a)
    return suma

#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(sum_array([]))
    print(sum_array([1, 2, 3]))
    print(sum_array([1.1, 2.2, 3.3]))