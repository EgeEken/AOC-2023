

def dictify(card):
    res = dict()
    for i in range(len(card)):
        if card[i] not in res:
            res[card[i]] = 0
        res[card[i]] += 1
    return res

def numerate(c):
    return 13 - ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"].index(c)

def sansj(d):
    res = dict()
    for i in d:
        if i != "J":
            res[i] = d[i]
    return res

def cardtype(dj):
    j = 0
    d = sansj(dj)
    if "J" in dj:
        j = dj["J"]
    if len(d) == 0:
        return 7
    if max(d.values()) + j == 1:
        return 1
    elif max(d.values()) + j == 2:
        if len(d) == 4:
            return 2
        else:
            return 3
    elif max(d.values()) + j == 3:
        if len(d) == 3:
            return 4
        else:
            return 5
    elif max(d.values()) + j == 4:
        return 6
    else:
        return 7

def compare(c1, c2):
    for i in range(len(c1)):
        if numerate(c1[i]) > numerate(c2[i]):
            return 1
        elif numerate(c1[i]) < numerate(c2[i]):
            return -1
    return 0

def realsort(cards):
    for i in range(len(cards)-1):
        if cards[i][0] == cards[i+1][0]:
            if compare(cards[i][2], cards[i+1][2]) == 1:
                cards[i], cards[i+1] = cards[i+1], cards[i]
        

fr = open("input.txt", "r")
lines = fr.readlines()
cards = []
for i in range(len(lines)):
    card, val = lines[i].split()
    cards.append((cardtype(dictify(card)), int(val), card, dictify(card)))
    
with open("output.txt", "w") as o:
    for i in range(len(lines)):
        o.write(str(lines[i]) + "\n")
        o.write(str(cards[i]) + "\n\n")


cards.sort(key=lambda x: x[0])

for i in range(len(cards)): 
    realsort(cards)
res = 0
for i in range(len(cards)):
    res += (i+1) * cards[i][1]

#for c in cards:
    #print(c)
print("---\n")
print(str(res) + "\n")