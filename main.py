import pygame, sys, os
from coopergame import BaseGame
from mainstate import *
from interstate import *
from level import LEVEL

filepath = os.path.dirname(os.path.abspath(__file__))
os.chdir(filepath)

game = BaseGame( 1280, 720, "gaem" )
game.bgcolor = "#282c34"
pauseState = ToggleState(game, "PAUSED", fillbg=False)
levelendState = InterState(game, "LEVEL OVER")
mainState = MainState(game, LEVEL, pauseState, levelendState)

game.run( mainState )


