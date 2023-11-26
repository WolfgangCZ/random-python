import pygame
import random

pygame.init()

class Vec2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
DIR_UP = Vec2(0, -1)
DIR_DOWN = Vec2(0, 1)
DIR_LEFT = Vec2(-1, 0)
DIR_RIGHT = Vec2(1, 0)

#TODO check boundaries for loop 
#TODO generate snack 
#TODO make it so its a head and list of body coordinates 

f = open("08-snake/score.txt", "r")
high_score = int(f.readline())
print(high_score)
f.close()



score = 0


class InfoPanel:
    def __init__(self, name) -> None:
        self.name = name

class SnakeField:
    
    global score
    global screen
    snake = list()
    snack = Vec2(2,4)

    def __init__(self, window: pygame.Rect, grid: int) -> None:
        self.window = window
        self.grid = grid
        self.tile_size = window.width/grid

    def init(self, starting_pos: Vec2):
        self.snake.clear()
        self.snake.append(starting_pos)

    def drawEverthing(self):
        for i in self.snake:
            pygame.draw.rect(screen, "black", pygame.Rect(self.window.x + i.x * self.tile_size, self.window.y + i.y * self.tile_size, self.tile_size, self.tile_size))
            pygame.draw.rect(screen, BACKGROUND_COLOR, pygame.Rect(self.window.x + i.x * self.tile_size, self.window.y + i.y * self.tile_size, self.tile_size, self.tile_size), 1)
        pygame.draw.rect(screen, "blue", pygame.Rect(self.window.x + self.snack.x * self.tile_size, self.window.y + self.snack.y * self.tile_size, self.tile_size, self.tile_size ))

    def moveSnake(self, dir: Vec2):
        temp_head = Vec2(self.snake[0].x + dir.x, self.snake[0].y + dir.y)
        temp_head.x %= self.grid
        temp_head.y %= self.grid
        self.snake.insert(0, temp_head)
        if not self.checkSnack(): 
            self.snake.pop(len(self.snake)-1)

    def checkCollision(self) -> bool:
        for i in range(len(self.snake)):
            if i == 0:
                continue
            if self.snake[i].x == self.snake[0].x and self.snake[i].y == self.snake[0].y:
                return True
        return False
        
    def checkSnack(self):
        if self.snake[0].x == self.snack.x and self.snake[0].y == self.snack.y:
            self.regenerateSnack()
            return True
        return False
    
    def regenerateSnack(self):
        self.snack.x = random.randint(0, self.grid-1)
        self.snack.y = random.randint(0, self.grid-1)
        for vec in self.snake:
            if vec.x == self.snack.x and vec.y == self.snack.y:
                self.regenerateSnack()




WIN_WIDTH = 800 
WIN_HEIGHT = 600
WIN_PANEL_HEIGHT = 40
WIN_PANEL_X = 0
WIN_PANEL_Y = 0
BACKGROUND_COLOR = "white"

SNAKE_WIN_WIDTH = min(WIN_WIDTH, (WIN_HEIGHT-WIN_PANEL_HEIGHT))
SNAKE_WIN_HEIGHT = SNAKE_WIN_WIDTH
SNAKE_WIN_X = WIN_WIDTH/2 - SNAKE_WIN_WIDTH/2
SNAKE_WIN_Y = WIN_HEIGHT/2 - SNAKE_WIN_HEIGHT/2 + WIN_PANEL_HEIGHT/2

GRID_NUM = 20 #in a row and its a square
STARTING_POS = Vec2(int(GRID_NUM/2), int(GRID_NUM/2))

info_panel_rect = pygame.Rect(WIN_PANEL_X, WIN_PANEL_Y, WIN_WIDTH, WIN_PANEL_HEIGHT)

game_window_rect = pygame.Rect(SNAKE_WIN_X, SNAKE_WIN_Y, SNAKE_WIN_WIDTH, SNAKE_WIN_HEIGHT)
game_window = SnakeField(game_window_rect, GRID_NUM)
game_window.init(STARTING_POS)



FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
timer = 0
dt = 0

# fonts = pygame.font.get_fonts()
# print(len(fonts))
# for f in fonts:
#     print(f)

blue = (0,0,255)


font_bahn = pygame.font.SysFont("bahnschrift", 30)

hscore_text = font_bahn.render(f'High score: {high_score}', True, blue, "white")
hscore_text_rect = hscore_text.get_rect()
hscore_text_rect.topleft = (0,0)

score_text = font_bahn.render(f'Score: {high_score}', True, blue, "white")
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (WIN_WIDTH/2,0)

end_text = font_bahn.render(f'Game over, press R to play again', True, blue, "white")
end_text_rect = end_text.get_rect()
end_text_rect.center = (WIN_WIDTH/2,WIN_HEIGHT/2)


snake_direction = DIR_UP
tail_direction = DIR_UP
snake_speed = 10 ##ticks per second
running = True
frame = 0
game_over = False

while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND_COLOR)

    if not game_over:
        score = len(game_window.snake)-1
        hscore_text = font_bahn.render(f'High score: {high_score}', True, blue, "white")
        score_text = font_bahn.render(f'Score: {score}', True, blue, "white")

        screen.blit(score_text,score_text_rect)
        screen.blit(hscore_text,hscore_text_rect)

        game_window.drawEverthing()

        #keyboards

        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT] and snake_direction != DIR_LEFT:
            snake_direction = DIR_RIGHT
        if key[pygame.K_LEFT] and snake_direction != DIR_RIGHT:
            snake_direction = DIR_LEFT
        if key[pygame.K_UP] and snake_direction != DIR_DOWN:
            snake_direction = DIR_UP
        if key[pygame.K_DOWN] and snake_direction != DIR_UP:
            snake_direction = DIR_DOWN

        if int(frame)%(int(FPS/snake_speed)) == 0:
            game_window.moveSnake(snake_direction)


        frame += 1
        pygame.draw.rect(screen, "blue", info_panel_rect, 2)
        pygame.draw.rect(screen, "red", game_window_rect, 2)
        pygame.display.flip()
        clock.tick(FPS)
        if game_window.checkCollision():
            game_over = True
        
        

    
    if game_over:
        if score > high_score:
            f = open("08-snake/score.txt", "w")
            f.write(f"{score}")
            f.close()
        screen.blit(end_text,end_text_rect)
        if key[pygame.K_r]:
            game_over = False
            game_window.snake.clear()
            game_window.init()
            f = open("08-snake/score.txt", "r")
            high_score = int(f.readline())
            f.close()

pygame.quit()