class Solution:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        canPlace = True
        ct = 0
        for i in range(1,len(flowerbed)):
            if(flowerbed[i]==flowerbed[i-1]):
                canPlace = False
            if(i%2==0 and i-1==i==i+1==0):
                ct+=1
        return n==ct or canPlace

if __name__ == "__main__":
    x = Solution()
    print(x.canPlaceFlowers([1,0,0,0,1,0,1],1))