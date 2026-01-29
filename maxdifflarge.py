"""Max Difference - Find maximum difference in array."""


def max_diff(arr, n):
    """max_diff function."""
    diff = [0] * (n - 1)
    for i in range(0, n - 1):
        diff[i] = arr[i + 1] - arr[i]

    # Now find the maximum sum
    # subarray in diff array
    max_diff_val = diff[0]
    for i in range(1, n - 1):
        if diff[i - 1] > 0:
            diff[i] += diff[i - 1]

        max_diff_val = max(max_diff_val, diff[i])

    return max_diff_val


if __name__ == "__main__":
    arr = [2, 3, 10, 6, 4, 8, 1]
    arr2 = [6, 3, 1, 2, 27, 5, 7, 8, 2]
    print(max_diff(arr2, len(arr2)))
