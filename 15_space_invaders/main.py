import pygame

print("hello world")

WIN_WIDTH = 800
WIN_HEIGHT = 600
BACKGROUND_COLOR = "black"

pygame.init()

FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
timer = 0
running = True

text_pad = 10

score_left = 0
score_right = 0

frame = 0

running = True

class enemy:
    def __init__(self):
        pass

class body:
    def __init__(self):
        pass



while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND_COLOR)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
