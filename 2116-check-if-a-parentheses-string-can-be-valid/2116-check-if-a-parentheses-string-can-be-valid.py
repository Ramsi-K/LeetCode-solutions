class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # If the string length is odd, it's impossible to make it valid
        if len(s) % 2 != 0:
            return False

        # Forward pass
        open_count = 0
        flexible_count = 0
        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    open_count += 1
                else:
                    open_count -= 1
            else:
                flexible_count += 1

            # Ensure that unmatched ')' never exceeds the number of '('
            if open_count + flexible_count < 0:
                return False

        # Backward pass
        close_count = 0
        flexible_count = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    close_count += 1
                else:
                    close_count -= 1
            else:
                flexible_count += 1

            # Ensure that unmatched '(' never exceeds the number of ')'
            if close_count + flexible_count < 0:
                return False

        return True