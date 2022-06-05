class Solution(object):
    def subArrayRanges(self, nums):
        subarray_sum = 0
        for i in range (len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    sub = nums[i:j+1]
                    miin = nums[i]
                    maax = nums[i]
                if nums[j] > maax:
                    maax = nums[j]
                elif nums[j] < miin:
                    miin = nums[j]  
                subarray_sum += (maax - miin)
        return subarray_sum
    
#     def subArrayRanges(self, nums):
#         """Time: O(n^2), Space: O(1)"""
#         range_sum = 0
#         for length in range(1, len(nums) + 1):
#             start = 0
#             stop = start + length
#             while stop <= len(nums):
#                 subarray = nums[start:stop]
#                 range_sum += (max(subarray) - min(subarray))
#                 start += 1
#                 stop = start + length
#         return range_sum
                
        