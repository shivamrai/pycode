"""Maximum Ascending Subarray Sum - Find max sum of increasing subarray."""


class Solution:
    """Solution class."""

    def max_ascending_sum(self, nums: list) -> int:
        """max_ascending_sum function."""
        prev, total, maxTotal = 0, 0, 0
        for n in nums:
            if prev < n:
                total += n
            else:
                total = n
            prev = n
            maxTotal = max(total, maxTotal)
        return maxTotal


if __name__ == "__main__":
    x = Solution()
    print(x.max_ascending_sum([10, 20, 30, 5, 10, 50]))
    print(x.max_ascending_sum([100, 10, 1]))
