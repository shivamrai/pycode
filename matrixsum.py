def diagonalDifference(arr):
    sumrightdiagonal = 0
    sumleftdiagonal = 0
    rows = len(arr)
    columns = len(arr[0])
    n = rows
    for i in range(rows):
        for j in range(columns):
            if i == j:
                print(arr[i][j])
                sumrightdiagonal = sumrightdiagonal + abs(arr[i][j])
                print(sumrightdiagonal)
            else:
                continue
    for i in range(rows):
        for j in range(columns):
            if i == n - j - 1:
                print(arr[i][j])
                sumleftdiagonal = sumleftdiagonal + abs(arr[i][j])
                print(sumleftdiagonal)
            else:
                continue
    print(sumrightdiagonal)
    print(sumleftdiagonal)
    return abs(sumleftdiagonal - sumrightdiagonal)


arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

arr1 = [
    [6, 6, 7, -10, 9, -3, 8, 9, -1],
    [9, 7, -10, 6, 4, 1, 6, 1, 1],
    [-1, -2, 4, -6, 1, -4, -6, 3, 9],
    [-8, 7, 6, -1, -6, -6, 6, -7, 2],
    [-10, -4, 9, 1, -7, 8, -5, 3, -5],
    [-8, -3, -4, 2, -3, 7, -5, 1, -5],
    [-2, -7, -4, 8, 3, -1, 8, 2, 3],
    [-3, 4, 6, -7, -7, -8, -3, 9, -6],
    [-2, 0, 5, 4, 4, 4, -3, 3, 0],
]
result = diagonalDifference(arr)
print(result)
