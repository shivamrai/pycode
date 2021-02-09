class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        dp = [0]*60
        ctr = 0
        for i in range(len(time)):
            if(time[i]%60==0):
                ctr+=dp[0]
            else:
                ctr+=dp[60-time[i]%60]
            dp[time[i]%60]+=1
        return ctr
    
if __name__ == "__main__":
    x = Solution()
    print(x.numPairsDivisibleBy60([[30,20,150,100,40]]))