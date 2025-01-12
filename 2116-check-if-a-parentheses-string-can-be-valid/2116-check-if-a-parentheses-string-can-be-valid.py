class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # If the length is odd, it's impossible to form valid parentheses
        if len(s) % 2 != 0:
            return False

        # Forward pass: Ensure enough '(' to match ')'
        balance = 0
        flexible = 0
        for i in range(len(s)):
            if locked[i] == '1':  # Locked position
                balance += 1 if s[i] == '(' else -1
            else:  # Flexible position
                flexible += 1

            # If ')' exceeds '(', use flexible positions
            if balance + flexible < 0:
                return False

        # Backward pass: Ensure enough ')' to match '('
        balance = 0
        flexible = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':  # Locked position
                balance += 1 if s[i] == ')' else -1
            else:  # Flexible position
                flexible += 1

            # If '(' exceeds ')', use flexible positions
            if balance + flexible < 0:
                return False

        return True