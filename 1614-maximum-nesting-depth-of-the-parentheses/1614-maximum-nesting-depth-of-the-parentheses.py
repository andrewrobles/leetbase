class Solution:
    def maxDepth(self, s: str) -> int:
        """
        >>> (1+(2*3)+((8)/4))+1
        >>> (1)+((2))+(((3)))
        >>> maxDepth = len(['(', '(' '('])
        """
        stack = []
        maxLen = 0
        for char in s:
            if char in ['(', ')']:
                if char == '(':
                    stack.append(char)
                    maxLen = max(len(stack), maxLen)
                elif char == ')':
                    stack.pop()
        return maxLen
                    
        
        
        