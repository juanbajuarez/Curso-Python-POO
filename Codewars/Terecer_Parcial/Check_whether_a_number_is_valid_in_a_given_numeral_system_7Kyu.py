# Autor: Juan Bautista Juárez
# Fecha: Junio de 2025
# Descripción: A numeral system is a way of writing numbers using a
# specific set of digits: for example, the decimal system (also called
# base-10), which is the most commonly used numeral system worldwide,
# uses the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 to represent numbers.
# There is also the binary system (also called base-2), which uses the
# digits 0 and 1.


def validate_base(num: str, base: int) -> bool:
    """
    Función que valída que el número ingresado pertenece a la base dada.
    :param num: Número.
    :param base: Base de la cual se verifica el número.
    :return: Si el número pertenece a la base ingresada.
    """
    caract_validos="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base_car=[]
    for i in range(0,base):
        base_car.append(caract_validos[i])
    print(base_car)
    for n in num:
        if not n in base_car:
            return False
    return True
#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(validate_base('7623',  8))
    print(validate_base('ABCDEF', 16))
    print(validate_base('6124',  5))
    print(validate_base('ABC', 12))
    print(validate_base('Y', 34))
    print(validate_base('0020', 10))