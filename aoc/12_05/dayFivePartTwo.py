import re

import aoc

data = aoc.get_input(5).splitlines()


def main(data):
    listOfDestinations = []
    listOfSeeds = data[0].split(" ")
    listOfSeeds.pop(0)
    listOfSeedRanges = []
    for i in range(0, len(listOfSeeds), 2):
        listOfSeedRanges.append([listOfSeeds[i], str(int(listOfSeeds[i]) + int(listOfSeeds[i+1]))])
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
    newListOfNextRanges = []
    for ranges in listOfRanges:
        for r in ranges:
            destinationStart = int(r[0])
            filterStart = int(r[1])
            length = int(r[2])
            filterEnd = filterStart + length - 1
            seedRangesToBeFilteredAgain = []
            while listOfSeedRanges:
                (srcSt, srcEnd) = listOfSeedRanges.pop()
                before = [int(srcSt), min(int(srcEnd), filterStart)]
                inter = [max(int(srcSt), filterStart), min(filterEnd, int(srcEnd))]
                after = [max(int(srcSt), filterEnd), int(srcEnd)]
                if before[1]>before[0]:
                    seedRangesToBeFilteredAgain.append(before)
                if inter[1]>inter[0]:
                    newListOfNextRanges.append((inter[0]-filterStart+destinationStart,inter[1]-filterStart+destinationStart-1))
                if after[1]>after[0]:
                    seedRangesToBeFilteredAgain.append(after)
            listOfSeedRanges = seedRangesToBeFilteredAgain
        listOfSeedRanges = newListOfNextRanges + listOfSeedRanges
        print(listOfSeedRanges)
        newListOfNextRanges = []

    resultList = []
    while listOfSeedRanges:
        (first, second) = listOfSeedRanges.pop()
        resultList.append(int(first))
        resultList.append(int(second))
    print("solution =" + str(min(resultList)))


    # [srcSt                            srcEnd]
    #         [filterStart    filterEnd]
    # [Before][inter                   ][After]
    #   seed range goes through one filter
    #   filter creates before, inter and after
    #   inter gets put into next array
    #   before and after put back into seeds range

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
