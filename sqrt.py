"""Square Root - Calculate integer square root."""


class Solution:
    """Solution class."""

    def reverse(self, x: int) -> int:
        """reverse function."""
        res = 0
        num = 0
        while x > 0:
            num = x % 10
            res = num * 10
            x = int(x / 10)
        return res
