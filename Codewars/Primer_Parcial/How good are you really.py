# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return true if you're better, else false!


def better_than_average(class_points, your_points)->bool:
    """
    Función que compara un promedio individual con el promedio grupal y devuelve un bool para indicar
    si es mayor que el grupal.
    :param class_points: Los puntos del resto del grupo.
    :param your_points: La calificación de un solo alumno
    :return: True si el promedio individual es mayor al grupal.
    """
    prom=sum(class_points)/len(class_points)
    if prom<your_points:
        return True
    else:
        return False
#Código a nivel de módulo.
if __name__ == '__main__':

# Mi código para hacer pruebas.
    print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))
    print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))
    print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))
    print(better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21))
    print(better_than_average([100, 90, 80], 85))
