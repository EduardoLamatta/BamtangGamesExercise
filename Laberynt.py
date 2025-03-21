import random

def AssingMatrixSize():
    randomNum = random.randint(10, 11)
    sizeMaze = 2 * randomNum + 1
    return sizeMaze




#MAZE GENERATER
fx ,fy = 0, 0
num = 2

def MazeGenerater(position, size):

    global fx, fy

    directions = [(-num, 0), (num, 0), (0, -num), (0, num)]
    random.shuffle(directions)

    x, y = position

    for dx, dy in directions:

        nx = x + dx
        ny = y + dy

        newPosition = (nx, ny)

        if 0 < nx < size - 1 and 0 < ny < size - 1 and mazeMatrix[x + dx][y + dy] == '*':
            mazeMatrix[x + dx][ y + dy] = '#'
            mazeMatrix[x + (dx // 2)][y + (dy // 2)] =  '#'
            fx = x + dx
            fy = y + dy
            MazeGenerater(newPosition, size)

    return 
   

#VERIFY ROAD LENGH

value = 0
crossroadsPositionsDict = {}
positionFinalDict = {}

def VerifyLenghLaberynt(position):

    global crossroadsPositionsDict
    global value

    count = 0

    x, y = position

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:

        nx = x + dx
        ny = y + dy

        newPosition = (nx, ny)

        if mazeMatrix[nx][ny] == '#':
            count += 1

    if count == 0:
        positionFinalDict[position] = value

    if count > 1:
        crossroadsPositionsDict[position] = value
    elif count == 0 and crossroadsPositionsDict:
        lastPosition = next(reversed(crossroadsPositionsDict))
        value = crossroadsPositionsDict.pop(lastPosition, None)
        VerifyLenghLaberynt(lastPosition)

    for dx, dy in directions:
        
        nx = x + dx
        ny = y + dy

        newPosition = (nx, ny)

        if mazeMatrix[x + dx][y + dy] == '#':
            value += 1
            mazeMatrix[x + dx][ y + dy] = ' '
            # if value < 10:
            #     mazeMatrix[x + dx][ y + dy] = "0" + str(value)
            # else: 
            #     mazeMatrix[x + dx][ y + dy] = str(value)

            VerifyLenghLaberynt(newPosition)


    return


#ASSING VALUE B

def AssingValueB():

    global mazeMatrix

    position = {}
    position = dict(sorted(positionFinalDict.items(), key= lambda x: x[1]))

    lastPosition = next(reversed(position))

    x, y = lastPosition
    mazeMatrix[x][y] = 'B'

    return position

def CreateMaze2D(n):
    MazeGenerater((1, 1), n)
    VerifyLenghLaberynt((1, 1))
    positionFinalDict = AssingValueB()

while (True):
    input("press enter")
    sizeMaze = AssingMatrixSize()

    fx ,fy = 0, 0
    num = 2
    
    value = 0
    crossroadsPositionsDict = {}
    positionFinalDict = {}

    mazeMatrix = [['*' for _ in range(sizeMaze)] for _ in range(sizeMaze)]
    mazeMatrix[1][1] = 'A'
    CreateMaze2D(sizeMaze)
    for row in mazeMatrix:
        print(" ".join(row))



