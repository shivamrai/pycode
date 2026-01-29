"""Min-Max Sum - Calculate sum excluding min/max."""


def minmaxsum(arr):
    """minmaxsum function."""
    for i in range(len(arr)):
        min = i
        for j in range(len(arr)):
            if arr[min] < arr[j]:
                swap = arr[min]
                arr[min] = arr[j]
                arr[j] = swap
            else:
                pass
        minmax = [0, 0]
        lista = arr.copy()
        listb = arr.copy()
        del lista[-1]
        listb.pop(0)
        minmax[0] = sum(lista)
        minmax[1] = sum(listb)
    print(minmax[0], " ", minmax[1])


a = [5, 2, 7, 1, 4]
minmaxsum(a)
