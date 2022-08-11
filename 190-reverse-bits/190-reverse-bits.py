class Solution:
    # https://leetcode.com/problems/reverse-bits/discuss/54787/python-solution-with-detailed-explanation
    def reverseBits(self, n: int) -> int:
        ret, NUM_BITS = 0, 32
        for i in range(NUM_BITS):
            ret = ret | (n&0x1)<<(NUM_BITS-1-i)
            n = n >> 1
        return ret
    
        