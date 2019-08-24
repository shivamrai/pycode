def minmaxsum(arr):
    total = 0
    for i in range(len(arr)):
        min = i
        for j in range(len(arr)):
            if a[min] < a[j]:
                swap = a[min]
                a[min] = arr[j]
                arr[j] = swap
            else:
                pass
    maxmin = [0,0]  
    maxmin[0] = sum(arr[slice(4)])
    maxmin[1] = sum(arr[:-4])
    return maxmin

a = [5,2,7,1,4]
b = minmaxsum(a)
print("sums list",b)