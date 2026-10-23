# Hundir la Flota en Python ⚓️

Proyecto en Python inspirado en el clásico juego de **Hundir la Flota** (*Battleship*).

### English Description of the game
This videogame, developed in Python, consists on a user playing against a machine through the console.
The game starts with two boards simulating the ocean for each player respectively.
Each board starts with 6 ships that are randomly positioned on the board and represented with letters "O".
The game consists on shoting to each others boards with the aim to sink each others boats.
The shots are random for the machine, and selected by the user, but the user can't see the ships on the boards.
Instead, two boards without ships but with signs of letters "X" for broken parts of ships and signs "-" for water shots will be shown.

### Descripción del juego en español
Cada jugador comienza con 6 barcos distribuidos aleatoriamente por el tablero que simula la posición en el mar mediante unidades, " ".
Se asume que las porciones de mar en las que se encuentra cada flota son disjuntas.
El juego consiste en disparar al tablero del adversario con el fin de destruir su flota.
Para este propósito los jugadores se turnan para ejecutar un único disparo que puede:
- destruir una unidad de eslora (la unidad de eslora pasa a ser "X" en su posición en el tablero)
- volver a disparar a una unidad de eslora ya destruida (la unidad de eslora sigue simbolizándose por "X")
- disparar a una unidad de agua (la unidad de agua pasa a ser "-")
- disparar fuera del tablero (se pide otro intento)


## Características principales

- 🎯 Juego por turnos: jugador vs. máquina.
- 📋 2 tableros para barcos y 2 para disparos.
- 💥 Impactos, hundimientos y detección de ganador.

## Estructura del proyecto
```
Hundir la flota/
├── main.py         # lógica del juego
├── utils.py        # funciones del juego
└── README.md
```
## Requisitos

- Python 3.x
- Numpy (`pip install numpy`)

## Cómo ejecutar

```bash
python main.py
```
