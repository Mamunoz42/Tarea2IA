import pygame
import sys
from time import sleep
from settings import Settings
from assets import StartButton, ReduceButton, AddButton, RestartButton, InputFiled, Marble
from board import Board
import screen_handling 
import board_functions as bf
from robot import Robot
from status import gameStatus
from minimax import get_potential_position
import json
from time import time

H_PLAYER = True
GUI = True
SECONS_DELAY = 0  #Numero de segundos entre jugadas
SHOW_MENU = True
NUM_GAMES = 1
WRITE_RESULTS = False
BOARD_SIZE = 7

results = {
    "red":0,
    "black":0,
    "tie":0
}

if len(sys.argv) > 1:
    for arg in sys.argv:
        if arg == "-ng" or arg=="-nogui" or arg=="-nomarbles":
            GUI = False
            SECONS_DELAY = 0
        if arg == "-np" or arg=="-noplayer":
            H_PLAYER = False
        if arg == "-ns" or arg=="-noscreens":
            SHOW_MENU = False
        if "-size" in arg:
            arg = arg.strip("-size")
            BOARD_SIZE = int(arg)
        if "-write" == arg:
            WRITE_RESULTS = True
        if "-ngames" in arg:
            arg = arg.strip("-ngames")
            NUM_GAMES = int(arg)



class Stats:
    def __init__(self, size=7):
        self.width = size
        self.height = size
        self.game_active = False
        self.game_restart = False

def run_game(DCCanicas_settings, SHOW_MENU=True, wins=[0,0,0]):
    ## inicializamos pygame y los settings iniciales
    pygame.init()
    background = pygame.image.load(DCCanicas_settings.initial_background)
    pygame.display.set_caption("DCCanicas")

    while True: ## este loop dibuja los botones y las superficies, NO tocar
        screen = pygame.display.set_mode((background.get_width(), background.get_height()))
        screen.blit(background, (0, 0))
        if SHOW_MENU:
            startbutton = StartButton(screen)
            startbutton.blitme()
            addbutton = AddButton(screen, startbutton)
            addbutton.blitme()
            reducebutton = ReduceButton(screen, startbutton)
            reducebutton.blitme()
            inputfield = InputFiled(screen, addbutton, reducebutton)
            inputfield.blitme()
        
        try:
            stats = Stats(BOARD_SIZE)
        except NameError:
            stats = Stats()



        font = pygame.font.Font(DCCanicas_settings.font, 40)
        surface = font.render(str(stats.width), True, DCCanicas_settings.font_color)
        screen_rect = screen.get_rect()
        if SHOW_MENU:
            screen.blit(surface, (
                int(screen_rect.centerx - 0.5 * surface.get_width()),
                int(reducebutton.rect.centery - 0.5 * surface.get_height())))
        if SHOW_MENU:
            while True: ## este loop es para chequear los eventos dentro del juego, como presionar botones
                screen_handling.check_events_in_start_screen(stats, startbutton, addbutton, reducebutton) ## chequea los botones de inicio y cambio de tamaño del board
                inputfield.blitme()
                surface = font.render(str(stats.width), True, (154, 202, 64))
                screen.blit(surface, (int(screen_rect.centerx - 0.5 * surface.get_width()),
                                    int(reducebutton.rect.centery - 0.5 * surface.get_height())))
                pygame.display.flip()
                if stats.game_active: ## si se inicia el juego se deja de chequear los cambios de esta parte
                    break

        ## aquí se inicializan las caracteristicas de la pantalla del juego    
        screen = pygame.display.set_mode((stats.width * DCCanicas_settings.hole_size, stats.height * DCCanicas_settings.hole_size))
        board = Board(screen, stats.width, stats.height, DCCanicas_settings.bg_color, DCCanicas_settings.hole_size, DCCanicas_settings.tile_edge_color)
        board.blitme()
        pygame.display.flip()
        Status = gameStatus(stats.width, stats.height)
        board.init_board_feature()

        ## AQUÍ SE INICIALIZA LA IA
        robot_black = Robot(
            Status, 
            board, 
            screen, 
            DCCanicas_settings.hole_size, 
            DCCanicas_settings.intelligence_robot_black, 
            DCCanicas_settings.robot_black_turn, 
            DCCanicas_settings.robot_black_IQ)

        if not H_PLAYER:
            robot_red = Robot(
                Status, 
                board, 
                screen, 
                DCCanicas_settings.hole_size, 
                DCCanicas_settings.intelligence_robot_red, 
                DCCanicas_settings.robot_red_turn, 
                DCCanicas_settings.robot_red_IQ)


        
        ## loop del juego, se mantiene en loop mientras el juego no haya terminado
        while True:
            if H_PLAYER: # Turnos en caso de robot y jugador
                if Status.turn == DCCanicas_settings.robot_black_turn:
                    robot_black.play()
                    board.draw_available_marks(Status, get_potential_position(Status, board), DCCanicas_settings.hole_size)
                    continue
                g = bf.check_events(Status, screen, DCCanicas_settings.hole_size, board)


            else: # Turnos en caso robot vs robot
                if Status.turn == DCCanicas_settings.robot_red_turn:
                    robot_red.play()
                else:
                    robot_black.play()
                sleep(SECONS_DELAY) # para que el juego no sea tan rapido

            if GUI:
                pygame.display.flip()

            if Status.end:
                # print("Game over")
                # print("red score:", Status.red_score, "black score:", Status.black_score)
                if Status.red_score > Status.black_score:
                    # print("RED WIN!")
                    Status.result = 0
                    wins["red"] += 1
                elif Status.black_score > Status.red_score:
                    # print("BLACK WIN!")
                    wins["black"] += 1
                    Status.result = 1
                else:
                    # print("TIE!")
                    wins["tie"] += 1
                    Status.result = 2
                break
        
        ## se muestran los resultados y el boton de restart
        result = screen_handling.ResultsScreen(screen, DCCanicas_settings.bg_color, Status, DCCanicas_settings)
        result.blitme()
        restartbutton = RestartButton(screen)
        restartbutton.blitme()
        pygame.display.flip()

        if SHOW_MENU:
            while True: ## para resetear el juego al cliquear el boton
                g = screen_handling.check_events_in_results_screen(stats, restartbutton)
                if stats.game_restart:
                    stats.game_restart = False
                    break
        else:
            stats.game_restart = False
            break




if __name__ == "__main__":
    tiempo_inicial = time()
    DCCanicas_settings = Settings()
    i = 0
    while i < NUM_GAMES:
        run_game(DCCanicas_settings, SHOW_MENU, results)
        i+=1

    if WRITE_RESULTS:
        print("wins: ", results)
        out_file = open("simulacion.json", "w")
        to_dump = {**DCCanicas_settings.__dict__, **{"results":results, "size": BOARD_SIZE, "ngames": NUM_GAMES}}
        json.dump(to_dump, out_file, indent = 6)
        out_file.close()
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("tiempo de ejecucion: ", tiempo_ejecucion)