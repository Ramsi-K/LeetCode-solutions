class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = [0] * 37  # Max digit sum = 9 + 9 + 9 + 9 = 36 (for n ≤ 10^4)

        def digit_sum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        for i in range(1, n + 1):
            s = digit_sum(i)
            counts[s] += 1

        max_size = max(counts)
        return counts.count(max_size)