#main.py

import numpy as np
from ClasesyFunciones import *

if __name__ == "__main__":
    print("------------------------------------------------------------------------")
    print("     ╔╗╔╗╔╗╔╗╔╗ ╔╗╔══╗ ╔══╗╔═══╗  ╔╗  ╔══╗  ╔══╗╔╗  ╔══╗╔════╗╔══╗")
    print("     ║║║║║║║║║╚═╝║║╔╗╚╗╚╗╔╝║╔═╗║  ║║  ║╔╗║  ║╔═╝║║  ║╔╗║╚═╗╔═╝║╔╗║")
    print("     ║╚╝║║║║║║╔╗ ║║║╚╗║ ║║ ║╚═╝║  ║║  ║╚╝║  ║╚═╗║║  ║║║║  ║║  ║╚╝║")
    print("     ║╔╗║║║║║║║╚╗║║║ ║║ ║║ ║╔╗╔╝  ║║  ║╔╗║  ║╔═╝║║  ║║║║  ║║  ║╔╗║")
    print("     ║║║║║╚╝║║║ ║║║╚═╝║╔╝╚╗║║║║   ║╚═╗║║║║  ║║  ║╚═╗║╚╝║  ║║  ║║║║")
    print("     ╚╝╚╝╚══╝╚╝ ╚╝╚═══╝╚══╝╚╝╚╝   ╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝  ╚╝  ╚╝╚╝")
    print("")
    print("╔════╗╔═══╗╔══╗╔╗  ╔╗  ╔═══╗╔══╗╔╗  ╔══╗ ╔═══╗╔╗ ╔╗   ╔╗╔╗╔══╗╔╗ ╔╗╔══╗ ")
    print("╚═╗╔═╝║╔══╝║╔╗║║║  ║║  ║╔══╝║╔╗║║║  ║╔╗╚╗║╔══╝║╚═╝║   ║║║║╚╗╔╝║╚═╝║║╔╗╚╗")
    print("  ║║  ║╚══╗║╚╝║║╚╗╔╝║  ║║╔═╗║║║║║║  ║║╚╗║║╚══╗║╔╗ ║   ║╚╝║ ║║ ║╔╗ ║║║╚╗║")
    print("  ║║  ║╔══╝║╔╗║║╔╗╔╗║  ║║╚╗║║║║║║║  ║║ ║║║╔══╝║║╚╗║   ║╔╗║ ║║ ║║╚╗║║║ ║║")
    print("  ║║  ║╚══╗║║║║║║╚╝║║  ║╚═╝║║╚╝║║╚═╗║╚═╝║║╚══╗║║ ║║   ║║║║╔╝╚╗║║ ║║║╚═╝║")
    print("  ╚╝  ╚═══╝╚╝╚╝╚╝  ╚╝  ╚═══╝╚══╝╚══╝╚═══╝╚═══╝╚╝ ╚╝   ╚╝╚╝╚══╝╚╝ ╚╝╚═══╝")
    print("")
    print("------------------------------------------------------------------------")
    print("                ¡¡Bienvedid@s a Hundir la Flota!!")
    print("            ¿Echamos una partidita? Sigue las instrucciones")
    print("------------------------------------------------------------------------")
    print("")
    print("")
    
    
    accion = input("Pulse Enter para jugar o 'q' para salir: ")
    if accion.lower() != 'q':

        #A continuación inicializa los tableros de ambos jugadores con los barcos.

        #Creamos los objetos tableros
        tab_humano = Tablero("humano1")
        tab_maquina = Tablero("maquina1")
        
        print("\n\nGracias por jugar. Aquí están los tableros:")    

        # Inicializamos los tableros con barcos fijos o de coordenadas aleatorias
        tab_humano.ini_tablero_alea() # Inicializamos el tablero jugador humano con coordenadas aleatorias
        #Imprimimos el tablero del humano
        print("**********************")
        print("Tablero de ",tab_humano.jugador_id)
        tab_humano.mostrar_tablero()

        pausa()

        tab_maquina.ini_tablero_alea() # Inicializamos el tablero de la maquina con coordenadas aleatorias
        #Imprimimos el tablero del humano
        print("\n\nTablero de ",tab_maquina.jugador_id)
        tab_maquina.mostrar_tablero()
        # print(tab_maquina.disparos)
        print("**********************")

        

        #Después de eso ya comienza el juego. Básicamente se irá ejecutando iterativamente en el while, y le irá preguntando coordenadas al usuario

        juego_terminado = False
        turno = "Jugador"

        while not juego_terminado:

            if turno == "Jugador":
                print("\nTurno del:", tab_humano.jugador_id)
                while True:
                    try:
                        respuesta = input("Introduce las coordenadas (fila columna) separadas por espacio o 'q' para salir: ")
                        if respuesta.lower() == 'q':
                            juego_terminado = True
                            break
                        fila, columna = map(int, respuesta.split())  
                        if 0 <= fila < tab_humano.dimension and 0 <= columna < tab_humano.dimension:  
                            break
                        else:
                            print(f"Las coordenadas deben estar entre 0 y {tab_humano.dimension - 1}.")
                    except ValueError:
                        print("Entrada inválida. Por favor, introduce dos números separados por espacio.")

                if juego_terminado:
                    break

                impacto = tab_maquina.recibir_disparo(fila, columna)
                if impacto:
                    print("\n¡Impacto! :)")
                else:
                    print("\nAgua :( ")
                    turno = "Máquina"

            else:
                # Turno de la máquina
                print("\n\nTurno de la maquina")
                import random

                # Se controla que la máquina no dispare sobre una coordenada en la que ya ha disparado
                while True:
                    fila = random.randint(0, tab_humano.dimension - 1)
                    columna = random.randint(0, tab_humano.dimension - 1)
                    if tab_humano.disparos[fila, columna] == " ":
                        break

                impacto = tab_humano.recibir_disparo(fila, columna)
                if impacto:
                    print("La máquina hizo impacto en tu tablero :( )")
                else:
                    print("La máquina falló :) ")
                    turno = "Jugador"



            # Condición de victoria
            if np.all(tab_maquina.tablero != "O"):
                print("¡Ganaste!")
                juego_terminado = True
            elif np.all(tab_humano.tablero != "O"):
                print("La máquina ganó.")
                juego_terminado = True

            input("Presione Enter para continuar")
            print("---------------------------")
            print("Tablero de ",tab_humano.jugador_id)    
            tab_humano.mostrar_tablero()
            print("\n\nTablero de ",tab_maquina.jugador_id)
            tab_maquina.mostrar_tablero()
            print("---------------------------")               

        print("FIN DEL JUEGO")
