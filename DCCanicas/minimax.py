import board_functions as bf
import math
import random as rd
import copy
import time

def get_potential_position(gameStatus, board):
    """Esta función recibe el gameStatus y el board.  
    Retorna una lista con tuplas. Cada tupla es una posible
    posición donde es posible jugar en el turno actual.
    NO TOCAR"""
    potential_position = []
    if gameStatus.last_opponent[0] == -1 and gameStatus.last_opponent[1] == -1:
        for i in range(gameStatus.width):
            for t in range(gameStatus.height):
                potential_position.append((i, t))
    else:
        x = gameStatus.last_opponent[0]
        y = gameStatus.last_opponent[1]
        for i in range(gameStatus.width):
            if bf.check_available(gameStatus, i, y, board, False):
                potential_position.append((i, y))
        for i in range(gameStatus.height):
            if bf.check_available(gameStatus, x, i, board, False):
                potential_position.append((x, i))
    return potential_position



def minimax(gameStatus, board,  depth, score_function, alpha = -math.inf, beta = math.inf):
    """Esta función es la que deben completar, lean muy bien los comentarios de cada
    parte para irse guiando. 
    Esta función debe retornar una tupla de la forma ((x,y),value), donde (x,y) es 
    el movimiento a jugar y value el puntaje de dicho movimiento."""

    # Lo primero que haremos será definir cuál es el jugador actual, si es Min o Max. Vamos a asumir
    # que Max será el jugador con canicas negras y Min el jugador con canicas rojas
    # recordar que gameStatus.turn nos dice cuál es el jugador actual
    maximizing_player = True if gameStatus.turn == 1 else False 

    # En segundo lugar vamos a obtener todos los movimientos válidos para el turno actual
    # para ello necesitas acceso a gameStatus y board
    valid_locations = [mov for mov in get_potential_position(gameStatus, board)]

    # Ahora vamos a agregar una condición de término para la recursión del MiniMax, tenemos dos casos
    # que la profundidad llegue a 0 o que no queden movimientos posibles.
    if depth == 0 or len(valid_locations) == 0: # condicion de término
    
        if len(valid_locations) == 0: # No hay más movs posibles
            """
            Este es el caso en que no hayan más movs. posibles.
            En esta parte hay 3 subcasos, uno donde se acabaron las jugadas y ganó negro,
            otro donde se acabaron las jugadas y ganó rojo, y otro donde se acabaron las jugadas y hubo empate.
            Para cada uno de esos se retorna una tupla de la forma ((None,None), score). El 
            score es +inf, -inf o 0 dependiendo del caso, y el movimiento es (None,None) 
            ya que no se puede seguir jugando.
            """
            if score_function(gameStatus, board, maximizing_player) > 0: # Gana el jugador negro
                return ((None, None), math.inf)

            elif score_function(gameStatus, board, maximizing_player) < 0: # Jugador rojo gana
                return ((None, None), -math.inf)

            else:	# Se termina el juego, no hay más movs posibles y hay empate
                return ((None, None), 0)

        elif depth == 0:
            """
            Caso en que se llegó al límite de profundidad.
            """
            if maximizing_player:
                return ((None, None), score_function(gameStatus, board, maximizing_player))
            else:
                return ((None, None), -score_function(gameStatus, board, maximizing_player))


    # Ahora debemos considerar 2 casos dependiendo del jugador actual, en primer lugar
    # veamos el caso en que el jugador actual es el MAX

    if maximizing_player:									
        value = -math.inf # definimos el valor inicial del score
        chosen_mov = rd.choice(valid_locations)	# pre-elegimos un mov al azar en caso de que no exista uno mejor

        for movement in valid_locations: # Expandimos los nodos según los movimientos posibles
            x = movement[0]
            y = movement[1]
            gameStatus_copy = copy.deepcopy(gameStatus) # hacemos una copia del gameStatus para guardar los movimientos que se realicen
            
            if bf.check_available(gameStatus_copy, x, y, board, play_move=True): # jugamos el movimiento si cumple las reglas
                """
                En esta parte del código debes ejecutar el movimiento seleccionado, para ello 
                debes cambiar los atributos correspondientes en gameStatus_copy,
                es decir los atributos available, occupy, turn y last_opponent
                según corresponda
                """
                #TODO: Ejecutar el movimiento seleccionado
                
                # Primero cambio el available utilizando las coordenadas que me entrega la variable
                # movement, que es una tupla de la forma (x,y)
                gameStatus_copy.available[x][y] = 1
                gameStatus_copy.occupy[x][y] = 1
                gameStatus_copy.turn = 0
                gameStatus_copy.last_opponent = (x, y)

                """Una vez jugado el movimiento en la copia de gameStatus, debes
                usar recursión para seguir expandiendo la búsqueda y reducir la profundidad"""
                #TODO: Usar recursión para seguir expandiendo la búsqueda
                # Aquí hago la recursión teniendo ojo en entregar la copia del gameStatus, y que la
                # profundidad la haya disminuido en 1, para que llegue en algún punto a 0, y entre 
                # en el caso base

                new_value = minimax(gameStatus_copy, board, depth - 1, score_function, alpha, beta)

                """Finalmente, debes chequear si el puntaje del movimiento en el nodo
                actual es mejor que el que se tenia
                guardado previamente. En caso de que sea mejor, debes guardar el nuevo puntaje en la variable 
                score y el movimiento que te lleva a dicho puntaje en chosen_mov"""
                #TODO: Chequear si el puntaje del movimiento en el nodo actual 
                # es mejor que el que se tenia guardado previamente
                if new_value[1] > value:
                    value = new_value[1]
                    chosen_mov = (x, y)

                # Reviso si el valor obtenido es mayor al que se tiene en el alpha, en tal caso,
                # se actualiza el valor de alpha
                if new_value[1] > alpha:
                    alpha = new_value[1]

                """Aquí debes implementar la poda alfa-beta (Actividad 2), para hacer el código más eficaz"""
                #TODO: Implementar la poda alfa-beta
                if alpha >= beta:
                    break
        return chosen_mov, value

    # Ahora es el caso en que el jugador sea MIN
    else:
        value = math.inf    # definimos el valor inicial del score
        chosen_mov = rd.choice(valid_locations) # pre-elegimos un mov al azar en caso de que no exista uno mejor

        for movement in valid_locations:
            x = movement[0]
            y = movement[1]
            gameStatus_copy = copy.deepcopy(gameStatus) # hacemos una copia del gameStatus para guardar los movimientos que se realicen
            if bf.check_available(gameStatus_copy, x, y, board, True):
                """
                En esta parte del código debes ejecutar el movimiento seleccionado, para ello 
                debes cambiar los atributos correspondientes en gameStatus_copy,
                es decir los atributos available, occupy, turn y last_opponent
                según corresponda
                """
                #TODO: Ejecutar el movimiento seleccionado
                gameStatus_copy.available[x][y] = 1
                gameStatus_copy.occupy[x][y] = 0
                gameStatus_copy.turn = 1
                gameStatus_copy.last_opponent = (x, y)

                """Una vez jugado el movimiento en la copia de gameStatus, debes
                usar recursión para seguir expandiendo la búsqueda y reducir la profundidad"""
                #TODO: Usar recursión para seguir expandiendo la búsqueda
                new_value = minimax(gameStatus_copy, board, depth - 1, score_function, alpha, beta)

                """Finalmente, debes chequear si el puntaje del movimiento en el nodo
                actual es mejor que el que se tenia
                guardado previamente. En caso de que sea mejor, debes guardar el nuevo puntaje en la variable 
                score y el movimiento que te lleva a dicho puntaje en chosen_mov"""
                #TODO: Chequear si el puntaje del movimiento en el nodo actual 
                # es mejor que el que se tenia guardado previamente
                if new_value[1] < value:
                    value = new_value[1]
                    chosen_mov = (x, y)
                # Reviso si el valor obtenido es mayor al que se tiene en el alpha, en tal caso,
                # se actualiza el valor de alpha
                if new_value[1] < beta:
                    beta = new_value[1]
                """Aquí debes implementar la poda alfa-beta (Actividad 2), para hacer el código más eficaz"""
                #TODO: Implementar la poda alfa-beta
                if alpha >= beta:
                    break
        return chosen_mov, value