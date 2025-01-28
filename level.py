import pygame
from events import *
from bullet import CircleBullet

class PopEvent(Event):

    def __init__(self, wait, pos: tuple, bullet_count, bullet_speed=20):
        super().__init__(wait)
        self.x, self.y = pos
        self.bullet_count = bullet_count
        self.bullet_speed = bullet_speed
        self.bullets = []

    def start(self, game, state):
        super().start(game, state)
        spread = 360 / self.bullet_count + 1
        for i in range(self.bullet_count):
            b = CircleBullet(self.x, self.y, spread*i, self.bullet_speed)
            self.bullets.append(b)

    def update(self, dt, screen):
        for b in self.bullets:
            self.state.bullets.add(b)
        return True

class BeamXEvent(Event):

    def __init__(self, wait, pos, dir, color="#FF0000", speed=10):
        self.wait = wait
        self.speed = speed
        self.color = color
        self.pos = pos
        self.dir = dir
        self._left = 0
        self._width = 0
    
    def start(self, game, state):
        super().start(game, state)
        pos = self.pos
        del self.pos
        top = min(pos)
        height = max(pos) - min(pos)
        if self.dir == -1:
            self._left =  self.game.screen.get_width() - 1
        else:
            self._left = 1
        self._width = 1
        self.rect = pygame.Rect(self._left, top, 1, height)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, dt, screen):
        self._left += self.dir * self.speed * dt
        self._width += self.speed * dt
        if self.dir == -1:self.rect.left = self._left
        self.rect.width = self._width
        if self.rect.w > screen.get_width():
            return True
        return False
    
class BeamYEvent(Event):

    def __init__(self, wait, pos, dir, color="#FF0000", speed=10):
        self.wait = wait
        self.speed = speed
        self.color = color
        self.pos = pos
        self.dir = dir
        self._top = 0
        self._height = 0
    
    def start(self, game, state):
        super().start(game, state)
        pos = self.pos
        del self.pos
        left = min(pos)
        width = max(pos) - min(pos)
        if self.dir == -1:
            self._top =  self.game.screen.get_height() - 1
        else:
            self._top = 0
        self._height = 1
        self.rect = pygame.Rect(left, self._top, width, self._height)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, dt, screen):
        self._top += self.dir * self.speed * dt
        self._height += self.speed * dt
        if self.dir == -1:self.rect.top = self._top
        self.rect.height = self._height
        if self.rect.h > screen.get_height():
            return True
        return False


# TODO: make a tool for making levels
LEVEL = [ \
        BeamYEvent(3, (300, 350), -1, speed = 100), \
        BeamYEvent(3, (300, 350), 1, speed = 100), \
        BeamXEvent(5, (300, 600), -1, speed = 100), \
        BeamXEvent(10, (300, 600), 1, speed = 100), \
        PopEvent(1, (300, 300), 5), \
        PopEvent(1, (400, 300), 8), \
        PopEvent(1, (800, 600), 360), \
        PopEvent(10, (800, 600), 1000), \
        Event(60) \
        ]

