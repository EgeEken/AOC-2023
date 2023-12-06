import numpy as np

def check_around(matrix, i, j):
    """return the list of surroundings in this format:
    for example, if there is a number on the top left, and no numbers around otherwise
               1 0 0
               0 * 0
               0 0 0    
               
    if the index goes out of bounds for one of the 8 directions, keep 0 for that direction,
    for example, for matrix, 0, 0, if all surroundings are numbers, return this:
                0 0 0
                0 * 1
                0 1 1 (because the top and left directions are all out of bounds)
    to clarify, this example would be something like this in the actual matrix:
            matrix[0][0] = *   matrix[0][1] = 1   matrix[1][0] = 2
    """
    res = [0, 0, 0,
           0,    0,
           0, 0, 0]
    
    if i > 0 and j > 0 and matrix[i-1][j-1].isdigit():
        res[0] = 1
    if i > 0 and matrix[i-1][j].isdigit():
        res[1] = 1
    if i > 0 and j < len(matrix[i]) - 1 and matrix[i-1][j+1].isdigit():
        res[2] = 1
    if j > 0 and matrix[i][j-1].isdigit():
        res[3] = 1
    if j < len(matrix[i]) - 1 and matrix[i][j+1].isdigit():
        res[4] = 1
    if i < len(matrix) - 1 and j > 0 and matrix[i+1][j-1].isdigit():
        res[5] = 1
    if i < len(matrix) - 1 and matrix[i+1][j].isdigit():
        res[6] = 1
    if i < len(matrix) - 1 and j < len(matrix[i]) - 1 and matrix[i+1][j+1].isdigit():
        res[7] = 1
    return res

def top_mid_bot(checklist):
    """
    return 3 elements, representing a case based on the number of numbers in top, middle and bottom
    """
    if sum(checklist[:3]) == 0:
        top = -1
    elif sum(checklist[:3]) == 1:
        top = 0
    elif checklist[:3] == [1, 0, 1]:
        top = 1
    else:
        top = 2
        
    if checklist[3:5] == [0, 0]:
        mid = -1
    elif checklist[3:5] == [1, 1]:
        mid = 1
    else:
        mid = 0
    
    if sum(checklist[5:]) == 0:
        bot = -1
    elif sum(checklist[5:]) == 1:
        bot = 0
    elif checklist[5:] == [1, 0, 1]:
        bot = 1
    else:
        bot = 2
    
    return (top, mid, bot)
        
def find_number(matrix, i, j):
    if not matrix[i][j].isdigit():
        return ""
    res = str(matrix[i][j])
    k = j + 1
    while k <= len(matrix[i]):
        if matrix[i][k].isdigit():
            res += matrix[i][k]
        else:
            break
        k += 1
    k = j - 1
    while k >= 0:
        if matrix[i][k].isdigit():
            res = matrix[i][k] + res
        else:
            break
        k -= 1
    return res


def partsum(matrix):
    """ this time gotta check for numbers around each *, if there is only 2 numbers, multiply them and add the multiplication to the sum (res)"""
    with open("output.txt", "w") as fw:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "*":
                    #fw.write("FOUND " + str(matrix[i][j]) + " AT: " + str(i) + ", " + str(j) + "\n")
                    check = check_around(matrix, i, j)
                    #fw.write("CHECKLIST: " + str(check) + "\n")
                    if sum(check) > 1 and sum(check) < 7:
                        tmb = top_mid_bot(check)
                        #fw.write("TOP MID BOT: " + str(tmb) + "\n")
                        #fw.write(str(sum(tmb)) + " " + str(tmb.count(1)) + "\n")
                        if (sum(tmb) == -1 or sum(tmb) == 1 or sum(tmb) == 3) and tmb.count(1) < 2:
                            DEBUGCHECK = res
                            fw.write("\nFOUND 2 NUMBERS AROUND: " + str(i) + ", " + str(j) + "\n")
                            #fw.write("CHECKLIST: " + str(check) + "\n")
                            #fw.write("TOP MID BOT: " + str(tmb) + "\n")
                            if tmb[0] == 1: # top = 1 0 1
                                res += int(find_number(matrix, i-1, j-1)) * int(find_number(matrix, i-1, j+1))
                                fw.write("MULTIPLIED: " + find_number(matrix, i-1, j-1) + " and " + find_number(matrix, i-1, j+1) + "\n")
                            elif tmb[1] == 1: # mid = 1 * 1
                                res += int(find_number(matrix, i, j-1)) * int(find_number(matrix, i, j+1))
                                fw.write("MULTIPLIED: " + find_number(matrix, i, j-1) + " and " + find_number(matrix, i, j+1) + "\n")
                            elif tmb[2] == 1: # bot = 1 0 1
                                res += int(find_number(matrix, i+1, j-1)) * int(find_number(matrix, i+1, j+1))
                                fw.write("MULTIPLIED: " + find_number(matrix, i+1, j-1) + " and " + find_number(matrix, i+1, j+1) + "\n")
                            else:
                                temp = 1
                                fw.write("MULTIPLIED: ")
                                for k in range(3):
                                    try:
                                        if tmb[k] == 0:
                                            temp *= int(find_number(matrix, i + k - 1, j) + find_number(matrix, i + k - 1, j-1) + find_number(matrix, i + k - 1, j+1))
                                            fw.write(find_number(matrix, i + k - 1, j) + find_number(matrix, i + k - 1, j-1) + find_number(matrix, i + k - 1, j+1) + " and ")
                                        if tmb[k] == 2:
                                            temp *= int(find_number(matrix, i + k - 1, j))
                                            fw.write(find_number(matrix, i + k - 1, j) + " and ")
                                    except ValueError:
                                        pass
                                fw.write("\n")
                                res += temp
                            fw.write("added to sum: " + str(res - DEBUGCHECK) + "\n")
                            fw.write("--new sum: " + str(res) + "\n")
        return res 
                
fr = open("input.txt", "r")
lines = fr.readlines()
matrix = []
for i in range(len(lines)):
    matrix.append(np.array(list(lines[i])))
matrix = np.array(matrix)

print(partsum(matrix))