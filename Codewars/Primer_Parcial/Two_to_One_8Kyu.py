# Autor: Juan Bautista Juárez
# Fecha: 24 de Marzo de 2025
# Descripción: Take 2 strings s1 and s2 including only letters from
# a to z. Return a new sorted string (alphabetical ascending), the
# longest possible, containing distinct letters - each taken only
# once - coming from s1 or s2.

def longest(a1, a2)->str:
    """
    Funcion que crea una lista de letras repetidas en dos cadenas.
    :param a1: Cadena 1.
    :param a2: Cadena 2.
    :return: Cadena con la union de las cadenas
    """
    a = set(a1.lower())
    b = set(a2.lower())
    cadena = a.union(b)
    cadenaf = ''.join(sorted(cadena))

    return cadenaf

#Código a nivel de módulo.
if __name__ == '__main__':
    # Mi código para hacer pruebas.
    print(longest("aretheyhere", "yestheyarehere"))
    print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
    print(longest("inmanylanguages", "theresapairoffunctions"))