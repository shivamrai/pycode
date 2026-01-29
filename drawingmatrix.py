"""Drawing Matrix - Create matrix pattern."""


def justmatrix(n):
    """justmatrix function."""
    for _ in range(n):
        for _ in range(n):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    justmatrix(3)
