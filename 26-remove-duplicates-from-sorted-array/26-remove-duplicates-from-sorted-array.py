class Solution(object):
    def removeDuplicates(self, nums):
        """Time: O(n), Space: O(1)"""
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i += 1
            j += 1
        return i + 1
        
        
            
        