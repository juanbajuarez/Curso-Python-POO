# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: Now you have to write a function that takes an argument and
# returns the square of it.

def square(n)->int:
    """
    Función que calcula el cuadrado de un número.
    :param n: Número entero.
    :return: El cuadrado del número ingresado.
    """
    cuadrado=n**2
    return cuadrado


#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(square(2))
    print(square(50))
    print(square(1))