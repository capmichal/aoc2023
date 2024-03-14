
with open("input.txt", "r") as file:
    data = file.read().split("\n")

# print(data[0])
# print(data[:1])

result = []

for line in data:

    line = list(map(int,line.split()))
    stack = [line]
    

    while True:

        if len(set(stack[-1])) == 1:
            break

        holder_stack = []
        for i in range(1,len(stack[-1])):
            f, s = stack[-1][i-1], stack[-1][i]
            diff = s-f
            holder_stack.append(diff)
        stack.append(holder_stack)
    
    final = []
    for element in stack:
        final.append(element[0])

    result.append(final)

wynik = 0
# for block in result:
#     block = list(reversed(block))
#     new_block = [block[0]]
#     for i in range(1,len(block)):
#         new_block.append(block[i]+new_block[i-1])
#     print(new_block)


for block in result:
    block = list(reversed(block))
    product = 0

    for i in range(len(block)):
        product = block[i]-product

    wynik += product

print(wynik)