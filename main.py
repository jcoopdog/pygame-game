import pygame, sys, os
from base_classes import BaseGame
from gamestate import *

filepath = os.path.dirname(os.path.abspath(__file__))
os.chdir(filepath)

game = BaseGame( 1280, 720, "gaem" )
game.bgcolor = "#282c34"
mainGameState = MainGameState(game)

game.run( mainGameState )


