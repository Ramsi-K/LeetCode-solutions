class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        # If the length of the string is odd, it's impossible to form valid parentheses
        if n % 2 == 1:
            return False

        # If the first or last character is locked in an invalid state, return False
        if (locked[0] == "1" and s[0] == ")") or (locked[-1] == "1" and s[-1] == "("):
            return False 

        # Stack to track locked opening parentheses
        locked_open = []
        # List to track indices of flexible positions
        flexible_indices = []

        # First pass: Process the string
        for i in range(n):
            if locked[i] == "0":  # Flexible position
                flexible_indices.append(i)
            elif s[i] == "(":  # Locked opening parenthesis
                locked_open.append(i)
            else:  # Locked closing parenthesis
                # Try to match with a locked opening parenthesis first
                if locked_open:
                    locked_open.pop()
                # If no locked opening parenthesis, use a flexible position
                elif flexible_indices:
                    flexible_indices.pop()
                else:
                    return False  # No match available, invalid state

        # Second pass: Match any remaining locked opening parentheses with flexible positions
        while locked_open and flexible_indices and locked_open[-1] < flexible_indices[-1]:
            locked_open.pop()
            flexible_indices.pop()

        # If there are unmatched locked opening parentheses, the string is invalid
        if locked_open:
            return False

        return True