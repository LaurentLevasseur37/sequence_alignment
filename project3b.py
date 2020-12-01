import sys

def getClosestMatch(seq1, seqArr, nameArr):
    maxDistance = 0
    alignArr  = []
    descriptionArr = []
    for i in range(0, len(seqArr)):
        #return two matrices: the dynamic programming matrix and the backtracking matrix
        temp = getDistance(seq1, seqArr[i])
        if (temp[0][len(seq1)][len(seqArr[i])] > maxDistance):
            #new max distance and answer array
            maxDistance = temp[0][len(seq1)][len(seqArr[i])]
            descriptionArr = []
            descriptionArr.append(nameArr[i])
            alignArr = []
            alignArr.append(getAlignment(temp[1], seq1, seqArr[i]))
        elif (temp[0][len(seq1)][len(seqArr[i])] == maxDistance):
            descriptionArr.append(nameArr[i])
            alignArr.append(getAlignment(temp[1], seq1, seqArr[i]))
    file = open("out.fna", 'w')
    for i in range(0, len(alignArr)):
        file.write(">")
        file.write(descriptionArr[i])
        file.write("\n")
        file.write(alignArr[i])
        file.write("\n")

def getDistance(a, b):
    x = len(a)
    y = len(b)
    matrix = [[0 for i in range(y + 1)] for j in range(x + 1)] #x rows, y columns
    back_matrix = [["" for i in range(y + 1)] for j in range(x + 1)]
    for i in range (1,x + 1):
        for j in range (1, y + 1):
            if (a[i - 1] == b[j - 1]):
                diag = matrix[i - 1][j - 1] + 2
                left = matrix[i - 1][j] - 2
                up = matrix[i][j - 1] - 2
                matrix[i][j] = max(diag, left, up)
                if (matrix[i][j] == diag):
                    back_matrix[i][j] = "↖"
                elif (matrix[i][j] == left):
                    back_matrix[i][j] = "←"
                elif (matrix[i][j] == up):
                    back_matrix[i][j] = "↑"
            else:
                diag = matrix[i - 1][j - 1] - 1
                left = matrix[i - 1][j] - 2
                up = matrix[i][j - 1] - 2
                matrix[i][j] = max(diag, left, up)
                if (matrix[i][j] == diag):
                    back_matrix[i][j] = "↖"
                elif (matrix[i][j] == left):
                    back_matrix[i][j] = "←"
                elif (matrix[i][j] == up):
                    back_matrix[i][j] = "↑"
    arr = []
    arr.append(matrix)
    arr.append(back_matrix)
    return arr

def getAlignment(matrix, a, b):
    x = len(a)
    y = len(b)
    seq1 = ""
    seq2 = ""
    found = False
    while not (found):
        if (matrix[x][y] == "↖"):
            seq1 += a[x - 1]
            seq2 += b[y - 1]
            x -= 1
            y -= 1
        elif (matrix[x][y] == "←"):
            seq1 += a[x - 1]
            seq2 += "-"
            x -= 1
        elif (matrix[x][y] == "↑"):
            seq1 += "-"
            seq2 += b[y - 1]
            y -= 1
        else:
            found = True
    return seq1[::-1]


def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    test = open(file1)
    test.readline()
    found = False
    seq1 = ""
    while not found:
        temp = test.readline()
        if (temp == "" or temp[0] == ">"):
            found = True
        else:
            seq1 += temp
    nameArr = []
    seqArr = []
    temp = ""
    with open(file2) as file:
        for line in file.readlines():
            if (line[0] == ">"):
                seqArr.append(temp)
                temp = ""
                nameArr.append(line[1:len(line) - 1])
            else:
                temp += line
    seqArr.append(temp)
    seqArr = seqArr[1:len(seqArr)]
    getClosestMatch(seq1, seqArr, nameArr)

if __name__ == '__main__':
    main()
