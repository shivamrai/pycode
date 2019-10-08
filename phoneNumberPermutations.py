def letterCombinations(digits):
    dialPad = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
    digitslength = len(digits)
    if digitslength == 1:
        return dialPad[digits[0]] 
    current_list = []
    mid_list = []
    for i in range(digitslength):
        if i == digitslength - 1:
            break
        if i == 0:
            current_list = dialPad[digits[i]]
        for each in current_list:
            for each_letter in dialPad[digits[i+1]]:
                mid_list.append(each+each_letter)
        current_list = mid_list
        mid_list = []
    return list(set(current_list))

if __name__ == "__main__":
    c = '6862377'
    s =letterCombinations(c)
    print(s)
