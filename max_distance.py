"""Maximum Distance - Find maximum distance between elements."""

import math


def max_distance(arrays) -> int:
    """max_distance function."""
    maxDistance = -math.inf
    minimum = arrays[0][0]
    maximum = arrays[0][-1]
    for i in range(0, len(arrays) - 1):
        maxDistance = max(
            maxDistance,
            abs(minimum - arrays[i + 1][-1]),
            abs(maximum - arrays[i + 1][0]),
        )
        minimum = min(minimum, arrays[i][0])
        maximum = max(maximum, arrays[i][-1])
    return maxDistance


if __name__ == "__main__":
    array = [[-8, -7, -7, -5, 1, 1, 3, 4], [-2], [-10, -10, -7, 0, 1, 3], [2]]
    print(max_distance(array))
