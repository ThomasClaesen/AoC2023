import re

import aoc

data = aoc.get_input(3).splitlines()

testData = ["467....100",
            "114*..*...",
            ".......633",
            "..*...#...",
            "617.......",
            "..*..+.58.",
            "..592.....",
            ".....*755.",
            "...$......",
            ".664...888"]


def main(data):
    total = 0
    indexY = -1
    for dataRow in data:
        indexY = indexY + 1
        editedDataRow = dataRow
        for char in dataRow:
            if char == '*':
                indexX = editedDataRow.find('*')
                editedDataRow = editedDataRow.replace('*', '.', 1)
                adjacentNumbers = findAdjacent(indexX, indexY, data)
                adjacentNumbers = list(dict.fromkeys(adjacentNumbers))
                print(adjacentNumbers)
                if len(adjacentNumbers) == 2:
                    total = total + (int(adjacentNumbers[0]) * int(adjacentNumbers[1]))

    print("answer = " + str(total))


def findAdjacent(x, y, data):
    result = []
    editedData = list(data)
    for j in range(y - 1, y + 2):
        indexY = clampY(j, data)
        editedDataRow = editedData[indexY]
        for i in range(x - 1, x + 2):
            indexX = clampX(i, data)
            symbol = editedDataRow[indexX]
            if symbol.isnumeric():
                number = findNumberAtPosition(indexX, indexY, editedDataRow)

                editedDataRow = editedDataRow.replace(number, '.' * len(number), 1)
                editedData[indexY] = editedDataRow
                result.append(number)
    return result


def findNumberAtPosition(x, y, row):
    if row[x - 1].isnumeric() & row[x + 1].isnumeric():
        return row[x - 1] + row[x] + row[x + 1]
    elif not row[x - 1].isnumeric():
        if row[x + 1].isnumeric() & row[x + 2].isnumeric():
            return row[x] + row[x + 1] + row[x + 2]
        elif row[x + 1].isnumeric() & (not row[x + 2].isnumeric()):
            return row[x] + row[x + 1]
        else:
            return row[x]
    elif not row[x + 1].isnumeric():
        if row[x - 1].isnumeric() & row[x - 2].isnumeric():
            return row[x - 2] + row[x - 1] + row[x]
        elif row[x - 1].isnumeric() & (not row[x - 2].isnumeric()):
            return row[x - 1] + row[x]
        else:
            return row[x]


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
