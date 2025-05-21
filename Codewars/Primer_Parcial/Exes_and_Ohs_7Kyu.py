# Autor: Juan Bautista Juárez
# Fecha:  18 de Marzo de 2025
# Descripción: Check to see if a string has the same amount of
# 'x's and 'o's. The method must return a boolean and be case
# insensitive. The string can contain any char.

def xo(s)->bool:
    """
    Función que verifica si existe la misma cantidad de x y x en una
    cadena.
    """
    ban=None
    contx=0
    contO=0
    for pal in s:
        if pal=='x' or pal=='X':
            contx+=1
        elif pal=='o' or pal=='O':
            contO+=1
    if contx==contO:
        ban=True
    else:
        ban=False
    return ban

#Código a nivel de módulo.
if __name__ == '__main__':
    # Mi código para hacer pruebas.
    print(xo("ooxx"))
    print(xo("xooxx"))
    print(xo("ooxXm"))
    print(xo("zpzpzpp"))