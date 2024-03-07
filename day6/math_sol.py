import math

with open("input.txt", "r") as file:
    time, distance = file.read().split("\n")

time = int("".join(time.split()[1:]))
distance = int("".join(distance.split()[1:]))

# (time - hold) * hold > distance
# hold being X

a = -1
b = time
c = -distance

pierw = b**2 - 4*a*c

root1 = (-b + math.sqrt(pierw)) / (2*a)
root2 = (-b - math.sqrt(pierw)) / (2*a)

# sort the roots
root1, root2 = sorted([root1, root2])

# need only numbers > 0
root1 = max(0, root1)
root2 = max(0, root2)

root1 = math.floor(root1)
root2 = math.floor(root2)


# bad habits counter implementation
# counter = 0
# for i in range(root1,root2):
#     counter += 1


# proper counter implementation
counter = len([i for i in range(root1, root2)])

print(counter)