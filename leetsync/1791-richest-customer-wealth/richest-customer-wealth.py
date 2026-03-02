class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_money = 0
        for _,x in enumerate(accounts):
            money_sum = sum(x)
            max_money = max(money_sum, max_money)

        return max_money