"""String to Number - Convert string to integer."""


def my_atoi(input_str):
    """my_atoi function."""
    sign = 1
    num = 0
    if input_str.strip == "":
        return 0
    if input_str.strip()[0] == "-":
        sign = -1
    input_str = input_str.strip()
    for x, y in enumerate(input_str):
        if (y in ('+', '-')) and x == 0:
            pass
        elif y.isdigit():
            num = num * 10 + int(y)
        else:
            break
    num = num * sign
    if num > (2**31) - 1:
        return (2**31) - 1
    if num < -(2**31):
        return -(2**31)
    return num


if __name__ == "__main__":
    input_value = "     -49 is here"
    print(input_value.strip())
    print(my_atoi(input_value))
