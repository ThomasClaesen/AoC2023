import re

import aoc

data = aoc.get_input(5).splitlines()


def main(data):
    listOfDestinations = []
    listOfSeeds = data[0].split(" ")
    listOfSeeds.pop(0)
    listOfMapTitles = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:",
                       "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:",
                       "humidity-to-location map:"]
    listOfMapIndexes = []
    for mapTitle in listOfMapTitles:
        listOfMapIndexes.append(data.index(mapTitle))
    listOfMapIndexes.append(len(data)+1)
    listOfRanges = []
    for i in range(len(listOfMapIndexes)-1):
        minRange = listOfMapIndexes[i]+1
        maxRange = listOfMapIndexes[i+1]-1
        rangeToBeAdded = []
        for j in range(minRange, maxRange):
            rangeToBeAdded.append(data[j].split(" "))
        listOfRanges.append(rangeToBeAdded)
    for seed in listOfSeeds:
        print("newSeed")
        print(seed)
        for ranges in listOfRanges:
            for r in ranges:
                destinationStart = int(r[0])
                sourceStart = int(r[1])
                length = int(r[2])
                if (int(seed) >= sourceStart) & (int(seed) <= sourceStart + length - 1):
                    seed = str(destinationStart + (int(seed) - sourceStart))
                    break
            print(seed)
        listOfDestinations.append(int(seed))
    print("solution = " + str(min(listOfDestinations)))

testData = ["seeds: 79 14 55 13",
            "",
            "seed-to-soil map:",
            "50 98 2",
            "52 50 48",
            "",
            "soil-to-fertilizer map:",
            "0 15 37",
            "37 52 2",
            "39 0 15",
            "",
            "fertilizer-to-water map:",
            "49 53 8",
            "0 11 42",
            "42 0 7",
            "57 7 4",
            "",
            "water-to-light map:",
            "88 18 7",
            "18 25 70",
            "",
            "light-to-temperature map:",
            "45 77 23",
            "81 45 19",
            "68 64 13",
            "",
            "temperature-to-humidity map:",
            "0 69 1",
            "1 0 69",
            "",
            "humidity-to-location map:",
            "60 56 37",
            "56 93 4"]

if __name__ == "__main__":
    main(data)
