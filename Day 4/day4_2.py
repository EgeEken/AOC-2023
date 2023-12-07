def winning(s):
    res = []
    winners, total = s.split("|")
    winners = [a for a in winners.split(": ")[1].split(" ") if a.isnumeric()]
    total = [a for a in total[:-1].split(" ") if a.isnumeric()]
    for n in total:
        if n in winners:
            res.append(n)
    return res

fr = open("input.txt", "r")
lines = fr.readlines()
res = [[] for _ in range(len(lines))]
copycount = [1 for _ in range(len(lines))]
for i in range(len(lines)):
    res[i] = winning(lines[i])
    for k in range(1, len(res[i]) + 1):
        copycount[i + k] += copycount[i]

with open("output.txt", "w") as o:
    for i in range(len(lines)):
        o.write(str(copycount[i]) + "\n")
        
print(sum(copycount))