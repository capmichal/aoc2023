import sys
import re # if it is allowed to use external libraries

decoded = []

with open("input.txt", "r") as file:
    content = file.read().splitlines() # instead of using readlines() which adds "\n" to each line

spelledNumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]



for line in content:
    integers = []
    for i in range(len(line)):
        if line[i].isnumeric():
            integers.append(line[i])
        for number in spelledNumbers:
            if line[i:].startswith(number):
                integers.append(str(spelledNumbers.index(number)+1))

    decoded.append(int(integers[0]+integers[-1]))


print(decoded[:10])
print(sum(decoded))

# anonymous user #3867819