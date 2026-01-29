"""Insertion sort Algorithm
Every repetition of insertion sort removes an element from the input data,
and inserts it into the correct position in the already-sorted list until no input elements remain.
Sorting is typically done in-place.
The resulting array after k iterations has the property where the first k + 1 entries aresorted.
Each element greater than x is copied to the right as it is compared against x.
Basically there are 2 portions of a list, sorted one and unsorted one. This algo transfers elements from
unsorted portion to sorted portion."""


def insertion_sort(unsortedlist):
    """insertion_sort function."""
    # sortedlist=[]
    # i=1
    # running index from position 1(2nd element of list, assuming 1st element
    # is in sorted part)
    for index in range(1, len(unsortedlist)):
        # choosing a number and assigning its index in list to a position
        currentvalue = unsortedlist[index]
        position = index
        # while the left number is greater than the selected number, shift
        # those in left side(ahead of list)
        while unsortedlist[position - 1] > currentvalue and position > 0:
            unsortedlist[position] = unsortedlist[position - 1]
            position -= 1
        # out of while, setting up value in the desired position after
        # iterating is complete.
        unsortedlist[position] = currentvalue
    return unsortedlist


unsortedlist = [6, 7, 2, 3, 1]
print("The Unsorted list is:", unsortedlist)
print("The Sorted list is:", insertion_sort(unsortedlist))
