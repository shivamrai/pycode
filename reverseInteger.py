import math


class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = False
        if x < 0:
            sign = True
            x *= -1
        while x > 0:
            # num=x%10
            res = (res * 10) + x % 10
            x = math.floor(x / 10)
        return res if sign == False else -1 * res


if __name__ == "__main__":
    x = Solution()
    print(x.reverse(123))
