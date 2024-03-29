import re

with open("input.txt", "r") as file:
    data = file.read().split("\n")


seeds = list(map(int,data[0].split()[1:]))

def preprocess_data(data): # for sure we can preprocess data better
    
    preprocessed_data = []
    add = []
    for line in data[3:]:
        if line:
            if line[0].isnumeric():
                add.append(list(map(int,line.split())))
        else:
            preprocessed_data.append(add)
            add = []
    preprocessed_data.append(add)

    return preprocessed_data


def mapper(map_part, seed=seeds[0]):

    found = seed
    for line in map_part:

        if seed>=line[1] and seed<(line[1]+line[2]):
            found = line[0]+(seed-line[1])
            return found # do not look further after finding

    return found        


preprocessed_data = preprocess_data(data)

def process_seeds(seeds): # again the same mistake --> DO NOT STORE SO MANY NUMBERS IN MEMORY

    new_seeds = [(seeds[0],seeds[0]+seeds[1]), (seeds[2],seeds[2]+seeds[3])]
    return new_seeds


processed_seeds = process_seeds(seeds)
# processed_list = []
# for i,seed in enumerate(processed_seeds):
#     current = processed_seeds[i]
#     for block in preprocessed_data:
#         current = mapper(block, current)
#     processed_list.append(current)

current_min = 999999999999
for element in processed_seeds:
    for i in range(element[0],element[1]):
        current = i
        for block in preprocessed_data:
            current = mapper(block, current)
        if current < current_min:
            current_min = current


print(current_min)

