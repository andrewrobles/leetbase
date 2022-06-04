class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """Time: O(n), Space: O(n)"""
        freqs = {}
        for s in stones:
            freqs[s] = 1 if s not in freqs else freqs[s] + 1
        count = 0
        for j in jewels:
            if j in freqs:
                count += freqs[j]
        return count
            
        