# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción:You are required to create a simple calculator that returns the result of
# addition, subtraction, multiplication or division of two numbers.
# Your function will accept three arguments:
# The first and second argument should be numbers.
# The third argument should represent a sign indicating the operation to perform on these two numbers.
# if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.

def calculator(x, y, op)-> int or str:
    """
    Función que implementa una calculadora validando que sean datos correctos.
    :param x: Primer número.
    :param y: Segundo número.
    :param op:Signo de la operación.
    :return: El resultado de la operación.
    """
    if isinstance(x, int) and isinstance(y, int):
        if op == '+' or op == '-' or op == '*' or op == '/':
            if op == '+':
                return x + y
            elif op == '-':
                return x - y
            elif op == '*':
                return x * y
            else:
                if y != 0:
                    return x / y
                else:
                    return ("unknown value")
        else:
            return ("unknown value")
    else:
        return ("unknown value")

#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.

    print(calculator(6, 2, '+'))
    print(calculator(4, 3, '-'))
    print(calculator(5, 5, '*'))
    print(calculator(5, 4, '/'))
    print(calculator(6, 2, '&'))