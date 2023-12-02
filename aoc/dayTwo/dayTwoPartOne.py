import re

import aoc

data = aoc.get_input(2).splitlines()

testData = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

highestRed = -1
highestBlue = -1
highestGreen = -1
total = 0
regexRed = "(\d+) red"
regexGreen = "(\d+) green"
regexBlue = "(\d+) blue"

for game in data:
    gameTurns = re.split('[;:]', game)
    gameId = int(gameTurns.pop(0).replace("Game ", ""))
    highestRed = 0
    highestGreen = 0
    highestBlue = 0
    for turn in gameTurns:
        try:
            highestRed = max(int(re.compile(regexRed).search(turn).group(1)), highestRed)
        except Exception:
            pass
        try:
            highestGreen = max(int(re.compile(regexGreen).search(turn).group(1)), highestGreen)
        except Exception:
            pass
        try:
            highestBlue = max(int(re.compile(regexBlue).search(turn).group(1)), highestBlue)
        except Exception:
            pass

    if (highestRed <= 12) & (highestGreen <= 13) & (highestBlue <= 14):
        total = total + gameId

print(total)

