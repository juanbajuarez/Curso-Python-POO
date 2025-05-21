# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Examen Primer parcial
# Equipo.

from Jugador import Jugador

class Equipo:
    """
    Declaración de la clase Equipo
    """
    id=1
    def __init__(self,nombre:str,*jugadores:tuple[Jugador]):
        """
        Inicialización del constructor.
        :param nombre: Nombre del equipo
        :param jugadores: Jugadores que formaran al equipo
        """
        self._nombre=nombre
        self._jugadores=list(jugadores)
        self._id_equipo=Equipo.id
        Equipo.id+=1

    def agregar_jugadores(self,*jugadores:tuple[Jugador])->None:
        """
        Métod0 para agregar jugadores a un equipo.
        :param jugadores:Jugadores que se agregaran al equipo.
        :return: None
        """
        self._jugadores.extend(jugadores)

    def remover_jugadores(self,*jugadores:tuple[Jugador])->None:
        """
        Métod0 para remover jugadores de un equipo.
        :param jugadores: Nombre de los jugadores a eliminar.
        :return: None
        """
        for jugador in jugadores:
            if jugador in self._jugadores:
                self._jugadores.remove(jugador)

    def mostrar_jugadores(self)->None:
        """
        Métod0 para mostrar los jugadores existentes.
        :return: None.
        """
        if self._jugadores:
            for jugador in self._jugadores:
                print(jugador)
        else:
            print("No hay jugadores en el equipo.")
    def total_goles(self)->int:
        """
        Métod0 que muestra los goles de un equipo.
        :return: La suma total de goles de los jugadores de un equipo.
        """
        return sum(jugador.goles for jugador in self._jugadores)

    def __str__(self):
        """
        Métod0 mágico.
        :return: Cadena de los atributos de la clase Equipo
        """
        if self._jugadores:
            cadena_jugadores = ", ".join(str(jugador) for jugador in self._jugadores)#Solución consultada en un foro
            return f"Equipo:({self._nombre}, Jugadores: [{cadena_jugadores}], Id: {self._id_equipo})"
        else:
            return f"Equipo:({self._nombre},Jugadores: [Sin jugadores],Id: {self._id_equipo})"


if __name__ == '__main__':
    pass
