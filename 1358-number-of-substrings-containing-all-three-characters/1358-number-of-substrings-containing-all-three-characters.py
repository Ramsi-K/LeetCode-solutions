class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}  # To track occurrences
        l = 0  # Left pointer
        result = 0  # Count of valid substrings

        for r in range(len(s)):  # Right pointer expanding
            count[s[r]] += 1  # Include s[r] in the window
            
            # Shrink the left side while we have at least one 'a', 'b', and 'c'
            while all(count[ch] > 0 for ch in "abc"):
                result += len(s) - r  # All substrings from (l, r) to (l, len(s)-1) are valid
                count[s[l]] -= 1  # Shrink the window from the left
                l += 1  # Move left pointer

        return result