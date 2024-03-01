"""
Game 1: 8 green; 5 green, 6 blue, 1 red; 2 green, 1 blue, 4 red; 10 green, 1 red, 2 blue; 2 blue, 3 red
Game 2: 10 blue, 12 red; 8 red; 7 green, 5 red, 7 blue
Game 3: 1 red, 15 blue, 3 green; 8 blue, 2 red, 4 green; 2 red, 5 green, 9 blue

is possible: 12 red cubes, 13 green cubes, and 14 blue cubes

"""


with open("input.txt", "r") as file:
    content = file.read().splitlines()


print(content[:3])

capacity = {"red": 12, "green": 13, "blue": 14}
possibleGames = []

for line in content:


    # initial data formatting
    gameIndex = int(line.split()[1][:-1])
    dwukropek = line.find(":")
    data = line[dwukropek+1:].split(";")
    dataFormatted = [element.split(",") for element in data]
    


    # analyse one "pull" from bag
    possible = True
    for element in dataFormatted:
        for x in element:
            y = x.split()
            if capacity[y[1]] < int(y[0]):
                possible = False

    if possible is True:
        possibleGames.append(gameIndex)


print(sum(possibleGames))
