class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Ascending
                current_sum += nums[i]
            else:  # Sequence breaks, restart
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        
        return max(max_sum, current_sum)  # Final check for max sum
