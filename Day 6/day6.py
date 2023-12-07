

def FUNCTION(timedist):
    res = 1
    for td in timedist:
        temp = 0
        for i in range(1, td[0]):
            if i * (td[0] - i) > td[1]:
                temp += 1
        print(temp)
        res *= temp
    return res
            

fr = open("input.txt", "r")
lines = fr.readlines()
time = [int(i) for i in lines[0][:-1].split(": ")[1].split(" ") if i.isnumeric()]
dist = [int(i) for i in lines[1][:-1].split(": ")[1].split(" ") if i.isnumeric()]
timedist = list(zip(time, dist))

print(time)
print(dist)
print(timedist)

print(FUNCTION(timedist))