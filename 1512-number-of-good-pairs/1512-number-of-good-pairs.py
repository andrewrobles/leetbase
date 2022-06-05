class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        1 2 3 1 1 3
        
        """
        freqs = {}
        for number in nums:
            if number in freqs:
                freqs[number] += 1
            else:
                freqs[number] = 1
        count = 0
        for number, freq in freqs.items():
            count += (freq * (freq - 1)// 2)
        return count
                    
        