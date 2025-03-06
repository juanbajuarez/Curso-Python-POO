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
        print("Estoy caminando.")
    def comer(self)->None:
        print("Estoy comiendo.")
    def jugar(self)->None:
        print("Estoy jugando.")
    def dormir(self)->None:
        print("Estoy durmiendo.")
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
