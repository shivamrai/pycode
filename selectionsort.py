# ""
# Algorithm
# 1. Find the minimum value in the list 
# 2. Swap it with the value	in the current position 
# 3. Repeat	this process for all the elements until	the	entire array is sorted
# This algorithm is	called selection sort since it repeatedly selects the smallest element.
# ""
def selectionsort(unsortedlist):
    #min=a[0]
    for i in range(len(unsortedlist)):
        min = i
        for j in range(len(unsortedlist)):
            if a[min] < a[j]:
                swap = a[min]
                a[min] = unsortedlist[j]
                unsortedlist[j] = swap
            else:
                pass
    return unsortedlist
            
a = [5,2,7,1,4]
b = selectionsort(a)
print("Sorted list",b)
