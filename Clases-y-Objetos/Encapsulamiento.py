# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Encapsulamiento

class CuentaBancaria:
    def __init__(self,titular:str,saldo_inicial:float=0):
        self.titular=titular
        self._saldo=saldo_inicial
    def depositar(self,cantidad:float)->None:
        self._saldo+=cantidad
    def retirar(self,cantidad:float)->None:
        self._saldo-=cantidad
    def __str__(self) -> str:
        return f"Titular({self.titular},saldo:{self._saldo})"
    @property
    def saldo(self)->float:
        return self._saldo
    @saldo.setter
    def saldo(self,nuevo_saldo:float):
        self._saldo=nuevo_saldo

if __name__ == '__main__':
    cuentaJB=CuentaBancaria("JUAN",200)
    print(cuentaJB)
    cuentaJB._saldo_inicial=10
    cuentaJB.depositar(1500)
    print(cuentaJB)
    cuentaJB.retirar(510)
    print(cuentaJB)
    cuentaJB.saldo=5
    print(cuentaJB)
    print(cuentaJB.saldo)