class Solution:
    # O(n^2) time | O(1) space
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        array = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    count += 1
            array.append(count)
        return array
        