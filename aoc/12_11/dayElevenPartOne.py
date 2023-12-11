import aoc
import numpy as np

data = aoc.get_input(11).splitlines()

testData = ["...#......",
            ".......#..",
            "#.........",
            "..........",
            "......#...",
            ".#........",
            ".........#",
            "..........",
            ".......#..",
            "#...#....."]


def main(data):
    coordsOfPlanets = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                coordsOfPlanets.append([x,y])
    print(coordsOfPlanets)

    #Expand rows
    for y in range(len(data)-1,-1,-1):
        rowIsEmpty = True
        for x in range(len(data[y])-1,-1,-1):
            rowIsEmpty = rowIsEmpty & (data[y][x] == '.')
        if rowIsEmpty:
            for planet in coordsOfPlanets:
                if planet[1] > y:
                    planet[1] = planet[1] + 1

    print(coordsOfPlanets)

    #Expand columns
    for x in range(len(data[0])-1,-1,-1):
        columnIsEmpty = True
        for y in range(len(data)-1,-1,-1):
            columnIsEmpty = columnIsEmpty & (data[y][x] == '.')
        if columnIsEmpty:
            for planet in coordsOfPlanets:
                if planet[0] > x:
                    planet[0] = planet[0] + 1

    print(coordsOfPlanets)

    totalDistance = 0
    for i in range(len(coordsOfPlanets)):
        for j in range(len(coordsOfPlanets)):
            distanceX = abs(coordsOfPlanets[i][0] - coordsOfPlanets[j][0])
            distanceY = abs(coordsOfPlanets[i][1] - coordsOfPlanets[j][1])
            totalDistance = totalDistance + distanceX + distanceY

    print("solution = " + str(totalDistance/2))


if __name__ == "__main__":
    main(data)
