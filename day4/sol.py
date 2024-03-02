import re

with open("input.txt", "r") as file:
    data = file.read().split("\n") # proper way of reading data in AOC to avoid "\n" being the last character in each line
    



def count_line(line):
    
    
    values = line[(line.index(":")+1):] # get rid of not important labelling
    values = values.split("|")

    winning = values[0].strip().split()
    ours = values[1].strip().split()

    result = 0

    for winner in winning:
        if winner in ours:
            result += 1

    return result


m = {}
for i, card in enumerate(data):
    
    if i not in m:
        m[i] = 1

    next = count_line(card)

    for k in range(i+1, i+next+1):
        m[k] = m.get(k, 1) + m[i]


print(sum(m.values()))