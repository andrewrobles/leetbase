class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        def sort_key(value):
            return -1 if value % 2 == 0 else 1
        nums.sort(key=sort_key)
        return nums
