"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
LeetCode 209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/
"""


class Solution:
    def bruteForce(self, target: int, nums: list[int]) -> int:
        sub_size = 1
        while sub_size <= len(nums):
            for i in range(len(nums) - sub_size + 1):
                # Calculate the sum of the current subarray
                sub_sum = sum(nums[i: i + sub_size])

                print(f"Checking subarray with {sub_size} with sum {sub_sum}")
                if sub_sum == target:
                    return sub_size
            sub_size += 1
        return 0

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start, end = 0, 0
        subarray_sum = 0
        min_length = float("inf")
        while end < len(nums):
            subarray_sum += nums[end]
            print(f"Adding {nums[end]} to subarray sum: {subarray_sum}")
            while subarray_sum >= target:
                min_length = min(min_length, end - start + 1)
                subarray_sum -= nums[start]
                print(
                    f"Subarray sum >= target, updating min_length: {min_length}, removing {
                        nums[start]} from sum")
                print(
                    f"New subarray sum after removing {
                        nums[start]}: {subarray_sum}")
                start += 1
            end += 1
        return min_length if min_length != float("inf") else 0


if __name__ == "__main__":
    solution = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    result = solution.minSubArrayLen(target, nums)
    print(f"Minimum size of subarray with sum >= {target} is: {result}")
