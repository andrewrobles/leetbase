class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        a, b = 0, 0
        for i, char in enumerate(s):
                if s[i] == ' ' or i == len(s) - 1:
                        # reverse word 
                        b = i if i == len(s) - 1 else i - 1
                        while a < b:
                                s[a], s[b] = s[b], s[a]
                                a += 1
                                b -= 1
                        a = i + 1       
        return ''.join(s)
        # result = ''
        # for word in s.split():
        #         result = '{}{} '.format(result, ''.join(list(reversed(word))))
        # return result[:-1]      
