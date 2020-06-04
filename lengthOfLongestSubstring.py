def lengthOfLongestSubstring(s):
    used = {}
    i,ans = 0,0
    for j, x in enumerate(s):
        if x in used and used[x] >= i:
            i = used[x] + 1
        used[x] = j
        ans = max(ans, j-i+1)
    return ans

if __name__ == "__main__":
    stringss="abcabcbb"
    snew= lengthOfLongestSubstring(stringss)
    print(snew)
