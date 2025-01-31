import pygame
from levelelements import *
from events import Event

LEVEL = [
        PopEvent(3, (130, 150), 5),
        PopEvent(3, (1100, 575), 5),
        PopEvent(3, (130, 575), 5),
        PopEvent(3, (1100, 150), 5),
        Event(120)
        ]
