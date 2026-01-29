"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ...,
numsr-1] of which the sum is greater than or equal to target. If there is
no such subarray, return 0 instead.
LeetCode 209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/
"""


class Solution:
    """Solution class."""

    def brute_force(self, target_val: int, nums_list: list[int]) -> int:
        """brute_force function."""
        sub_size = 1
        while sub_size <= len(nums_list):
            for i in range(len(nums_list) - sub_size + 1):
                # Calculate the sum of the current subarray
                sub_sum = sum(nums_list[i: i + sub_size])

                print(f"Checking subarray with {sub_size} with sum {sub_sum}")
                if sub_sum == target_val:
                    return sub_size
            sub_size += 1
        return 0

    def min_sub_array_len(self, target_val: int, nums_list: list[int]) -> int:
        """min_sub_array_len function."""
        start, end = 0, 0
        subarray_sum = 0
        min_length = float("inf")
        while end < len(nums_list):
            subarray_sum += nums_list[end]
            print(f"Adding {nums_list[end]} to subarray sum: {subarray_sum}")
            while subarray_sum >= target_val:
                min_length = min(min_length, end - start + 1)
                subarray_sum -= nums_list[start]
                print(f"Subarray sum >= target, updating min_length: {min_length}, "
                      f"removing {nums_list[start]} from sum")
                print(f"New subarray sum after removing {nums_list[start]}: {subarray_sum}")
                start += 1
            end += 1
        return min_length if min_length != float("inf") else 0


if __name__ == "__main__":
    solution = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    result = solution.min_sub_array_len(target, nums)
    print(f"Minimum size of subarray with sum >= {target} is: {result}")
