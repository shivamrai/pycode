class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
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
    print(x.decodeAtIndex("ha22", 5))
