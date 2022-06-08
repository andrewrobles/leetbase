class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """Time: O(n^2), Space: O(1)"""
        subarray_sum = 0
        for i, start in enumerate(nums):
            minimum = start
            maximum = start
            for curr in nums[i+1:]:
                minimum = min(minimum, curr)
                maximum = max(maximum, curr)
                subarray_sum += maximum - minimum
        return subarray_sum
        