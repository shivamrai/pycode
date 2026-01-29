"""Count Binary Substrings - Count consecutive ones and zeros."""


# this logic is broken and would be fixed later
def one_counter(n):
    """one_counter function."""
    arrayList = []
    b = 0
    while n > 2:
        b = int(n % 2)
        arrayList.append(b)
        n = n / 2
    if n == 1:
        arrayList.append(n)
    arrayList.reverse()
    str1 = "".join(str(arrayList))
    return str1


if __name__ == "__main__":
    c = one_counter(6)
    counter = 0
    consecutiveCounter = 0
    print(c)
    for i in range(0, len(c)):
        if c[i] == "1":
            counter += 1
            if counter >= consecutiveCounter:
                consecutiveCounter = counter
        else:
            counter = 0
    print(consecutiveCounter)
