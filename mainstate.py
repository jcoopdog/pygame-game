import pygame, os
from coopergame import *
from settings import *
from bullet import *
from player import *
from events import *
from console import *

class MainState(GameState):

    def __init__(self, game, level, pauseState, levelendState, bgcolor="#494e53", console = False):
        super().__init__(game)
        
        self.CONSOLE = console
        self.bgcolor = bgcolor
        self.levelendState = levelendState
        self.pauseState = pauseState
        self.player = Player(self.game.screen.get_width() / 2, self.game.screen.get_height() / 2, 13)
        self.bullets = BulletController()
        self.eventer = EventManager(game, self, level)

    def consolereturn(self, value) -> str:
        cmd = value.lower().strip().split()
        if len(cmd) <= 0:
            return " no command entered"
        match cmd[0]:
            case "gameover":
                self.game.changeState(None)
                return "game ended"
            case "set":
                match cmd[1]:
                    case "playerx":
                        self.player.x = int(cmd[2])
                    case "playery":
                        self.player.y = int(cmd[2])
                    case _:
                        return "specify value to set"
            case "print":
                return cmd[1]
            case _:
                return "command not found"

    def enter(self, prevState):
        if self.CONSOLE: 
            self.console = ConsoleThread(target=Console, args=(self.consolereturn, ))
            self.console.start()
        
    def exit(self):
        if self.CONSOLE:
            self.console.kill()
            self.console.join()
    
    def update(self, dt, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            self.eventer.clear()
            self.bullets.clear()
        if self.eventer.update(dt, screen):
            self.game.changeState(self.levelendState)
            return
        self.player.update(dt, screen, keys=keys)
        b = self.player.rect.collideobjects( self.bullets.bullets, key=lambda b: b.rect ) or \
                self.player.rect.collideobjects( self.eventer.events, key=lambda e: e.rect )
        if b:
            self.player.damage()
        self.bullets.update(dt, screen)

    def draw(self, screen):
        screen.fill(self.bgcolor)
        self.bullets.draw(screen)
        self.eventer.draw(screen)
        self.player.draw(screen)

    def event(self, event):
        match event.type:
            case pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.game.changeState(self.pauseState)
    
