import pygame, sys, os
from base_classes import BaseGame
from gamestate import *
from pausestate import *

filepath = os.path.dirname(os.path.abspath(__file__))
os.chdir(filepath)

game = BaseGame( 1280, 720, "gaem" )
game.bgcolor = "#282c34"
pauseState = PauseState(game)
mainGameState = MainGameState(game, pauseState)

game.run( mainGameState )


