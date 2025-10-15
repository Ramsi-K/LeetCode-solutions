class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        prev = 0
        curr = 1
        record = 0
        nums.append(-10**10)

        for i in range(n):
            if nums[i] < nums[i+1]:
                curr += 1
            else:
                record = max(record, curr//2, min(prev, curr))
                prev, curr = curr, 1
        
        return record