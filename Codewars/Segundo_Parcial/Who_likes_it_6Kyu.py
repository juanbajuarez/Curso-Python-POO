# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items. We want to create the
# text that should be displayed next to such an item.
# Implement the function which takes an array containing the names of people
# that like an item. It must return the display text as shown in the examples:

def likes(names)->str:
    """
    Función que agrega likes a una lista de personas.
    :param names: Lista de personas.
    :return: Cadena con nombres y likes.
    """
    largoC = len(names)
    if largoC == 0:
        return "no one likes this"
    elif largoC == 1:
        return f"{names[0]} likes this"
    elif largoC == 2:
        return f"{names[0]} and {names[1]} like this"
    elif largoC == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {largoC - 2} others like this"

#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(likes([]))
    print(likes(["Peter"] ))
    print(likes(["Jacob", "Alex"] ))
    print(likes(["Max", "John", "Mark"]))
    print(likes(["Alex", "Jacob", "Mark", "Max"]))

