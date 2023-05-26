import random as rd
import board_functions as bf
from assets import Marble
import math
import minimax
import score


class Robot:
    def __init__(self, gameStatus, board, screen, hole_size, intelligence, robot_turn, deep):
        self.gameStatus = gameStatus
        self.board = board
        self.screen = screen
        self.hole_size = hole_size
        self.intelligence = intelligence
        self.robot_turn = robot_turn
        self.deep = deep

    # la siguiente función entrega una jugada aleatoria para la ia
    def decision_randomly(self, potential_position):
        decision = rd.choice(potential_position)
        #print(f"El movimiento elegido por la IA {self.intelligence} es: ", decision) # para poder ver el movimiento
        return decision

    def put_marble(self, x, y):
        if bf.check_available(self.gameStatus, x, y, self.board, True):
            # mention that available table is not match true board, it is diagonally flipped
            self.gameStatus.available[x][y] = 1
            self.gameStatus.occupy[x][y] = self.gameStatus.turn
            marble = Marble(self.screen, self.gameStatus)
            marble.blitme_xy(int((x + 0.5) * self.hole_size), int((y + 0.5) * self.hole_size))
            if self.gameStatus.turn == 1:
                self.gameStatus.turn = 0
            else:
                self.gameStatus.turn = 1
            self.gameStatus.last_opponent = (x, y)
            # calculate score
            bf.calculate_score(self.gameStatus, self.board)
            # print("red score:", self.gameStatus.red_score, "black score:", self.gameStatus.black_score)
            # check game end
            if bf.check_end(self.gameStatus, self.board, x, y):
                self.gameStatus.end = True
                

    def play(self):
        if self.intelligence == "Random":
            potential_position = minimax.get_potential_position(self.gameStatus, self.board)
            decision = self.decision_randomly(potential_position)
        if self.intelligence == "Minmax":
            decision = minimax.minimax(self.gameStatus, self.board, self.deep, score.get_score, alpha = -math.inf, beta = math.inf)[0]
        if self.intelligence == "Minmax-Bonus":
            decision = minimax.minimax(self.gameStatus, self.board, self.deep, score.bonus_score, alpha = -math.inf, beta = math.inf)[0]
        self.put_marble(decision[0], decision[1])


