# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: You take your son to the forest to see the monkeys. You know that
# there are a certain number there (n), but your son is too young to just appreciate
# the full number, he has to start counting them from 1.
# As a good parent, you will sit and count with him. Given the number (n), populate
# an array with all numbers up to and including that number, but excluding zero.


def monkey_count(n)->list:
    """
    Funcion que crea una lista con los números del 1 al n.
    :param n: Último número de la lista.
    :return: Lista con los números del 1 al n.
    """
    cadena=[]
    for i in range(1,n+1):
        cadena.append(i)
    return cadena


#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(monkey_count(3))
    print(monkey_count(5))
    print(monkey_count(9))
    print(monkey_count(10))