class Solution(object):
    def subArrayRanges(self, nums):
        """
        Order of subarray sum computation:
        1
        1 2
        1 2 3
        2
        2 3
        3
        """
        subarray_sum = 0
        for i, start in enumerate(nums):
            minimum = start
            maximum = start
            for curr in nums[i+1:]:
                minimum = min(minimum, curr)
                maximum = max(maximum, curr)
                subarray_sum += (maximum - minimum)
        return subarray_sum
                
                
        
        
                
        