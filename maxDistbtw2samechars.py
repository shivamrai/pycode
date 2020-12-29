
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        distance = 0
        maxDistance = -1
        freq = {}
        for i in range(0,len(s)):
            if(s[i] not in freq):
                freq[s[i]] = i
            else:
                distance = i - freq[s[i]] -1
                if(distance>maxDistance): maxDistance = distance
        return maxDistance
if __name__ == "__main__":
    x = Solution()
    print(x.maxLengthBetweenEqualCharacters("ygtqdztaduxlsaacrwgtewywwchlnqzgjxhqgdhybncgaifonbe"))