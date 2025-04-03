# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Examen Primer parcial
# Menú principal
from torneo import Torneo
from Equipo import Equipo
from Jugador import Jugador


def menu():
    """
    Función que despliega el menú.
    :return: La opción del menú.
    """
    while True:
        print("1. Crear jugador")
        print("2. Crear equipo")
        print("3. Ver lista de jugadores")
        print("4. Ver lista de equipos")
        print("5. Agregar jugador a equipo")
        print("6. Eliminar jugador de equipo")
        print("7. Agregar equipo al torneo")
        print("8. Eliminar equipo del torneo")
        print("9. Anotar gol(es) a jugador")
        print("10. Conocer goles totales de equipos")
        print("11. Generar rol de juegos")
        print("12. Salir")
        op = input("Seleccione una opción: ")
        if op.isnumeric():
            op=int(op)
            return op
        else:
            print("Opción no válida. Intente de nuevo.")

# Código a nivel de módulo
if __name__ == '__main__':
    jugadores = []
    equipos = []
    torneo = Torneo("Champios Leaguaje")
    opcion = None
    while opcion != 12:
        print(f"--Bienvenido al torneo: {torneo._nombre}--")
        opcion = menu()

        if opcion == 1:
            while True:
                nombre = input("Nombre del jugador: ")
                ban = True
                for car in nombre:
                    if not (car.isalpha() or car.isspace()):
                        ban = False
                        break
                if ban:
                    print(f"Nombre {nombre} ingresado correctamente.")
                    break
                else:
                    print("Nombre invalido")
            while True:
                numero = input("numero del jugador: ")
                if numero.isnumeric():
                    break
                else:
                    print("Numero no valido")
            jugador = Jugador(nombre,numero)
            jugadores.append(jugador)

        elif opcion == 2:
            nombre = input("Nombre del equipo: ")
            equipo = Equipo(nombre)
            equipos.append(equipo)

        elif opcion == 3:
            print("Lista de jugadores:")
            if len(jugadores)==0:
                print("No hay jugadores")
            else:
                for i,jugador in enumerate(jugadores):
                    print(f"{i+1}) {jugador} ")

        elif opcion == 4:
            print("Lista de equipos:")
            if len(equipos) == 0:
                print("No hay equipos")
            else:
                for i, equipo in enumerate(equipos):
                    print(f"{i+1}) {equipo} ")

        elif opcion == 5:
            if len(equipos)!=0:
                no=None
                lista_agregar=[]
                print("Lista de jugadores:")
                for i, jugador in enumerate(jugadores):
                    print(f"{i + 1}) Nombre:{jugador.nombre}")
                jugadores_agregados =input("Ingrese nombre separado por comas")
                lista_jugadores = jugadores_agregados.split(",") #Divide la cadena por comas

                for nombre in lista_jugadores:
                    nombre = nombre.strip()
                    # Buscar el jugador con ese nombre en la lista de jugadores
                    band1 = False
                    for jugador in jugadores:
                        if jugador.nombre.lower() == nombre.lower():
                            lista_agregar.append(jugador)
                            band1 = True
                            print(f"Jugador '{jugador.nombre}' encontrado.")
                            break

                    if not band1:
                        print(f"Jugador '{nombre}' no encontrado en la lista.")
                        no=False
                        break

                print("Lista de equipos")
                for i, equipo in enumerate(equipos):
                    print(f"{i + 1}. {equipo._nombre}")
                no_equipo=input("Seleccione un equipo para agregar a los jugadores:")
                band2 = False
                for equipo in equipos:
                    if equipo._nombre.lower() == no_equipo.lower():
                        equipo.agregar_jugadores(*lista_agregar)
                        band2 = True
                        print(f"Jugadores agregados .")
                        break
                if not band2:
                    print(f"Equipo '{no_equipo}' no encontrado en la lista.")
                    if not no:
                        print("NO se pudo agregar jugador")
            else:
                print("No hay equipos para agregar jugadores")

        elif opcion == 6:
            if len(equipos) != 0:
                lista_eliminar = []
                print("Lista de equipos:")
                for i, equipo in enumerate(equipos):
                    print(f"{i + 1}) Nombre:{equipo._nombre}")
                while True:
                    equipo_selec = input("Ingrese el nombre del equipo: ").strip()
                    if not equipo_selec.isnumeric():
                        break
                    else:
                        print("valor ingresado no valido")
                selec = None
                band1 = False

                for equipo in equipos:
                    if equipo._nombre.lower() == equipo_selec.lower():
                        selec = equipo
                        band1 = True
                        break
                if selec:
                    print(f"Equipo {selec} encontrado.")
                    if len(selec._jugadores) > 0:
                        print(f"Lista de jugadores en el equipo {selec._nombre}:")
                        for i, jugador in enumerate(selec._jugadores):
                            print(f"{i + 1}) Nombre: {jugador.nombre}")

                        jugador_eliminar = input("Ingrese los nombres de los jugadores a eliminar, separados por comas: ").strip()
                        lista_eliminados = jugador_eliminar.split(",")
                        for nombre in lista_eliminados:
                            nombre = nombre.strip()
                            selec2 = None
                            for jugador in selec._jugadores:
                                if jugador.nombre.lower() == nombre.lower():
                                    selec2 = jugador
                                    break
                            if selec2:
                                lista_eliminar.append(selec2)
                            else:
                                print(f"Jugador '{nombre}' no encontrado en el equipo {selec._nombre}.")
                        if lista_eliminar:
                            selec.remover_jugadores(*lista_eliminar)
                            for jugador in lista_eliminar:
                                print(f"Jugador '{jugador.nombre}' eliminado del equipo {selec._nombre}.")
                        else:
                            print("No se eliminaron jugadores.")
                    else:
                        print("No hay jugadores en este equipo.")
                else:
                    print(f"Equipo '{equipo_selec}' no encontrado.")
            else:
                print("No hay equipos disponibles para eliminar jugadores.")

        elif opcion == 7:
            if len(equipos) != 0:
                print("Seleccione un equipo para agregar al torneo:")
                alta = []
                for i, equipo in enumerate(equipos):
                    print(f"{i + 1}. {equipo._nombre}")
                equipos_alta = input("Ingrese los nombres de equipos para el torneo, separados por comas: ").strip()
                lista_alta = equipos_alta.split(",")

                for equipos1 in lista_alta:
                    encontrado = False
                    for equipo in equipos:
                        if equipo._nombre.lower() == equipos1.lower():
                            alta.append(equipo)
                            encontrado = True
                            break

                    if not encontrado:
                        print(f"El equipo '{equipos1}' no existe en la lista de equipos.")


                if len(alta) != 0:
                    torneo.agregar_equipos(*alta)
                    print("Equipos agregados al torneo:")
                    for equipo in alta:
                        print(f"Eqipo:{equipo._nombre}")
                else:
                    print("No se agregaron equipos al torneo.")
            else:
                print("No hay equipos para agregar al torneo.")

            #Datos del torneo para pruebas
            print(torneo)

        elif opcion==8:
            if len(torneo._equipos) != 0:
                print("Seleccione un equipo para eliminar del torneo:")


                for i, equipo in enumerate(torneo._equipos):
                    print(f"{i + 1}. {equipo._nombre}")


                equipos_eliminar = input("Ingrese los nombres de los equipos a eliminar, separados por comas: ").strip()
                lista_eliminados = equipos_eliminar.split(",")

                equipos_a_eliminar = []

                for equipos1 in lista_eliminados:
                    equipos1 = equipos1.strip()
                    encontrado = False


                    for equipo in torneo._equipos:
                        if equipo._nombre.lower() == equipos1.lower():
                            equipos_a_eliminar.append(equipo)
                            encontrado = True
                            break

                    if not encontrado:
                        print(f"El equipo '{equipos1}' no existe en el torneo.")

                if len(equipos_a_eliminar) != 0:
                    torneo.eliminar_equipos(*equipos_a_eliminar)
                    print("Equipos eliminados del torneo:")
                    for equipo in equipos_a_eliminar:
                        print(f"- {equipo._nombre}")
                else:
                    print("No se eliminaron equipos del torneo.")
            else:
                print("No hay equipos en el torneo para eliminar.")

            # Datos del torneo para pruebas
            print(torneo)

        elif opcion == 9:
            print("Seleccione un jugador para anotar goles:")
            if len(jugadores)!=0:
                for i, jugador in enumerate(jugadores):
                    print(f"{i + 1}. {jugador.nombre}")
                jugador_goles = input("Ingrese el nombre del jugador: ").strip()#Borra espacios
                for jugador in jugadores:
                    if jugador.nombre.lower() == jugador_goles.lower():
                        while True:
                            goles=input("Jugador encontrado, ingrese los goles a sumar")
                            if goles.isnumeric() and int(goles)>0:
                                jugador.anotar_goles(int(goles))
                                break
                            else:
                                print("Dato invalido")
                    else:
                        print("El jugador no existe")
            else:
                print("No hay jugadores")
        elif opcion == 10:
            print("Goles totales por equipo:")
            for equipo in equipos:
                print(f"{equipo._nombre}: {equipo.total_goles()} goles")

        elif opcion == 11:
            print("Generando rol de juego")
            torneo.generar_rol()

        elif opcion == 12:
            print("Programa Terminado")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
