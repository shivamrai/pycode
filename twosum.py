"""Two Sum - Find two numbers that sum to target."""


class TwoSum:
    """TwoSum class."""

    @staticmethod
    def two_sum(givenList, target):
        """two_sum function."""
        listanswer = []
        for i, i1 in enumerate(givenList):
            for j, j1 in enumerate(givenList):
                if i1 + j1 == target and i != j:
                    listanswer.append(i)
                    listanswer.append(j)
                    break
            return listanswer

    @staticmethod
    def two_sum_dict(givenList, target):
        """two_sum_dict function."""
        num_dict = {}
        for num in givenList:
            complement = target - num
            if complement in num_dict:
                return [complement, num]
            num_dict[num] = True
        return []

    @staticmethod
    def main():
        """main function."""
        listA = [3, 2, 4]
        total = 5
        listB = TwoSum.two_sum(listA, total)
        print(listB)


if __name__ == "__main__":
    TwoSum.main()
    TwoSum.two_sum_dict([3, 2, 4], 6)
