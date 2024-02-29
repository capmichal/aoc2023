
with open("input.txt", "r") as file:
    inp = file.readlines()

length = len(inp[0])
rows = (len(inp))
#print(rows)


matrix = [
    "..3..",
    ".*...",
]

# function to see if any symbols are adjacent to given index
def any_adjacent(matrix, x, y):
    
    has_adjacent = False

    # defined adjacent positons
    matrix_h = len(matrix)
    matrix_w = len(matrix[0])-1
    left = matrix[x][y-1] if y>0 else None
    up_left = matrix[x-1][y-1] if x>0 and y>0 else None
    up = matrix[x-1][y] if x>0 else None
    up_right = matrix[x-1][y+1] if x>0 and y<matrix_w-1 else None
    right = matrix[x][y+1] if y<matrix_w-1 else None
    down_right = matrix[x+1][y+1] if x<matrix_h-1 and y<matrix_w-1 else None
    down = matrix[x+1][y] if x<matrix_h-1 else None
    down_left = matrix[x+1][y-1] if x<matrix_h-1 and y>0 else None


    positions = [left, up_left, up, up_right, right, down_right, down, down_left]
    for position in positions:
        if str(position).isnumeric()==False and position != "." and position is not None:
            has_adjacent = True

    return has_adjacent    
    

#print(any_adjacent(matrix, 0, 2))

gatered_numbers =[]

for x in range(rows):
    current_number = ""
    found_adjacent = False
    for y in range(length):
        #print(f"[{x}][{y}]")
        if inp[x][y].isnumeric():
            current_number += inp[x][y]
            if any_adjacent(inp, x, y):
                found_adjacent = True
        else:
            if found_adjacent:
                print(f"from line {x+1} adding {current_number}")
                gatered_numbers.append(int(current_number))
            #if len(current_number)>0:
                #print(current_number)
            current_number = ""
            found_adjacent = False

#print(gatered_numbers)
print(sum(gatered_numbers))