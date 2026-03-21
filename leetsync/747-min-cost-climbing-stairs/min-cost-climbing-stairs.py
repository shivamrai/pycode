class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # step_selection = cost[0] if cost[0] < cost[1] else cost[1]
        length = len(cost)
        # prev, curr = 0 , 0
        dp = [0] * length
        dp[-1], dp[-2] = cost[-1], cost[-2]
        i = length - 3
        while i >= 0:
            #print(f"{cost[i]} {dp[i+1]} {dp[i+2]}")
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
            i-=1

        for _, x in enumerate(dp):
            print(x)
        return min(dp[0], dp[1])