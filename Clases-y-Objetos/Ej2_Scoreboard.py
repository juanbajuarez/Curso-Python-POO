# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Se necesita desarrollar un sistema que permita
# gestionar y visualizar un scoreboard (puntuación) dentro de una ventana gráfica.

from typing import Tuple

#Declaración de la clase
class Scoreboard:
    #Constructor de la clase
    def __init__(self,point:int=0,text_color:tuple[int,int,int]=(0,0,0),font:str="kimono",size:float=48):
        """
        Inicializa una nueva instancia.
        :param point: Puntuación inicial.
        :param text_color: Color del texto.
        :param font: Tipo de fuente del texto.
        :param size: Tamaño de la fuente del texto.
        """
        self._point=point
        self._text_color=text_color
        self._font=font
        self._size=size
    #Metodos de las clases
    def draw(self)->None:
        """
        Dibuja el scoreboard, mostrando la puntuación.
        :return: None
        """
        print(f"Score: {self._point}")

    def __str__(self):
        """
        Métodos mágicos
        :return: Cadena que describe Scoreboard.
        """
        return f"Scoreboard(points={self._point},text_color:{self.text_color},size={self._size},font={self._font})"
    @property
    def point(self)->int:
        """
        Devuelve la puntuación actual.
        :return: La puntuación actual.
        """
        return self._point
    @property
    def text_color(self)->Tuple[int,int,int]:
        """
        Devuelve el color del texto en formato RGB.
        :return: Tupla con los valores del color del texto.
        """
        return self._text_color
    @property
    def font(self)->str:
        """
        Devuelve la fuente del texto.
        :return: La fuente utilizada.
        """
        return self._font
    @property
    def size(self)->float:
        """
        Devuelve el tamaño de la fuente.
        :return: El tamaño de la fuente.
        """
        return self._size
    @point.setter
    def point(self,points:int):
        """
        Modifica la puntuación sumando los puntos indicados.
        :param points: Los puntos a sumar.
        :return: None
        """
        self._point+=points
#Código a nivél de módulo
if __name__ == '__main__':
    # Se crean objetos de la clase y se imprime.
    print("  -- Se crean objetos de la clase Scoreboard.")

    print()
    print("Se crea un objeto sin argumentos:")
    marcador1 = Scoreboard()
    print(f"marcador1 = {marcador1}")

    print()
    print("Se crea otro objeto con (points, font y text_color) como argumentos por nombre:")
    marcador2 = Scoreboard(10, font="Arial", text_color=(127, 127, 127))
    print(f"marcador2 = {marcador2}")

    print()
    print("Se prueba el método draw() en ambos objetos:")
    marcador1.draw()
    marcador2.draw()
