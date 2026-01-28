class Solution:
    def maxProfit(self, prices) -> int:
        minPrice = 899237498237
        maxProfit = 0
        for i in range(0, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        return maxProfit


if __name__ == "__main__":
    x = Solution()
    print(x.maxProfit([2, 4, 1]))
