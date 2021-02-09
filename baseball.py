class Solution:
    def calPoints(self, ops: list) -> int:
        record = []
        for i in range(len(ops)):
            if(ops[i]=='+'):
                record.append((record[-1])+(record[-2]))
            elif(ops[i]=='D'):
                record.append(2*(record[-1]))
            elif(ops[i]=='C'):
                record.pop()
            else:
                record.append(int(ops[i]))
        #return record
        score = 0
        for rec in record:
            score+=rec
        return score
        
                
if __name__ == "__main__":
    x = Solution()
    print(x.calPoints(["5","-2","4","C","D","9","+","+"]))