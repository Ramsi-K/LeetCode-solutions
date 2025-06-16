class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        res = -1
        for j in range(1, len(nums)):
            if nums[j] > min_val:
                res = max(res, nums[j] - min_val)
            min_val = min(min_val, nums[j])
        return res