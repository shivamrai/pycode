"""
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # when consecutive 0 is encountered, count the number of consecutive 1's and vice versa
        groups: list[int] = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)  # Append the last group count
        # Now count the valid substrings
        result = 0
        print(groups)
        # Iterate through the groups and count pairs of consecutive groups
        # where the number of 0's and 1's are equal
        if len(groups) < 2:
            return 0
        result = 0
        # We can only form valid substrings between pairs of groups
        # e.g., between group[i] and group[i+1]
        # where group[i] is the count of 0's and group[i+1]# is the count of 1's or vice versa
        for i in range(1, len(groups)):
            result += min(groups[i - 1], groups[i])
        return result

if __name__ == "__main__":
    solution = Solution()
    # Example 1
    s1 = "00110011"
    print(solution.countBinarySubstrings(s1))  # Output: 6

    # Example 2
    s2 = "10101"
    print(solution.countBinarySubstrings(s2))  # Output: 4