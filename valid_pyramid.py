"""Solution to LeetCode problem."""

# pylint: disable=duplicate-code


def valid_pyramid(A: list) -> bool:
    """valid_pyramid function."""
    if A == [] or len(A) < 3:
        return False
    getMax = max(A)
    print(getMax)
    i = 0
    j = A.index(getMax)
    validPyramidBool = False
    if j in (len(A) - 1, 0):
        return False
    while i < j:
        if A[i] < A[i + 1]:
            validPyramidBool = True
        else:
            validPyramidBool = False
            return validPyramidBool
        i += 1
    while j < len(A) - 1:
        if A[j] > A[j + 1]:
            validPyramidBool = True
        else:
            validPyramidBool = False
            break
        j += 1
    return validPyramidBool


if __name__ == "__main__":
    # https://leetcode.com/problems/valid-mountain-array/
    listA = [2, 1]
    print(valid_pyramid(listA))
