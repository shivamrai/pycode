"""Longest Substring Without Repeating Characters."""


def length_of_longest_substring(s):
    """length_of_longest_substring function."""
    used = {}
    i, ans = 0, 0
    for j, x in enumerate(s):
        if x in used and used[x] >= i:
            i = used[x] + 1
        used[x] = j
        ans = max(ans, j - i + 1)
    return ans


if __name__ == "__main__":
    stringss = "abcabcbb"
    snew = length_of_longest_substring(stringss)
    print(snew)
