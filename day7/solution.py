import re

with open("input2.txt", "r") as file:
    data = file.read().split("\n")


hand = []
bid = []

# should i do it like that 
for element in data:
    element = element.split()
    hand.append(element[0])
    bid.append(int(element[1]))

print(hand)
print(bid)



# how to create a hierarchy by which by can sort
# create a list [five_of_kind, four_of_kind, full_house, etc.]
# and sort using this list

