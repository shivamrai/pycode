def maxSubArray(nums):
    #subArray = []
    # maxTotal = -64
    # if(len(nums)<2):
    #     return sum(nums)
    # if(len(nums)==2):
    #     return max(sum(nums),nums[0],nums[1])
    # for i in range(0,len(nums)):
    #     total = 0
    #     subArray = []
    #     for j in range(i,len(nums)+1):
    #         if(i==j):
    #             subArray = [nums[i]]
    #         elif(j==len(nums)and i!=len(nums)-1):
    #             subArray.append(nums[-1])
    #         else:
    #             subArray = nums[i:j]
    #         total = sum(subArray)
    #         #print(subArray)
    #         if(total>maxTotal): maxTotal = total
    # return maxTotal
    dp = [0]*len(nums)
    for i in range(0,len(nums)):
        dp[i] = max(dp[i-1]+nums[i],nums[i]) 
    return max(dp)       
if __name__ == "__main__":
    print(maxSubArray([-2,1]))