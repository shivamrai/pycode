def closestNumber(a, b, x):
    return round(a**b / x) * x


if __name__ == "__main__":
    arrayinput = [
        [540385427, 0, 7],
        [959, 0, 9],
        [861022531, 0, 10],
        [674, 2, 6],
        [635724059, 0, 3],
        [653379374, 1, 3],
        [756899538, 0, 10],
        [1, -734575199, 1],
        [1, 973594325, 1],
    ]
    for i in range(len(arrayinput)):
        print(
            closestNumber(
                arrayinput[i][0],
                arrayinput[i][1],
                arrayinput[i][2]))
    # print(closestNumber(540385427, 0, 7))
