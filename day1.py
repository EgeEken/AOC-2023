def calibrate(s):
    res = ""
    for c in s:
        if c.isnumeric():
            res += c
    return int(res[0] + res[-1])

fr = open("input.txt", "r")
lines = fr.readlines()
for i in range(len(lines)):
    lines[i] = calibrate(lines[i])

with open("output.txt", "w") as o:
    for i in range(len(lines)):
        o.write(str(lines[i]) + "\n") 

print(sum(lines))