class Solution:
    # O(n^2) time, O(1) space
    def subArrayRanges(self, nums: List[int]) -> int:
        subarray_sum = 0
        for i, start in enumerate(nums):
            minimum = start
            maximum = start
            for curr in nums[i+1:]:
                minimum = min(minimum, curr)
                maximum = max(maximum, curr)
                subarray_sum += maximum - minimum
        return subarray_sum
        