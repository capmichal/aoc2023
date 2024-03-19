import re


# remember to SWITCH S to some symbol
# remember that on top of NEW_PLACE accepting me, i also have to BE ABLE to go to NEW_PLACE


with open("input2.txt", "r") as file:
    data = file.read().split("\n")

# look for starting point, not using re.search("S", data)
# + propagating break into the loop
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if data[i][j] == "S":
            start_x = i
            start_y = j
            break
    else:
        continue
    break


# got my starting point
print(start_x, start_y)


