# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Clases y objetos.



class Persona:
    def __init__(self,nombre:str,edad:int,altura:float,peso:float):
        self.nombre=nombre
        self.edad=edad
        self.altura=altura
        self.peso=peso
    def caminar(self)->None:
        """
        Función que despliega la acción de caminar.
        :return:
        """
        print(f"{self.nombre} esta caminando para bajar sus {self.peso}. Kgs")
    def comer(self)->None:
        """
        Función que despliega la acción de comer.
        :return:
        """

        print(f"{self.nombre} esta comiendo .")
    def jugar(self)->None:
        """
        Función que despliega la acción de jugar.
        :return:
        """
        print(f"{self.nombre} esta jugando.")
    def dormir(self)->None:
        """
        Función que despliega la acción de dormir.
        :return:
        """
        print(f"{self.nombre} esta durmiendo.")

if __name__ == '__main__':
    juan=Persona("Juan",25,1.78,82.300)
    print(juan.nombre)
    print(juan.edad)
    print(juan.altura)
    print(juan.peso)
    juan.caminar()
    juan.jugar()
    juan.comer()
    juan.dormir()
    juan2=Persona("Bautista",22,1.80,85.520)
    juan2.caminar()
    juan2.comer()
    juan2.jugar()
    juan2.dormir()
    juan.peso=80.5
    juan.altura=1.82
    juan.caminar()
    print(juan.nombre)