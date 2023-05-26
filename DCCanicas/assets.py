import pygame

## este módulo contiene las clases para los botones y elementos dentro del juego, NO tocar


class AddButton():
    def __init__(self, screen, startbutton):
        self.screen = screen
        self.image = pygame.image.load('image/add_button.png')
        self.image = pygame.transform.scale(self.image, (int(screen.get_height()*0.075), int(screen.get_height()*0.075)))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.right = startbutton.rect.right
        self.rect.centery = int(screen.get_height()*0.82)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def blitme_xy(self, x, y):
        self.screen.blit(self.image, (x, y))


class ReduceButton():
    def __init__(self, screen, startbutton):
        self.screen = screen
        self.image = pygame.image.load('image/reduce_button.png')
        self.image = pygame.transform.scale(self.image, (int(screen.get_height()*0.075), int(screen.get_height()*0.075)))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = startbutton.rect.left
        self.rect.centery = int(screen.get_height()*0.82)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def blitme_xy(self, x, y):
        self.screen.blit(self.image, (x, y))

class RestartButton():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('image/start_button.png')
        self.image = pygame.transform.scale(self.image, (int(screen.get_width()*0.4), int(screen.get_height()*0.2)))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = int(screen.get_height()*0.72)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def blitme_xy(self, x, y):
        self.screen.blit(self.image, (x, y))


class StartButton():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('image/start_button.png')
        self.image = pygame.transform.scale(self.image, (int(screen.get_width()*0.3), int(screen.get_height()*0.12)))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = int(screen.get_height()*0.72)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def blitme_xy(self, x, y):
        self.screen.blit(self.image, (x, y))


class InputFiled():
    def __init__(self, screen, addbutton, reducebutton):
        self.screen = screen
        self.image = pygame.image.load('image/size.png')
        self.image = pygame.transform.scale(self.image, (addbutton.rect.left - reducebutton.rect.right, int(screen.get_height()*0.075)))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = reducebutton.rect.right
        self.rect.centery = int(screen.get_height()*0.82)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def blitme_xy(self, x, y):
        self.screen.blit(self.image, (x, y))


class Marble():
    def __init__(self, screen, gameStatus):
        self.screen = screen
        if gameStatus.turn == 0:
            self.image = pygame.image.load('image/red_marble.png')
        else:
            self.image = pygame.image.load('image/black_marble.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

    def blitme_xy(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y
        self.screen.blit(self.image, self.rect)