import pygame, os
from player import *
from bullet import *
from utils import *
from settings import *
from sentry import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
#screen = pygame.display.set_mode((33,33))
clock = pygame.time.Clock()
running = True
dt = 0
filepath = os.path.dirname(os.path.abspath(__file__))
os.chdir(filepath)
pygame.display.set_caption("gaem")

damage_cd = 0
damage_cd_max = 1

playerspeed = 13
player = Player(screen.get_width() / 2, screen.get_height() / 2, playerspeed, os.path.join(assetdir, "player.png"))

bullets = []
sentrys = []
keys = []

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == damage_event:
            if damage_cd <= 0:
                player.image = pygame.image.load(os.path.join(assetdir, "player_damage.png"))
                player.xvel += 30 * cmp(player.xvel, 0)
                player.yvel += 30 * cmp(player.yvel, 0)
                player.xvel *= -1
                player.yvel *= -1
                damage_cd = damage_cd_max
        else:
            player.image = pygame.image.load(os.path.join(assetdir, "player.png"))
    damage_cd -= dt          

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#282c34")

    player.render(screen)
    for bullet in bullets:
        bullet.render(screen)
    for sentry in sentrys:
        sentry.render(screen)

    prevkeys = keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_g]:
        bullets.append(Bullet( 300 , 300 , 50 , 45 , os.path.join(assetdir, "bullet.png")))
    if keys[pygame.K_h]:
        bullets.append(Bullet( 300 , 300 , 0 , 45 , os.path.join(assetdir, "bullet.png")))
    if keys[pygame.K_j] and not prevkeys[pygame.K_j]:
        sentrys.append(Sentry(player.x, player.y, os.path.join(assetdir, "sentry.png")))
    
    player.move(keys, dt, 0.95)
    player.check_wall(screen.get_width(), screen.get_height())

    for bullet in bullets:
        bullet.move(dt)
        if bullet.check_wall(screen.get_width(), screen.get_height()):
            bullets.remove(bullet)
        if player.rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(damage_event))
    for sentry in sentrys:
        tickdata = sentry.tick(dt)
        if tickdata[0]:
            bullets.append(tickdata[1])
    

    # flip() the display to put your work on screen
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()




