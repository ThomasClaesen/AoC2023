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

testData3 = ["...........",
             ".S-------7.",
             ".|F-----7|.",
             ".||OOOOO||.",
             ".||OOOOO||.",
             ".|L-7OF-J|.",
             ".|II|O|II|.",
             ".L--JOL--J.",
             ".....O....."]

testData4 = ["FF7FSF7F7F7F7F7F---7",
             "L|LJ||||||||||||F--J",
             "FL-7LJLJ||||||LJL-77",
             "F--JF--7||LJLJ7F7FJ-",
             "L---JF-JLJ.||-FJLJJ7",
             "|F|F-JF---7F7-L7L|7|",
             "|FFJF7L7F-JF7|JL---7",
             "7-L-JL7||F7|L7F-7F7|",
             "L.L7LFJ|||||FJL7||LJ",
             "L7JLJL-JLJLJL--JLJ.L"]

testData5 = [".F----7F7F7F7F-7....",
             ".|F--7||||||||FJ....",
             ".||.FJ||||||||L7....",
             "FJL7L7LJLJ||LJ.L-7..",
             "L--J.L7...LJS7F-7L7.",
             "....F-J..F7FJ|L7L7L7",
             "....L7.F7||L7|.L7L7|",
             ".....|FJLJ|FJ|F7|.LJ",
             "....FJL-7.||.||||...",
             "....L---J.LJ.LJLJ..."]


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
    dictVisited.update({(x, y): True})
    # test = dictVisited.get((startX+1,startY))
    backToStart = False
    listOfPoints = []
    listOfPoints.append((x, y))
    highestX = 0
    lowestX = 999
    highestY = 0
    lowestY = 999
    while not backToStart:
        stepDone = False

        # up
        if (gridOfPipes[y][x] in 'J|L') & (not stepDone):
            if dictVisited.get((x, y - 1)) is None:
                dictVisited.update({(x, y - 1): True})
                y = y - 1
                stepDone = True
                listOfPoints.append((x, y))
                lowestY = y if y < lowestY else lowestY

        # down
        if (gridOfPipes[y][x] in '7|F') & (not stepDone):
            if dictVisited.get((x, y + 1)) is None:
                dictVisited.update({(x, y + 1): True})
                y = y + 1
                stepDone = True
                listOfPoints.append((x, y))
                highestY = y if y > highestY else highestY

        # left
        if (gridOfPipes[y][x] in 'J-7') & (not stepDone):
            if dictVisited.get((x - 1, y)) is None:
                dictVisited.update({(x - 1, y): True})
                x = x - 1
                stepDone = True
                listOfPoints.append((x, y))
                lowestX = x if x < lowestX else lowestX

        # right
        if (gridOfPipes[y][x] in 'F-L') & (not stepDone):
            if dictVisited.get((x + 1, y)) is None:
                dictVisited.update({(x + 1, y): True})
                x = x + 1
                stepDone = True
                listOfPoints.append((x, y))
                highestX = x if x > highestX else highestX

        backToStart = ((x == startX) & (y == startY))
        # No remaining steps = loop done
        if not stepDone:
            backToStart = True

    for y in range(len(gridOfPipes)):
        for x in range(len(gridOfPipes[y])):
            if (x, y) not in listOfPoints:
                gridOfPipes[y][x] = "."

    totalPointsInside = 0
    for x in range(lowestX, highestX + 1):
        for y in range(lowestY, highestY + 1):
            if (x, y) not in listOfPoints:
                totalPointsInside = totalPointsInside + 1 if isInsideLoop(x, y, gridOfPipes) else totalPointsInside
    print("solution = " + str(totalPointsInside))


def isInsideLoop(x, y, data):
    totalVerticals = 0
    rowOfPipes = data[y]
    amountOfDashes = np.count_nonzero(rowOfPipes == '-')
    rowOfPipes = [value for value in rowOfPipes if value != '-']
    for i in range(0, x - amountOfDashes):
        symbol = rowOfPipes[i]
        nextSymbol = rowOfPipes[i + 1]
        if symbol == '|':
            totalVerticals = totalVerticals + 1
        elif (symbol == 'L') & (nextSymbol == '7'):
            totalVerticals = totalVerticals + 1
        elif (symbol == 'F') & (nextSymbol == 'J'):
            totalVerticals = totalVerticals + 1
    return totalVerticals % 2 == 1


if __name__ == "__main__":
    main(data)
