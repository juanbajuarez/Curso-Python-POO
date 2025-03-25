# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Se necesita desarrollar un sistema que permita
# gestionar y visualizar un scoreboard (puntuación) dentro de una ventana gráfica.
from symtable import Class
from typing import Tuple


class Scoreboard:
    def __init__(self,point:int,text_color:tuple[int]=(0,0,0),font:str="kimono",size:float=48):
        self._point=point
        self._text_color=text_color
        self._font=font
        self._size=size

    def draw(self)->None:
        pass

    def __str__(self):
        return f"Scoreboard(points={self.points},size={self.size},font={self._font})"
    @property
    def points(self)->int:
        return self.points
    @property
    def text_color(self)->Tuple[int,int,int]:
        return self.text_color()
    @property
    def font(self)->str:
        return self._font
    @property
    def size(self)->float:
        return self._size
    @ points.setter
    def points(self,points=int):
        self._point=points
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