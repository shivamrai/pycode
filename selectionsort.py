"""Selection Sort - Sort using selection sort algorithm."""


# ""
# Algorithm
# 1. Find the minimum value in the list
# 2. Swap it with the value	in the current position
# 3. Repeat	this process for all the elements until	the	entire array is sorted
# This algorithm is	called selection sort since it repeatedly selects the smallest element.
# ""
def selectionsort(unsortedlist):
    """selectionsort function."""
    # min_val =a[0]
    for i in range(len(unsortedlist)):
        min_val = i
        for j in range(len(unsortedlist)):
            if unsortedlist[min_val] < unsortedlist[j]:
                swap = unsortedlist[min_val]
                unsortedlist[min_val] = unsortedlist[j]
                unsortedlist[j] = swap

    return unsortedlist


a = [5, 2, 3, 1]
b = selectionsort(a)
print("Sorted list", b)
