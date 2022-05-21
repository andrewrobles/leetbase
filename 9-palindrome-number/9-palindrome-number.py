class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Time: O(n), Space: O(n)"""
        digits = [digit for digit in str(x)]
        i, j = 0, len(digits) - 1
        while i < j:
            if digits[i] != digits[j]:
                return False
            i += 1
            j -= 1
        return True