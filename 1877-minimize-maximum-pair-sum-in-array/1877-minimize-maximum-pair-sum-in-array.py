class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair_sums = []

        for i in range(len(nums)//2):
            pair_sum = nums[i] + nums.pop()
            pair_sums.append(pair_sum)
        
        return max(pair_sums)
