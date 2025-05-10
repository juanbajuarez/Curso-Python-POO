# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: Create a function that takes an integer as an argument and returns
# "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number)->str:
    """
    Función que indica si un número es par o impar.
    :param number: Número a clasificar
    :return: Cadena indicando si es par o impar.
    """
    if number%2==0 or number%-2==0:
        return f"Even"
    else:
        return f"Odd"


#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(even_or_odd(2))
    print(even_or_odd(-2))
    print(even_or_odd(-3))
    print(even_or_odd(3))