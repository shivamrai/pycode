"""Duplicate Zeros - Duplicate each zero in array."""


def duplicate_zeros(arr_input):
    """duplicate_zeros function."""
    i = 0
    while i < len(arr_input):
        if arr_input[i] == 0:
            print("Condition hit!! \n")
            arr_input.pop()
            arr_input.insert(i, 0)
            i = i + 1
        i = i + 1
    print(arr_input)


if __name__ == "__main__":
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicate_zeros(arr)
