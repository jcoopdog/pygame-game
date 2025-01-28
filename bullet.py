import pygame, math, os
from settings import *

class Bullet:

    image = pygame.image.load(os.path.join(assetdir, "bullet.png"))

    def __init__(self, startx, starty, angle, speed):
        self.x = startx
        self.y = starty
        self.xvel = speed * math.cos(math.radians(angle))
        self.yvel = speed * math.sin(math.radians(angle))
        self.image = pygame.transform.rotate(self.image, -angle)
        self.rect = self.image.get_rect(topleft=(startx, starty))
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, dt):
        self.x += self.xvel * dt
        self.y += self.yvel * dt
        self.rect.topleft = (self.x, self.y)
    
    def check_wall(self, width, height):
        if ((self.x >= width - self.image.get_width()) or (self.x <= 0) or (self.y >= height - self.image.get_height()) or (self.y <= 0)):
            return True
        else:
            return False

class BulletController:

    def __init__(self):
        self.bullets = []

    def clear(self):
        self.bullets = []
    
    def add(self, bullet):
        self.bullets.append(bullet)
    
    def remove(self, bullet):
        self.bullets.remove(bullet)
    
    def update(self, dt, screen):
        for b in self.bullets:
            b.move(dt)
            if b.check_wall(screen.get_width(), screen.get_height()):
                self.remove(b)
                continue

    def draw(self, screen):
        for b in self.bullets:
            b.draw(screen)
    
class CircleBullet(Bullet):
    
    def __init__(self, startx, starty, angle, speed, color="#FF0000"):
        self.x = startx
        self.y = starty
        self.xvel = speed * math.cos(math.radians(angle))
        self.yvel = speed * math.sin(math.radians(angle))
        self.color = color
        self.rect = pygame.Rect((startx, starty), (4, 4))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

