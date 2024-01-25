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


class LineGrid:
    def __init__(self, screen, win_w, win_h, pixel_size, color):
        self.pixel_size = pixel_size
        self.color = color
        self.win_w = win_w
        self.win_h = win_h
        self.screen = screen

    def draw_grid(self):
        for i in range(int(self.win_w/self.pixel_size)+1):
            pygame.draw.line(self.screen, self.color,
                             (self.pixel_size*i, 0),
                             (self.pixel_size*i, self.win_h), 1)
        for i in range(int(self.win_h/self.pixel_size+1)):
            pygame.draw.line(self.screen, self.color,
                             (0, self.pixel_size*i),
                             (self.win_w, self.pixel_size*i), 1)


class EnemyGrid:
    def __init__(self, cols, rows, pixel_size, pad_hor, pad_ver):
        self.rows = rows
        self.cols = cols
        self.pad_hor = pad_hor
        self.pad_ver = pad_ver


FPS = 60
SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()
timer = 0
frame = 0
running = True

pixel_drawer = PixelDrawer(SCREEN, PIXEL_SIZE)
body_factory = BodyFactory()
enemy_body_mid = body_factory.create(enemy_pix_mid, Vector2(100, 100))
enemy = Enemy(enemy_body_mid)
line_grid = LineGrid(SCREEN, WIN_WIDTH, WIN_HEIGHT, PIXEL_SIZE, "gray20")


while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
    SCREEN.fill(BACKGROUND_COLOR)
    # grid
    pixel_drawer.draw(enemy.body)
    line_grid.draw_grid()

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()










