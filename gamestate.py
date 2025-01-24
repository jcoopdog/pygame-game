import pygame, os
from base_classes import *
from settings import *
from bullet import *
from player import *
from sentry import *

class MainGameState(GameState):

    def __init__(self, game, pauseState):
        super().__init__(game)
        
        self.pauseState = pauseState
        self.pause = False
        self.player = Player(self.game.screen.get_width() / 2, self.game.screen.get_height() / 2, 13)
        bulletController = BulletController()
        sentryController = SentryController(bulletController)
        
        self.controllers = { "bullet" : bulletController, \
                "sentry" : sentryController }

    def enter(self, prevState):
        self.pause = False

    def exit(self):
        pass
    
    def update(self, dt, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.pause = True
        elif self.pause:
            self.game.changeState(self.pauseState)
            return
        self.player.update(dt, screen, keys=keys)
        bullets = self.controllers["bullet"]
        self.player.check_projectiles(bullets.bullets, bullets)
        for ctrl in self.controllers.values():
            ctrl.update(dt, screen)

    def draw(self, screen):
        self.player.draw(screen)
        for ctrl in self.controllers.values():
            ctrl.draw(screen)

    
