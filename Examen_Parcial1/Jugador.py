# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Examen Primer parcial
# Jugadores

class Jugador:

    def __init__(self,nombre:str,numero:int,goles:int=0):
        self._nombre=nombre
        self._numero=numero
        self._goles=goles
    def anotar_goles(self,no_goles:int)->None:
        self._goles+=no_goles

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def goles(self) -> int:
        return self._goles

    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    @numero.setter
    def numero(self, numero: int):
        self._numero = numero

    @goles.setter
    def goles(self, goles: int):
        self._goles = goles
    def __str__(self)->str:
        return f"Jugador:(Nombre:{self._nombre},numero:{self._numero},goles:{self._goles})"

if __name__ == '__main__':
    pass