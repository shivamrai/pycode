"""Time Conversion - Convert time format."""


def time_conversion(s):
    """time_conversion function."""
    #
    # Write your code here.
    #
    n = s
    if s[-2:] == "PM":
        if s[0:2] != "12":
            n = str(int(s[:2]) + 12) + s[2:8]
            # print(n)
    else:
        if s[0:2] == "12":
            n = s.replace(s[0:2], "00")
    return n[:-2]


input = "07:05:45PM"
# print(input[-2:])
# print(input[0:2])
input[-2:].replace("PM", "XX")
print(input)
# stringtime = time_conversion(input)
# print(stringtime)
input[0:2].replace("07", "19")
print(input)
