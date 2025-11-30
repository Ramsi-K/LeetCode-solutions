class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        r = total % p
        if r == 0:
            return 0

        mp = {0: -1}
        prefix = 0
        n = len(nums)
        ans = n

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - r) % p

            if target in mp:
                ans = min(ans, i - mp[target])

            mp[prefix] = i

        return ans if ans < n else -1
