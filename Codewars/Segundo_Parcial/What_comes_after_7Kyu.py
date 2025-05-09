# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: You will be given two inputs: a string of words and a letter.
# For each string, return the alphabetic character after every instance of
# letter(case insensitive).
# If there is a number, punctuation or underscore following the letter, it
# should not be returned.
from numpy.core.defchararray import lower

def comes_after(st, l)->str:
    """
    Función que devuelve una cadena con los caracteres posteriores del
    carácter dado.
    :param st: Cadena de carácteres
    :param l: Carácter cualquiera
    :return: Cadena con los caracteres que le siguen al carácter dado.
    """
    letras = ""
    tam = len(st)
    carac= str(l)

    for i in range(tam - 1):
        if st[i] ==carac.lower() or st[i] ==carac.upper():
            siguiente = st[i + 1]
            if siguiente.isalpha():
                letras += siguiente
    return letras

#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(comes_after("Pirates say arrrrrrrrr.",'r'))
    print(comes_after("Free coffee for all office workers!", 'F'))
    print(comes_after("king kUnta is the sickest rap song ever kNown k!", 'k'))