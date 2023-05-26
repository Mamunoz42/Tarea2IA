class Settings():
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 900
        self.bg_color = (243,222,187)
        self.initial_background = "image/dccanicas.jpg"
        self.hole_size = 50
        self.tile_edge_color = (150, 127, 103)
        self.font_color = (154, 202, 64)
        self.font = 'image/Phosphate-Solid.ttf'
        # 0 indica canicas rojas, 1 indica canicas negras
        self.robot_red_turn = 0
        self.robot_black_turn = 1
        # --------------------------------------------------------------------
        # Recomendamos modificar solo las siguientes lineas
        # el IQ del robot indica la profundidad de búsqueda del Minimax
        self.robot_red_IQ = 3
        self.robot_black_IQ = 6
        # Las posibles inteligencias son Random, Minmax, Minmax-Bonus
        self.intelligence_robot_red = "Minmax"
        self.intelligence_robot_black = "Minmax" 
