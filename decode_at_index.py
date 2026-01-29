"""Decode String at Index - Find character at decoded position."""


class Solution:
    """Solution class."""

    def decode_at_index(self, S: str, K: int) -> str:
        """decode_at_index function."""
        decodeS = ""
        i = 0
        while i < len(S):
            reserve = ""
            if S[i].isnumeric():
                S.replace(S[i], "")
                decodeS = S[:i]
                for j in range(1, int(S[i])):
                    reserve += decodeS
                # if(reserve[-1].isnumeric()):
                #     reserve=reserve[:-1]
                decodeS += reserve
            i += 1
        print(decodeS)
        return "h"


if __name__ == "__main__":
    x = Solution()
    print(x.decode_at_index("ha22", 5))
