class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n  # dp[i] = size of the largest subset ending at i
        prev = [-1] * n  # to reconstruct the path
        max_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[max_idx]:
                max_idx = i

        # Reconstruct the result
        result = []
        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = prev[max_idx]

        return result[::-1]