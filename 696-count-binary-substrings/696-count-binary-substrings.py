class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        00110011
        |
           |
           
        
         
        For every inflection point
            Advance two pointers outward
            Break if no longer a binary substring
        """
        i = 0
        count = 0
        while i < len(s)-1:
            curr = s[i:i+2]
            if curr == '01':
                j = i
                k = i + 1
                count += 1
                while j-1>=0 and k+1<len(s) and s[j-1]=='0' and s[k+1]=='1':
                    j -= 1
                    k += 1
                    curr = s[j:k+1]
                    count += 1
            elif curr == '10':
                j = i
                k = i + 1
                count += 1
                while j-1 >= 0 and k+1 < len(s) and s[j-1]=='1' and s[k+1]=='0':
                    j -= 1
                    k += 1
                    curr = s[j:k+1]
                    count += 1
            i += 1
        return count
                
                
                
                