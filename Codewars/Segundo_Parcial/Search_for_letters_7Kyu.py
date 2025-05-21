# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: Create a function which accepts one arbitrary string as an
# argument, and return a string of length 26.
# The objective is to set each of the 26 characters of the output string to
# either '1' or '0' based on the fact whether the Nth letter of the alphabet
# is present in the input (independent of its case).
# So if an 'a' or an 'A' appears anywhere in the input string
# (any number of times), set the first character of the output string to '1',
# otherwise to '0'. if 'b' or 'B' appears in the string, set the second character
# to '1', and so on for the rest of the alphabet.

def change(st):
    st = st.lower()
    resultado = ""
    for i in range(26):
        letra = chr(ord('a') + i)  # genera el alfabeto usando condigo ASCII
                                   # sumando 1
        if letra in st:
            resultado += '1'
        else:
            resultado += '0'
    return resultado

#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(change("a **&  bZ"))
    print(change('Abc e  $$  z'))