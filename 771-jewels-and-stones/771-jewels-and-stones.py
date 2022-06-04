class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """Time: O(n), Space: O(n)"""
        count = 0
        freqs = {}
        for s in stones:
            if s not in freqs:
                freqs[s] = 1
            else:
                freqs[s] += 1 
        for j in jewels:
            if j in freqs:
                count += freqs[j]
        return count
            
        