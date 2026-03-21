class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        usable_money = money - children
        q = usable_money // 7
        r = usable_money % 7
        if q > children:
            return children - 1
        if r > 0 and children == q:
            return children - 1
        if r == 3 and (children - q) == 1:
            return q - 1
        return q
