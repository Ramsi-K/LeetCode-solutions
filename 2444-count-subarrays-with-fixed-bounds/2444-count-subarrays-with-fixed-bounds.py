class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        left_bound = -1
        last_min = -1
        last_max = -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                left_bound = i
                last_min = -1
                last_max = -1
                continue
            
            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i
            
            if last_min != -1 and last_max != -1:
                res += min(last_min, last_max) - left_bound
        
        return res