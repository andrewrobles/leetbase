class Solution:
    def romanToInt(self, s: str) -> int:
        """Time: O(n), Space: O(1)"""
        index, integer, values = 0, 0, {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        while index < len(s):
            symbol = s[index]
            if index + 1 < len(s):
                next_symbol = s[index + 1]
                if symbol == 'I' and (next_symbol == 'V' or next_symbol == 'X')\
                or symbol == 'X' and (next_symbol == 'L' or next_symbol == 'C')\
                or symbol == 'C' and (next_symbol == 'D' or next_symbol == 'M'):
                    integer += values[next_symbol] - values[symbol]
                    index += 2
                    continue
            integer += values[symbol]
            index += 1
        return integer