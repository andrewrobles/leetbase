class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Time: O(n^2), Space: O(n)"""
        longest_prefix = ''
        longest_word = max(strs, key=len)       
        for i in range(0, len(longest_word)+1):
            current_prefix = longest_word[:i]
            for j, word in enumerate(strs):
                if word[:i] != current_prefix:
                    return longest_prefix
                elif j == len(strs) - 1:
                    longest_prefix = max(current_prefix, longest_prefix, key=len)
        return longest_prefix