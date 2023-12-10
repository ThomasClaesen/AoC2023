import aoc
import numpy as np

data = aoc.get_input(10).splitlines()

testData1 = ["-L|F7",
             "7S-7|",
             "L|7||",
             "-L-J|",
             "L|-JF"]

testData2 = ["7-F7-",
             ".FJ|7",
             "SJLL7",
             "|F--J",
             "LJ.LJ"]


def main(data):
    gridOfPipes = []
    for lineOfPipes in data:
        gridOfPipes.append(list(lineOfPipes))
    gridOfPipes = np.array(gridOfPipes)
    (startY, startX) = np.where(gridOfPipes == "S")
    startX = startX[0]
    startY = startY[0]
    gridOfPipes[startY, startX] = "7"
    x = startX
    y = startY
    dictVisited = {}
    dictVisited.update({(x,y):True})
    #test = dictVisited.get((startX+1,startY))
    backToStart = False
    totalSteps = 0
    while not backToStart:
        totalSteps = totalSteps + 1
        stepDone = False

        # up
        if (gridOfPipes[y][x] in 'J|L') & (not stepDone):
            if dictVisited.get((x, y-1)) is None:
                dictVisited.update({(x, y-1): True})
                y = y-1
                stepDone = True

        # down
        if (gridOfPipes[y][x] in '7|F') & (not stepDone):
            if dictVisited.get((x, y+1)) is None:
                dictVisited.update({(x, y+1): True})
                y = y+1
                stepDone = True

        # left
        if (gridOfPipes[y][x] in 'J-7') & (not stepDone):
            if dictVisited.get((x-1, y)) is None:
                dictVisited.update({(x-1, y): True})
                x = x-1
                stepDone = True

        # right
        if (gridOfPipes[y][x] in 'F-L') & (not stepDone):
            if dictVisited.get((x+1, y)) is None:
                dictVisited.update({(x+1, y): True})
                x = x+1
                stepDone = True

        backToStart = ((x == startX) & (y == startY))

        #No remaining steps = loop done
        if not stepDone:
            backToStart = True

    print(str(totalSteps/2))

if __name__ == "__main__":
    main(data)
