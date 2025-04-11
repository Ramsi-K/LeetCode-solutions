class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(x):
            s = str(x)
            if len(s) % 2 != 0:
                return False
            mid = len(s) // 2
            return sum(int(d) for d in s[:mid]) == sum(int(d) for d in s[mid:])

        count = 0
        for num in range(low, high + 1):
            if is_symmetric(num):
                count += 1
        return count