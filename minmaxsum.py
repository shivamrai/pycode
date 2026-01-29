"""Min-Max Sum - Calculate sum excluding min_val/max."""


def minmaxsum(arr):
    """minmaxsum function."""
    for i in range(len(arr)):
        min_val = i
        for j in range(len(arr)):
            if arr[min_val] < arr[j]:
                arr[min_val], arr[j] = arr[j], arr[min_val]
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
