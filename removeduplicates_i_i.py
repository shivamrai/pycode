"""Remove Duplicates - Remove duplicate elements."""


class Solution:
    """Solution class."""

    def remove_duplicates(self, nums: list) -> int:
        """remove_duplicates function."""
        dup = 0
        size = len(nums)
        i = 1
        while i < size:
            if dup == 2:
                nums.pop(i)
            if nums[i - 1] == nums[i]:
                dup += 1
            else:
                dup = 0
            size = len(nums)
            i += 1
        return len(nums)


if __name__ == "__main__":
    x = Solution()
    print(x.remove_duplicates([1, 1, 1, 2, 2, 3]))
