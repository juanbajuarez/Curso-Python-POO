# Autor: Juan Bautista Juárez
# Fecha: 23 de Marzo de 2025
# Descripción: Template Strings, this kata is mainly aimed at the new JS ES6 Update introducing Template Strings
# Task
# Your task is to return the correct string using the Template String Feature.
# Input
# Two Strings, no validation is needed.
# Output
# You must output a string containing the two strings with the word ```' are '```


def temple_strings(obj, feature)->str:
    """
    Función que concatena dos palabra agregando are entre ellas.
    :param obj:Primer parte de la cadena
    :param feature: Segunda parte de la cadena.
    :return: Cadena concatenada agregando él are
    """
    return f'{obj} are {feature}'

#Código a nivel de módulo.
if __name__ == '__main__':

    # Mi código para hacer pruebas.
    print(temple_strings("lives","frozen"))
    print(temple_strings("Animals","Good"))
    print(temple_strings("You","Special"))
    print(temple_strings("lives","frozen"))