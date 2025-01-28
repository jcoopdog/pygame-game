import pygame, os
from coopergame import *

class InterState(GameState):

    def __init__(self, game, message, message_color="#FFFFFF", bgcolor="#494e53", fillbg=True):
        super().__init__(game)

        self.fillbg = fillbg
        self.bgcolor = bgcolor
        self.msg = message
        self.msgcolor = message_color
        self.font = pygame.font.SysFont(pygame.font.get_fonts(), 10)

    def enter(self, prevState):
        self.nextState = prevState

    def update(self, dt, screen):
        pass

    def draw(self, screen):
        if self.fillbg: screen.fill(self.bgcolor)
        x = screen.get_width() / 2
        y = screen.get_height() / 2
        screen.blit(self.font.render(self.msg, True, self.msgcolor), (x, y))

class ToggleState(InterState):

    def __init__(self, game, message, message_color="#FFFFFF", key=pygame.K_ESCAPE, bgcolor="#494e53", fillbg=True):
        super().__init__(game, message, message_color, bgcolor, fillbg)

        self.key = key
        self.toggle = False

    def enter(self, prevState):
        self.nextState = prevState
        self.toggle = False

    def event(self, event):
        if event.type == pygame.KEYUP:
            if event.key == self.key:
                self.game.changeState(self.nextState)

