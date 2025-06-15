# Autor: Juan Bautista Juárez
# Fecha: Junio de 2025
# Descripción:Since Fahrenheit never lived the world kept on
# using the Rømer scale, invented by fellow Dane Ole Rømer
# to this very day, skipping over the Fahrenheit and Celsius
# scales entirely.
#
# Your magnum opus contains several thousand references to
# temperature, but those temperatures are all currently in
# degrees Celsius. You don't want to convert everything by
# hand, so you've decided to write a function that takes a
# temperature in degrees Celsius and returns the equivalent
# temperature in degrees Rømer. Fortunately, you remember that
# the function for converting is pretty simple and it looks
# like this:

# ∘Rø= 21/40 ∘C + 7.5

def celsius_to_romer(temp)->float:
    """
    Función que convierte grados centígrados a grados rome.
    :param temp:Temperatura en grados centígrados
    :return: Temperatura en grados rome
    """
    return (21 / 40) * temp + 7.5


#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(celsius_to_romer(24))
    print(celsius_to_romer(8))
    print(celsius_to_romer(29))