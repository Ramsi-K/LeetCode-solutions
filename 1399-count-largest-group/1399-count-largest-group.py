class Solution:
    def countLargestGroup(self, n: int) -> int:
        num_digits = int(log10(n)) + 1
        max_digit_sum = 9 * num_digits
        digit_sum_counts = [0] * (max_digit_sum + 1)

        for i in range(1, n + 1):
            s = sum(int(d) for d in str(i))  
            digit_sum_counts[s] += 1

        max_group_size = max(digit_sum_counts)
        return digit_sum_counts.count(max_group_size)