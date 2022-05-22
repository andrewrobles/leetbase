class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = '([{'
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                bracket = stack.pop()
                if bracket != pairs[char]:
                    return False
        return len(stack) == 0
                
        