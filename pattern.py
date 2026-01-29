"""Pattern - Implement pattern matching."""


def drawpattern(n):
    """drawpattern function."""
    # counter = 1
    # handle spaces and then handle stars

    for i in range(0, n):
        # spaces
        for _ in range(0, i + 1):
            print(" ")
        # stars
        for _ in range(i, n):
            print("*", end="")

    print("\r")


drawpattern(2)
