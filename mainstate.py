import pygame, os
from coopergame import *
from settings import *
from bullet import *
from player import *
from events import *

class MainState(GameState):

    def __init__(self, game, level, pauseState, levelendState, bgcolor="#494e53"):
        super().__init__(game)
        
        self.bgcolor = bgcolor
        self.levelendState = levelendState
        self.pauseState = pauseState
        self.pause = False
        self.player = Player(self.game.screen.get_width() / 2, self.game.screen.get_height() / 2, 13)
        bulletController = BulletController()
        self.eventer = EventManager(game, self, level)
        self.controllers = { "bullets" : bulletController }

    def enter(self, prevState):
        self.pause = False

    def exit(self):
        pass
    
    def update(self, dt, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            self.eventer.clear()
        if keys[pygame.K_ESCAPE]:
            self.pause = True
        elif self.pause:
            self.game.changeState(self.pauseState)
            return
        if self.eventer.update(dt):
            self.game.changeState(self.levelendState)
            return
        self.player.update(dt, screen, keys=keys)
        bullets = self.controllers["bullets"]
        b = self.player.rect.collideobjects( bullets.bullets, key=lambda b: b.rect )
        if b:
            self.player.damage()
        for ctrl in self.controllers.values():
            ctrl.update(dt, screen)

    def draw(self, screen):
        screen.fill(self.bgcolor)
        self.player.draw(screen)
        for ctrl in self.controllers.values():
            ctrl.draw(screen)

    
