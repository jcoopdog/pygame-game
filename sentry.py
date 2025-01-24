import pygame, random, os
from bullet import *
from settings import *

class Sentry:

    image = pygame.image.load(os.path.join(assetdir, "sentry.png"))

    def __init__(self, startx, starty, lifespan = 23):
        self.x = startx
        self.y = starty
        self.lifespan = lifespan
        self.rect = self.image.get_rect(topleft=(startx, starty))
        self.cooldown = 0
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def tick(self, dt, bullets):
        if self.lifespan <= 0:
            return True
        self.lifespan -= dt
        if self.cooldown > 0:
            self.cooldown -= dt
            return False
        self.cooldown = random.randint(100,300) / 100
        angle = random.randint(0,7) * 45
        bullet = Bullet(self.rect.centerx, self.rect.centery, angle, 40)
        bullets.add(bullet)
        return False

class SentryController:
    
    def __init__(self, bulletController, cd = 5):
        self.sentrys = []
        self.bullets = bulletController
        self.spwn_cd_max = cd
        self.spwn_cd = self.spwn_cd_max

    def clear(self):
        self.sentrys = []

    def add(self, sentry):
        self.sentrys.append(sentry)

    def remove(self, sentry):
        self.sentrys.remove(sentry)

    def update(self, dt, screen):
        self.spwn_cd -= dt
        if self.spwn_cd <= 0:
            x = random.randint(0, screen.get_width() - Sentry.image.get_width())
            y = random.randint(0, screen.get_height() - Sentry.image.get_height())
            self.sentrys.append(Sentry(x, y))
            self.spwn_cd = self.spwn_cd_max
        for s in self.sentrys:
            if s.tick(dt, self.bullets):
                self.remove(s)

    def draw(self, screen):
        for s in self.sentrys:
            s.draw(screen)
