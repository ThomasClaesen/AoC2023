import aoc

data = aoc.get_input(12).splitlines()

testData = ["???.### 1,1,3",
            ".??..??...?##. 1,1,3",
            "?#?#?#?#?#?#?#? 1,3,1,6",
            "????.#...#... 4,1,1",
            "????.######..#####. 1,6,5",
            "?###???????? 3,2,1"]

memo = {}


def main(data):
    total = 0
    for line in data:
        springs, numbers = line.split(" ")
        numbers = tuple(map(int, numbers.split(",")))
        numbers *= 5
        springs = '?'.join([springs]*5)
        total += getAmountOfPossibleAnswers(springs, numbers)
    print("solution = " + str(total))


def getAmountOfPossibleAnswers(springs, numbers):
    if springs == "":
        return 1 if numbers == () else 0

    if numbers == ():
        return 0 if "#" in springs else 1

    if (springs, numbers) in memo:
        return memo[(springs, numbers)]

    result = 0

    if springs[0] in ".?":
        result += getAmountOfPossibleAnswers(springs[1:], numbers)

    if springs[0] in "#?":
        if numbers[0] <= len(springs) and "." not in springs[:numbers[0]] and (numbers[0] == len(springs) or springs[numbers[0]] != "#"):
            result += getAmountOfPossibleAnswers((springs[numbers[0]+1:]), numbers[1:])

    memo[(springs,numbers)] = result

    return result


if __name__ == "__main__":
    main(data)
