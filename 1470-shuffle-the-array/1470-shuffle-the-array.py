class Solution(object):
    def shuffle(self, nums, n):
        """Time: O(n), Space: O(n)"""
        array = [None] * (2*n)
        for i in range(0, n):
            array[2*i] = nums[i]
            array[2*i + 1] = nums[n + i]
        return array
        
        