class Solution:
    # https://leetcode.com/problems/sum-of-all-subset-xor-totals/discuss/2439315/Python-bit-masking-2pow-n-solution
    def subsetXORSum(self, nums: List[int]) -> int:
        def checkbit(i,j):
            if 1 << i & j:
                return True
            return False

        N = len(nums)
        rng = 1 << N
        ans = 0
        for i in range(rng):
            xor = 0
            for j in range(N):
                if checkbit(j,i):
                    xor ^= nums[j]

            ans += xor

        return ans  
                