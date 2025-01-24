import pygame, os
from base_classes import *

class PauseState(GameState):

    def __init__(self, game):
        super().__init__(game)

        self.font = pygame.font.SysFont(pygame.font.get_fonts(), 10)
        self.unpause = False

    def enter(self, prevState):
        self.nextState = prevState
        self.unpause = False

    def update(self, dt, screen):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            self.unpause = True
        elif self.unpause:
            self.game.changeState(self.nextState)
            return

    def draw(self, screen):
        x = screen.get_width() / 2
        y = screen.get_height() / 2
        screen.blit(self.font.render("PAUSED", True, "#FFFFFF"), (x, y))

