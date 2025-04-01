# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Clases y objetos.

#Definicion de la clase personaje.
class Personaje:
    contador_id=1
    def __init__(self,x=0,y=0):
        """
        Inicialización del constructor de la clase personaje
        :param x: posición inicial en x
        :param y: posición inicial en y
        """
        self.posx=x
        self.posy=y
        self.id_Personaje=Personaje.contador_id
        Personaje.contador_id+=1

    def moverse(self,ordenes:str)->None:
        """
        Mé_todos que permite el desplazamiento
        :param ordenes:cadena con las instrucciones del desplazamiento
        :return:
        """
        #Lógica para el desplazamiento
        for i in range(0,len(ordenes)):
            if ordenes[i]=='A' or ordenes[i]=='a':
                if 0<=self.posy <10:
                    self.posy+=1
            elif ordenes[i]=='R' or ordenes[i]=='r':
                if self.posy!=0:
                    self.posy-=1
            elif ordenes[i]=='D' or ordenes[i]=='d':
                if 0 <=self.posx < 10:
                    self.posx += 1
            elif ordenes[i]=='I' or ordenes[i]=="i":
                if self.posx != 0:
                    self.posx -= 1
            else:
                print("Datos incorrectos")

    def posicion_actual(self)->None:
        """
        Mé_todo que imprime la posición actual del personaje
        :return:
        """
        print(f"Posicion actual: (x,y)= {self.posx,self.posy}")

    def __str__(self) -> str:
        """
        Mé_todo mágico que imprime los valores del objeto
        :return: Valores del objeto
        """
        return f"Personaje(id:{self.id_Personaje},(x,y)= {self.posx,self.posy})"
#Código a nivel de módulo.
if __name__ == '__main__':
    """
    Creacion de clases para la implementación del 
    movimiento de un personaje
    """
    personaje1=Personaje()
    print(personaje1)
    personaje2 = Personaje()
    print(personaje2)
    ban=None
    while ban!=1:
        mov=input("Ingrese las ordenes de movimiento: ")
        if mov=='s' or mov=='S':
            print("Programa terminado")
            break
        else:
            personaje1.moverse(mov)
            personaje1.posicion_actual()
    #Programa terminado