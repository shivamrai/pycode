class Solution:
    def removeDuplicates(self, nums: list) -> int:
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
    print(x.removeDuplicates([1, 1, 1, 2, 2, 3]))
