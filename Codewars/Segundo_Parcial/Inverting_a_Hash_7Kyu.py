# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: Given a Hash made up of keys and values, invert the
# hash by swapping them.

def invert_hash(dictionary)-> dict:
    """
    Función que invierte los datos de un diccionario.
    :param dictionary: Diccionário con datos.
    :return: Diccionario con los datos invertidos.
    """
    invertido = {}
    for key, value in dictionary.items():
        invertido[value] = key
    return invertido


#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.

    print(invert_hash({'hello':'world'}))
    print(invert_hash({'a':1, 'b':2, 'c':3}))