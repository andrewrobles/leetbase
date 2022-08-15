class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        for word in s.split():
                result = '{}{} '.format(result, ''.join(list(reversed(word))))
        return result[:-1]      
