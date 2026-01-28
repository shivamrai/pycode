def maxDiff(arr, n):
    diff = [0] * (n - 1)
    for i in range(0, n - 1):
        diff[i] = arr[i + 1] - arr[i]

    # Now find the maximum sum
    # subarray in diff array
    max_diff = diff[0]
    for i in range(1, n - 1):
        if diff[i - 1] > 0:
            diff[i] += diff[i - 1]

        if max_diff < diff[i]:
            max_diff = diff[i]

    return max_diff


if __name__ == "__main__":
    arr = [2, 3, 10, 6, 4, 8, 1]
    arr2 = [6, 3, 1, 2, 27, 5, 7, 8, 2]
    print(maxDiff(arr2, len(arr2)))
