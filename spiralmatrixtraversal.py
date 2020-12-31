class Solution:
    def spiralOrder(self, matrix):
        soln = []
        if(len(matrix)==0):
            return soln
        r1,c1 = 0,0
        r2,c2 = len(matrix)-1,len(matrix[0])-1
        while(r1<=r2 and c1<=c2):
            for c in range(c1,c2+1): soln.append(matrix[r1][c])
            for r in range(r1+1,r2): soln.append(matrix[r][c2])
            if(r1<r2 and c1<c2):    
                for c in range(c2,c1,-1): soln.append(matrix[r2][c])
                for r in range(r2,r1,-1): soln.append(matrix[r][c1])
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        return soln
if __name__ == "__main__":
    x = Solution()
    print(x.spiralOrder([[3],[2]]))