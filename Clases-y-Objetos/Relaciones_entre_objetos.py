# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Relaciones entre objetos


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
        return f"Empleado(id:{self.id},nombre:{self.nombre},sueldo:{self.sueldo})"

class Empresa:
    def __init__(self, nombre: str, *empleados:Empleado):
        self.nombre=nombre
        self.empleados=list(empleados)
    def __str__(self) -> str:
        empleados = ", ".join(str(empleado) for empleado in self.empleados)
        return f"Empresa({self.nombre = }, {empleados})"
    def agregar_empleados(self,*nuevos_empleados:Empleado):
        for empleado in list(nuevos_empleados):
            self.empleados.append(empleado)


if __name__ == '__main__':
    juan= Empleado("Juan",8500)
    print(juan)
    ivan= Empleado("Ivan",8000)
    print(ivan)
    amazon=Empresa("Amazon",juan,ivan)
    print(amazon)
    amazon.agregar_empleados(juan,ivan)
    print(amazon)
    print("Programa finalizado")
    print("Adios")
    print("Hola mundo")