class TwoSum:
    @staticmethod
    def twoSum(givenList, target):
        listanswer = []
        for i, i1 in enumerate(givenList):
            for j, j1 in enumerate(givenList):
                if (i1 + j1 == target and i != j):
                    listanswer.append(i)
                    listanswer.append(j)
                    break
            return listanswer

    @staticmethod
    def twoSumDict(givenList, target):
        num_dict = {}
        for num in givenList:
            complement = target - num
            if complement in num_dict:
                return [complement, num]
            num_dict[num] = True
        return []

    @staticmethod
    def main():
        listA = [3, 2, 4]
        sum = 5
        listB = TwoSum.twoSum(listA, sum)
        print(listB)

if __name__ == "__main__":
    TwoSum.main()
    TwoSum.twoSumDict([3, 2, 4], 6)