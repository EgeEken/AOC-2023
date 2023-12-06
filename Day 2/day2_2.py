

def minimum_power(s):
    maxcolors = {"red": -1, "green": -1, "blue": -1}
    for sect in ("".join(s.split(": ")[1])).split("; "):
        colors = dict()
        for c in sect.split(", "):
            colors[c.split(" ")[1] if "\n" not in c.split(" ")[1] else c.split(" ")[1][:-1]] = int(c.split(" ")[0])
        for c in colors:
            if colors[c] > maxcolors[c]:
                maxcolors[c] = colors[c]
    res = 1
    for c in maxcolors:
        res = res * maxcolors[c]
    return res

fr = open("input.txt", "r")
lines = fr.readlines()
for i in range(len(lines)):
    lines[i] = minimum_power(lines[i])
    print(lines[i])


with open("output.txt", "w") as o:
    total = 0
    for i in range(len(lines)):
        o.write(str(lines[i]) + "\n")
        total += lines[i]

print(total)