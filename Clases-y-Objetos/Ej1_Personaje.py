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
        movimientos=len(ordenes)
        for i in range (0,movimientos-1):
            if ordenes[i]=='A' or ordenes[i]=='a':
                if 0<self.posy <10:
                    self.posy+=1
            elif ordenes[i]=='R' or ordenes[i]=='r':
                if self.posy!=0:
                    self.posy-=1

            elif ordenes[i]=='D' or ordenes[i]=='d':
                if 0 < self.posx < 10:
                    self.posx += 1
            elif ordenes[i]=='I' or ordenes[i]=="i":
                if self.posy != 0:
                    self.posy -= 1
            else:
                print("Datos incorrectos")

    def posicion_actual(self)->None:
        pass
    def __str__(self) -> str:
        return f"Posicion actual: (x,y)= {self.posicion_actual()})"

if __name__ == '__main__':
    personaje1=Personaje()
    print(personaje1)
    instruccion=None
    while instruccion!='s' or instruccion!='S'