"""Kth Factor - Find kth smallest factor of n."""


class Solution:
    """Solution class."""

    def kth_factor(self, n: int, k: int) -> int:
        """kth_factor function."""
        fcount = 1
        if n == 1 or k == 1:
            return fcount
        i = 2
        while i <= n:
            if n % i == 0:
                fcount += 1
            if fcount == k:
                return i
            i += 1
        return -1


if __name__ == "__main__":
    x = Solution()
    print(x.kth_factor(7, 2))
