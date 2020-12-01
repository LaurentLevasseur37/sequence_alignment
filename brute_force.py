import sys

def getClosestMatch(seq1, seqArr, nameArr):
    maxDistance = 0
    alignArr  = []
    descriptionArr = []
    for i in range(0, len(seqArr)):
        temp = getAlign(seq1, seqArr[i])
        if (temp[1] < minDistance):
            minDistance = temp[1]
            alignArr = []
            alignArr.append(temp[0])
            descriptionArr = []
            descriptionArr.append(nameArr[i])
        elif (temp[1] == minDistance):
            alignArr.append(temp[0])
            descriptionArr.append(nameArr[i])
    file = open("out.fna", 'w')
    for i in range(0, len(alignArr)):
        file.write(">")
        file.write(nameArr[i])
        file.write("\n")
        file.write(alignArr[i])
        file.write("\n")

def align(seq1, seq2, ans, depth, arr):
    length = max(len(seq1), len(seq2))
    depth += 1
    if (depth == length):
        arr.append(ans)
    else:
        for i in range(0,2):
            if (i == 0):
                newAns = ans + seq1[depth]
            elif (i == 1):
                newAns = ans + seq2[depth]
            align(seq1, seq2, newAns, depth, arr)

def HammingDistance(a, b):
    count = 0
    for i in range(len(a)):
        if(a[i] != b[i]):
            count = count + 1
    return count

def getAlign(seq1, seq2):
    temp = []
    align(seq1, seq2, "", -1, temp)

    minDist = 100000
    minIndex = -1
    for i in range(1, len(temp) - 1):
        dist = HammingDistance(seq1, temp[i])
        if (dist < minDist):
            minDist = dist
            minIndex = i
    ans = []
    ans.append(minIndex)
    ans.append(minDist)
    return ans
    
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

if __name__ == "__main__":
    main()
