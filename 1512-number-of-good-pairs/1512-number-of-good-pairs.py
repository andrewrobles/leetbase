class Solution(object):
    def numIdenticalPairs(self, nums):
        """Time: O(n^2), Space: O(1)"""
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count
                    
        