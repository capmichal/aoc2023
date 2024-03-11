
with open("input2.txt", "r") as file:
    data = file.read().split("\n")


path, *steps = data
og_path_length = len(path)
steps = steps[1:]
steps = [step.split(" = ") for step in steps]

# again using two lists, instead of ditionarties
point, lr = zip(*steps)



print("#####################")
print(point[:3])
print(lr[:3])


current_position = "AAA"
final_position = "ZZZ"

current_step_number = 0
path_length = len(path)

while current_position != final_position:

        if current_step_number == path_length:
            path_length = path_length + og_path_length
            path += path


        position_index = point.index(current_position)
        left, right = lr[position_index]