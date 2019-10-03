# Complete the hourglassSum function below.
def hourglassSum(arr):
    largestSum = -32767
    currentSum = -32767
    i = 0 
    j = 0 
    k = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
                largestSum = arr[j,k]+arr[j,k+1]+arr[j,k+2]+arr[j+1,k+1]+arr[j+2,k]+arr[j+2,k+1]+arr[j+2,k+2]
                
    if(largestSum<currentSum):
            largestSum = currentSum
    return largestSum

if __name__ == "__main__":
    # arr = [[0 for x in range(6)] for y in range(6)]
    # print(arr)
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    print(arr)
    largestsum = hourglassSum(arr)