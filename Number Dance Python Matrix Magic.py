import random

def setOneDim(r):
    print(f"Enter {r} integers:", end=" ")
    oneDim = list(map(int, input().split()))
    return oneDim

def printOneDim(oneDim):
    print(" ".join(map(str, oneDim)))

def setZerosTwoDim(r, c):
    return [[0] * c for _ in range(r)]

def doubleColumns(oneDim, twoDim):
    for i in range(len(twoDim)):
        twoDim[i][0] = oneDim[i]
        for j in range(1, len(twoDim[i])):
            twoDim[i][j] = 2 * twoDim[i][j - 1]

def printTwoDim(twoDim):
    for row in twoDim:
        print("\t".join(map(str, row)))

def main():

    #Step 1
    r = random.randint(4, 7)
    oneDim = setOneDim(r)

    #Step 2
    print("oneDim list")
    printOneDim(oneDim)

    #Step 3
    c = random.randint(4, 7)
    twoDim = setZerosTwoDim(r, c)

    #Step 4
    print("zero twoDim list")
    printTwoDim(twoDim)

    #Step 5
    doubleColumns(oneDim, twoDim)
    print("\ndouble columns list")
    printTwoDim(twoDim)

main()

