class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 
        mask = 1 
        while n > 0:
                if n & mask == 1:
                        count += 1
                n = n >> 1
        return count


