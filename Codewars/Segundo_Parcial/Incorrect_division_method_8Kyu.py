# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: This method, which is supposed to return the result of dividing
# its first argument by its second, isn't always returning correct values. Fix it.

def divide_numbers(x,y):
    #return x // y linea corregida
    return x /y  #Muestra el resultado con decimales


#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.

    print(divide_numbers(4,2))
    print(divide_numbers(10,2))
    print(divide_numbers(9,4))