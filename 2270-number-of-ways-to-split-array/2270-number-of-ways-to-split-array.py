class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Total sum of the array
        left_sum = 0           # Initialize left sum
        valid_splits = 0       # Counter for valid splits

        # Iterate through the array, stopping at n-1 to ensure non-empty right segment
        for i in range(len(nums) - 1):
            left_sum += nums[i]         # Add current element to left sum
            total_sum -= nums[i]        # Subtract current element from total_sum (right sum)
            
            if left_sum >= total_sum:   # Check if it's a valid split
                valid_splits += 1
        
        return valid_splits