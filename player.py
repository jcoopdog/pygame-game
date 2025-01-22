import pygame, os
from settings import *
from utils import *

class Player:
    os.chdir(assetdir)
    images = { "green" : pygame.image.load("player_green.png"), \
               "red"   : pygame.image.load("player_red.png") }
    os.chdir("..")

    def __init__(self, startx, starty, speed=13, imgpath=os.path.join(assetdir, "player.png"), damage_cd_max = 1):
        self.x = startx
        self.y = starty
        self.xvel = 0
        self.yvel = 0
        self.speed = speed
        self.damage_cd = 0
        self.damage_cd_max = damage_cd_max
        self.image = self.images["green"]
        self.rect = self.image.get_rect(topleft=(startx, starty))
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, dt, screen, friction=0.95, keys=None):
        if keys == None:
            keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.yvel -= self.speed
        if keys[pygame.K_s]:
            self.yvel += self.speed
        if keys[pygame.K_a]:
            self.xvel -= self.speed
        if keys [pygame.K_d]:
            self.xvel += self.speed
        self.xvel *= friction
        self.yvel *= friction
        self.x += self.xvel * dt
        self.y += self.yvel * dt
        self.rect.topleft = (self.x, self.y)
        self.check_wall(screen.get_width(), screen.get_height())
        self.damage_cd -= dt
        if self.damage_cd > 0:
            self.image = self.images["red"]
        else:
            self.image = self.images["green"]
    
    def check_wall(self, width, height):
        if (self.x >= width - self.image.get_width()):
            self.x = width - self.image.get_width()
            self.xvel *= -1
        if (self.x <= 0):
            self.x = 0
            self.xvel *= -1
        if (self.y >= height - self.image.get_height()):
            self.y = height - self.image.get_height()
            self.yvel *= -1
        if (self.y <= 0):
            self.y = 0
            self.yvel *= -1

    def check_projectiles(self, proj, projcon):
        if self.damage_cd > 0:
            return
        for p in proj:
            if self.rect.colliderect(p):
                projcon.remove(p)
                self.damage()
                break

    def damage(self):
        self.image = self.images["red"]
        self.xvel += 30 * cmp(self.xvel, 0)
        self.yvel += 30 * cmp(self.yvel, 0)
        self.xvel *= -1
        self.yvel *= -1
        self.damage_cd = self.damage_cd_max



