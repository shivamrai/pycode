"""Can Place Flowers - Check if flowers can be planted."""


class Solution:
    """Solution class."""

    def can_place_flowers(self, flowerbed, n) -> bool:
        """can_place_flowers function."""
        canPlace = True
        ct = 0
        for i in range(1, len(flowerbed)):
            if flowerbed[i] == flowerbed[i - 1]:
                canPlace = False
            if i % 2 == 0 and i - 1 == i == i + 1 == 0:
                ct += 1
        return n == ct or canPlace


if __name__ == "__main__":
    x = Solution()
    print(x.can_place_flowers([1, 0, 0, 0, 1, 0, 1], 1))
