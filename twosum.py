def twoSum(self, nums, target):
    sum=0
    for i in range(0,len(nums)):
        if(sum == target):
            break
        elif(sum > target):
           target=0
           continue 
        else:
            sum = sum+target
            continue
        i=i+1
    return sum

nums=[11, 15, 2, 7]
sum = twoSum(1,nums,9)
print(sum)