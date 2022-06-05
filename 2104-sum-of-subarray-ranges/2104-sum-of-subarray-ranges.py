class Solution(object):
    def subArrayRanges(self, nums):
        res = 0
        for i, x in enumerate(nums):
            minv = x
            maxv = x
            for  y in nums[i+1:]:
                minv = min(minv, y)
                maxv = max(maxv, y)
                res += maxv-minv 
        return res
    
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
                
        