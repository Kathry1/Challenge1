
# main.py
from clases import Tablero

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
    print("                ¡¡Bienvedid@s a nuestro Team Challenge!!")
    print("                        ¿Echamos una partidita?")
    print("------------------------------------------------------------------------")
    print("")
    print("")
    
    #Cuando arranque el programa, primero pon algún mensaje de bienvenida y las instrucciones del juego.
    print("\n\nBienvenido al juego Hundir la Flota\n\nEstas son las instrucciones del juego:\n(1)blablabla\n(2)blablabla\n(3)blablabla\n")
    
    #A continuación inicializa los tableros de ambos jugadores con los barcos.

    #Creamos los objetos tableros
    tab_humano = Tablero("humano1")
    tab_maquina = Tablero("maquina1")

    # Imprimimos los atributos del objeto tablero
    print("\nJugadores:\n")
    print("ID jugador humano:",tab_humano.jugador_id)
    print("ID jugador máquina:",tab_maquina.jugador_id)
    #print(tab_humano.dimension)
    #print(tab_humano.tablero)
    #print(tab_humano.disparos)
    #print(tab_humano.barcos)    

    # Inicializamos los tableros con barcos fijos o de coordenadas aleatorias
    tab_humano.ini_tablero_alea() # Inicializamos el tablero jugador humano con coordenadas aleatorias
    #Imprimimos el tablero del humano
    print("\n\nTablero humano\n",tab_humano.tablero)
    for nombre_barco,coordenadas in tab_humano.barcos_creados.items():
        print(nombre_barco,":",coordenadas)
    #tab_maquina.ini_tablero_alea()

    tab_maquina.ini_tablero_alea() # Inicializamos el tablero de la maquina con coordenadas aleatorias
    #Imprimimos el tablero del humano
    print("\n\nTablero máquina\n",tab_maquina.tablero)
    for nombre_barco,coordenadas in tab_maquina.barcos_creados.items():
        print(nombre_barco,":",coordenadas)
    #tab_maquina.ini_tablero_alea()



#Después de eso ya comienza el juego. Básicamente se irá ejecutando iterativamente en el while, y le irá preguntando coordenadas al usuario.

    '''



    while True:
        accion = input("Ingresa una coordenada (X,Y) para disparar o 'q' para salir: ")
        if accion.lower() == 'q':
            print("Gracias por jugar. Aquí están los tableros:")
            print("Tu tablero:")
            print(tablero)
            # Si tienes un tablero del oponente, puedes mostrarlo aquí también
            break
        # Aquí procesas el input para disparar en coordenadas


    '''