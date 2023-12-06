import numpy as np

SYMBOLS = {'#', '$', '%', '&', '*', '+', '-', '/', '=', '@'}

def partsum(matrix):
    with open("output.txt", "w") as fw:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                number = ""
                counting = False
                if matrix[i][j].isdigit():
                    k = j
                    while k < len(matrix[i]):
                        if not counting and matrix[i][k].isdigit():
                            if ((i > 0 and matrix[i-1][k] in SYMBOLS) or
                                (i < len(matrix) - 1 and matrix[i+1][k] in SYMBOLS) or 
                                (k > 0 and matrix[i][k-1] in SYMBOLS) or
                                (k < len(matrix[i]) - 1 and matrix[i][k+1] in SYMBOLS) or
                                (i > 0 and k > 0 and matrix[i-1][k-1] in SYMBOLS) or
                                (i > 0 and k < len(matrix[i]) - 1 and matrix[i-1][k+1] in SYMBOLS) or
                                (i < len(matrix) - 1 and k > 0 and matrix[i+1][k-1] in SYMBOLS) or
                                (i < len(matrix) - 1 and k < len(matrix[i]) - 1 and matrix[i+1][k+1] in SYMBOLS)):
                                counting = True
                                fw.write("FOUND SYMBOL AROUND: " + str(matrix[i][k]) + "\n")
                        if matrix[i][k].isdigit():
                            number += matrix[i][k]
                            matrix[i][k] = '.'
                        else:
                            k += 1
                            break
                        k += 1
                    if number != "" and counting:
                        fw.write("COUNTED: " + str(number) + "\n")
                        res += int(number)
                        fw.write("--new sum: " + str(res) + "\n")
        return res 
                
fr = open("input.txt", "r")
lines = fr.readlines()
matrix = []
for i in range(len(lines)):
    matrix.append(np.array(list(lines[i])))
matrix = np.array(matrix)

print(partsum(matrix))