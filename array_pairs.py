"""Array Pairs - Check if array can be divided into pairs divisible by 60."""


def can_arrange(arr, k):
    """can_arrange function."""
    result = False
    len_ = len(arr) - 1
    iterations = int(len(arr) / 2)
    for i in range(0, iterations):
        if (arr[i] + arr[len_ - i]) % k == 0:
            result = True
    return result


if __name__ == "__main__":
    listA = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
    number = 5
    boolNumber = False
    boolNumber = can_arrange(listA, number)
    print(boolNumber)
