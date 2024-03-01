import re # is used in most tasks in AOC

regex_sym = "[^\d\.]" # everything that is not digits and dots
regex_dig = "\d+" # all digits strings



with open("input.txt", "r") as file:
    data = file.readlines()

print(data[1])
print(re.findall(regex_dig, data[1]))
print(re.findall(regex_sym, data[1]))
print(list(re.finditer(regex_dig, data[1]))) #re.finditer
print(data[1][24:25])

