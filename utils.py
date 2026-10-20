import numpy as np
import random

def crea_tablero(lado = 10):
    tablero = np.full((lado,lado)," ")
    return tablero

def crea_barco_aleatorio(tablero,eslora = 4, num_intentos = 100):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    while True:
        barco = []
        # Construimos el hipotetico barco
        pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
        print("Pieza original:", pieza_original)
        barco.append(pieza_original)
        orientacion = random.choice(["N","S","O","E"])
        print("Con orientacion", orientacion)
        fila = pieza_original[0]
        columna = pieza_original[1]
        for i in range(eslora -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_barco_plus(tablero, barco)
        if type(tablero_temp) == np.ndarray:
            return tablero_temp
        print("Tengo que intentar colocar otro barco")

def coloca_barco_plus(tablero, barco):
    # Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0  or fila >= num_max_filas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if columna <0 or columna>= num_max_columnas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            print(f"No puedo poner la pieza {pieza} porque hay otro barco")
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp

def recibir_disparo(t, b, coordenada):
    if b[coordenada] == "O":
        t[coordenada] = "X"
        b[coordenada] = "X"
        print("Tocado")
    elif b[coordenada] == "X":
        print("Agonia, deja de perder el tiempo, dispara a otro sitio")
    else:
        t[coordenada] = "-"
        b[coordenada] = "-"
        #print("Agua")
    return t, b

def arregla_barcos(tablero):
    tablero[tablero == "X"] = "O"
    #tablero.where(tablero == "X","O", tablero)
    return tablero

'''
1. Crea la función `colocar_barcos(tablero)`, que deberá de colocar la lista de barcos generados de forma aleatoria (6 barcos en total (3 barcos de eslora 2, 2 de eslora 3 y 1 eslora 4))
    ¡Mucho ojo con barcos que estén superpuestos (no pueden ocupar dos barcos la misma casilla) o barcos que se salgan del tablero!

    '''
def colocar_barcos(tablero):
    t1 = crea_barco_aleatorio(tablero, eslora = 4)
    while type(t1) != np.ndarray:
        t1 = crea_barco_aleatorio(tablero, eslora = 4)
    t2 = crea_barco_aleatorio(t1, eslora = 3)
    while type(t2) != np.ndarray:
        t2 = crea_barco_aleatorio(t1, eslora = 3)
    t3 = crea_barco_aleatorio(t2, eslora = 3)
    while type(t3) != np.ndarray:
        t3 = crea_barco_aleatorio(t2, eslora = 3)
    t4 = crea_barco_aleatorio(t3, eslora = 2)
    while type(t4) != np.ndarray:
        t4 = crea_barco_aleatorio(t3, eslora = 2)
    t5 = crea_barco_aleatorio(t4, eslora = 2)
    while type(t5) != np.ndarray:
        t5 = crea_barco_aleatorio(t4, eslora = 2)
    t6 = crea_barco_aleatorio(t5, eslora = 2)
    while type(t6) != np.ndarray:
        t6 = crea_barco_aleatorio(t5, eslora = 2)
    return t6
