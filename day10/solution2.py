import re
from collections import deque
# deque is used for faster append(), pop() operations that on lists --> O(1)

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

# already seen points
seen = {(start_x, start_y)}
queue = deque([(start_x, start_y)])

"""
this approach using deque(which can be done using list easily but with worse time-complexity)
just adds ALL pipes, but with no particular order, len(seen) // 2 is the answer for part1, but we have
no clue about the order of pipes
"""

# TBC 22.03.2024