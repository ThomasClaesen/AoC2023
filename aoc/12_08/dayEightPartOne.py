import re

import aoc

data = aoc.get_input(8).splitlines()

testData1 = ["RL",
             "",
             "AAA = (BBB, CCC)",
             "BBB = (DDD, EEE)",
             "CCC = (ZZZ, GGG)",
             "DDD = (DDD, DDD)",
             "EEE = (EEE, EEE)",
             "GGG = (GGG, GGG)",
             "ZZZ = (ZZZ, ZZZ)"]

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
    for route in mapDestinations:
        key = re.compile(regexRed).search(route).group(1)
        dest1 = re.compile(regexRed).search(route).group(2)
        dest2 = re.compile(regexRed).search(route).group(3)
        value = [dest1, dest2]
        routeTable.update({key: value})
    totalSteps = 0
    currentLocation = "AAA"
    while currentLocation != "ZZZ":
        for direction in directions:
            totalSteps = totalSteps + 1
            if direction == "R":
                currentLocation = routeTable.get(currentLocation)[1]
                print(currentLocation)
            elif direction == "L":
                currentLocation = routeTable.get(currentLocation)[0]
                print(currentLocation)
            if currentLocation == "ZZZ":
                break

    print("totalSteps = " + str(totalSteps))



if __name__ == "__main__":
    main(data)
