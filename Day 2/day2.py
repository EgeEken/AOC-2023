

def possible(s, givendict):
    for sect in ("".join(s.split(": ")[1])).split("; "):
        colors = dict()
        for c in sect.split(", "):
            colors[c.split(" ")[1] if "\n" not in c.split(" ")[1] else c.split(" ")[1][:-1]] = int(c.split(" ")[0])
        for c in colors:
            if c in givendict and colors[c] > givendict[c]:
                return False
    return True


inputdict = {"red": 12, "green": 13, "blue": 14}

fr = open("input.txt", "r")
lines = fr.readlines()
for i in range(len(lines)):
    lines[i] = possible(lines[i], inputdict)


with open("output.txt", "w") as o:
    total = 0
    for i in range(len(lines)):
        o.write(str(lines[i]) + "\n")
        total += lines[i] * (i + 1)
        o.write(str(total) + "\n")

print(total)