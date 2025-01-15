class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Step 1: Count the number of set bits in num2
        num2_set_bits = bin(num2).count('1')

        # Step 2: Create x starting from num1
        x = 0
        for i in range(31, -1, -1):  # Check each bit from MSB to LSB
            if num2_set_bits > 0 and (num1 & (1 << i)):
                x |= (1 << i)  # Set this bit in x
                num2_set_bits -= 1

        # Step 3: If more set bits are needed, fill from the LSB
        for i in range(32):
            if num2_set_bits > 0 and not (x & (1 << i)):
                x |= (1 << i)
                num2_set_bits -= 1

        return x
