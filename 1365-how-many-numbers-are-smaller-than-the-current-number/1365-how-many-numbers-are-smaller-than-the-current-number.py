class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Final list to be returned
        final_list = []      
        
        # Make copy of nums list, but sorted
        nums_sorted = sorted(nums)

        # Find location of num in nums_sorted, index = number of numbers below it
        final_list = [nums_sorted.index(num) for num in nums]
        
        return final_list
    
    # # O(n^2) time | O(1) space
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    #     array = []
    #     for i in range(len(nums)):
    #         count = 0
    #         for j in range(len(nums)):
    #             if i != j and nums[i] > nums[j]:
    #                 count += 1
    #         array.append(count)
    #     return array
        