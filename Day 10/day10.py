
from tracemalloc import start
import numpy as np

UP = np.array((-1, 0))      # because matrix[i+(-1)][j+0] is the cell above matrix[i][j]
DOWN = -1 * UP      # UP is also -1 * DOWN
LEFT = np.array((0, -1))
RIGHT = -1 * LEFT   # LEFT is also -1 * RIGHT

TC = dict() # tile connections
TC["L"] = [DOWN, LEFT] # so if coming with dir DOWN (from UP), goes (LEFT * -1), RIGHT
                        #   elif coming with dir LEFT (from RIGHT), goes (DOWN * -1), UP
TC["7"] = [UP, RIGHT]
TC["J"] = [DOWN, RIGHT]
TC["F"] = [UP, LEFT]
TC["|"] = [UP, DOWN]
TC["-"] = [LEFT, RIGHT]

def printable(dir):
    if np.array_equal(dir, UP):
        return "UP"
    elif np.array_equal(dir, DOWN):
        return "DOWN"
    elif np.array_equal(dir, LEFT):
        return "LEFT"
    elif np.array_equal(dir, RIGHT):
        return "RIGHT"
    else:
        return "ERROR"

def np_in(a, alist):
    for i in alist:
        if np.array_equal(a, i):
            return True
    return False

def reverseTC(dir1, dir2):
    for k in TC:
        if (np_in(dir1, TC[k])) and (np_in(dir2, TC[k])):
            return k


def newdir(tile, dir):
    if tile in TC:
        if np.array_equal(dir, TC[tile][0]):
            return -1 * TC[tile][1]
        elif np.array_equal(dir, TC[tile][1]):
            return -1 * TC[tile][0]
    return np.array((0,0))
    

def replace_S(matrix, i, j):
    if matrix[i][j] != "S":
        print("ERROR, replace_S called on non-S tile")
        return
    res = []
    for dir in [UP, DOWN, LEFT, RIGHT]:
        if sum(newdir(matrix[i + dir[0]][j + dir[1]], dir)) != 0:
            res.append(dir)
    matrix[i][j] = reverseTC(res[0], res[1])
    

def find_replace_S(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "S":
                replace_S(matrix, i, j)
                return np.array((i, j))
    return "ERROR S NOT FOUND"

fr = open("input.txt", "r")
lines = fr.readlines()
matrix = []
for i in range(len(lines)):
    matrix.append(list(lines[i].split()[0]))


startpos = find_replace_S(matrix)
starti, startj = startpos[0], startpos[1]
#print(startpos)
# 25 77
#print(matrix[startpos[0]][startpos[1]])
    
res = 0

temp = startpos
n = newdir(matrix[temp[0]][temp[1]], DOWN)

while res == 0 or not (temp[0] == starti) or not (temp[1] == startj):
    temp += n
    n = newdir(matrix[temp[0]][temp[1]], n)
    res += 1
    #print(res, temp, matrix[temp[0]][temp[1]], printable(n))
    #print(temp[0], starti, temp[1], startj)

print(res//2)