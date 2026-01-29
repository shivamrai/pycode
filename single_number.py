"""Single Number - Find single number in array."""
from typing import List


class solution:
    """solution class."""

    #     Iterate over all the elements in nums\text{nums}nums
    #     If some number in nums\text{nums}nums is new to array, append it
    #     If some number is already in the array, remove it
    def single_number(self, nums: List[int]) -> int:
        """single_number function."""
        counter = []
        nums_list = nums
        nums_list.sort()
        for num in nums_list:
            if num in counter:
                counter.remove(num)
            else:
                counter.append(num)
        return counter.pop()


if __name__ == "__main__":
    sample_nums = [2, 1, 2]
    s = solution()
    s.single_number(sample_nums)
