"""Max Profit Shares - Calculate maximum profit from stocks."""


class Solution:
    """Solution class."""

    def max_profit(self, prices) -> int:
        """max_profit function."""
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
    print(x.max_profit([2, 4, 1]))
