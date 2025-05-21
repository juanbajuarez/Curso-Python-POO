# Autor: Juan Bautista Juárez
# Fecha: 19 de Marzo de 2025
# Descripción: The method is supposed to remove even numbers from the list and return
# a list that contains the odd numbers.
# However, there is a bug in the method that needs to be resolved.

def kata_13_december(lst)->list[int]:
    """
    Función que retorna una lista de números impares dentro de una lista.
    :param lst: Lista de números.
    :return: Lista de números impares.
    """
    impares=[]
    for i in range(0,len(lst)):
        if lst[i]%2==1:
            impares.append(lst[i])
    return impares

#Código a nivel de módulo.
if __name__ == '__main__':
    # Mi código para hacer pruebas.

    print(kata_13_december([1, 2, 2, 2, 4, 3, 4, 5, 6, 7]))
    print(kata_13_december([1, 2, 2, 2, 4, 3, 4]))





