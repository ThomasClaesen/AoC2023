import aoc

data = aoc.get_input(1).splitlines()

totalValue = 0
firstNumber = 0
secondNumber = 0
listOfNumbers = {"one": "o1e",
                 "two": "t2o",
                 "three": "t3e",
                 "four": "f4r",
                 "five": "f5e",
                 "six": "s6x",
                 "seven": "s7n",
                 "eight": "e8t",
                 "nine": "n9e"}

for string in data:
    print("oldString = " + string)
    for key, value in listOfNumbers.items():
        string = string.replace(key, value)

    for letter in string:
        if letter.isnumeric():
            firstNumber = int(letter)
            break

    for letter in string[::-1]:
        if letter.isnumeric():
            secondNumber = int(letter)
            break

    totalValue = totalValue + (firstNumber*10 + secondNumber)

print(totalValue)
