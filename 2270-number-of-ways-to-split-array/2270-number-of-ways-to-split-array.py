class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = (sum(nums) + 1) // 2  # Precompute the threshold
        valid_splits = 0

        for i in range(len(nums) - 1):  # Ensure non-empty right part
            left_sum += nums[i]            # Incrementally compute the left sum
            if left_sum >= right_sum:      # Check the condition for valid split
                valid_splits += 1
        return valid_splits