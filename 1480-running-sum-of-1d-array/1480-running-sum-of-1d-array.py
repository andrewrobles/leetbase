class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr = 0
        result = []
        for i, num in enumerate(nums):
                curr += num
                result.append(curr)
        return result
