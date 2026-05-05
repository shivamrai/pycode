class Solution:
    def isValid(self, s: str) -> bool:
        characters = {"(":")", "{":"}", "[":"]"}
        stack = []

        for chr in s:
            if chr in characters.keys():
                stack.append(chr)
            elif chr in characters.values():
                if stack and characters[stack[-1]] == chr:
                    stack.pop()
                else:
                    return False
            
        return True if (len(stack) == 0) else False