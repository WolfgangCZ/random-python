import pygame
from pixel_drawer import PixelDrawer
from body_factory import BodyFactory
from pygame.math import Vector2
from body_shapes import enemy_pix_top, enemy_pix_mid, enemy_pix_bot
from enemy import Enemy

WIN_WIDTH = 800
WIN_HEIGHT = 600
START_POS = Vector2(50, 50)
PIXEL_SIZE = 4

NUM_ENEMY_ROWS = 5
NUM_ENEMY_COLS = 11


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
    def __init__(self, cols, rows, pos: Vector2, grid_w, grid_h):
        self.rows = rows
        self.cols = cols
        self.pos = pos
        self.grid_w = grid_w
        self.grid_h = grid_h

    def get_pos(self, pos: Vector2, col, row):
        curr_pos = Vector2()
        curr_pos.x = pos.x + col*self.grid_w/self.cols
        curr_pos.y = pos.y + row*self.grid_h/self.rows
        return curr_pos
# TODO color of bodies

FPS = 60
SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()
timer = 0
frame = 0
running = True

pixel_drawer = PixelDrawer(SCREEN, PIXEL_SIZE)
body_factory = BodyFactory()
line_grid = LineGrid(SCREEN, WIN_WIDTH, WIN_HEIGHT, PIXEL_SIZE, "gray20")
enemy_grid = EnemyGrid(NUM_ENEMY_COLS,
                       NUM_ENEMY_ROWS,
                       START_POS,
                       0.8 * WIN_WIDTH,
                       0.6 * WIN_HEIGHT)
grid_pos = Vector2(50, 50)
enemies = []

for i in range(NUM_ENEMY_ROWS):
    for j in range(NUM_ENEMY_COLS):
        if i == 0:
            enemy_pos = enemy_grid.get_pos(grid_pos, j, i)
            enemy_body_top = body_factory.create(enemy_pix_top, enemy_pos)
            enemy = Enemy(enemy_body_top)
            enemies.append(enemy)
        elif i < 3:
            enemy_pos = enemy_grid.get_pos(grid_pos, j, i)
            enemy_body_mid = body_factory.create(enemy_pix_mid, enemy_pos)
            enemy = Enemy(enemy_body_mid)
            enemies.append(enemy)
        else:
            enemy_pos = enemy_grid.get_pos(grid_pos, j, i)
            enemy_body_bot = body_factory.create(enemy_pix_bot, enemy_pos)
            enemy = Enemy(enemy_body_bot)
            enemies.append(enemy)






while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
    SCREEN.fill(BACKGROUND_COLOR)

    for enemy in enemies:
        pixel_drawer.draw(enemy.body)
    # line_grid.draw_grid()

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()










