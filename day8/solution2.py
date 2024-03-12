
with open("input3.txt", "r") as file:
    data = file.read().split("\n")
    

path, *steps = data
og_path_length = len(path)
steps = steps[1:]
steps = [step.split(" = ") for step in steps]

# again using two lists, instead of ditionarties
point, lr = zip(*steps)
lr = [tuple(element[1:-1].split(", ")) for element in lr]


current_position = "AAA"
final_position = "ZZZ"


ends_with_A = [p for p in point if p[-1]=="A"]

result = 0
current_step_number = 0
path_length = len(path)

while True:


        count = 0
        for element in ends_with_A:
             if element[-1]=="Z":
                  count+=1

        if count==len(ends_with_A):
             break
        

        if current_step_number == path_length:
            result += current_step_number
            current_step_number = 0



        for pos in ends_with_A:

            position_index = point.index(pos)
            left, right = lr[position_index]

            if path[current_step_number]=="R":
                ends_with_A[ends_with_A.index(pos)] = right
            else:
                ends_with_A[ends_with_A.index(pos)] = left
            
        current_step_number += 1
    


result += current_step_number
print(ends_with_A)
print(result)

