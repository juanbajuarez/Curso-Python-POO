# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: Given a string containing a list of integers separated by commas,
# write the function that takes said string and returns a new array / list
# containing all integers present in the string, preserving the order.

def string_to_int_list(s)->list:
    """
    Función que convierte una cadena de números a una lista de números enteros.
    :param s:Cadenas de números
    :return:Lista de números enteros.
    """
    cadena=[]
    s=s.split(',')
    for num in s:
        if num.strip() != '':
            numero = int(num)
            cadena.append(numero)
    return cadena


#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(string_to_int_list("1,2,3,4,5"))
    print(string_to_int_list("21,12,23,34,45"))