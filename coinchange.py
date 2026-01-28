class Solution:
    def coinChange(self, coins, amount: int) -> int:
        # bottomup approach
        # try building problems for all the combinations till amount and select the least possible number of coins for every consecutive answer
        # min(prev, current)
        array = [amount + 1] * (amount + 1)
        array[0] = 0
        for i in range(1, len(array)):
            for coin in coins:
                if i - coin > len(array) or i - coin < 0:
                    continue
                else:
                    array[i] = min(array[i - coin] + 1, array[i])
        return array[-1] if array[-1] != amount + 1 else -1


if __name__ == "__main__":
    x = Solution()
    print(x.coinChange([1, 2, 5], 11))
