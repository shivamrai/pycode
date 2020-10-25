def isPerfectSquare(num) -> bool:
    left = 1
    right = num
    while(left<right):
        midpoint  = (left+right)//2;
        if(midpoint**2==num):
            return True
        elif(midpoint**2>num):
            right = midpoint - 1
        elif(midpoint**2<num):
            left = midpoint+1
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
    #s = Solution()
    print(isPerfectSquare(104976))