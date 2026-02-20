from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res: List = []
        tmp: int = 0
        for _,ele in enumerate(nums):
            res_ele = tmp + ele
            tmp = res_ele
            res.append(res_ele)

        return res