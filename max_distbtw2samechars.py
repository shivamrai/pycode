"""Max Distance Between Same Characters."""


class Solution:
    """Solution class."""

    def max_length_between_equal_characters(self, s: str) -> int:
        """max_length_between_equal_characters function."""
        distance = 0
        maxDistance = -1
        freq = {}
        for i in range(0, len(s)):
            if s[i] not in freq:
                freq[s[i]] = i
            else:
                distance = i - freq[s[i]] - 1
                if distance > maxDistance:
                    maxDistance = distance
        return maxDistance


if __name__ == "__main__":
    x = Solution()
    print(x.max_length_between_equal_characters("ygtqdztaduxlsaacrwgtewywwchlnqzgjxhqgdhybncgaifonbe"))
