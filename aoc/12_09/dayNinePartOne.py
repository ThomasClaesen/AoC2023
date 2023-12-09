import aoc

data = aoc.get_input(9).splitlines()

testData = ["0 3 6 9 12 15",
            "1 3 6 10 15 21",
            "10 13 16 21 30 45"]


def main(data):
    totalResult = 0

    for numberLine in data:
        numbers = numberLine.split(" ")
        numbers = [int(x) for x in numbers]
        nextNumber = getNextNumber(numbers)
        totalResult = totalResult + nextNumber

    print("solution = " + str(totalResult))


def getNextNumber(numbers):
    newListOfNumbers = []
    if numbers.count(0) == len(numbers):
        print("nextnumber = 0")
        return 0
    for i in range(1, len(numbers)):
        difference = numbers[i] - numbers[i - 1]
        newListOfNumbers.append(difference)
    nextNumber = numbers[len(numbers) - 1] + getNextNumber(newListOfNumbers)
    print("nextnumber = " + str(nextNumber))
    return nextNumber


if __name__ == "__main__":
    main(data)
