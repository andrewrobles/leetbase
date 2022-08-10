class Solution:
    # https://www.geeksforgeeks.org/find-excel-column-number-column-title/
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            result *= 26
            print(result)
            result += ord(columnTitle[i]) - ord('A') + 1
        return result