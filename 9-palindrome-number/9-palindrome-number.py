class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Time: O(log n), Space: O(1)"""
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        y = 0
        while x > y:
            y *= 10
            y += (x % 10)
            x //= 10
        return x == y or x == y // 10