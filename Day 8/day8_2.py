fr = open("input.txt", "r")
lines = fr.readlines()

route = lines[0].strip()
d = dict()

for i in range(2, len(lines)):
    key, value = lines[i].split(" = ")
    value = (value[1:4], value[6:9])
    d[key] = value

res = 0
i = 0
temp = [i for i in d if i[2] == "A"]
lcmthis = [0 for i in d if i[2] == "A"]

while not all(lcmthis):
    for j in range(len(temp)):
        if temp[j][2] == "Z":
            if lcmthis[j] == 0:
                lcmthis[j] = res
    if route[i] == "R":
        temp = [d[i][1] for i in temp]
    elif route[i] == "L":
        temp = [d[i][0] for i in temp]
    res += 1
    i += 1
    if i == len(route):
        i = 0
        
        
print(lcmthis)
import math
print(math.lcm(*lcmthis))