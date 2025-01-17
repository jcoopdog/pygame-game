import pygame
from player import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player = Player(screen.get_width() / 2, screen.get_height() / 2)
playerspeed = 3

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    player.render(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.yvel -= playerspeed
    if keys[pygame.K_s]:
        player.yvel += playerspeed
    if keys[pygame.K_a]:
        player.xvel -= playerspeed
    if keys[pygame.K_d]:
        player.xvel += playerspeed
    
    player.move(dt, 0.99)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()




