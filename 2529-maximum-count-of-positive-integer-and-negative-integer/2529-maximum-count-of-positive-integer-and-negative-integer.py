class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count_neg = 0
        count_pos = 0
        for num in nums:
            if num < 0:
                count_neg += 1
            elif num > 0:
                count_pos += 1
        return max(count_neg, count_pos)