
def twoSum(givenList, target):
        listanswer = []
        for i,i1 in enumerate(givenList):
            for j,j1 in enumerate(givenList):
                if(i1+j1 == target and i != j):
                    listanswer.append(i)
                    listanswer.append(j)
                    break
            return listanswer

listA=[3,2,4]
sum = 5
listB = []
listB = twoSum(listA, sum)
print(listB)