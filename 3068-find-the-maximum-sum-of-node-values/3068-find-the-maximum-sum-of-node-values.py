class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        cnt = 0
        for idx, num in enumerate(nums):
            nxork = num ^ k
            if nxork > num:
                nums[idx] = nxork
                cnt += 1
        if cnt % 2 == 1:
            min_diff, num_idx = float('inf'), -1
            for idx, num in enumerate(nums):
                curr_diff = abs(num - (num ^ k))
                if curr_diff < min_diff:
                    min_diff, num_idx = curr_diff, idx
            nums[num_idx] ^= k
        return sum(nums)  