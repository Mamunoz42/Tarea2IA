import copy

## esta clase contiene el estado del juego en un turno dado
class gameStatus:
    def __init__(self, width, height):
        self.turn = 0 ## guarda al jugador con el turno actual, 0 para canicas rojas y 1 para canicas negras
        self.width = width ## ancho de pantalla
        self.height = height ## alto de pantalla
        self.available = [[0 for t in range(height)] for i in range(width)] ## celdas disponibles se marcan con 0 y ocupadas con 1
        self.occupy = [[-1 for t in range(height)] for i in range(width)] ## indica qué jugador ocupa cada celda, 0 para rojas y 1 para negras
        self.last_opponent = (-1, -1)  ## última celda donde se jugó
        self.tile_opponent = -1 ## guarda la última pieza NO CELDA donde jugó el oponente
        self.tile_self = -1 ## guarda la última pieza donde jugó el jugador actual (es decir, en el penúltimo turno)
        self.end = False  ## para cuando termine el juego
        self.red_score = 0 
        self.black_score = 0
        self.result = -1
