# Autor: Juan Bautista Juárez
# Fecha: 17 de Marzo de 2025
# Descripción: You are an intern working in the software development department of the X-COM agency, responsible
# for fighting off a large-scale invasion of extraterrestrials. Your task for today is described with the bug report below:
# Pilots have reported discrepancies in their flight logs after returning from interception missions. The travel distance
# logged in the logistics software does not match actual flight paths, potentially leading to incorrect fuel calculations
# and errors in planning of future missions.

def travel_distance(avg_speed, travel_time)->float:
    """
    Función que calcula la distancia de un viaje con base a la velocidad y tiempo de viaje.
    :param avg_speed: Velocidad del viaje.
    :param travel_time: Tiempo de viaje.
    :return: Distancia en KM.
    """
    KM_PER_MILE = 1.852
    travel_hours = travel_time / 60
    travel_miles = avg_speed * travel_hours
    travel_kms = travel_miles * KM_PER_MILE
    return travel_kms

#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.

    print("Km: ",travel_distance(0, 0))
    print("Km: ",travel_distance(600, 60))
    print("Km: ",travel_distance(800, 60))
