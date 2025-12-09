from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        # Count of single numbers seen so far
        singles = {}
        # Count of valid pair sums encountered so far
        pairs = {}

        MOD = 10**9 + 7
        result = 0

        for x in nums:
            # Any pair matching x completes a triplet
            result = (result + pairs.get(x, 0)) % MOD

            doubled = x * 2

            # every occurrence forms a new valid pair (doubled, x)
            if doubled in singles:
                pairs[doubled] = (pairs.get(doubled, 0) + singles[doubled]) % MOD

            singles[x] = singles.get(x, 0) + 1

        return result
