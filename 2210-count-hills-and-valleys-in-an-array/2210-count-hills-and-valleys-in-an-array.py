from typing import List
from itertools import groupby

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Remove consecutive duplicates
        filtered = [val for val, _ in groupby(nums)]

        count = 0
        for i in range(1, len(filtered) - 1):
            prev = filtered[i - 1]
            curr = filtered[i]
            next_ = filtered[i + 1]

            if prev < curr > next_:  # Hill
                count += 1
            elif prev > curr < next_:  # Valley
                count += 1

        return count
