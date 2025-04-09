class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(num < k for num in nums):
            return -1

        # Count how many unique values are strictly greater than k
        unique_greater = set(num for num in nums if num > k)
        return len(unique_greater)