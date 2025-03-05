# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Exámen diagnóstico.

import random
def genera_par(grupo_404:list)->None:
    """
    Función que genera parejas con la restricción de que no
    puede haber dos personas que ya estuvieron en el mismo equipo.
    :param grupo_404: Lista de todos los alumnos del grupo 403 de informática.
    :return:
    """
    alg_Anar = ["Héctor", "Addi", "Jesús Alberto"]
    hack_cafe = ["Tania", "Patricia", "Rebeca"]
    cod_nocturno = ["Jamileth", "Bryan", "Rosalinda"]
    ctrl_z = ["Galilea", "Jennifer", "Juan"]
    print(grupo_404)
    equipo1 = [" ", " "]
    equipo2 = [" ", " "]
    equipo3 = [" ", " "]
    equipo4 = [" ", " "]
    equipo5 = [" ", " "]
    equipo6 = [" ", " "]
    equipos_nuevos = [equipo1, equipo2, equipo3, equipo4, equipo5, equipo6]

    for i in range(0, 6):
        val = 1
        while val != 0:
            equipos_nuevos[i][0] = random.choice(grupo_404)
            equipos_nuevos[i][1] = random.choice(grupo_404)
            if equipos_nuevos[i][0] != equipos_nuevos[i][1]:
                if equipos_nuevos[i][0] in alg_Anar and equipos_nuevos[i][1] in alg_Anar:
                    val = 1
                elif equipos_nuevos[i][0] in hack_cafe and equipos_nuevos[i][1] in hack_cafe:
                    val = 1
                elif equipos_nuevos[i][0] in cod_nocturno and equipos_nuevos[i][1] in cod_nocturno:
                    val = 1
                elif equipos_nuevos[i][0] in ctrl_z and equipos_nuevos[i][1] in ctrl_z:
                    val = 1
                else:
                    val = 0
                    grupo_404.remove(equipos_nuevos[i][0])
                    grupo_404.remove(equipos_nuevos[i][1])

    for i in range(0, 6):
        print(f"Equipo {i + 1}:{equipos_nuevos[i]}")

def main()->None:
    """
    Función principal del programa.
    :return: No regresa ningún valor.
    """
    grupo_404=["Héctor", "Addi",  "Jesús Alberto","Tania","Patricia", "Rebeca","Jamileth", "Bryan", "Rosalinda","Galilea", "Jennifer", "Juan"]
    genera_par(grupo_404)

if __name__ == '__main__':
    """
    Ejecución del programa principal
    """
    main()