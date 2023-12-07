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
        #print("----")
    elif lines[i] != "\n":
        d, s, r = parsetoint(lines[i])
        #print(d, s, r)
        maplist[j][(s,s+r)] = d-s
        #print("maplist", j, ":", maplist[j])
            
            
firststart = time.time()
minimum = float("inf")
for s in seeds:
    start = time.time()
    temp = s
    #print("--seed:", temp)
    for m in maplist:
        #print("map: ", m)
        for n in m:
            if temp >= n[0] and temp < n[1]:
                #print(n, m[n], "+", temp, "=", m[n] + temp)
                temp = m[n] + temp
                break
                
    print(temp)
    minimum = min(minimum, temp)
    print("seed", s, "complete in:", time.time() - start)

print("-----------------------------------")
print("FINAL MINIMUM:", minimum)
print("TOTAL TIME:", time.time() - firststart)
print("-----------------------------------")
        

#res = 0
#
#with open("output.txt", "w") as o:
#    for i in range(len(lines)):
#        o.write(str(lines[i]) + "\n")
#        
#print(res)