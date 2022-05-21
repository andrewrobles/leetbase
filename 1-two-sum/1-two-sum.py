class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Time: O(n^2) | Space: O(1)"""        
        for i, number_i in enumerate(nums):
            for j, number_j in enumerate(nums):
                if i != j and number_i + number_j == target:
                    return [i, j]