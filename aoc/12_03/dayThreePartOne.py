import re

import aoc

data = aoc.get_input(3).splitlines()

testData = ["4.....114.",
            ".*....*...",
            "..35..633.",
            "......#..*",
            "617.......",
            "...*.+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.."]


def main(data):
    total = 0
    indexY = -1
    for dataRow in data:
        indexY = indexY + 1
        listOfNumbers = list(filter(None, re.split(r'\D+', dataRow)))
        editedDataRow = dataRow
        for number in listOfNumbers:
            indexX = editedDataRow.find(number)
            editedDataRow = editedDataRow.replace(number, '.' * len(number), 1)
            adjacent = findIfAdjacent(indexX, indexY, len(number), data)
            if adjacent:
                print(number)
                total = total + int(number)

    print("answer = " + str(total))


def findIfAdjacent(x, y, length, data):
    result = False
    for j in range(y-1, y+2):
        for i in range(x-1, x+length+1):
            indexX = clampX(i, data)
            indexY = clampY(j, data)
            symbol = data[indexY][indexX]
            if (not symbol.isnumeric()) & (symbol != '.'):
                result = True
                return result
    return result

def clampX(x, data):
    if x < 0:
        return 0
    elif x > (len(data[0]) - 1):
        return len(data[0]) - 1
    else:
        return x

def clampY(x, data):
    if x < 0:
        return 0
    elif x > (len(data) - 1):
        return len(data) - 1
    else:
        return x

if __name__ == "__main__":
    main(data)
