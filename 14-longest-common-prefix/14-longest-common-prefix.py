class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixes = []
        if len(strs) == 1:
            return strs[0]
        longest_common_prefix = ''
        for i in range(len(strs) - 1):
            current_word = strs[i]
            next_word = strs[i+1]
            current_prefix = ""
            for j in range(len(current_word)):
                if j < len(next_word) and current_word[j] == next_word[j]:
                    current_prefix = current_word[:j + 1]
                else:
                    break
            prefixes.append(current_prefix)
        return min(prefixes) if len(prefixes) != 0 else ""
        
        # """Time: O(n^2), Space: O(n)"""
        # longest_prefix = ''
        # longest_word = max(strs, key=len)       
        # for i in range(0, len(longest_word)+1):
        #     current_prefix = longest_word[:i]
        #     for j, word in enumerate(strs):
        #         if word[:i] != current_prefix:
        #             return longest_prefix
        #         elif j == len(strs) - 1:
        #             longest_prefix = max(current_prefix, longest_prefix, key=len)
        # return longest_prefix