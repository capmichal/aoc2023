import math
with open("input.txt", "r") as file:
    data = file.read().split("\n")
    

path, *steps = data
og_path_length = len(path)
steps = steps[1:]
steps = [step.split(" = ") for step in steps]
#print(steps)
# again using two lists, instead of ditionarties
point, lr = zip(*steps)
lr = [tuple(element[1:-1].split(", ")) for element in lr]


current_position = "AAA"
final_position = "ZZZ"
final = []

path_length = len(path)

ends_with_A = [p for p in point if p[-1]=="A"]

for element in ends_with_A:
    current_position = element

    result = 0
    current_step_number = 0
    while current_position[-1] != "Z":

            if current_step_number == path_length:
                result += current_step_number
                current_step_number = 0


            position_index = point.index(current_position)
            left, right = lr[position_index]

            if path[current_step_number]=="R":
                current_position = right
            else:
                current_position = left
            
            current_step_number += 1
    


    result += current_step_number
    final.append(result)



print(math.lcm(*final))