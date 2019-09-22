def timeConversion(s):
    #
    # Write your code here.
    #
    if(s[-2:] == 'PM'):
        if(s[0:2] != '12'):
            s[0:2].replace('12','00')
        else:
            s[0:2].replace(s[0:2], s[0:2]+12)
    return s[:-2]

input = "07:05:45PM"
# print(input[-2:])
# print(input[0:2])
input[-2:].replace('PM','XX')
print(input)
#stringtime = timeConversion(input)
#print(stringtime)
input[0:2].replace('07','19')
print(input)
