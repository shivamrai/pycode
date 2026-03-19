class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [0, 1]:
            return 1
        i=2
        prev, curr = 1, 1
        while i <= n:
            temp = curr
            curr = prev + curr
            prev = temp
            i += 1
        return curr