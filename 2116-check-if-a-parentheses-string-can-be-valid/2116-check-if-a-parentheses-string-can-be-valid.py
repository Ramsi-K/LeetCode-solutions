class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # Early exit if length is odd
        if len(s) % 2 != 0:
            return False

        # Forward pass: Ensure enough '(' to balance ')'
        balance = 0
        flexibility = 0
        for i in range(len(s)):
            if locked[i] == '1':  # Locked position
                balance += 1 if s[i] == '(' else -1
            else:  # Flexible position
                flexibility += 1

            # If unmatched ')' exceeds the total available '(' + flexibility
            if balance + flexibility < 0:
                return False

        # Backward pass: Ensure enough ')' to balance '('
        balance = 0
        flexibility = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':  # Locked position
                balance += 1 if s[i] == ')' else -1
            else:  # Flexible position
                flexibility += 1

            # If unmatched '(' exceeds the total available ')' + flexibility
            if balance + flexibility < 0:
                return False

        return True