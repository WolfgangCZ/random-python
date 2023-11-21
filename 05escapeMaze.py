from enum import Enum
import time

class Direction(Enum):
    DOWN = 0
    LEFT = 1
    UP = 2
    RIGHT = 3

mazeLayout = [
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
['X',' ','X',' ',' ',' ',' ',' ','X',' ','X',' ',' ',' ',' ',' ',' ',' ','X',' ','X'],
['X',' ','X',' ','X','X','X','X','X',' ','X','X','X',' ','X',' ','X','X','X',' ','X'],
['X',' ',' ',' ','X',' ',' ',' ',' ',' ','X',' ',' ',' ','X',' ',' ',' ',' ',' ','X'],
['X',' ','X','X','X','X','X','X','X',' ','X','X','X',' ','X','X','X','X','X',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ','X',' ','X',' ',' ',' ',' ',' ','X'],
['X',' ','X',' ','X','X','X','X','X',' ','X','X','X','X','X','X','X','X','X',' ','X'],
['X',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ','X',' ',' ',' ',' ',' ','X'],
['X',' ','X',' ','X','X','X','X','X','X','X',' ','X',' ','X','X','X','X','X',' ','X'],
['X',' ','X',' ',' ',' ','X',' ',' ',' ','X',' ',' ',' ','X',' ',' ',' ',' ',' ','X'],
['X','X','X',' ','X','X','X',' ','X',' ','X',' ','X','X','X',' ','X','X','X',' ','X'],
['X',' ',' ',' ','X',' ',' ',' ','X',' ','X',' ',' ',' ','X',' ','X',' ','X',' ','X'],
['X',' ','X','X','X',' ','X',' ','X','X','X',' ','X',' ','X','X','X',' ','X',' ','X'],
['X',' ',' ',' ','X',' ','X',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ','X','X','X',' ','X','X','X',' ','X','X','X','X','X','X','X',' ','X',' ','X'],
['X',' ',' ',' ','X',' ',' ',' ','X',' ','X',' ',' ',' ','X',' ','X',' ','X',' ','X'],
['X','X','X','X','X',' ','X','X','X','X','X','X','X',' ','X',' ','X',' ','X',' ','X'],
['X',' ',' ',' ','X',' ','X',' ',' ',' ',' ',' ','X',' ','X',' ','X',' ','X',' ','X'],
['X',' ','X',' ','X',' ','X',' ','X','X','X',' ','X',' ','X',' ','X','X','X',' ','X'],
['X',' ','X',' ',' ',' ','X',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','E','X']
]

#print maze smoothly
def printMaze(maze, playerPos):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'X':
                print("X", end=' ')
                continue
            if maze[i][j] == 'E':
                print("E", end=' ')
                continue
            if maze[i][j] == 'o':
                maze[i][j] = ' '
            if maze[i][j] == ' ' and j == playerPos.x and i == playerPos.y:
                maze[i][j] = 'o'
                print("o", end=' ')
            else: 
                print(" ", end=' ')
        print("")

def checkObstacle(playerPos, maze, dir):
    obstacle = False
    obstacle = maze[playerPos.y+dir.y][playerPos.x+dir.x] == " "
    return obstacle
    
def checkExit(playerPos, maze, dir):
    exit = False
    exit = maze[playerPos.y+dir.y][playerPos.x+dir.x] == "E"
    return exit


class playerPos:
    def __init__(self, x ,y) -> None:
        self.x = x
        self.y = y

class Vector2:
    def __init__(self, x ,y) -> None:
        self.x = x
        self.y = y


iteration = 0



#make direction vector

player = playerPos(1,1)

directions = ["down", "left", "up", "right"]
dirVectors = [Vector2(0,1), Vector2(-1,0), Vector2(0,-1), Vector2(1,0)]
frontDirIndex = 0
leftDirIndex = 0
rightDirIndex = 0
backDirIndex = 0

print(dirVectors[0].x)
print(dirVectors[0].y)

fps = 5

while True:
    frontDirIndex %= 4; 
    leftDirIndex = (frontDirIndex - 1)%4
    rightDirIndex = (frontDirIndex + 1)%4
    backDirIndex = (frontDirIndex + 2)%4
    time.sleep(1/fps)
    frontIsClear = checkObstacle(player, mazeLayout,dirVectors[frontDirIndex])
    leftIsClear = checkObstacle(player, mazeLayout,dirVectors[leftDirIndex])
    print("-----------------------------------------------------------------------------")
    print("direction: {}".format(directions[frontDirIndex]))
    print("iteration: {}".format(iteration))
    print("is path clear: {}".format(frontIsClear))
    print("is left clear: {}".format(leftIsClear))
    print("-----------------------------------------------------------------------------")
    iteration += 1


    #check main dir and move if its clear
    #check side dir and rotate there if its clear
    #if not rotate opposite direction
    if checkExit(player, mazeLayout, dirVectors[frontDirIndex%4]):
        print("FINISH YOU WON, it took {} iterations".format(iteration))
        exit()

    if leftIsClear:
        frontDirIndex -= 1
        frontDirIndex %= 4

    frontIsClear = checkObstacle(player, mazeLayout,dirVectors[frontDirIndex])

    if frontIsClear:
        player.x += dirVectors[frontDirIndex].x
        player.y += dirVectors[frontDirIndex].y
    if not frontIsClear and not leftIsClear:
        frontDirIndex += 1

    printMaze(mazeLayout, player)


    

