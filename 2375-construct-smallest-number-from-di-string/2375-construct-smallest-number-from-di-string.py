class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        digits = list(range(1, n + 2))  # digits from 1 to n+1
        result = []
        stack = []

        for i, char in enumerate(pattern + 'I'):  # Add 'I' to handle the last digit
            if char == 'I':
                stack.append(digits[i])
                # Now, we need to add all numbers from stack in reverse order
                result.extend(reversed(stack))
                stack = []
            else:  # char == 'D'
                stack.append(digits[i])

        # Convert to string
        return ''.join(map(str, result))