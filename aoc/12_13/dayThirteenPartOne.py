import aoc

data = aoc.get_input(13)

testData = "#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.\n\n#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#"

memo = {}


def main(data):
    total = 0
    patterns = data.split("\n\n")
    for pattern in patterns:
        rows = pattern.splitlines()
        total += 100 * getRowMirror(rows)

        columns = list(zip(*rows))
        total += getRowMirror(columns)

    print("solution = " + str(total))


def getRowMirror(rows):
    for i in range(1, len(rows)):
        upperSide = rows[:i]
        lowerSide = rows[i:]
        upperSide = upperSide[::-1]

        upperSide = upperSide[:len(lowerSide)]
        lowerSide = lowerSide[:len(upperSide)]

        difference = 0
        for upper, lower in zip(upperSide, lowerSide):
            for upperLetter, lowerLetter in zip(upper, lower):
                if upperLetter != lowerLetter:
                    difference += 1
        if difference == 1:
            return i
    return 0


if __name__ == "__main__":
    main(data)
