"""Given two strings ransomNote and magazine, return true if ransomNote
can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Leetcode 383. Ransom Note
https://leetcode.com/problems/ransom-note/
"""


class Solution:
    """Solution class."""

    def can_construct(self, ransom_note: str, mag_str: str) -> bool:
        """can_construct function."""
        mag_dict = {}
        for x in mag_str:
            if x in mag_dict:
                mag_dict[x] += 1
            else:
                mag_dict[x] = 1
        for x in ransom_note:
            if x in mag_dict and mag_dict[x] > 0:
                mag_dict[x] -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    ransom_note_str = "a"
    magazine_str = "b"
    result = solution.can_construct(ransom_note_str, magazine_str)
    print(f"Can construct '{ransom_note_str}' from '{magazine_str}': {result}")

    ransomNote = "aa"
    magazine = "ab"
    result = solution.can_construct(ransomNote, magazine)
    print(f"Can construct '{ransomNote}' from '{magazine}': {result}")

    ransomNote = "aa"
    magazine = "aab"
    result = solution.can_construct(ransomNote, magazine)
    print(f"Can construct '{ransomNote}' from '{magazine}': {result}")
