"""
6. Zigzag Conversion
Medium
Topics
conpanies iconCompanies

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);



Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

"""


class Solution:
    """Solution class."""

    def convert(self, s: str, numRows: int) -> str:
        """convert function."""
        if numRows == 1 or numRows >= len(s):
            return s

        # removed invalid pattern[str][str] assignment

        # lets build a 2D list to hold the zigzag pattern
        # each row will have len_s // numRows + 1 chars
        # this is to ensure that we can fill the pattern correctly
        # we will fill the pattern row by row
        # and then read it line by line
        # this will ensure that we can read the pattern correctly
        # if numRows is 1, we can return the string as it is
        pattern: list[list[str]] = [[""] for _ in range(numRows)]
        print(f"Initial pattern: {pattern}")
        for i, x in enumerate(s):
            row = i % (2 * numRows - 2)  # Calculate the row
            if row < numRows:
                pattern[row].append(x)
            else:
                pattern[2 * numRows - 2 - row].append(x)
        print(f"Filled pattern: {pattern}")
        return "".join("".join(row) for row in pattern if row)


if __name__ == "__main__":
    sol = Solution()
    # Example 1
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    print(sol.convert(s1, numRows1))  # Output: "PAHNAPLSIIGYIR"

    # Example 2
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    print(sol.convert(s2, numRows2))  # Output: "PINALSIGYAHRPI"

    # Example 3
    s3 = "A"
    numRows3 = 1
    print(sol.convert(s3, numRows3))  # Output: "A"
