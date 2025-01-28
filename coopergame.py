import pygame, os, sys

class GameState(object):
    
    """
    Initialise the Game state class. Each sub-type must call this method. Takes one parameter, which
    is the game instance.
    """
    def __init__(self, game):
        self.game = game
        
    """
    Called by the game when entering the state for the first time.
    """
    def enter(self, prevState):
        pass
    
    """
    Called by the game when leaving the state.
    """
    def exit(self):
        pass
        
    """
    Called by the game allowing the state to update itself. The game time (in milliseconds) since
    the last call is passed.
    """
    def update(self, dt, screen):
        pass
        
    """
    Called by the game allowing the state to draw itself. The surface that is passed is the
    current drawing surface.
    """
    def draw(self, screen):
        pass
        
    def event(self, event):
        pass

class BaseGame:
            
    """
    Initialise the Raspberry Pi Game class.
    """
    def __init__(self, width, height, caption):
        
        pygame.init()
        pygame.display.set_caption(caption);
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        self.bgcolor = pygame.Color(0, 0, 0)
        self.state = None
        
    """
    Change the current state. If the newState is 'None' then the game will terminate.
    """
    def changeState(self, newState):
        if ( self.state != None ):
            self.state.exit()
            
        if ( newState == None ):
            pygame.quit()
            sys.exit()	
            
        prevState = self.state
        self.state = newState
        newState.enter(prevState)

    """
    Run the game. Initial state must be supplied.
    """
    def run(self, initialState):
        
        self.changeState( initialState )
        
        dt = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state.exit()
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
