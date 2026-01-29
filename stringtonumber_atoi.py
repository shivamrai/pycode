"""String to Number - Convert string to integer."""


def my_atoi(str):
    """my_atoi function."""
    sign = 1
    num = 0
    if str.strip == "":
        return 0
    if str.strip()[0] == "-":
        sign = -1
    str = str.strip()
    for x, y in enumerate(str):
        if (y == "+" or y == "-") and x == 0:
            pass
        elif y.isdigit():
            num = num * 10 + int(y)
        else:
            break
    num = num * sign
    if num > (2**31) - 1:
        return (2**31) - 1
    elif num < -(2**31):
        return -(2**31)
    return num


if __name__ == "__main__":
    str = "     -49 is here"
    print(str.strip())
    print(my_atoi(str))
