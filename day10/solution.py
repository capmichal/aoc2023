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
print(f"starting position {start_position}")
print(f"start: {data[start_x][start_y]}")

    



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
    elif character == ".":
        return []
    else:
        return [(x+1, y), (x, y+1), (x, y-1), (x-1, y)]

def get_possible(x, y):
    possible_moves = []
    for move in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
        if (0 <=move[0] < len(data)) and (0 <= move[1] < len(data[0])):
            possible_moves.append(move)
    return possible_moves

def classify_start(start_position):
    mozliwe = get_possible(start_position[0], start_position[1])
    my_pattern = []

    for move in mozliwe:
        #sprawdzam czy s jest tak mile widziane
        if start_position in get_open(move[0], move[1]):
            if move == (start_position[0]+1,start_position[1]):
                my_pattern.append("down")
            elif move == (start_position[0]-1,start_position[1]):
                my_pattern.append("up")
            elif move == (start_position[0],start_position[1]+1):
                my_pattern.append("right")
            elif move == (start_position[0],start_position[1]-1):
                my_pattern.append("left")

    if "up" in my_pattern and "down" in my_pattern:
        data[start_position[0]] = data[start_position[0]].replace("S", "|")
        print("zmieniam na |")
    elif "up" in my_pattern and "left" in my_pattern:
        data[start_position[0]] = data[start_position[0]].replace("S", "J")
        print("zmieniam na J")
    elif "up" in my_pattern and "right" in my_pattern:
        data[start_position[0]] = data[start_position[0]].replace("S", "L")
        print("zmieniam na L")
    elif "down" in my_pattern and "left" in my_pattern:
        data[start_position[0]] = data[start_position[0]].replace("S", "7")
        print("zmieniam na 7")
    elif "down" in my_pattern and "right" in my_pattern:
        data[start_position[0]] = data[start_position[0]].replace("S", "F")
        print("zmieniam na F")
    elif "right" in my_pattern and "left" in my_pattern:
        data[start_position[0]] = data[start_position[0]].replace("S", "-")
        print("zmieniam na -")



litera_start = classify_start(start_position)

current_position = (start_x, start_y)
num_steps = 0
previous_path = []
koniec = False
while True:

    possible_moves = get_possible(current_position[0], current_position[1])
    #print(f"possible moves {possible_moves}")
    # if (start_position in possible_moves) and (start_position != previous_path[-1]):
    #     print(f"final position: {current_position}")
    #     print("mamy to")
    #     break
    if koniec == True:
        break

    # check if possible move is a properly set pipe that allows us
    for possible_move in possible_moves:
        can_go = get_open(possible_move[0], possible_move[1])
        my_connections = get_open(current_position[0], current_position[1])

        # good catch of edge case ()
        if (possible_move == start_position) and (start_position != previous_path[-1]) and (current_position in can_go) and (possible_move in my_connections):
            print(f"tam moge issc {my_connections}")
            print("mamy to")
            print(f"ending position {current_position}")
            koniec = True
            break
        if possible_move not in previous_path:
            #print(f"can go : {can_go}")
            #print(f"my connections : {my_connections}")
            if (current_position in can_go) and (possible_move in my_connections):
                #print(f"ide do tej pozycji {possible_move}")
                num_steps += 1
                previous_path.append(current_position)
                #print(f"sciezka ostatnich {previous_path}")
                current_position = possible_move
                break
            else:
                #print(f"aktualnie jestem {current_position}")
                #print("nie wpuszcza mnie")
                pass

print((num_steps+1)//2)




