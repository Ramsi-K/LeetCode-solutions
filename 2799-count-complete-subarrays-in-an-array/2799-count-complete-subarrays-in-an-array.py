class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        total_unique = len(set(nums))

        for i in range(n):
            freq = {}
            unique = 0
            for j in range(i, n):
                if nums[j] not in freq:
                    freq[nums[j]] = 1
                    unique += 1
                else:
                    freq[nums[j]] += 1
                if unique == total_unique:
                    total += 1
        return total