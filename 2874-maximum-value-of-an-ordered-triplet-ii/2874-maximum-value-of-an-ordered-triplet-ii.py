class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = [0] * n
        max_right = [0] * n

        # Precompute max to the left
        max_so_far = nums[0]
        for i in range(1, n):
            max_left[i] = max_so_far
            max_so_far = max(max_so_far, nums[i])

        # Precompute max to the right
        max_so_far = nums[-1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max_so_far
            max_so_far = max(max_so_far, nums[i])

        # Compute max value of the triplet
        result = 0
        for j in range(1, n - 1):
            val = (max_left[j] - nums[j]) * max_right[j]
            result = max(result, val)

        return max(result, 0)