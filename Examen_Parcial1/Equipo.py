# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Examen Primer parcial

from Jugador import Jugador

class Equipo:
    id=1
    def __init__(self,nombre:str,jugadores:list[Jugador]):
        self._nombre=nombre
        self._jugadores=jugadores
        self._id_equipo=Equipo.id
        Equipo.id+=1
    def __str__(self):
        return f"Equipo({self._nombre}{self._jugadores}{self._id_equipo})"

if __name__ == '__main__':
    juan = Jugador("Juan", 5)
    print(juan)
    juan.anotar_goles(5)
    print(juan)
    lista=[]
    cefor=Equipo("Cefors",lista)
    print(cefor)
    atom = Equipo("Atom", lista)
    print(atom)