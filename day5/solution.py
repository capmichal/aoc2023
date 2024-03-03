import re

with open("input2.txt", "r") as file:
    data = file.read().split("\n")


seeds = data[0].split()[1:]

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


preprocessed_data = preprocess_data(data)


def mapper(map_part):
    destination = []
    source = []

    for line in map_part:
        # print(f"zajmuje sie ta linia {line}") PO CO GENERUJESZ TO WSZYSTKO !!!!!!?!?!?!?!?!?!?
        dest_range = [i for i in range(line[0], line[0]+line[2])]
        source_range = [i for i in range(line[1], line[1]+line[2])]

        destination.append(dest_range)
        source.append(source_range)

    
    return destination, source


     

# for map in preprocessed_data:
#     print(map)
#     print("\n")


destination, source = mapper(preprocessed_data[0])
print(destination)
print(source)
