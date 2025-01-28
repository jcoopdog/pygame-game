import pygame, os, sys, threading
from coopergame import *
from console import *


class Game(BaseGame):

    def run(self, initialState):
        
        self.changeState( initialState )
        self.console = threading.Thread(target=Console, args=(self.consolereturn, self.consolerunning)).start()
        dt = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()	
                else:
                    if self.state != None:self.state.event(event)
            
            if self.state != None:
                self.state.update(dt, self.screen)
                
            #self.screen.fill(self.bgcolor)	
            if self.state != None:
                self.state.draw(self.screen)
                
            pygame.display.update()
            dt = self.clock.tick(60) / 1000   
