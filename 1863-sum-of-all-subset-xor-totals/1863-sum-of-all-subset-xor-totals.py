class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, xor_sum):
            if i == len(nums):
                return xor_sum
            return dfs(i + 1, xor_sum) + dfs(i + 1, xor_sum ^ nums[i])
        
        return dfs(0, 0)