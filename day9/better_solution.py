# this is supposed to be a better, more elegant solution for day9 of aoc2023
# will try to use recurrent functions 


with open("input2.txt", "r") as file:
    data = file.read().split("\n")


def calculate(array):

    # first in recursive function we have to account for break/return statement
    if len(set(array)) == 1:
        return array[0]

    pairs = list(zip(array, array[1:]))
    deltas = [y-x for x,y in pairs]
    diff = calculate(deltas)

    return array[-1] + diff


array = [10, 13, 16, 21, 30, 45]

print(calculate(array))

    
