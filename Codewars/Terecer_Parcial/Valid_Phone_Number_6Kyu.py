# Autor: Juan Bautista Juárez
# Fecha: Junio de 2025
# Descripción: Write a function that accepts a string, and returns true
# if it is in the form of a phone number.
# Assume that any integer from 0-9 in any of the spots will produce
# a valid phone number.
#
# Only worry about the following format:
# (123) 456-7890 (don't forget the space after the close parentheses)


def valid_phone_number(phone_number):
    if len(phone_number) != 14:
        return False
    indices=[1,2,3,6,7,8,10,11,12,13]
    if phone_number[0]!='(' or phone_number[4]!=')':
        return False
    if phone_number[5]!=' ':
        return False
    if phone_number[9]!='-':
        return False
    for i in indices:
        if  not phone_number[i].isnumeric():
            return False
    return True

#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(valid_phone_number("(123) 456-7890"))
    print(valid_phone_number("(1111)555 2345"))
    print(valid_phone_number("(098) 123 4567"))