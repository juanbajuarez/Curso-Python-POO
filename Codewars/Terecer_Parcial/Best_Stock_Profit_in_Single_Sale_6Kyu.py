# Autor: Juan Bautista Juárez
# Fecha: Junio de 2025
# Descripción: You're a buyer/seller and your buisness is at stake... You need to
# make profit... Or at least, you need to lose the least amount of money!
# Knowing a list of prices for buy/sell operations, you need to pick two of them.
# Buy/sell market is evolving across time and the list represent this evolution.
# First, you need to buy one item, then sell it later. Find the best profit you
# can do.

def max_profit(prices)->int:
    """
    Función que calcula el mejor precio en base con una lista de precios.
    :param prices: Lista de precios.
    :return: El mejor costo compra-Venta.
    """
    # Primero compra luego vende
    precio_minimo = prices[0]
    ganancia = prices[1] - prices[0]

    for price in prices[1:]:
        diferencias = price - precio_minimo
        if diferencias > ganancia:
            ganancia = diferencias
        if price < precio_minimo:
            precio_minimo = price

    return ganancia
#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(max_profit([10, 7, 5, 8, 11, 9]))
    print(max_profit([3, 4]))
    print(max_profit([9, 9]))
    print(max_profit([10, 7, 5, 4, 1]))