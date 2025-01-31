import pygame,sys

try:
    width = sys.argv[1]
    height = sys.argv[2]
except IndexError:
    if not sys.flags.quiet == 1 :print("Screen size not entered!\nUsing 1280x720 as screen size.")
    width = 1280
    height = 720

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

screen.fill( "#282c34" )
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            mousepos = event.pos
            pygame.display.set_caption(str(event.pos))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print(mousepos)

    dt = clock.tick(60) / 1000
