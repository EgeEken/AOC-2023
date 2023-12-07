import time as te
start = te.time()
def FUNCTION(time, dist):
    res = 0
    for i in range(1, time):
        if i * (time - i) > dist:
            res += 1
    return res
            

fr = open("input.txt", "r")
lines = fr.readlines()
time = [i for i in lines[0][:-1].split(": ")[1].split(" ") if i.isnumeric()]
dist = [i for i in lines[1][:-1].split(": ")[1].split(" ") if i.isnumeric()]
tres = ""
for t in time:
    tres += t
dres = ""
for d in dist:
    dres += d

print(tres)
print(dres)

print(FUNCTION(int(tres), int(dres)))
print(te.time() - start)