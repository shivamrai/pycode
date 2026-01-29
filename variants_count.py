"""Variants Count - Count number of variants."""


def variants_count(n, s0, k, b, m, a):
    """variants_count function."""
    s = [s0]
    c = 0
    for i in range(1, n):
        s.append(((k * s[i - 1] + b) % m) + 1 + s[i - 1])
        if a / s[-1] >= s[-1]:
            c = len(s) ** 2
        else:
            l, r = 0, len(s) - 1
            x = a / s[-1]
            val = 0
            while l <= r:
                mid = l + (r - l) // 2
                if s[mid] == x:
                    val = mid
                    break
                elif s[mid] < x:
                    val = mid
                    l = mid + 1
                else:
                    r = mid - 1
            c += (val + 1) * 2
    return c
