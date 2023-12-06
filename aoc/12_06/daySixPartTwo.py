import math
import re
from math import sqrt

import aoc

data = aoc.get_input(6).splitlines()



def main():

    x = 55826490
    y = 246144110121111
    breakpoint1 = (-x + sqrt(pow(x, 2) - 4 * 1 * y)) / (-2)
    breakpoint2 = (-x - sqrt(pow(x, 2) - 4 * 1 * y)) / (-2)
    print("breakpoint1 = " + str(breakpoint1))
    print("breakpoint2 = " + str(breakpoint2))
    amountOfVictories = math.floor(breakpoint2) - math.floor(breakpoint1)
    print("amount of victories = " + str(amountOfVictories))


if __name__ == "__main__":
    main()
