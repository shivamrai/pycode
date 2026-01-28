"""LeetCode 88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has a size equal to m + n such that at least m elements of nums1 are valid.
Note: The solution should be done in-place, meaning that the merged array should be stored in nums1 and not returned as a new array.
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Example 4:
Input: nums1 = [1], m = 1, nums2 = [0], n = 1
Output: [0,1]
Example 5:
Input: nums1 = [0], m = 0, nums2 = [1,2], n = 2
Output: [1,2]
Example 6:
Input: nums1 = [0], m = 0, nums2 = [1,2,3], n = 3
Output: [1,2,3]
Example 7:
Input: nums1 = [0], m = 0, nums2 = [1,2,3,4], n = 4
Output: [1,2,3,4]
Example 8:
Input: nums1 = [0], m = 0, nums2 = [1,2,3,4,5], n = 5
Output: [1,2,3,4,5]
Example 9:
Input: nums1 = [0], m = 0, nums2 = [1,2,3,4,5,6], n = 6
Output: [1,2,3,4,5,6]"""


class Solution:
    def merge(
            self,
            nums1: list[int],
            m: int,
            nums2: list[int],
            n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # Pointer for nums1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # If there are remaining elements in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1


if __name__ == "__main__":
    # nums1 = [1,2,3,0,0,0]
    # m = 3
    # nums2 = [2,5,6]
    # n = 3
    sol = Solution()
    # nums1 = [1]
    # nums2 = []
    # m = 1
    # n = 0
    # print(sol.merge(nums1,m,nums2,n))
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    print(sol.merge(nums1, m, nums2, n))
