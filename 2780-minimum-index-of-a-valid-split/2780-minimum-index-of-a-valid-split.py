class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        total = Counter(nums)
        dom = max(total, key=total.get)
        count = 0
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == dom:
                count += 1
            left_len = i + 1
            right_len = n - i - 1
            if count * 2 > left_len and (total[dom] - count) * 2 > right_len:
                return i

        return -1