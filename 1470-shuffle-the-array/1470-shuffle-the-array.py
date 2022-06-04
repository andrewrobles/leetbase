class Solution(object):
    def shuffle(self, nums, n):
        """
        Example:
        11 21 12 22 13 23
        0     2     4
           1     3     5
        First n elements map to i * 2
        Second n elements map to i * 2 + 1
        
        Approach:
        - Create a new array of size 2 * n
        - Place first n elements in i * 2 indices
        - Place second n elements in i * 2 + 1 indices
        """
        array = [None] * (2*n)
        for i in range(0, n):
            array[2*i] = nums[i]
            array[2*i + 1] = nums[n + i]
        return array
        
        