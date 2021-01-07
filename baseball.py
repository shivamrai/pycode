class Solution:
    def calPoints(self, ops: list) -> int:
        record = []
        opA = 0
        opB = 0
        for i in range(len(ops)):
            if(ops[i]=='+'):
                opA = record[-1]
                opB = record[-2]
                record.append((opA)+(opB))
            elif(ops[i]=='D'):
                opA = record[-1]
                record.append(2*(opA))
            elif(ops[i]=='C'):
                record.pop()
            else:
                record.append(int(ops[i]))
        return record
                
        
                
if __name__ == "__main__":
    x = Solution()
    print(x.calPoints(["5","-2","4","C","D","9","+","+"]))