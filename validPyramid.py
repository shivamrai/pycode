def validPyramid(A: list) -> bool:
    if A == [] or len(A) < 3:
        return False
    getMax = max(A)
    print(getMax)
    i = 0
    j = A.index(getMax)
    validPyramidBool = False
    if j == len(A) - 1 or j == 0:
        return False
    else:
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
    print(validPyramid(listA))
