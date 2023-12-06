import re

import aoc

data = aoc.get_input(4).splitlines()

testData = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]


def main(data):
    total = 0
    alteredData = list(data)
    lengthOfCardList = len(alteredData)
    indexCounter = 0
    regexCardnumber = "Card *(\d+)"
    while(indexCounter < lengthOfCardList):
        cardRow = alteredData[indexCounter]
        cardNumber = int(re.compile(regexCardnumber).search(cardRow).group(1))
        amountCorrect = processCard(indexCounter, alteredData)
        for i in range(1, amountCorrect+1):
            alteredData.append(data[cardNumber+i-1])
        indexCounter = indexCounter + 1
        lengthOfCardList = len(alteredData)
        print(len(alteredData))

    print(len(alteredData))


def processCard(cardIndex, data):
    cardRowSplit = list(filter(None, re.split('[|:]', data[cardIndex])))
    winningNumbers = list(filter(None, cardRowSplit[1].split(" ")))
    guessedNumbers = list(filter(None, cardRowSplit[2].split(" ")))
    amountCorrect = 0
    for winningNum in winningNumbers:
        if winningNum in guessedNumbers:
            amountCorrect = amountCorrect + 1
    return amountCorrect


if __name__ == "__main__":
    main(data)