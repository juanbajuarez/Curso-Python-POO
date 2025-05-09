# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: Write function RemoveExclamationMarks which removes all
# exclamation marks from a given string.

def remove_exclamation_marks(s):
    cadena = s.replace('!', '')  # .replace sustituye el primer argumento por el
    # segundo
    return cadena


#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.

    print(remove_exclamation_marks("Hello World!"))
    print(remove_exclamation_marks("Hello World!!!"))
    print(remove_exclamation_marks("Hi! Hello!"))