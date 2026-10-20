import numpy as np
import random

import utils
'''
2. Escribe el flujo completo del programa, con la dinámica de turnos y funcionalidades necesarios para jugar contra la máquina (dispara a tu tablero de forma aleatoria).
    Crea todas las funciones que necesites y aplica todo lo aprendido que te sea útil.

    '''
tA = utils.crea_tablero(15)
bA = utils.colocar_barcos(tA)

tB = utils.crea_tablero(15)
bB = utils.colocar_barcos(tB)

while (bB == "O").any() and (bA == "O").any():
    v1 = int(input("Introduzca un número del 0 al 14: "))
    v2 = int(input("Introduzca otro número: "))
    tB, bB = utils.recibir_disparo(tB, bB, (v1,v2))
    tA, bA = utils.recibir_disparo(tA, bA, (random.randint(0,14),random.randint(0,14)))
    print(tA)
    #print(bA)
    print(tB)
    #print(bB)
else:
    if "O" in bB:
        print("Gana B")
    if "O" in bA:
        print("Gana A")

'''

3. Encapsula todo en un `main.py` y un `utils.py` para ejecutarlo desde terminal.

4. Sube tu proyecto a un repositorio de github y prepara una demo (solo se podrá enseñar desde terminal) para la presentación de tu proyecto.

'''