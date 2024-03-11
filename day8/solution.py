
with open("input.txt", "r") as file:
    data = file.read().split("\n")
    

path, *steps = data
og_path_length = len(path)
steps = steps[1:]
steps = [step.split(" = ") for step in steps]

# again using two lists, instead of ditionarties
point, lr = zip(*steps)
lr = [tuple(element[1:-1].split(", ")) for element in lr]



# print("#####################")
# print(point[:3])
# print(lr[:3])

# siema, eniu = lr[2]
# print(f"przykladowe lr[2] == {lr[2]}")


current_position = "AAA"
final_position = "ZZZ"

result = 0
current_step_number = 0
path_length = len(path)

while current_position != final_position:

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
print(result)
