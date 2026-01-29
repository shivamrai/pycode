"""2D Array Hourglass - Find maximum hourglass sum."""


# Complete the hourglassSum function below.
def hourglass_sum(arr):
    """hourglass_sum function."""
    largestSum = -32767
    currentSum = -32767
    i = 0
    j = 0
    k = 0
    for j in range(0, 4):
        for k in range(0, 4):
            currentSum = (
                arr[j][k]
                + arr[j][k + 1]
                + arr[j][k + 2]
                + arr[j + 1][k + 1]
                + arr[j + 2][k]
                + arr[j + 2][k + 1]
                + arr[j + 2][k + 2]
            )
            if largestSum < currentSum:
                largestSum = currentSum
    return largestSum


if __name__ == "__main__":
    # arr = [[0 for x in range(6)] for y in range(6)]
    # print(arr)
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    print(arr)
    largestSum = hourglass_sum(arr)
    print(largestSum)
