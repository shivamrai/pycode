"""Single Number - Find single number in array."""


class solution:
    """solution class."""

    #     Iterate over all the elements in nums\text{nums}nums
    #     If some number in nums\text{nums}nums is new to array, append it
    #     If some number is already in the array, remove it
    def single_number(self, nums: List[int]) -> int:
        """single_number function."""
        counter = []
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] in counter:
                counter.remove(nums[i])
            else:
                counter.append(nums[i])
        return counter.pop()


if __name__ == "__main__":
    nums = [2, 1, 2]
    s = solution
    s.single_number(nums)
