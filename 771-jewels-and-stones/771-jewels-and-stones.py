class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """Time: O(n^2), Space: O(1)"""
        count = 0
        for j in jewels:
            for s in stones:
                if j == s: 
                    count += 1
        return count
        