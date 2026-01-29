"""2D Array Hourglass - Find maximum hourglass sum."""


# Complete the hourglassSum function below.
def hourglass_sum(arr_input):
    """hourglass_sum function."""
    largest_sum = -32767
    for j in range(0, 4):
        for k in range(0, 4):
            current_sum = (
                arr_input[j][k]
                + arr_input[j][k + 1]
                + arr_input[j][k + 2]
                + arr_input[j + 1][k + 1]
                + arr_input[j + 2][k]
                + arr_input[j + 2][k + 1]
                + arr_input[j + 2][k + 2]
            )
            largest_sum = max(largest_sum, current_sum)
    return largest_sum


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
    result_sum = hourglass_sum(arr)
    print(result_sum)
