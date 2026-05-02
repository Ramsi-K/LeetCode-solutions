class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0

        for num in range(1, n + 1):
            is_valid = True
            has_change = False

            while num > 0:
                digit = num % 10
                if digit in [3, 4, 7]:
                    is_valid = False
                    break

                if digit in [2, 5, 6, 9]:
                    has_change = True

                num //= 10

            if is_valid and has_change:
                count += 1

        return count
