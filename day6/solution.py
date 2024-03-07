import re


with open("input.txt", "r") as file:
    time, distance = file.read().split("\n")

time = list(map(int,time.split()[1:]))
distance = list(map(int,distance.split()[1:]))


print(time)
print(distance)


beating = 1
for i in range(len(time)):

    t = time[i]
    d = distance[i]

    min_beating = 0
    for j in range(1,t+1): # check holding button for [1,entire_time]
        reach_distance = (t-j)*j
        if reach_distance > d:
            min_beating += 1
    
    beating = beating * min_beating


print(beating)

 

