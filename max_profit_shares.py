"""Max Profit Shares - Calculate maximum profit from stocks."""


class Solution:
    """Solution class."""

    def max_profit(self, prices) -> int:
        """max_profit function."""
        minPrice = 899237498237
        maxProfit = 0
        for _, price in enumerate(prices):
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit


if __name__ == "__main__":
    x = Solution()
    print(x.max_profit([2, 4, 1]))
