class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = [(target - num) for num in nums]
        zip_list = list(zip(nums, new_nums))
        for i, item in enumerate(zip_list):
          a, b = item
          if a in nums and b in nums[i+1:]:
            return(nums.index(a), nums[i+1:].index(b)+i+1)
        # for i, num in enumerate(nums):
        #   if (target-num) in nums[i+1:]:
        #     return(i, nums[i+1:].index(target-num)+i+1)

