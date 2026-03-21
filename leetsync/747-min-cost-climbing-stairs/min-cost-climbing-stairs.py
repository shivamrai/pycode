from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0] * length
        dp[-1], dp[-2] = cost[-1], cost[-2]
        i = length - 3
        while i >= 0:
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
            i-=1

        return min(dp[0], dp[1])
