import pygame, os
from player import *
from bullet import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
#screen = pygame.display.set_mode((33,33))
clock = pygame.time.Clock()
running = True
dt = 0
filepath = os.path.dirname(os.path.abspath(__file__))
os.chdir(filepath)
assetdir = "assets"
pygame.display.set_caption("gaem")

player = Player(screen.get_width() / 2, screen.get_height() / 2, os.path.join(assetdir, "player.png"))
playerspeed = 13

bullets = []

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#282c34")

    player.render(screen)
    for bullet in bullets:
        bullet.render(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.yvel -= playerspeed
    if keys[pygame.K_s]:
        player.yvel += playerspeed
    if keys[pygame.K_a]:
        player.xvel -= playerspeed
    if keys[pygame.K_d]:
        player.xvel += playerspeed
    if keys[pygame.K_f]:
        bullets.append(Bullet( 300 , 300 , 50 , 45 , os.path.join(assetdir, "bullet.png")))
    
    for bullet in bullets:
        bullet.move(dt)
        if bullet.check_wall(screen.get_width(), screen.get_height()):
            bullets.remove(bullet)
    
    player.move(dt, 0.95)

    player.check_wall(screen.get_width(), screen.get_height())

    # flip() the display to put your work on screen
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()




