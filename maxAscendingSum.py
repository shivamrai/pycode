class Solution:
    def maxAscendingSum(self, nums: list) -> int:
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
    print(x.maxAscendingSum([10, 20, 30, 5, 10, 50]))
    print(x.maxAscendingSum([100, 10, 1]))
