# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: Take an array and remove every second element from the array.
# Always keep the first element and start removing with the next element.

def remove_every_other(my_list)->list:
    """
    Función que elimina los segundos elementos de la lista.
    :param my_list: Lista de elementos.
    :return: Lista sin los segundos elemtos
    """
    tam = len(my_list)
    lista = []

    for i in range(tam):
        if i % 2 == 0:
            lista.append(my_list[i])

    return lista


#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
    print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(remove_every_other([[1, 2]]))