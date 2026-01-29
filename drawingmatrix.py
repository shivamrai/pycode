"""Drawing Matrix - Create matrix pattern."""


def justmatrix(n):
    """justmatrix function."""
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    justmatrix(3)
