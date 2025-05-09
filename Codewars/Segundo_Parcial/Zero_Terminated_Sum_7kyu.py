# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: Mary has another puzzle book, and it's up to you to help
# her out! This book is filled with zero-terminated substrings, and you have
# to find the substring with the largest sum of its digits. For example,
# one puzzle looks like this: "72102450111111090"
# Here, there are 4 different substrings: 721, 245, 111111, and 9. The sums
# of their digits are 10, 11, 6, and 9 respectively. Therefore, the substring
# with the largest sum of its digits is 245, and its sum is 11.


def largest_sum(s)->int:
    """
    Función que encuentra la sumatoria más grande de la subcadena separada por ceros.
    :param s:Cadena de números.
    :return: Entero correspondiente a la suma más grande de las subcadenas.
    """
    subcadena = s.split('0')
    sumas = []
    for i in range(len(subcadena)):
        if subcadena[i]:
            suma = 0
            for d in subcadena[i]:
                num = int(d)
                suma += num
        else:
            suma = 0

        sumas.append(suma)
    return max(sumas)

#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(largest_sum("72102450111111090"))
    print(largest_sum("123004560"))
    print(largest_sum("0"))