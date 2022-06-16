class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """Approach #1: Group By Character"""
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1
        count = 0
        for i in range(1, len(groups)):
            count += min(groups[i-1], groups[i])
        return count
    
    # def countBinarySubstrings(self, s: str) -> int:
    #     i = 0
    #     count = 0
    #     while i < len(s)-1:
    #         curr = s[i:i+2]
    #         if curr == '01':
    #             j = i
    #             k = i + 1
    #             count += 1
    #             while j-1>=0 and k+1<len(s) and s[j-1]=='0' and s[k+1]=='1':
    #                 j -= 1
    #                 k += 1
    #                 curr = s[j:k+1]
    #                 count += 1
    #         elif curr == '10':
    #             j = i
    #             k = i + 1
    #             count += 1
    #             while j-1 >= 0 and k+1 < len(s) and s[j-1]=='1' and s[k+1]=='0':
    #                 j -= 1
    #                 k += 1
    #                 curr = s[j:k+1]
    #                 count += 1
    #         i += 1
    #     return count
                
                
                
                