class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # combs = itertools.combinations(nums, 2)
        # return[(nums.index(i[0]), nums[nums.index(i[0])+1:].index(i[1]) + nums.index(i[0]) +1) for i in combs if sum(i)==target][0]

        for i, num in enumerate(nums):
          if (target-num) in nums[i+1:]:
            return(i, nums[i+1:].index(target-num)+i+1)

