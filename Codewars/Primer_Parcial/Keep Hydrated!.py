# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción:Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.

def litres(time)->int:
    """
    Función que calcula los litros de agua que debe tomar en relación con el tiempo de ejercicio.
    :param time: Tiempo de ejercicio.
    :return: Litro de agua que debe tomar.
    """
    return time // 2

#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.

    print("Litros: ",litres(0))
    print("Litros: ",litres(1))
    print("Litros: ",litres(2))
    print("Litros: ",litres(3))
    print("Litros: ",litres(4))
    print("Litros: ",litres(1.4))
    print("Litros: ",litres(12.3))
    print("Litros: ",litres(0.82))
    print("Litros: ",litres(11.8))
    print("Litros: ",litres(1787))