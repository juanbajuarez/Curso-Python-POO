# Autor: Juan Bautista Juárez
# Fecha: Junio de 2025
# Descripción: Write a function that will take in any array and reverse it.
# Sounds simple doesn't it?
# NOTES:
# Array should be reversed in place! (no need to return it)
# Usual builtins have been deactivated. Don't count on them.
# You'll have to do it fast enough, so think about performances

def reverse(seq):
    tam= len(seq)
    for i in range(tam // 2):
        aux = seq[i]
        seq[i] = seq[tam - 1 - i]
        seq[tam - 1 - i] = aux
    return seq

#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.
    print(reverse([-3, 1, 2, 3, -1, -4, -2]))
    print(reverse(['?','you','are','how','world','hello']))