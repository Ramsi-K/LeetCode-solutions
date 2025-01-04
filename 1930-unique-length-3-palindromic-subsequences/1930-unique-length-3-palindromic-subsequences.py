class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:     
        n = len(s)
        unique_palindromes = set()  # Hash Table to store unique palindromes
        
        # Step 1: Precompute prefix sums for character frequencies
        prefix = [[0] * 26 for _ in range(n)]
        for i in range(n):
            if i > 0:
                prefix[i] = prefix[i - 1][:]
            prefix[i][ord(s[i]) - ord('a')] += 1

        # Step 2: Iterate through each unique character as the first and last character
        for char in set(s):
            first = s.find(char)  # String operation to find the first occurrence
            last = s.rfind(char)  # String operation to find the last occurrence

            if last - first > 1:  # Ensure space for a middle character
                # Step 3: Use Bit Manipulation to track intermediate characters
                bitmask = 0
                for mid_char in s[first + 1 : last]:
                    bitmask |= (1 << (ord(mid_char) - ord('a')))
                
                # Step 4: Use the prefix sum to verify valid palindromes
                for i in range(26):  # Iterate over possible middle characters
                    if bitmask & (1 << i):  # Check if character exists between first and last
                        palindrome = char + chr(i + ord('a')) + char
                        unique_palindromes.add(palindrome)
        
        return len(unique_palindromes)