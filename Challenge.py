#import numpy as np
#import panda as pd

# variables.py
DIMENSIONES_TABLERO = 10
BARCOS = {
    "barcos_1": 4,  # 4 barcos de 1 posición
    "barcos_2": 3,  # 3 barcos de 2 posiciones
    "barcos_3": 2,  # 2 barcos de 3 posiciones
    "barcos_4": 1   # 1 barco de 4 posiciones
}

# tablero.py
import numpy as np
from variables import DIMENSIONES_TABLERO, BARCOS

class Tablero:
    def __init__(self, jugador_id):
        self.jugador_id = jugador_id
        self.dimension = DIMENSIONES_TABLERO
        self.tablero = np.full((self.dimension, self.dimension), " ")
        self.disparos = np.full((self.dimension, self.dimension), " ")
        self.barcos = BARCOS
    
    def inicializar_tablero(self):
        # Colocar los barcos en el tablero de acuerdo a la configuración
        for tipo_barco, cantidad in self.barcos.items():
            for _ in range(cantidad):
                self.posicionar_barco(int(tipo_barco.split('_')[1]))

    def posicionar_barco(self, eslora):
        # Implementar la lógica para colocar un barco en una posición aleatoria y en dirección aleatoria
        pass
    
    def disparo(self, fila, columna):
        if self.tablero[fila, columna] == "O":
            self.disparos[fila, columna] = "X"
            return True
        else:
            self.disparos[fila, columna] = "-"
            return False

# main.py
from tablero import Tablero

def jugar():
    jugador = Tablero("Jugador")
    maquina = Tablero("Máquina")
    
    jugador.inicializar_tablero()
    maquina.inicializar_tablero()
    
    juego_terminado = False
    turno = "Jugador"
    
    while not juego_terminado:
        if turno == "Jugador":
            # Pedir coordenadas al jugador
            fila, columna = map(int, input("Introduce las coordenadas (fila columna): ").split())
            impacto = maquina.disparo(fila, columna)
            if impacto:
                print("¡Impacto!")
            else:
                print("Agua.")
                turno = "Máquina"
        else:
            # Turno de la máquina
            import random
            fila = random.randint(0, jugador.dimension - 1)
            columna = random.randint(0, jugador.dimension - 1)
            impacto = jugador.disparo(fila, columna)
            if impacto:
                print("La máquina hizo impacto en tu tablero.")
            else:
                print("La máquina falló.")
                turno = "Jugador"

        # Condición de victoria
        if np.all(maquina.tablero != "O"):
            print("¡Ganaste!")
            juego_terminado = True
        elif np.all(jugador.tablero != "O"):
            print("La máquina ganó.")
            juego_terminado = True

if __name__ == "__main__":
    jugar()

def recibir_disparo(tablero, fila, columna):
    try:
        if not (0 <= fila < 10 and 0 <= columna < 10):
            raise ValueError("Coordenada fuera del tablero.")
        if tablero[fila, columna] == "O":
            tablero[fila, columna] = "X"
            print(f"Disparo en ({fila},{columna}): ¡Impacto!")
        elif tablero[fila, columna] == " ":
            tablero[fila, columna] = "-"
            print(f"Disparo en ({fila},{columna}): Agua.")
        else:
            print(f"Disparo en ({fila},{columna}): Ya disparado antes.")
    except ValueError as e:
        print(e)
        # Solicita al usuario que vuelva a introducir las coordenadas


while True:
    accion = input("Ingresa una coordenada (X,Y) para disparar o 'q' para salir: ")
    if accion.lower() == 'q':
        print("Gracias por jugar. Aquí están los tableros:")
        print("Tu tablero:")
        print(tablero)
        # Si tienes un tablero del oponente, puedes mostrarlo aquí también
        break
    # Aquí procesas el input para disparar en coordenadas


def selecciona_dificultad():
    print("Seleccione el nivel de dificultad:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")
    try:
        nivel = int(input("Ingrese el número del nivel deseado: "))
        if nivel not in [1, 2, 3]:
            raise ValueError("Opción de dificultad no válida.")
        return nivel
    except ValueError as e:
        print(e)
        return selecciona_dificultad()
   
def disparo_maquina(tablero_jugador, dificultad):
    intentos = dificultad
    for _ in range(intentos):
        fila, columna = random.randint(0, 9), random.randint(0, 9)
        recibir_disparo(tablero_jugador, fila, columna)