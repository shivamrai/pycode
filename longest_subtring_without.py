"""
Given a string s, find the length of the longest substring without repeating characters.
substring = s[i:]
substring = s[i:j] where i <= j
Leetcode 3: Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    """Solution class."""

    def length_of_longest_substring(self, input_str: str) -> int:
        """length_of_longest_substring function."""
        subset = set()
        start = 0
        max_len = 0
        for i, char in enumerate(input_str):
            while char in subset:
                subset.remove(input_str[start])
                start += 1
            subset.add(char)
            max_len = max(max_len, i - start + 1)
        return max_len


if __name__ == "__main__":
    solution = Solution()
    input_str = "abcabcbb"
    result = solution.length_of_longest_substring(input_str)
    print(f"Length of the longest substring without repeating characters in '{input_str}' is: {result}")
    input_str = " "
    result = solution.length_of_longest_substring(input_str)
    print(f"Length of the longest substring without repeating characters in '{input_str}' is: {result}")
    input_str = "aab"
    result = solution.length_of_longest_substring(input_str)
    print(f"Length of the longest substring without repeating characters in '{input_str}' is: {result}")
    input_str = "pwwkew"
    result = solution.length_of_longest_substring(input_str)
    print(f"Length of the longest substring without repeating characters in '{input_str}' is: {result}")
