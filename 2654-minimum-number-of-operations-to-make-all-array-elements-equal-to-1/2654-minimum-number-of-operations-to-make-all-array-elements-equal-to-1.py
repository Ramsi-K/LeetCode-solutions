class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)

        if ones:
            return n - ones
        res = inf
        # try finding the shortest subarray with a gcd equal to 1.
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    res = min(res, j - i)

        if res == inf:
            return -1

        return res + n - 1
