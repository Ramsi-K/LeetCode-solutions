class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        from itertools import combinations

        max_or = 0
        count = 0

        # Find max OR value possible
        for num in nums:
            max_or |= num

        # Try all subsets and count how many match max OR
        def dfs(i, curr_or):
            nonlocal count
            if i == len(nums):
                if curr_or == max_or:
                    count += 1
                return
            dfs(i + 1, curr_or | nums[i])  # include nums[i]
            dfs(i + 1, curr_or)            # exclude nums[i]

        dfs(0, 0)
        return count
