"""Maximum Time - Find valid time with maximum hour/minute."""


class Solution:
    """Solution class."""

    def _check_permutation(self, arr: list[int], ptr1: int, ptr2: int, ptr3: int, ptr4: int) -> int:
        """Check a specific permutation configuration and return max valid time."""
        max_time = -1

        for _ in range(64):
            hour = arr[ptr1] * 10 + arr[ptr2]
            minute = arr[ptr3] * 10 + arr[ptr4]

            if hour < 24 and minute < 60:
                time_value = hour * 100 + minute
                max_time = max(max_time, time_value)

            ptr1 = (ptr1 + 1) % 4
            ptr2 = (ptr2 + 1) % 4
            ptr3 = (ptr3 + 1) % 4
            ptr4 = (ptr4 + 1) % 4

        return max_time

    def largest_time_from_digits(self, arr: list[int]) -> str:
        """Find valid time with maximum hour/minute from 4 digits."""
        # All 6 permutations of 4 positions: (pos1, pos2, pos3, pos4)
        permutations_config = [
            (0, 1, 2, 3),
            (3, 2, 0, 1),
            (2, 0, 3, 1),
            (2, 3, 1, 0),
            (1, 3, 0, 2),
            (1, 0, 3, 2),
        ]

        max_time = -1
        for ptr1, ptr2, ptr3, ptr4 in permutations_config:
            time_result = self._check_permutation(arr, ptr1, ptr2, ptr3, ptr4)
            max_time = max(max_time, time_result)

        # If no valid time found, return empty string
        if max_time == -1:
            return ""

        # Format the time string
        hours = max_time // 100
        minutes = max_time % 100
        return f"{hours:02d}:{minutes:02d}"


if __name__ == "__main__":
    solution = Solution()
    print(solution.largest_time_from_digits([1, 9, 6, 0]))
