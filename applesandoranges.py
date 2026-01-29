"""Apples and Oranges - Count fruits within distance ranges."""


# Complete the countApplesAndOranges function below.
def count_apples_and_oranges(s, t, a, b, apples, oranges):
    """count_apples_and_oranges function."""
    countofApples = 0
    countofOranges = 0
    for apple in range(len(apples)):
        apples[apple] = apples[apple] + a
    for orange in range(len(oranges)):
        oranges[orange] = oranges[orange] + b
    for apple in range(len(apples)):
        if apples[apple] >= s and apples[apple] <= t:
            countofApples = countofApples + 1
    for orange in range(len(oranges)):
        if oranges[orange] >= s and oranges[orange] <= t:
            countofOranges = countofOranges + 1
    print(countofApples, " ", countofOranges)


if __name__ == "__main__":
    # st = input().split()

    s = 7

    t = 11

    # ab = input().split()

    a = 5

    b = 15

    # mn = input().split()

    m = 3

    n = 2

    apples = [-2, 2, 1]

    oranges = [5, -6]

    count_apples_and_oranges(s, t, a, b, apples, oranges)
