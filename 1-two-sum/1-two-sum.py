class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Time: O(n), Space: O(n)"""
        """
        a + b = c
        b = c - a
        
        {
        3:0,
        4:1,
        2:2
        }
        """
        values = {target-x: i for i, x in enumerate(nums)}
        for i, x in enumerate(nums):
            if x in values and values[x] != i:
                return [i, values[x]]
            