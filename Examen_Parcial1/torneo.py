# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Examen Primer parcial
# Torneo
from Jugador import Jugador
from Equipo import Equipo


class Torneo:
    def __init__(self,nombre:str,equipos:list[Jugador]):
        self._nombre=nombre
        self._equipos=equipos
    def agregar_equipos(self,*equipos:tuple[Equipo])->None:
        pass
    def eliminar_equipos(self,*equipos:tuple[Equipo])->None:
        pass
    def mostrar_equipo(self)->None:
        pass
    def general_rol(self)->None:
        pass
    def __str__(self)->str:
        return f"Torne:(Nombre:{self._nombre}, Equipos:{self._equipos})"