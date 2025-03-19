class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0  # Count of flips
        
        for i in range(n - 2):  # We stop at `n-3` because we flip in groups of 3
            if nums[i] == 0:  # If we find a `0`, flip the next 3 elements
                ops += 1
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1

        return ops if all(num == 1 for num in nums) else -1