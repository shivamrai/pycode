"""
Given a string s, find the length of the longest substring without repeating characters.
substring = s[i:]
substring = s[i:j] where i <= j
Leetcode 3: Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()
        start = 0
        max_len = 0
        for i, x in enumerate(s):
            while x in subset:
                print(f"Removing {s[start]} from subset because it is a duplicate of {x}")
                subset.remove(s[start])
                start += 1
            subset.add(x)
            max_len = max(max_len, i - start + 1)
        return max_len
            
if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring(s)
    print(f"Length of the longest substring without repeating characters in '{s}' is: {result}")
    s = " "
    result = solution.lengthOfLongestSubstring(s)
    print(f"Length of the longest substring without repeating characters in '{s}' is: {result}")
    s ="aab"
    result = solution.lengthOfLongestSubstring(s)
    print(f"Length of the longest substring without repeating characters in '{s}' is: {result}")
    s= "pwwkew"
    result = solution.lengthOfLongestSubstring(s)
    print(f"Length of the longest substring without repeating characters in '{s}' is: {result}")