# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Examen Primer parcial
# Equipo
from typing import Tuple

from Jugador import Jugador

class Equipo:
    id=1
    def __init__(self,nombre:str,jugadores:list[Jugador]):
        self._nombre=nombre
        self._jugadores=jugadores
        self._id_equipo=Equipo.id
        Equipo.id+=1
    def agregar_jugadores(self,*jugadores:Tuple[Jugador])->None:
        pass
    def remover_jugadores(self,*jugadores:Tuple[Jugador])->None:
        pass
    def mostrar_jugadores(self)->None:
        pass
    def total_goles(self)->None:
        pass
    def __str__(self):
        return f"Equipo({self._nombre}{self._jugadores}{self._id_equipo})"

if __name__ == '__main__':
    juan = Jugador("Juan", 5)
    ivan = Jugador("Ivan", 5)
    luis = Jugador("luis", 5)
    guille = Jugador("guille", 5)
    lista=[]
    lista.append(juan._nombre)
    lista.append(ivan._nombre)
    lista.append(luis._nombre)
    lista.append(guille._nombre)
    print(lista)
    cefor=Equipo("Cefors",lista)
    print(cefor)
    atom = Equipo("Atom", lista)
    print(atom)