import pygame
from pixel_drawer import PixelDrawer
from body_factory import BodyFactory
from pygame.math import Vector2
from body_shapes import enemy_pix_mid
from enemy import Enemy

WIN_WIDTH = 800
WIN_HEIGHT = 600

PIXEL_SIZE = 5

BACKGROUND_COLOR = "black"

pygame.init()

FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
timer = 0
frame = 0
running = True

pixel_drawer = PixelDrawer(screen, PIXEL_SIZE)
body_factory = BodyFactory()
enemy_body_mid = body_factory.create(enemy_pix_mid, Vector2(100, 100))
enemy = Enemy(enemy_body_mid)


while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND_COLOR)
    for i in range(int(WIN_WIDTH/PIXEL_SIZE)+1):
        pygame.draw.line(screen, "gray20",
                         (PIXEL_SIZE*i, 0),
                         (PIXEL_SIZE*i, WIN_HEIGHT), 1)
    for i in range(int(WIN_HEIGHT/PIXEL_SIZE+1)):
        pygame.draw.line(screen, "gray20",
                         (0, PIXEL_SIZE*i),
                         (WIN_WIDTH, PIXEL_SIZE*i), 1)
    pixel_drawer.draw(enemy_body_mid)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
