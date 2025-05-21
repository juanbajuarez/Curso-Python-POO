# Autor: Juan Bautista Juárez
# Fecha: 26 de Marzo de 2025
# Descripción: Bob needs a fast way to calculate the volume
# of a rectangular cuboid with three values: the length, width
# and height of the cuboid. Write a function to help Bob
# with this calculation.

def get_volume_of_cuboid(length, width, height)->int:
    """
    Función que calcula el volumen de un cuboide.
    :param length: Largo del cuboide.
    :param width: Ancho del cuboide.
    :param height: Alto del cuboide.
    :return: El volumen del cuboide
    """
    return int (length * width * height)

#Código a nivel de módulo.
if __name__ == '__main__':
    # Mi código para hacer pruebas.
    print(get_volume_of_cuboid(1, 2, 2))
    print(get_volume_of_cuboid(6.3, 2, 5))