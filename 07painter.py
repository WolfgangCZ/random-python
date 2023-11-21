import pygame
import copy

pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 600

PANEL_WIDTH = 50
PANEL_HEIGHT = 50

CANVAS_WIDTH = WIN_WIDTH
CANVAS_HEIGHT = WIN_HEIGHT - PANEL_HEIGHT


screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


class Vec2:
    def __init__(self, x ,y) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, start_pos: Vec2, end_pos: Vec2) -> None:
        self.start_pos = start_pos
        self.end_pos = end_pos

class LinesBuffer:
    
    def __init__(self, color = "black", width = 1) -> None:
        self.color = color
        self.width = width
        self.lines = []
    
    def AddLine(self, start_pos: Vec2, end_pos: Vec2):
        self.lines.append((start_pos, end_pos))

    def DrawLines(self, screen):
        # print(len(self.lines))
        for line in self.lines:
            pygame.draw.line(screen, self.color, (line[0].x, line[0].y), (line[1].x, line[1].y), self.width)
            # print((line[0].x, line[0].y), (line[1].x, line[1].y))
            
    def print_lines_coord(self):
        
        for line in self.lines:
            pass
            # print(str(line[0].x) + " " + str(line[0].y))



clock = pygame.time.Clock()
running = True
IsDrawing = False

dt = 0
player_pos = pygame.Vector2(WIN_WIDTH / 2, WIN_HEIGHT / 2)
speed = 1000

start_mouse_pos = Vec2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
end_mouse_pos = Vec2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

linesBuffer = LinesBuffer()

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    
    

    end_mouse_pos.x = pygame.mouse.get_pos()[0]
    end_mouse_pos.y = pygame.mouse.get_pos()[1]
    #it doesnt work like this
    # if pygame.mouse.get_pressed()[0]:
    #     linesBuffer.AddLine(copy.deepcopy(start_mouse_pos), copy.deepcopy(end_mouse_pos))
    #     # print(pygame.mouse.get_pos()[0])
    #     # print(pygame.mouse.get_pos()[1])
    #     #print(pygame.mouse.get_pressed()[0])
    linesBuffer.DrawLines(screen)
    
    # linesBuffer.print_lines_coord()


    pygame.display.flip()
    clock.tick(300)
    dt = clock.tick(60) / 1000

    start_mouse_pos.x = end_mouse_pos.x
    start_mouse_pos.y = end_mouse_pos.y
    print(len(linesBuffer.lines))



pygame.quit()