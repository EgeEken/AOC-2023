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
temp = "AAA"
while temp != "ZZZ":
    if route[i] == "R":
        temp = d[temp][1]
    elif route[i] == "L":
        temp = d[temp][0]
    res += 1
    i += 1
    if i == len(route):
        i = 0
    
print(res)