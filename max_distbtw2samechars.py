"""Max Distance Between Same Characters."""


class Solution:
    """Solution class."""

    def max_length_between_equal_characters(self, s: str) -> int:
        """max_length_between_equal_characters function."""
        maxDistance = -1
        freq = {}
        for i, char in enumerate(s):
            if char not in freq:
                freq[char] = i
            else:
                distance = i - freq[char] - 1
                maxDistance = max(maxDistance, distance)
        return maxDistance


if __name__ == "__main__":
    x = Solution()
    print(x.max_length_between_equal_characters("ygtqdztaduxlsaacrwgtewywwchlnqzgjxhqgdhybncgaifonbe"))
