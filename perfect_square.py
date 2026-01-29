"""Perfect Square - Check if number is perfect square."""


def is_perfect_square(num) -> bool:
    """is_perfect_square function."""
    left = 1
    right = num
    while left < right:
        midpoint = (left + right) // 2
        square = midpoint**2
        if square == num:
            return True
        if square > num:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return False
    # divisorDict = {}
    # i=2
    # while(i<num or num>1):
    #     if(num%i==0 and i not in divisorDict.keys()):
    #         divisorDict[i] = 1
    #         num = num/i
    #     elif(num%i==0 and i in divisorDict.keys()):
    #         divisorDict[i]+=1
    #         num = num/i
    #     elif(num%i!=0):
    #         i+=1
    # setFlag = False
    # print(divisorDict)
    # for k,v in divisorDict.items():
    #     if(v%2==0 and v!=1):
    #         setFlag = True
    #     elif(v==1):
    #         setFlag = False
    # return setFlag


if __name__ == "__main__":
    # s = Solution()
    print(is_perfect_square(104976))
