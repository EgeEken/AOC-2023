import time

def range_remove(r1, r2):
    if r2[1] == r1[1]:
        if r2[0] > r1[0]:
            return {(r1[0], r2[0])}, (r2[0], r1[1])
        else:
            return set(), r1
        
    elif r2[1] > r1[1]:
        if r2[0] >= r1[1]:
            return {r1}, ()
        elif r2[0] < r1[1] and r2[0] > r1[0]:
            return {(r1[0], r2[0])}, (r2[0], r1[1])
        else:
            return set(), r1
    
    elif r2[1] < r1[1] and r1[0] < r2[1]:
        if r2[0] > r1[0]:
            return {(r1[0], r2[0]), (r2[1], r1[1])}, (r2[0], r1[1])
        else:
            return {(r2[1], r1[1])}, (r1[0], r2[1])
    
    else:
        return {r1}, ()

def recursive_min(r, mapindex, ml):
    if mapindex == len(ml):
        return r[0]
    cutset = set()
    remset = set()
    for n in ml[mapindex]:
        _, cut = range_remove(r, n)
        if cut != ():
            cutset.add(cut)
            remset.add((cut[0] + ml[mapindex][n], cut[1] + ml[mapindex][n]))
    remaining = {r}
    while len(cutset) > 0:
        c2 = cutset.pop()
        for r2 in remaining:
            rem, cut = range_remove(r2, c2)
            if cut != ():
                remaining = rem
    remset |= remaining
    return min(recursive_min(ri, mapindex + 1, ml) for ri in remset)


fr = open("input.txt", "r")
lines = fr.readlines()
seeds = [int(_) for _ in lines[0].split(": ")[1][:-1].split(" ") if _ != ""]

maplist = [{}, {}, {}, {}, {}, {}, {}]
j = -1
for i in range(1, len(lines)):
    if ":" in lines[i]:
        j += 1
    elif lines[i] != "\n":
        d, s, r = (int(_) for _ in lines[i][:-1].split(" ") if _ != "")
        maplist[j][(s,s+r)] = d-s


firststart = time.time()
minimum = float("inf")

seedranges = []
si = 0
while si < len(seeds):
    seedranges.append((seeds[si], seeds[si] + seeds[si+1]))
    si += 2
    

for i in seedranges:
    start = time.time()
    rec_min = recursive_min(i, 0, maplist)
    if rec_min != 0:
        minimum = min(minimum, rec_min)


print("-----------------------------------")
print("RESULT:", minimum)
print("TOTAL TIME:", time.time() - firststart)
print("-----------------------------------")      