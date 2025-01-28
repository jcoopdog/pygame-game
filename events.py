import pygame, os


class Event:

    def __init__(self, wait=1):
        self.wait = wait
        self.rect = pygame.Rect(-1, -1, 1, 1)

    def start(self, game, state):
        self.game = game
        self.state = state

    def update(self, dt, screen) -> bool:
        return False
    
    def draw(self, screen):
        pass

class EventManager:

    def __init__(self, game, state, level: list):
        self.game = game
        self.state = state
        self.events = []
        self.event_wait = level[0].wait
        self.event_counter = 0
        self.level = level

    def clear(self):
        self.events = []

    def remove(self, event):
        self.events.remove(event)

    def add(self, event):
        self.events.append(event)

    def update(self, dt, screen):
        self.event_wait -= dt
        if self.event_wait <= 0:
            e = self.level[self.event_counter]
            e.start(self.game, self.state)
            self.add(e)
            #if len(self.level) > self.event_counter:
            #    return True
            self.event_counter += 1
            try:
                self.event_wait = self.level[self.event_counter].wait
            except IndexError:
                return True
            return False
        for e in self.events:
            if e.update(dt, screen):
                self.remove(e)
                continue
    
    def draw(self, screen):
        for e in self.events:
            e.draw(screen)


