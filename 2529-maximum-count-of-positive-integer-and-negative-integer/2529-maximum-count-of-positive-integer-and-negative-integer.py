class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Count negatives: all numbers strictly less than 0
        count_neg = bisect_left(nums, 0)
        # Count positives: all numbers strictly greater than 0
        count_pos = len(nums) - bisect_right(nums, 0)
        return max(count_neg, count_pos)