import math
def get_score(gameStatus, board, player): ## asumimos que el maximizing es el jugador con canicas negras
    """Esta función recibe el gameStatus, el board y un entero binario que indica
    cuál es el jugador al que le estamos calculando el score. Es 1 si el jugador
    tiene las canicas negras y 0 si es rojo."""
    red_score = 0
    black_score = 0
    for t in board.tiles: ## iteramos a través de las piezas del tablero
        red_count = 0
        black_count = 0
        for x in range(t[0], t[0] + t[2]): ## en este loop contamos las bolitas de cada color
            for y in range(t[1], t[1] + t[3]):
                if gameStatus.occupy[x][y] == 0:
                    red_count += 1
                if gameStatus.occupy[x][y] == 1:
                    black_count += 1
        ## le asignamos ptje al que tiene más bolitas en la pieza, el ptje asignado es el area de la pieza
        if black_count > red_count:
            black_score += t[2] * t[3]
        if red_count > black_count:
            red_score += t[2] * t[3]

    ## retornamos el score según el jugador entregado, ojo que esta función no cambia el score en gameStatus
    if player == 1:
        return black_score - red_score
    else:
        return red_score - black_score

def bonus_score(gameStatus, board, player):
    """Nueva función de score. Propone una estrategia diferente dado que se explorará a profundidad 3."""
    return 0
