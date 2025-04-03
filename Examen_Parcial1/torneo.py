# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Examen Primer parcial
# Torneo
from typing import Tuple

from Equipo import Equipo
from Jugador import Jugador

class Torneo:
    """
    Declaración de la clase Torneo
    """
    def __init__(self,nombre:str,*equipos:tuple[Equipo]):
        """
        Inciación del constructor
        :param nombre: Nombre del torneo
        :param equipos: Nombre de los equipos
        """
        self._nombre=nombre
        self._equipos=list(equipos)

    def agregar_equipos(self,*equipos:tuple[Equipo])->None:
        """
        Métod0 para agregar equipos al torneo.
        :param equipos: NOmbre de los equipos que se agragaran.
        :return: None
        """
        #En Python, extend() es una función que permite extender una
        # lista con los elementos de otra lista, tupla, cadena,
        # conjunto, etc.
        self._equipos.extend(equipos)

    def eliminar_equipos(self,*equipos:tuple[Equipo])->None:
        """
        Métod0 para eliminar equipos del torneo.
        :param equipos: Nombre de los equipos a eliminar
        :return: None
        """
        for equipo in equipos:
            if equipo in self._equipos:
                self._equipos.remove(equipo)
    def mostrar_equipo(self)->None:
        """
        Métod0 que muestra los equipos del torneo.
        :return: None
        """
        if self._equipos:
            for equipo in self._equipos:
                print(equipo)
        else:
            print("No hay equipos en el torneo.")
    def generar_rol(self,)->None:
        """
        Métod0 que genera el rol de juegos.
        :return: None
        """
        if len(self._equipos) < 2:
            print("El torneo necesita al menos dos equipos para generar el rol.")
            return

        partidos = []
        for i in range(len(self._equipos)):
            for j in range(i + 1, len(self._equipos)):
                equipo1 = self._equipos[i]
                equipo2 = self._equipos[j]
                partidos.append((equipo1._nombre, equipo2._nombre))

        num_jornadas = len(self._equipos) - 1
        jornadas = {i: [] for i in range(1, num_jornadas + 1)}

        num_jornada = 1
        for partido in partidos:
            if num_jornada > num_jornadas:
                num_jornada = 1
            jornadas[num_jornada].append(partido)
            num_jornada += 1

        print(f"\nTabla de partidos para el Torneo: {self._nombre}")
        for jornada, partidos_jornada in jornadas.items():
            print(f"\nJornada {jornada}:")
            for partido in partidos_jornada:
                print(f"{partido[0]} vs {partido[1]}")
    def __str__(self)->str:
        """
        Métod0 magico
        :return:Cadena con los atributos de la clase Torneo.
        """
        equipos_nombres = ", ".join([equipo._nombre for equipo in self._equipos])
        return f"Torneo({self._nombre}, Equipos:{equipos_nombres})"
#Código a nivel de módulo.
if __name__ == '__main__':
    pass