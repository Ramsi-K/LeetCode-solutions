class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Compare with next element, wrap around at end
                count += 1
                if count > 1:  # More than 1 break? Not a rotated sorted array.
                    return False
        
        return True