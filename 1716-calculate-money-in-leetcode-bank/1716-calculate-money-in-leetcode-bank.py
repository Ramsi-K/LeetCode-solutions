class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks, remaining_days = divmod(n, 7)
        # full weeks contribution
        total = 28 * full_weeks + 7 * (full_weeks - 1) * full_weeks // 2
        # leftover days
        start = full_weeks + 1
        for i in range(remaining_days):
            total += start + i
        return total
