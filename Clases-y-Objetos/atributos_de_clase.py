# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Clases y objetos.


class Empleado:
    no_id=1
    def __init__(self,nombre:str,sueldo:float):
        self.nombre=nombre
        self.sueldo=sueldo
        self.id=Empleado.no_id
        Empleado.no_id+=1
    def aumentar_sueldo(self,porcentaje:float)->None:
        pass
    def __str__(self) -> str:
        return f"Profesor(id:{self.id},nombre:{self.nombre},sueldo:{self.sueldo})"

if __name__ == '__main__':
    Empleado1=Empleado("Cristian",1551)
    Empleado2=Empleado("Sebastian",2551)
    print(Empleado1)
    print(Empleado2)