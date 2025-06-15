# Autor: Juan Bautista Juárez
# Fecha: Junio de 2025
# Descripción:Check if it is a vowel(a, e, i, o, u,) on the n position
# in a string (the first argument). Don't forget about uppercase.
# A few cases:
# checkVowel('cat', 1)  ->   true // 'a' is a vowel


def check_vowel(strng, position)->bool:
    """
    Funcion que verifica que una vocal está en la posición dada
    :param strng: Cadena de caracteres.
    :param position: Posición donde se verificará si está una vocal.
    :return: Valor bool sí se encontró la vocal en la posición indicada.
    """
    long=len(strng)
    strng=strng.lower()
    vocales=['a','e','i','o','u']
    if position>=long or position<0:
        return False
    if strng[position] in vocales:
        return True
    else:
        return False

#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(check_vowel('cat', 1))
    print(check_vowel('cat', 0))
    print(check_vowel('Amanda', 0))