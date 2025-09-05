class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num1 == 0:
            return 0

        for m in range(1, 61): 
            S = num1 - m * num2
            if S > 0 and m <= S and S.bit_count() <= m:
                return m
            if num2 > 0 and S <= 0:
                return -1

        return -1
