# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Se necesita desarrollar un sistema que permita
# gestionar y visualizar un scoreboard (puntuación) dentro de una ventana gráfica.

from  Ej2_Scoreboard import Scoreboard

class Window:

    def __init__(self,text:str,width:int,height:int,scoreboard:Scoreboard=Scoreboard()):
        self.text=text
        self.width=width
        self.height=height
        self.scoreboard=scoreboard

    def  draw_scoreboard(self)->None:
        print(f"Score:{self.scoreboard.point}")
    def update_score(self,points:int)->None:
        self.scoreboard._point=points
        print(f"Score:{self.scoreboard.point}")

    def __str__(self)->str:
        return  f"Windows:(Title:{self.text},Width:{self.width},Height:{self.height}.Scoreboard:{self.scoreboard})"

if __name__ == "__main__":
    # Se crean objetos de la clase Window sin un objeto de la clase Scoreboard creado
    # y se prueban sus métodos.
    print("  -- Se crea un objeto de la clase Window sin un objeto de la clase Scoreboard.")

    buscaminas = Window("Buscaminas", 800, 900)

    print("Se imprime el objeto:")
    print(f"Buscaminas = {buscaminas}")

    print()
    print("Método para dibujar el scoreboard:")
    buscaminas.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    buscaminas.update_score(1)


    # Se crean objetos de ambas clases y se prueban sus métodos.
    print()
    print("  -- Se crea otro objeto de la clase Window, pero ahora con un objeto de la clase Scoreboard.")

    marcador_solitario = Scoreboard(10,(40, 40, 40), "Arial", 40)
    solitario = Window("Solitario", 1_000, 1_000, marcador_solitario)

    print("Se imprimen los objetos:")
    print(f"marcador_solitario = {marcador_solitario}")
    print(f"Solitario = {solitario}")

    print()
    print("Método para dibujar el scoreboard:")
    solitario.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    solitario.update_score(11)


    # Se modifican los atributos mediante los métodos de acceso.
    print()
    print("  -- Se modifican los atributos mediante los métodos de acceso.")

    print("Se tiene la ventana buscaminas:")
    print(f"buscaminas = {buscaminas}")
    print("Se reemplaza el scoreboard utilizando el setter:")
    buscaminas.scoreboard = marcador_solitario
    print(f"buscaminas = {buscaminas}")