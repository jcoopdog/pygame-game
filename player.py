import pygame

class Player:
    
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty
        self.xvel = 0
        self.yvel = 0
    
    def render(self, screen):
        pygame.draw.circle(screen, "red", (self.x, self.y), 40)

    def move(self, dt, friction):
        self.xvel *= friction
        self.yvel *= friction
        self.x += self.xvel * dt
        self.y += self.yvel * dt
