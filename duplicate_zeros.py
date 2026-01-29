"""Duplicate Zeros - Duplicate each zero in array."""


def duplicate_zeros(arr):
    """duplicate_zeros function."""
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            print("Condition hit!! \n")
            arr.pop()
            arr.insert(i, 0)
            i = i + 1
        i = i + 1
    print(arr)


if __name__ == "__main__":
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicate_zeros(arr)
