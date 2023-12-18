import time

def parsetoint(s):
    return (int(_) for _ in s[:-1].split(" ") if _ != "")

fr = open("input.txt", "r")
lines = fr.readlines()
seeds = parsetoint(lines[0].split(": ")[1])

maplist = [{}, {}, {}, {}, {}, {}, {}]
j = -1
for i in range(1, len(lines)):
    if ":" in lines[i]:
        j += 1
    elif lines[i] != "\n":
        d, s, r = parsetoint(lines[i])
        maplist[j][(s,s+r)] = d-s
            
            
firststart = time.time()
minimum = float("inf")
for s in seeds:
    start = time.time()
    temp = s
    for m in maplist:
        for n in m:
            if temp >= n[0] and temp < n[1]:
                temp = m[n] + temp
                break
                
    print(temp)
    minimum = min(minimum, temp)
    print("seed", s, "complete in:", time.time() - start)

print("-----------------------------------")
print("FINAL MINIMUM:", minimum)
print("TOTAL TIME:", time.time() - firststart)
print("-----------------------------------")
