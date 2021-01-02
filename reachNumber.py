class Solution:
    def reachNumber(self, target: int) -> int:
        num = 0
        move = 1
        ctr = 0
        while(num!=target):
            if(num+(move*-1)>=target):
                num=num+(move*-1)
            elif(num+move<=target):
                num+=move
            move+=1
            ctr+=1
        return ctr

if __name__ == "__main__":
    x=Solution()
    print(x.reachNumber(-2))