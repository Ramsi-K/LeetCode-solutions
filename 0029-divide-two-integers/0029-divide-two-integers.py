class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        if divisor == 0 or (dividend == MIN and divisor == -1):
            return MAX
        
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1 
        else: sign = 1

        quotient = 0

        absoluteDividend = abs(dividend)
        absoluteDivisor = abs(divisor)

        while absoluteDividend >= absoluteDivisor:
            shift=0
            while absoluteDividend >= (absoluteDivisor << shift):
                shift +=1
            
            quotient += 1 << (shift - 1)
            absoluteDividend -= absoluteDivisor << (shift - 1)

        return quotient * sign
            