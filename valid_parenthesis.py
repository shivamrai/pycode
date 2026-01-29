"""Valid Parentheses - Check if parentheses valid."""


def is_valid(s):
    """is_valid function."""
    # openBracketCounter = 0
    # openSquareCounter = 0
    # openRoundCounter = 0
    # for i in range(0,len(s)):
    #     if(s[i] == '['):
    #         openSquareCounter += 1
    #     elif(s[i]== ']'):
    #         openSquareCounter -= 1
    #     if(s[i] == '('):
    #         openRoundCounter += 1
    #     elif(s[i]== ')'):
    #         openRoundCounter -= 1
    #     if(s[i] == '{'):
    #         openBracketCounter += 1
    #     elif(s[i]== '}'):
    #         openBracketCounter -= 1
    # if(openBracketCounter == 0 and openRoundCounter == 0 and openSquareCounter == 0):
    #     return True
    # else:
    #     return False
    parentheis_dict = {"[": "]", "(": ")", "{": "}"}
    open_parenthesis = parentheis_dict.keys()
    stack = []
    if s == "":
        return True
    if len(s) % 2 != 0:
        return False
    for element in s:
        if element in open_parenthesis:
            stack.append(element)
        else:
            if len(stack) == 0:
                return False
            if element != parentheis_dict[stack[-1]]:
                return False
            stack.pop()
    if not stack:
        return True
    return False


if __name__ == "__main__":
    isValidParantheis = False
    s = is_valid("([)]")
    print(s)
