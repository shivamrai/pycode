if __name__ == "__main__":
    # for i in range(0,3):
    #     for k in range(0,i):
    #         print('*', end=" ")
    #     print("\n")
    n, i = 8, 0
    rowCounter = 0
    while i < n:
        for k in range(0, i + 1):
            print("*", end=" ")
            if i == n:
                break
        i += 1
        print("\r")
