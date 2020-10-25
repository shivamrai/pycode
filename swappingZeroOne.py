def minMoves(arr):
    countOnes =0
    displacement = 0
    for element in arr:
        if(element == 1):countOnes+=1 
        if(element ==0):displacement+=countOnes
    countZeros = len(arr) - countOnes
    revDisplacement = countOnes*countZeros - displacement
    return min(displacement,revDisplacement)

if __name__ == "__main__":
    print(minMoves([1,1,1,1,0,1,0,1]))