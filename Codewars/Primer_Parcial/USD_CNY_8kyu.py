# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Create a function that converts US dollars (USD) to Chinese Yuan (CNY) .
# The input is the amount of USD as an integer, and the output should be a string that states the amount of
# Yuan followed by 'Chinese Yuan'

#Examples (Input -> Output)
#15  -> '101.25 Chinese Yuan'
#465 -> '3138.75 Chinese Yuan'
#The conversion rate you should use is 6.75 CNY for every 1 USD.
# All numbers should be represented as a string with 2 decimal
# places. (e.g. "21.00" NOT "21.0" or "21")


def usdcny(usd)->str:
    """
    Función que convierte dólares a yuanes.
    :param usd: Cantidad de dinero en dólares.
    :return: Cantidad convertida en yuanes.
    """
    conversion = 6.75
    yuan = conversion * usd
    return f"{yuan:.2f} Chinese Yuan"

#Código a nivel de módulo.
if __name__ == '__main__':
    
    #Mi código para hacer pruebas.
    print(usdcny(15))
    print(usdcny(465))