class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(number):
            curr = number
            while curr > 0:
                digit = curr % 10
                if digit == 0 or number % digit != 0:
                    return False
                curr = curr // 10
            return True
        result = []
        for i in range(left, right + 1):
            if is_self_dividing(i):
                result.append(i)
        return result
                
            
        