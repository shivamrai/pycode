"""Baseball Game - Calculate score with special operations."""


class Solution:
    """Solution class."""

    def cal_points(self, ops: list) -> int:
        """cal_points function."""
        record = []
        for op in ops:
            if op == "+":
                record.append((record[-1]) + (record[-2]))
            elif op == "D":
                record.append(2 * (record[-1]))
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        # return record
        score = 0
        for rec in record:
            score += rec
        return score


if __name__ == "__main__":
    x = Solution()
    print(x.cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"]))
