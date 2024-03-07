import re


with open("input.txt", "r") as file:
    time, distance = file.read().split("\n")

time = int("".join(time.split()[1:]))
distance = int("".join(distance.split()[1:]))


print(time)
print(distance)

beaten = 0
for j in range(1,time+1):
    reach_distance = (time-j)*j
    if reach_distance > distance:
        beaten += 1


print(beaten)

 

