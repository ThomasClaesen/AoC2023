import math

import numpy as np
import re

import aoc

data = aoc.get_input(8).splitlines()

testData1 = ["LR",
             "",
             "AAA = (BBB, XXX)",
             "BBB = (XXX, ZZZ)",
             "ZZZ = (BBB, XXX)",
             "BBA = (AAB, XXX)",
             "AAB = (BBC, BBC)",
             "BBC = (AAZ, AAZ)",
             "AAZ = (AAB, AAB)",
             "XXX = (XXX, XXX)"]

testData2 = ["LLR",
             "",
             "AAA = (BBB, BBB)",
             "BBB = (AAA, ZZZ)",
             "ZZZ = (ZZZ, ZZZ)"]

regexRed = "(\w{3}) = \((\w{3}), (\w{3})\)"


def main(data):
    directions = data[0]
    mapDestinations = data[2::]
    routeTable = {}
    listOfStarts = []
    for route in mapDestinations:
        key = re.compile(regexRed).search(route).group(1)
        dest1 = re.compile(regexRed).search(route).group(2)
        dest2 = re.compile(regexRed).search(route).group(3)
        value = [dest1, dest2]
        routeTable.update({key: value})
        if key[2] == "A":
            listOfStarts.append(key)
    totalStepsList = []
    for i in range(len(listOfStarts)):
        totalSteps = 0
        currentDestination = listOfStarts[i]
        while currentDestination[2] != "Z":
            for direction in directions:
                totalSteps = totalSteps + 1
                if direction == "R":
                    currentDestination = routeTable.get(currentDestination)[1]
                elif direction == "L":
                    currentDestination = routeTable.get(currentDestination)[0]
                if currentDestination[2] == "Z":
                    print(currentDestination)
                    break
        totalStepsList.append(totalSteps)

    print("totalSteps = " + str(totalStepsList))

    solution = 1
    for i in range(len(totalStepsList)):
        solution = math.lcm(totalStepsList[i], solution)

    print("solution = " + str(solution))


if __name__ == "__main__":
    main(data)
