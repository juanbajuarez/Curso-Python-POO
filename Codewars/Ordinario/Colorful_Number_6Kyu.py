# Autor: Juan Bautista Juárez
# Fecha: Junio de 2025
# Descripción: Determine whether a non-negative integer
# number is colorful or not.
# 263 is a colorful number because [2, 6, 3, 2*6, 6*3, 2*6*3]
# are all different; whereas
# 236 is not colorful, because [2, 3, 6, 2*3, 3*6, 2*3*6]
# has 6 twice.
# So take all consecutive subsets of digits, take their
# products, and ensure all the products are different.

def colorful(number):
    cadena = str(number)
    productos = []
    tam=len(cadena)

    for i in range(tam):
        producto = 1
        for j in range(i,tam):
            digito = int(cadena[j])
            producto = producto * digito
            if producto in productos:
                return False
            productos.append(producto)
    return True

#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(colorful(5))
    print(colorful(23))
    print(colorful(50))
    print(colorful(13))
    print(colorful(236))