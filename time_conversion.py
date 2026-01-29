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


input_time = "07:05:45PM"
# print(input_time[-2:])
# print(input_time[0:2])
input_time[-2:].replace("PM", "XX")
print(input_time)
# stringtime = time_conversion(input_time)
# print(stringtime)
input_time[0:2].replace("07", "19")
print(input_time)
