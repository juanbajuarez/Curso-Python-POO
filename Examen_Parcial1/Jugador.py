# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Examen Primer parcial

class Jugador:

    def __init__(self,nombre:str,numero:int,goles:int=0):
        self._nombre=nombre
        self._numero=numero
        self._goles=goles
    def anotar_goles(self,no_goles:int)->None:
        self._goles+=no_goles
    def __str__(self)->str:
        return f"Jugador:(Nombre:{self._nombre},numero:{self._numero},goles:{self._goles})"

if __name__ == '__main__':
    """
    valores prueba...
    """
    juan=Jugador("Juan",5)
    print(juan)
    juan.anotar_goles(5)
    print(juan)