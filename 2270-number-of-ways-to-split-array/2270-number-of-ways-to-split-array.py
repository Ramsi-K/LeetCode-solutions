class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left = 0
        right = (sum(nums) + 1) // 2  # Precompute the threshold
        res = 0

        for i in range(len(nums) - 1):  # Ensure non-empty right part
            left += nums[i]            # Incrementally compute the left sum
            if left >= right:          # Check the condition for valid split
                res += 1
        return res