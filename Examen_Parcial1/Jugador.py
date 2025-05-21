# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Examen Primer parcial
# Jugadores.

class Jugador:
    """
    Declaración de la clase jugador
    """

    def __init__(self,nombre:str,numero:int,goles:int=0):
        """
        Implementación del constructor.
        :param nombre: Nombre del jugador
        :param numero: Número del jugador
        :param goles: Número de goles inicia en 0.
        """
        self._nombre=nombre
        self._numero=numero
        self._goles=goles
    def anotar_goles(self,no_goles:int)->None:
        """
        Métod0 para sumar goles a un jugador
        :param no_goles: Número de goles que incrementará un jugador
        :return: None
        """
        self._goles+=no_goles
    # Métodos sets y gets
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
        """
        Métod0 mágico.
        :return: Cadena con los atributos de la clase Jugador.
        """
        return f"Jugador:(Nombre:{self._nombre},numero:{self._numero},goles:{self._goles})"

if __name__ == '__main__':
    pass