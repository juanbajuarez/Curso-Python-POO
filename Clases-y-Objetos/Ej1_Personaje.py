# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Clases y objetos.


class Personaje:
    contador_id=1
    def __init__(self,x=0,y=0):
        self.posx=x
        self.posy=y
        self.id_Personaje=Personaje.contador_id
        Personaje.contador_id+=1

    def moverse(self,ordenes:str)->None:
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
        print(f"Posicion actual: (x,y)= {self.posx,self.posy}")
    def __str__(self) -> str:
        return f"Personaje(id:{self.id_Personaje},(x,y)= {self.posx,self.posy})"

if __name__ == '__main__':
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