def mergeSorted(nums1, nums2):
    i, j, k = 0, 0, 0
    combined = []
    while i < len(nums1):
        if nums1[j] < nums2[k]:
            combined[i] = nums1[j]
            j += 1
        else:
            combined[i] = nums2[k]
            k += 1
        i += 1
    print(combined)


if __name__ == "__main__":
    a = [1, 2, 3, 0, 0, 0]
    b = 3
    c = [2, 5, 6]
    d = 3
    mergeSorted(a, c)
