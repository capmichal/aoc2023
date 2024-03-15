import re

with open("input.txt", "r") as file:
    data = file.read().split("\n")

# how to properly find an index of starting position "S", re.search / re.finditer
for i, line in enumerate(data):
    starting_point = re.search("S", line)
    if starting_point:
        start_x = i
        start_y = starting_point.start()
        print(start_x, start_y)

start_position = (start_x, start_y)




# get a list of indexes accepted by a character on map
def get_open(x, y):
    character = data[x][y]
    if character == "|":
        return [(x+1, y), (x-1, y)]
    elif character == "-":
        return [(x, y+1), (x, y-1)]
    elif character == "L":
        return [(x-1, y), (x, y+1)]
    elif character == "J":
        return [(x-1, y), (x, y-1)]
    elif character == "7":
        return [(x, y-1), (x+1, y)]
    elif character == "F":
        return [(x+1, y), (x, y+1)]
    elif character == "S":
        return "back"
    elif character == ".":
        return []

def get_possible(x, y):
    possible_moves = []
    for move in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
        if (0 <=move[0] < len(data)) and (0 <= move[1] < len(data[0])):
            possible_moves.append(move)
    return possible_moves



current_position = (start_x, start_y)
num_steps = 0
previous_path = []
while True:

    possible_moves = get_possible(current_position[0], current_position[1])
    print(f"possible moves {possible_moves}")
    if (start_position in possible_moves) and (start_position != previous_path[-1]):
        print("mamy to")
        break

    # check if possible move is a properly set pipe that allows us
    for possible_move in possible_moves:
        if possible_move not in previous_path:
            can_go = get_open(possible_move[0], possible_move[1])
            if current_position in can_go:
                print(f"ide do tej pozycji {possible_move}")
                num_steps += 1
                previous_path.append(current_position)
                #print(f"sciezka ostatnich {previous_path}")
                current_position = possible_move
                break
            else:
                print(f"aktualnie jestem {current_position}")
                print("nie wpuszcza mnie")
        else:
            print("bylem")


print((num_steps+1)//2)




