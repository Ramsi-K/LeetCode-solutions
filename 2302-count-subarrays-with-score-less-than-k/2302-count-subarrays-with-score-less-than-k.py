class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        left = 0
        current_sum = 0
        
        for right in range(n):
            current_sum += nums[right]
            
            while current_sum * (right - left + 1) >= k and left <= right:
                current_sum -= nums[left]
                left += 1
            
            res += right - left + 1
        
        return res