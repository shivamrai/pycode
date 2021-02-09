class Solution:
    def isSubArray(self,arr1,arr2):
        i,j=0,0
        n,m=len(arr1),len(arr2)
        while(i<n and j<m):
            if(arr1[i]==arr2[j]):
                i+=1
                j+=1
                if(j==m):
                    return True
            else:
                i=i-j+1
                j=0
        return False

if __name__ == "__main__":
    x = Solution()
    print(x.isSubArray([1, 4, 2, 3, 5],[1, 4, 2]))