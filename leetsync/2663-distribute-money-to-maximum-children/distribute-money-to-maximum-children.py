class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # eligible_child = money // 8  # 3
        # remainder = money % 8   # 2
        # if remainder == 4:
        #     return eligible_child -1 
        # elif money<8:
        #     return -1
        # else: 
        #     return eligible_child
        if money < children:
            return -1
        usable_money = money - children
        q = usable_money // 7
        r = usable_money % 7
        if q > children:
            return children - 1
        elif r > 0 and children == q:
            return children - 1
        elif r == 3 and (children - q )== 1:    
            return q - 1
        else: 
            return q