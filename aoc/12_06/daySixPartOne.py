import math
import re
from math import sqrt

import aoc

data = aoc.get_input(6).splitlines()

testData = ["Time:      7  15   30",
            "Distance:  9  40  200"]


def main(data):
    maxTime = list(filter(None, data[0].split(" ")))
    recordDist = list(filter(None, data[1].split(" ")))
    maxTime = maxTime[1:]
    recordDist = recordDist[1:]

    for x, y in zip(maxTime, recordDist):
        x = int(x)
        y = int(y)
        breakpoint1 = (-x + sqrt(pow(x, 2) - 4 * 1 * y)) / (-2)
        breakpoint2 = (-x - sqrt(pow(x, 2) - 4 * 1 * y)) / (-2)
        print("breakpoint1 = " + str(breakpoint1))
        print("breakpoint2 = " + str(breakpoint2))
        amountOfVictories = math.floor(breakpoint2) - math.floor(breakpoint1)
        print("amount of victories = " + str(amountOfVictories))


if __name__ == "__main__":
    main(data)
