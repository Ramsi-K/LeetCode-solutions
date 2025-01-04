class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:     
        unique_palindromes = set()

        # Iterate over all unique characters in the string
        for char in set(s):
            first = s.find(char)
            last = s.rfind(char)

            # If there are characters between first and last, process them
            if last - first > 1:
                # Use a set to track intermediate characters
                for mid_char in set(s[first + 1:last]):
                    unique_palindromes.add(char + mid_char + char)

        return len(unique_palindromes)