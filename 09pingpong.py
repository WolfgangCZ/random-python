import pygame
import math
import random

class Paddle:
    global PADDLE_COLOUR
    global PADDLE_SPEED
    global WIN_HEIGHT
    global screen
    speed = 0
    def __init__(self, paddle_rec: pygame.Rect) -> None:
        self.paddle_rec = paddle_rec
    def draw(self):
        pygame.draw.rect(screen, PADDLE_COLOUR, self.paddle_rec)
        if self.paddle_rec.y <= 0:
            self.paddle_rec.y = 0
        elif self.paddle_rec.y + self.paddle_rec.height >= WIN_HEIGHT:
            self.paddle_rec.y = WIN_HEIGHT - self.paddle_rec.height
    def moveUp(self, key):
        if pygame.key.get_pressed()[key]:
            self.paddle_rec.y -= PADDLE_SPEED
    def moveDown(self, key):
        if pygame.key.get_pressed()[key]:
            self.paddle_rec.y += PADDLE_SPEED

class Vector2:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    def lenght(self) -> float:
        return float(math.sqrt(self.x*self.x + self.y*self.y))
    def normalize(self):
        l = self.lenght()
        if self.x != 0:
            t_x = 1/l*self.x
        else:
            t_x = 0
        if self.y != 0:
            t_y = 1/l*self.y
        else:
            t_y = 0
        self.x = t_x
        self.y = t_y

class Ball:
    global screen
    global BALL_COLOUR
    global WIN_WIDTH
    global WIN_HEIGHT
    global BALL_RADIUS
    def __init__(self, speed) -> None:
        self.direction = Vector2(random.random(), random.random())
        self.direction.normalize()
        self.speed = speed
        self.coord = pygame.math.Vector2(WIN_WIDTH/2, WIN_HEIGHT/2)
        print(self.direction.x)
        print(self.direction.y)
    def draw(self):
        pygame.draw.circle(screen, BALL_COLOUR, self.coord, BALL_RADIUS)
        self.checkBoundaries()
    def move(self):
        self.coord.x += self.speed*self.direction.x
        self.coord.y += self.speed*self.direction.y
    def checkBoundaries(self):
        #bottom
        if self.coord.y + BALL_RADIUS > WIN_HEIGHT:
            self.coord.y = WIN_HEIGHT - BALL_RADIUS
            self.direction.y *= -1
        #top
        if self.coord.y - BALL_RADIUS < 0:
            self.coord.y = BALL_RADIUS
            self.direction.y *= -1
            
    def checkCollision(self):
        pass

PADDLE_WIDTH = 50

WIN_WIDTH = 800
WIN_HEIGHT = 600
BACKGROUND_COLOR = "black"
PADDLE_OFFSET = 20
PADDLE_WIDTH = 100
PADDLE_THICKNESS = 20
PADDLE_COLOUR = "white"
BALL_COLOUR = "white"
PADDLE_SPEED = 5
BALL_SPEED = 5
BALL_RADIUS = 8
PLAYER_LEFT_UP = pygame.K_w
PLAYER_LEFT_DOWN = pygame.K_s
PLAYER_RIGHT_UP = pygame.K_UP
PLAYER_RIGHT_DOWN = pygame.K_DOWN

PADDLE_LEFT_RECT = pygame.Rect(PADDLE_OFFSET, WIN_HEIGHT/2, PADDLE_THICKNESS, PADDLE_WIDTH)
PADDLE_RIGHT_RECT = pygame.Rect(WIN_WIDTH - PADDLE_OFFSET - PADDLE_THICKNESS, WIN_HEIGHT/2, PADDLE_THICKNESS, PADDLE_WIDTH)

paddle_left = Paddle(PADDLE_LEFT_RECT)
paddle_right = Paddle(PADDLE_RIGHT_RECT)
ball = Ball(BALL_SPEED)

FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
timer = 0
running = True


frame = 0

while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND_COLOR)
    frame += 1
    paddle_left.moveUp(PLAYER_LEFT_UP)
    paddle_left.moveDown(PLAYER_LEFT_DOWN)
    paddle_right.moveUp(PLAYER_RIGHT_UP)
    paddle_right.moveDown(PLAYER_RIGHT_DOWN)
    ball.move()
    ball.draw()
    paddle_left.draw()
    paddle_right.draw()

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()