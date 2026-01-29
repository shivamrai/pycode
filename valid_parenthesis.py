"""Valid Parentheses - Check if parentheses valid."""


def is_valid(input_str):
    """is_valid function."""
    # openBracketCounter = 0
    # openSquareCounter = 0
    # openRoundCounter = 0
    # for i in range(0,len(input_str)):
    #     if(input_str[i] == '['):
    #         openSquareCounter += 1
    #     elif(input_str[i]== ']'):
    #         openSquareCounter -= 1
    #     if(input_str[i] == '('):
    #         openRoundCounter += 1
    #     elif(input_str[i]== ')'):
    #         openRoundCounter -= 1
    #     if(input_str[i] == '{'):
    #         openBracketCounter += 1
    #     elif(input_str[i]== '}'):
    #         openBracketCounter -= 1
    # if(openBracketCounter == 0 and openRoundCounter == 0 and openSquareCounter == 0):
    #     return True
    # else:
    #     return False
    parentheis_dict = {"[": "]", "(": ")", "{": "}"}
    open_parenthesis = parentheis_dict.keys()
    stack = []
    if input_str == "":
        return True
    if len(input_str) % 2 != 0:
        return False
    for element in input_str:
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
    result = is_valid("([)]")
    print(result)
