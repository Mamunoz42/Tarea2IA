import sys
import pygame

class ResultsScreen():
    def __init__(self, screen, boardcolor, gameStatus, setting):
        self.boardcolor = boardcolor
        self.screen = screen
        self.gameStatus = gameStatus
        self.setting = setting

    def blitme(self):
        rect = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA, 32)
        rect.fill((self.boardcolor[0], self.boardcolor[1], self.boardcolor[2], 220))
        self.screen.blit(rect, (0, 0))
        if self.gameStatus.result == 0:
            slogan = "RED WIN!"
        elif self.gameStatus.result == 1:
            slogan = "BLACK WIN!"
        else:
            slogan = "TIE!"
        font = pygame.font.Font(self.setting.font, int(self.screen.get_width()/len(slogan)))
        surface = font.render(slogan, True, self.setting.font_color)
        self.screen.blit(surface, (int(self.screen.get_width()/2 - 0.5 * surface.get_width()),
                              int(self.screen.get_height())/3 - 0.5 * surface.get_height()))



def check_events_in_start_screen(stats, startbutton, addbutton, reducebutton):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_start_button(stats, startbutton, mouse_x, mouse_y)
            check_add_button(stats, addbutton, mouse_x, mouse_y)
            check_reduce_button(stats, reducebutton, mouse_x, mouse_y)


def check_start_button(stats, startbutton, mouse_x, mouse_y):
    if startbutton.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True

def check_add_button(stats, addbutton, mouse_x, mouse_y):
    if addbutton.rect.collidepoint(mouse_x, mouse_y) and stats.width<20:
        stats.width += 1
        stats.height += 1

def check_reduce_button(stats, reducebutton, mouse_x, mouse_y):
    if reducebutton.rect.collidepoint(mouse_x, mouse_y) and stats.width>3:
        stats.width -= 1
        stats.height -= 1

def check_events_in_results_screen(stats, restartbutton):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_restart_button(stats, restartbutton, mouse_x, mouse_y)

def check_restart_button(stats, restartbutton, mouse_x, mouse_y):
    if restartbutton.rect.collidepoint(mouse_x, mouse_y):
        stats.game_restart = True