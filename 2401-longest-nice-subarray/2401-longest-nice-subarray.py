class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0  # Left pointer for sliding window
        window_and = 0  # Stores OR of current window
        max_length = 0  

        for right in range(len(nums)):  # Expand the window
            while (window_and & nums[right]) != 0:  # Condition breaks? Shrink window
                window_and ^= nums[left]  # Remove nums[left] from bitmask
                left += 1

            window_and |= nums[right]  # Add nums[right] to window bitmask
            max_length = max(max_length, right - left + 1)  # Update max length
        
        return max_length