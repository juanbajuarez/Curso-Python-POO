# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: Given an integer (1 <= n <= 100) representing a person's age,
# return their minimum and maximum age range.
# This equation doesn't work when the age <= 14, so if the age <= 14, use this
# equation instead:
# min = age - 0.10 * age
# max = age + 0.10 * age
# You should floor all your answers so that an integer is given instead of a float
# (which doesn't represent age). Return your answer in the form "[min]-[max]"

def dating_range(age)->str:
    """
    Función que calcula el rango ideal para una cita según tu edad.
    :param age: Edad de la persona
    :return: Rango de edad de las personas con las que puedes salir.
    """
    if age <= 14:
        min = age - 0.10 * age
        max = age + 0.10 * age
    else:
        min = age / 2 + 7
        max = 2 * (age - 7)

    return f"{int(min)}-{int(max)}"


#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(dating_range(17))
    print(dating_range(40))
    print(dating_range(15))