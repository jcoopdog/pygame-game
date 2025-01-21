import pygame, math

class Bullet:
    
    def __init__(self, startx, starty, speed, angle, imgpath):
        self.x = startx
        self.y = starty
        self.xvel = speed * math.cos(math.radians(angle))
        self.yvel = speed * math.sin(math.radians(angle))
        self.image = pygame.transform.rotate(pygame.image.load(imgpath), angle)
        self.rect = self.image.get_rect(topleft=(startx, starty))
    
    def render(self, screen):
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

