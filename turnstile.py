def turnstileTimes(numCustomers, arrTime, direction):
    entryTime = []
    exitTime = []
    for i in range(0, numCustomers):
        if (direction[i] == 0):
            entryTime.append(i, arrTime[i], direction[i])
        else:
            exitTime.append(i, arrTime[i], direction[i])
    exitTime.sort()
    entryTime.sort()
    ans = [None] * numCustomers
    p, q = len(entryTime), len(exitTime)
    i, j = 0, 0
    for t in range(0, 100000000):
        if i < p and j < q:
            en = entryTime.index(i)
            ex = exitTime.index(j)
            if t < en:
                pass


def compare(enterTime, exitTime, time, status):
    enterTime -= time
    exitTime -= time
    if (enterTime < 0):
        enterTime = 0
    if (exitTime < 0):
        exitTime
    if (enterTime < exitTime):
        return -1
    if (enterTime == exitTime):
        if (status == 1):
            return 1
        else:
            return -1
    return 1


if __name__ == "__main__":
    numCustomers = 4
    arrTime = [0, 0, 1, 5]
    direction = [0, 1, 1, 0]
    print(turnstileTimes(numCustomers, arrTime, direction))
