class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = 0

        for j in range(1, n - 1):
            max_left = max(nums[:j])
            for k in range(j + 1, n):
                val = (max_left - nums[j]) * nums[k]
                max_val = max(max_val, val)

        return max_val