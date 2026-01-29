"""Partition Labels - Partition string with no repeated characters."""

import unittest


class Solution:
    """Solution class."""

    def partition_labels(self, S: str) -> list:
        """partition_labels function."""
        # keep track of end Index

        end_idx = [0] * 26
        for i, char in enumerate(S):
            end_idx[ord(char) - ord("a")] = i

        res = []
        start, end = 0, 0

        for i, char in enumerate(S):
            end = max(end, end_idx[ord(char) - ord("a")])
            if i == end:
                res.append(i - start + 1)
                start = i + 1

        return res


class TestSolution(unittest.TestCase):
    """TestSolution class."""

    def testpartitionlabels(self):
        """testpartitionlabels function."""
        x = Solution()
        res = x.partition_labels("ababcbacadefegdehijhklij")
        self.assertEqual(res, [9, 7, 8])


if __name__ == "__main__":
    unittest.main()
