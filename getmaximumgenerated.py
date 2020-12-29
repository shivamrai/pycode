class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        lmax = -64
        num = []
        num.append(0)
        num.append(1)
        for i in range(2,n+1):
            if(i%2==0):
                num.append(num[int(i//2)])
            else:
                currNum = num[int(i//2)] + num[int(i//2) + 1 ]
                num.append(currNum)
            lmax = max(lmax,num[i])
        return lmax

if __name__ == "__main__":
    s = Solution()
    print(s.getMaximumGenerated(7))