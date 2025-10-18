class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        next_free = -10**18
        distinct = 0

        for x in nums:
            lo = x - k
            hi = x + k

            if next_free <= hi:
                assign = max(lo, next_free)
                distinct += 1
                next_free = assign + 1


        return distinct