import pygame, os
from base_classes import *
from settings import *
from bullet import *
from player import *
from sentry import *

class MainGameState(GameState):

    def __init__(self, game):
        super().__init__(game)
        
        self.player = Player(self.game.screen.get_width() / 2, self.game.screen.get_height() / 2, 13)
        bulletController = BulletController()
        sentryController = SentryController(bulletController)
        
        self.controllers = { "bullet" : bulletController, \
                "sentry" : sentryController }

    def enter(self, prevState):
        pass

    def exit(self):
        pass
    
    def update(self, dt, screen):
        self.player.update(dt, screen)
        bullets = self.controllers["bullet"]
        self.player.check_projectiles(bullets.bullets, bullets)
        for ctrl in self.controllers.values():
            ctrl.update(dt, screen)

    def draw(self, screen):
        self.player.draw(screen)
        for ctrl in self.controllers.values():
            ctrl.draw(screen)

    
