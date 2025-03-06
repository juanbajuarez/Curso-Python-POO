# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Clases y objetos.
from symtable import Class


class Estudiante:
    def __init__(self,nombre:str):
        self.nombre=nombre
        self.temas_aprendidos=[]
    def aprender_tema(self,tema:str):
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendió {tema}")

class Profesor:
    def __init__(self,nombre:str):
        self.nombre=nombre
        self.temas_dominados=[]
    def dominar_tema(self,tema:str):
        pass
    def esenar_tema(self,no_tema:int)->str:
        pass

