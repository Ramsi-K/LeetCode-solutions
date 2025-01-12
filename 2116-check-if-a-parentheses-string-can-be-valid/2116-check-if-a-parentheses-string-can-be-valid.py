class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open_count = 0  # Count of open parentheses
        flexible_count = 0  # Count of flexible positions

        # Forward pass: Check for sufficient open parentheses
        for i in range(len(s)):
            if locked[i] == '1':  # Fixed
                if s[i] == '(':
                    open_count += 1
                else:
                    open_count -= 1
            else:  # Flexible
                flexible_count += 1

            # Invalid state: More ')' than '(' + flexible
            if open_count + flexible_count < 0:
                return False

        open_count = 0
        flexible_count = 0

        # Backward pass: Check for sufficient close parentheses
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':  # Fixed
                if s[i] == ')':
                    open_count += 1
                else:
                    open_count -= 1
            else:  # Flexible
                flexible_count += 1

            # Invalid state: More '(' than ')' + flexible
            if open_count + flexible_count < 0:
                return False

        return True