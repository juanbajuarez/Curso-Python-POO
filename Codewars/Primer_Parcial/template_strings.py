# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Template Strings, this kata is mainly aimed at the new JS ES6 Update introducing Template Strings
# Task
# Your task is to return the correct string using the Template String Feature.
# Input
# Two Strings, no validation is needed.
# Output
# You must output a string containing the two strings with the word ```' are '```


def temple_strings(obj, feature)->str:
    """

    :param obj:Primer parte de la cadena
    :param feature: Segunda parte de la cadena.
    :return: Cadena concatenada agregando él are
    """
    return f'{obj} are {feature}'
if __name__ == '__main__':
    """
    Código dado por Codewars.
    import codewars_test as test
    from solution import temple_strings
    
    @test.describe('Example Tests')
    def example_tests():
        test.assert_equals(temple_strings("Animals","Good"), 'Animals are Good')
        test.assert_equals(temple_strings("Animals","Good"), 'Animals are Good')
        test.assert_equals(temple_strings("You","Special"), 'You are Special')
        test.assert_equals(temple_strings("lives","frozen"), 'lives are frozen')
    """
    # Mi código para hacer pruebas.
    print(temple_strings("lives","frozen"))
    print(temple_strings("Animals","Good"))
    print(temple_strings("You","Special"))
    print(temple_strings("lives","frozen"))