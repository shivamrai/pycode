"""Reach Number - Find steps to reach target."""


class Solution:
    """Solution class."""

    def reach_number(self, target: int) -> int:
        """reach_number function."""
        num = 0
        move = 1
        ctr = 0
        while num != target:
            if num + (move * -1) >= target:
                num = num + (move * -1)
            elif num + move <= target:
                num += move
            move += 1
            ctr += 1
        return ctr


if __name__ == "__main__":
    x = Solution()
    print(x.reach_number(-2))
