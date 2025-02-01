class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        return all(a % 2 != b % 2 for a, b in zip(nums, nums[1:]))