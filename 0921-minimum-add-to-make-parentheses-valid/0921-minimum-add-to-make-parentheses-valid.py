class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Counters for unmatched opening and missing parentheses
        open_count = 0
        add_count = 0

        for char in s:
            if char == '(':
                open_count += 1  # Track unmatched opening
            elif char == ')':
                if open_count > 0:
                    open_count -= 1  # Balance with an unmatched opening
                else:
                    add_count += 1  # Missing an opening parenthesis

        # Total additions needed = unmatched openings + unmatched closings
        return open_count + add_count
