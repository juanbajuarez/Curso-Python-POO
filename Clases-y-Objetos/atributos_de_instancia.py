# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Clases y objetos.
from symtable import Class


class Estudiante:
    def __init__(self,nombre:str):
        self.nombre=nombre
        self.temas_aprendidos=[]

    def __str__(self) -> str:
        return f"Estudiante(Nombre:{self.nombre} temas_aprendidos: {self.temas_aprendidos})"
    def aprender_tema(self,tema:str):
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendió {tema}")

class Profesor:
    def __init__(self,nombre:str,temas_dominados:list[str]):
        self.nombre=nombre
        self.temas_dominados=temas_dominados
    def __str__(self) -> str:
        return f"Profesor(Nombre:{self.nombre} temas_dominados: {self.temas_dominados})"

    def dominar_tema(self,tema:str)->list[str]:
        pass
    def esenar_tema(self,no_tema:int)->str:
        if no_tema>len(self.temas_dominados):
            return self.temas_dominados[no_tema]
        else:
            return "Fuera de rango"

if __name__ == '__main__':
    Estudiante1=Estudiante("JUAN")
    Estudiante2=Estudiante("CRISTIAN")
    Estudiante1.aprender_tema("Evolución sitios web")
    Estudiante2.aprender_tema("Iot")
    print(Estudiante1)
    print(Estudiante2)
    Profesor1=Profesor("Betho",["Estructura de datos"])
    Profesor2=Profesor("Magdiel",["Programación estructurada"])
    Profesor1.esenar_tema(1)
    Profesor2.esenar_tema(1)
    print(Profesor1)
    print(Profesor2)
