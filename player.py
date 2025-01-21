import pygame

class Player:
    
    def __init__(self, startx, starty, speed, imgpath):
        self.x = startx
        self.y = starty
        self.xvel = 0
        self.yvel = 0
        self.speed = speed
        self.image = pygame.image.load(imgpath)
        self.rect = self.image.get_rect(topleft=(startx, starty))
    
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, keys, dt, friction):
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

