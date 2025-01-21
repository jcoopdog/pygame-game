import pygame, random, os
from bullet import *
from settings import *

class Sentry:
    
    def __init__(self, startx, starty, imgpath):
        self.x = startx
        self.y = starty
        self.image = pygame.image.load(imgpath)
        self.rect = self.image.get_rect(topleft=(startx, starty))
        self.cooldown = 0
    
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def tick(self, dt):
        if self.cooldown > 0:
            self.cooldown -= dt
            return (False, None)
        self.cooldown = random.randint(100,300) / 100
        dir = random.randint(0,3) * 90
        bullet = Bullet(self.rect.centerx, self.rect.centery, 20, dir, os.path.join(assetdir, "bullet.png"))
        return (True, bullet)
