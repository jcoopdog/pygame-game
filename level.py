import pygame
from events import *
from bullet import CircleBullet

class PopEvent(Event):

    def __init__(self, wait, pos: tuple, bullet_count, bullet_speed=20):
        self.wait = wait
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

    def update(self, dt):
        for b in self.bullets:
            self.state.controllers["bullets"].add(b)
        return True

# TODO: make a tool for making levels
LEVEL = [ \
        PopEvent(1, (300, 300), 5), \
        PopEvent(1, (400, 300), 8), \
        PopEvent(1, (800, 600), 360), \
        PopEvent(10, (800, 600), 1000), \
        Event(60) \
        ]

