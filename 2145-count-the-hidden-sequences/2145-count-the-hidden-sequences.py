class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = 0
        min_sum = 0
        max_sum = 0

        for diff in differences:
            prefix += diff
            min_sum = min(min_sum, prefix)
            max_sum = max(max_sum, prefix)

        min_start = lower - min_sum
        max_start = upper - max_sum

        return max(0, max_start - min_start + 1)