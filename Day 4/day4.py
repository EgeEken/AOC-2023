def winning(s):
    res = []
    winners, total = s.split("|")
    winners = [a for a in winners.split(": ")[1].split(" ") if a.isnumeric()]
    total = [a for a in total[:-1].split(" ") if a.isnumeric()]
    for n in total:
        if n in winners:
            res.append(n)
    return res

res = 0
fr = open("input.txt", "r")
lines = fr.readlines()
for i in range(len(lines)):
    lines[i] = winning(lines[i])
    res += 2**(len(lines[i]) - 1) if len(lines[i]) > 0 else 0

with open("output.txt", "w") as o:
    for i in range(len(lines)):
        o.write(str(lines[i]) + "\n")
        
print(res)