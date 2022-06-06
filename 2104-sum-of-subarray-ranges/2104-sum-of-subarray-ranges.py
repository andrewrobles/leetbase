class Solution(object):
    def subArrayRanges(self, nums):
        """
        Time: O(n^2), Space: O(1)
        
        ORDER OF SUBARRAY SUM COMPUTATION FOR [1,2,3]
        =====================================================
        for i=0, start in enumerate(nums):
            for curr=1 in nums[i=0+1:]:
            subarray_sum += calc_subarray_sum(1)
            ----------------------------------------
            for curr=2 in nums[i=0+1:]:
            subarray_sum += calc_subarray_sum(1 2)
            ----------------------------------------
            for curr=3 in nums[i=0+1:]:
            subarray_sum += calc_subarray_sum(1 2 3)
        =====================================================
        for i=1, start in enumerate(nums):
            for curr=2 in nums[i=1+1:]:
            subarray_sum += calc_subarray_sum(2)
            ----------------------------------------
            for curr=3 in nums[i=1+1:]:
            subarray_sum += calc_subarray_sum(2 3)
        =====================================================
        for i=2, start in enumerate(nums):
            for curr=3 in nums[i=2+1:]:
            subarray_sum += calc_subarray_sum(3)
        =====================================================
        """
        subarray_sum = 0
        for i, start in enumerate(nums):
            minimum = start
            maximum = start
            for curr in nums[i+1:]:
                minimum = min(minimum, curr)
                maximum = max(maximum, curr)
                subarray_sum += maximum - minimum
        return subarray_sum
                
                
        
        
                
        