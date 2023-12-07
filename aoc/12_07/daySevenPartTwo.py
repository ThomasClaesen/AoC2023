import aoc

data = aoc.get_input(7).splitlines()

testData = ["2T8JJ 0",
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483"]


def main(data):
    listOfFiveOfAKind = []
    listOfFourOfAKind = []
    listOfFullHouse = []
    listOfThreeOfAKind = []
    listOfTwoPair = []
    listOfPair = []
    listOfHighCard = []
    for cardBid in data:
        [cards, bid] = cardBid.split(" ")
        cardsUnpacked = [*cards]
        cardsNumerated = numerateCards(cardsUnpacked)
        if isFiveOfAKind(list(cardsNumerated)):
            listOfFiveOfAKind.append([cardsNumerated, bid, getHighCardValue(cardsNumerated), getHighCardHex(cardsNumerated)])
        elif isFourOfAKind(list(cardsNumerated)):
            listOfFourOfAKind.append([cardsNumerated, bid, getHighCardValue(cardsNumerated), getHighCardHex(cardsNumerated)])
        elif isFullHouse(list(cardsNumerated)):
            listOfFullHouse.append([cardsNumerated, bid, getHighCardValue(cardsNumerated), getHighCardHex(cardsNumerated)])
        elif isThreeOfAKind(list(cardsNumerated)):
            listOfThreeOfAKind.append([cardsNumerated, bid, getHighCardValue(cardsNumerated), getHighCardHex(cardsNumerated)])
        elif isTwoPairs(list(cardsNumerated)):
            listOfTwoPair.append([cardsNumerated, bid, getHighCardValue(cardsNumerated), getHighCardHex(cardsNumerated)])
        elif isPair(list(cardsNumerated)):
            listOfPair.append([cardsNumerated, bid, getHighCardValue(cardsNumerated), getHighCardHex(cardsNumerated)])
        else:
            listOfHighCard.append([cardsNumerated, bid, getHighCardValue(cardsNumerated), getHighCardHex(cardsNumerated)])
    print("")
    listOfFiveOfAKind.sort(key=lambda x: x[2])
    listOfFourOfAKind.sort(key=lambda x: x[2])
    listOfFullHouse.sort(key=lambda x: x[2])
    listOfThreeOfAKind.sort(key=lambda x: x[2])
    listOfTwoPair.sort(key=lambda x: x[2])
    listOfPair.sort(key=lambda x: x[2])
    listOfHighCard.sort(key=lambda x: x[2])
    fullList = listOfHighCard + listOfPair + listOfTwoPair + listOfThreeOfAKind + listOfFullHouse + listOfFourOfAKind + listOfFiveOfAKind
    result = 0
    for i in range(len(fullList)):
        bid = fullList[i][1]
        result = result + (int(bid) * (i + 1))
    print("result = " + str(result))


def getHighCardValue(cards):
    hexString = "0x" + hex(cards[0])[2] + hex(cards[1])[2] + hex(cards[2])[2] + hex(cards[3])[2] + hex(cards[4])[2]
    return int(hexString, 16)


def getHighCardHex(cards):
    hexString = "0x" + hex(cards[0])[2] + hex(cards[1])[2] + hex(cards[2])[2] + hex(cards[3])[2] + hex(cards[4])[2]
    return hexString


def isFiveOfAKind(cards):
    if cards.count(1) > 0:
        if cards.count(1) == 5:
            return True
        else:
            cards.sort()
            highestCard = cards[4]
            return cards.count(highestCard) + cards.count(1) == 5
    else:
        return cards[0] == cards[1] == cards[2] == cards[3] == cards[4]


def isFourOfAKind(cards):
    # JXYYY JYYYX JJXYY JJYYX JJJXY JJJYX
    if cards.count(1) > 0:
        cards.sort()
        middleCard = cards[3]
        return cards.count(middleCard) + cards.count(1) == 4
    else:
        cards.sort()
        middleCard = cards[2]
        return cards.count(middleCard) == 4


def isFullHouse(cards):
    # JXXYY JJXYY JJYYX
    if cards.count(1) > 0:
        if cards.count(1) == 1:
            cards.sort()
            return (cards[1] == cards[2]) & (cards[3] == cards[4])
        elif cards.count(1) == 2:
            cards.sort()
            middleCard = cards[3]
            return cards.count(middleCard) == 2
    else:
        cards.sort()
        middleCard = cards[2]
        if cards.count(middleCard) != 3:
            return False
        else:
            return (cards[0] == cards[1]) & (cards[3] == cards[4])


def isThreeOfAKind(cards):
    if cards.count(1) > 0:
        # JAABC JABBC JABCC
        if cards.count(1) == 1:
            cards.sort()
            return (cards[1] == cards[2]) | (cards[2] == cards[3]) | (cards[3] == cards[4])
        # JJABC
        elif cards.count(1) == 2:
            return True
    else:
        cards.sort()
        middleCard = cards[2]
        return cards.count(middleCard) == 3


def isTwoPairs(cards):
    if cards.count(1) > 0:
        return False
    else:
        # XXYZZ YXXZZ XXZZY
        cards.sort()
        firstPairCard = cards[1]
        secondPairCard = cards[3]
        return (cards.count(firstPairCard) == 2) & (cards.count(secondPairCard) == 2)


def isPair(cards):
    if cards.count(1) > 0:
        return True
    else:
        cards.sort()
        # XXABC AXXBC ABXXC ABCXX
        firstPairCard = cards[1]
        secondPairCard = cards[3]
        return (cards.count(firstPairCard) == 2) | (cards.count(secondPairCard) == 2)


def numerateCards(cards):
    returnCards = []
    for card in cards:
        if card == "A":
            card = 14
        elif card == "K":
            card = 13
        elif card == "Q":
            card = 12
        elif card == "J":
            card = 1
        elif card == "T":
            card = 10
        else:
            card = int(card)
        returnCards.append(card)
    return returnCards


if __name__ == "__main__":
    main(data)
