"""Reverse Integer - Reverse digits of integer."""

import math


class Solution:
    """Solution class."""

    def reverse(self, num: int) -> int:
        """reverse function."""
        res = 0
        sign = False
        if num < 0:
            sign = True
            num *= -1
        while num > 0:
            # num=num%10
            res = (res * 10) + num % 10
            num = math.floor(num / 10)
        return res if not sign else -1 * res


if __name__ == "__main__":
    x = Solution()
    print(x.reverse(123))
